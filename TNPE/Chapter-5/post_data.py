# encoding: utf-8
# Example 5-5 shows a complete POSTing client. Beyond the StringProducer, the code
# is almost identical to the resource-requesting client in Example 5-3.
# Example 5-5. post_data.py
import sys
from twisted.internet import reactor
from twisted.internet.defer import Deferred, succeed
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent
from twisted.web.iweb import IBodyProducer
from zope.interface import implements
class StringProducer(object):
    implements(IBodyProducer)
    def __init__(self, body):
        self.body = body
        self.length = len(body)
    def startProducing(self, consumer):
        consumer.write(self.body)
        return succeed(None)
    def pauseProducing(self):
        pass
    def stopProducing(self):
        pass
class ResourcePrinter(Protocol):
    def __init__(self, finished):
        self.finished = finished
    def dataReceived(self, data):
        print data
    def connectionLost(self, reason):
        self.finished.callback(None)
def printResource(response):
    finished = Deferred()
    response.deliverBody(ResourcePrinter(finished))
    return finished
def printError(failure):
    print >>sys.stderr, failure
def stop(result):
    reactor.stop()
if len(sys.argv) != 3:
    print >>sys.stderr, "Usage: python post_resource.py URL 'POST DATA'"
    exit(1)
agent = Agent(reactor)
body = StringProducer(sys.argv[2])
d = agent.request('POST', sys.argv[1], bodyProducer=body)
d.addCallbacks(printResource, printError)
d.addBoth(stop)
reactor.run()
# To  test  this  example,  we  need  a  URL  that  accepts  POST  requests.  http://
# www.google.com is not such a URL, as it turns out. This:
# python post_data.py http://www.google.com 'Hello World'
# prints:
# The request method POST is inappropriate for the URL /. That’s all we know.
# This is an occasion where being able to spin up a basic web server easily for testing
# would be useful. Fortunately, we covered Twisted web servers in the previous chapter!
