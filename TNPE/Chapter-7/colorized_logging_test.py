# Example 7-5. colorized_logging_test.py
import sys
from twisted.python import log
from log_colorizer import ColorizedLogObserver
observer = ColorizedLogObserver(sys.stdout)
log.addObserver(observer.emit)
log.msg("Starting experiment")
log.msg("Logging an exception")
try:
    1 / 0
except ZeroDivisionError, e:
    log.err(e)
log.msg("Ending experiment")
