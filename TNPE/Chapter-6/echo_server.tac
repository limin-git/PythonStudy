# Example 6-3. echo_server.tac, a Twisted application configuration file

import sys, os, os.path
sys.path.append(os.getcwd())

from twisted.application import internet, service
from echo import EchoFactory
application = service.Application("echo")
echoService = internet.TCPServer(8000, EchoFactory())
echoService.setServiceParent(application)

# We can run our echo server application with:
# twistd -y echo_server.tac
