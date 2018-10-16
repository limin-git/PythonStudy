# encoding: utf-8
#
# use_omniorb.py
#

import sys
import os
import os.path

OMNIORBPY_HOME = r'C:\MyCots\omniORB\omniORBpy-4.2.2-win64-python2.7\omniORBpy-4.2.2'
OMNIORBPY_LIB_PYTHON = os.path.join(OMNIORBPY_HOME, r'lib\python')
OMNIORBPY_LIB_X86_WIN32 = os.path.join(OMNIORBPY_HOME, r'lib\x86_win32')
OMNIORBPY_BIN_X86_WIN32 = os.path.join(OMNIORBPY_HOME, r'bin\x86_win32')

sys.path.insert(0, OMNIORBPY_LIB_PYTHON)
sys.path.insert(0, OMNIORBPY_LIB_X86_WIN32)
os.environ['PATH'] = ';'.join([os.environ['PATH'], OMNIORBPY_BIN_X86_WIN32])

import CORBA
omniorb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
