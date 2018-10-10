# encoding: utf-8
# Example 12-2 shows an IRC server that listens for IRC connections on port 6667 and
# authenticates users based on the contents of a colon-delimited passwords.txt file.
# Example 12-2. irc_server.py
from twisted.cred import checkers, portal
from twisted.internet import reactor
from twisted.words import service
wordsRealm = service.InMemoryWordsRealm("example.com")
wordsRealm.createGroupOnRequest = True
checker = checkers.FilePasswordDB("passwords.txt")
portal = portal.Portal(wordsRealm, [checker])
reactor.listenTCP(6667, service.IRCFactory(wordsRealm, portal))
reactor.run()
