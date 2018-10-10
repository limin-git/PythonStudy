# encoding: utf-8
# Let’s say we wanted to write a unit test suite for our echo protocol logic from Chap‐
# ter 2 , reproduced Example 11-2 in for convenience.
# Example 11-2. echo.py
from twisted.internet import protocol, reactor
class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()
