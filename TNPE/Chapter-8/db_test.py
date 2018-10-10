# encoding: utf-8
# Example 8-1. db_test.py
from twisted.internet import reactor
from twisted.enterprise import adbapi
dbpool = adbapi.ConnectionPool("sqlite3", "users.db", check_same_thread=False)
def getName(email):
    return dbpool.runQuery("SELECT name FROM users WHERE email = ?",
                           (email,))
def printResults(results):
    for elt in results:
        print elt[0]
def finish():
    dbpool.close()
    reactor.stop()
d = getName("jane@foo.com")
d.addCallback(printResults)
reactor.callLater(1, finish)
reactor.run()

# When using adbapi with SQLite, if you encounter an error of the form:
# sqlite3.ProgrammingError: SQLite objects created in a thread
# can only be used in that same thread.The object was created in
# thread id 5972 and this is thread id 4916
# you’ll  need  to  create  your  ConnectionPool  with
# check_same_thread=False, as in:
# dbpool = adbapi.ConnectionPool("sqlite3", "users.db",
#                                check_same_thread=False)
# See Twisted ticket 3629 for details.
