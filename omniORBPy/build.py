#
# build.py
#

import sys
import os
import os.path
from glob import glob

OMNIORBPY_HOME = r'C:\MyCots\omniORB\omniORBpy-4.2.2-win64-python2.7\omniORBpy-4.2.2'
OMNIORBPY_BIN_X86_WIN32 = os.path.join(OMNIORBPY_HOME, r'bin\x86_win32')
OMNIIDL = os.path.join(OMNIORBPY_BIN_X86_WIN32, r'omniidl.exe')
HERE = os.path.dirname(os.path.realpath(__file__))
IDL_DIR = os.path.join(HERE, 'idl')

if not os.path.isdir(IDL_DIR):
    print('Can not find idl path')
    exit()

os.chdir(IDL_DIR)

if 1 < len(sys.argv) and sys.argv[1] == '--clean':
    os.system('DEL /F *.py')
    exit()

for idl in glob(os.path.join(HERE, r'idl\*.idl')):
    os.system(' '.join([OMNIIDL, '-bpython', os.path.basename(idl)]))
