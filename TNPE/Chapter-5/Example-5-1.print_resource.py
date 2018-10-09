# encoding: utf-8
# Printing a Web Resource
# twisted.web.client.getPage asynchronously retrieves a resource at a given URL. It
# returns a Deferred, which fires its callback with the resource as a string. Example 5-1
# demonstrates the use of getPage; it retrieves and prints the resource at the user-supplied
# URL.
# Example 5-1. print_resource.py
from twisted.internet import reactor
from twisted.web.client import getPage
import sys
def printPage(result):
    print result
def printError(failure):
    print >>sys.stderr, failure
def stop(result):
    reactor.stop()
if len(sys.argv) != 2:
    print >>sys.stderr, "Usage: python print_resource.py <URL>"
    exit(1)
d = getPage(sys.argv[1])
d.addCallbacks(printPage, printError)
d.addBoth(stop)
reactor.run()
