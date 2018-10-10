# encoding: utf-8
# Example 4-8 serves a page where users can fill out and submit to the web server the
# contents of a text box. The server will then display that text back to the user.
# Example 4-8. handle_post.py
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import cgi
class FormPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return """
<html>
 <body>
  <form method="POST">
   <input name="form-field" type="text" />
   <input type="submit" />
   </form>
   </body>
   </html>
"""
    def render_POST(self, request):
        return """
<html>
 <body>You submitted: %s</body>
 </html>
""" % (cgi.escape(request.args["form-field"][0]),)
factory = Site(FormPage())
reactor.listenTCP(8000, factory)
reactor.run()
