# encoding: utf-8
# Example 4-10 demonstrates how to use a Deferred instead of blocking on an expensive
# resource. deferLater replaces the blocking time.sleep(5) with a Deferred that will
# fire after five seconds, with a callback to _delayedRender to finish the request when the
# fake resource becomes available. Then, instead of waiting on that resource, render_GET
# returns NOT_DONE_YET immediately, freeing up the web server to process other requests.
# Example 4-10. non_blocking.py
from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET
import time
class BusyPage(Resource):
    isLeaf = True
    def _delayedRender(self, request):
        request.write("Finally done, at %s" % (time.asctime(),))
        request.finish()
    def render_GET(self, request):
        d = deferLater(reactor, 5, lambda: request)
        d.addCallback(self._delayedRender)
        return NOT_DONE_YET
factory = Site(BusyPage())
reactor.listenTCP(8000, factory)
reactor.run()
