from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
root = File('..')
root.putChild("chapter-2", File(r"..\Chapter-2"))
root.putChild("chapter-3", File(r"..\Chapter-3"))
root.putChild("chapter-4", File(r"..\Chapter-4"))
factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()
