# encoding: utf-8
# Example 11-1 shows a single test case class called MyFirstTestCase, containing a single
# test called test_something, which makes an assertion using the Twisted version of
# unittest’s TestCase.assertTrue. Most unittest assertions have Twisted versions,
# and Trial has additional assertions for exercising Failures.
# Example 11-1. test_foo.py
from twisted.trial import unittest

class MyFirstTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(True)
