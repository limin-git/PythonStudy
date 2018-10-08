__metaclass__ = type

import traceback


def hello():
    print 'hello, world!'
    traceback.print_stack()

from twisted.internet import reactor
reactor.callWhenRunning(hello)
reactor.run()

