# encoding: utf-8
# Example 4-6 demonstrates a calendar server that displays the calendar for the year
# provided in the URL. For example, visiting http://localhost:8000/2013 will display the
# calendar for 2013, as shown in Figure 4-2.
# Example 4-6. dynamic_dispatch.py

from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site
from calendar import calendar
from datetime import datetime
from twisted.web.util import redirectTo
class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year
    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year),)
class CalendarHome(Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        if name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()
    def render_GET(self, request):
        # return "<html><body>Welcome to the calendar server!</body></html>"
        return redirectTo(str(datetime.now().year), request)
root = CalendarHome()
factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()
