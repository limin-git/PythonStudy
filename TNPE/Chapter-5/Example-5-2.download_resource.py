# encoding: utf-8
# Downloading a Web Resource
# twisted.web.client.downloadPage asynchronously downloads a resource at a given
# URL to the specified file. Example 5-2 demonstrates the use of getPage.
# Example 5-2. download_resource.py
from twisted.internet import reactor
from twisted.web.client import downloadPage
import sys
def printError(failure):
    print >>sys.stderr, failure
def stop(result):
    reactor.stop()
if len(sys.argv) != 3:
    print >>sys.stderr, "Usage: python download_resource.py <URL> <output file>"
    exit(1)
d = downloadPage(sys.argv[1], sys.argv[2])
d.addErrback(printError)
d.addBoth(stop)
reactor.run()
# We can test this script with:
# python download_resource.py http://www.google.com google.html
# which will save the contents of Google’s home page to the file google.html.
