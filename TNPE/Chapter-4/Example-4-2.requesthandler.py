# encoding: utf-8
# An HTTP request is represented by twisted.web.http.Request. We can specify how
# requests are processed by subclassing http.Request and overriding its process meth‐
# od. Example 4-2 subclasses http.Request to serve one of three resources: an HTML
# page for the root resource /, a page for /about, and a 404 http.NOT_FOUND if any other
# path is specified.
# Example 4-2. requesthandler.py

from twisted.internet import reactor
from twisted.web import http
class MyRequestHandler(http.Request):
    resources = {
        '/': '<h1>Home</h1>Home page',
        '/about': '<h1>About</h1>All about me',
        }
    def process(self):
        self.setHeader('Content-Type', 'text/html')
        if self.resources.has_key(self.path):
            self.write(self.resources[self.path])
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>Not Found</h1>Sorry, no such resource.")
        self.finish()
class MyHTTP(http.HTTPChannel):
    requestFactory = MyRequestHandler
class MyHTTPFactory(http.HTTPFactory):
    def buildProtocol(self, addr):
        return MyHTTP()
reactor.listenTCP(8000, MyHTTPFactory())
reactor.run()
