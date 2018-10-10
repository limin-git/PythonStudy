# encoding: utf-8
# Example  11-3  has  a  test  case  for  the  Echo  protocol.  It  creates  an  instance  of
# EchoFactory, uses that factory to build an instance of the Echo protocol, and sets the
# protocol’s transport to an instance of proto_helpers.StringTransport. The proto‐
# col’s  makeConnection  method  is  called  to  simulate  a  client  connection,  and
# dataReceived is called to simulate receiving client data. At that point, the transport
# should contain the echoed version of the fake client data, so we make an assertion on
# transport.value().
# Example 11-3.  test_echo.py
from twisted.test import proto_helpers
from twisted.trial import unittest
from echo import EchoFactory
class EchoServerTestCase(unittest.TestCase):
    def test_echo(self):
        factory = EchoFactory()
        self.proto = factory.buildProtocol(("localhost", 0))
        self.transport = proto_helpers.StringTransport()
        self.proto.makeConnection(self.transport)
        self.proto.dataReceived("test\r\n")
        self.assertEqual(self.transport.value(), "test\r\n")
