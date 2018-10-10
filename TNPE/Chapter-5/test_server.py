# Example 5-6 is a simple web server that echoes the body of a POST, only reversed.
# Example 5-6. test_server.py
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
class TestPage(Resource):
    isLeaf = True
    def render_POST(self, request):
        return request.content.read()[::-1]
resource = TestPage()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()
# python test_server.py will start the web server listening on port 8000. With that server
# running, we can then test our client with:
# $ python post_data.py http://127.0.0.1:8000 "Hello World"
# dlroW olleH
