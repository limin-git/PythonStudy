# encoding: utf-8
# Example 4-9 implements a dummy BusyPage resource that sleeps for five seconds before
# returning a response to the request.
# Example 4-9. blocking.py
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import time
class BusyPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        time.sleep(5)
        return "Finally done, at %s" % (time.asctime(),)
factory = Site(BusyPage())
reactor.listenTCP(8000, factory)
reactor.run()
