#
# build.py
#

import sys
import os
import os.path
import os
from glob import glob
import shutil
from concurrent.futures import ThreadPoolExecutor

OMNIORBPY_HOME = r'D:\MyCots\omniORB\omniORBpy-4.2.2-win64-python2.7\omniORBpy-4.2.2'
OMNIORBPY_BIN_X86_WIN32 = os.path.join(OMNIORBPY_HOME, r'bin\x86_win32')
OMNIIDL = os.path.join(OMNIORBPY_BIN_X86_WIN32, r'omniidl.exe')
HERE = os.path.dirname(os.path.realpath(__file__))
IDL_DIR = os.path.join(HERE, 'idl')

if not os.path.isdir(IDL_DIR):
    print('Can not find idl path')
    exit()

os.chdir(IDL_DIR)

if '--clean' in sys.argv:
    for dirpath, dirnames, filenames in os.walk(IDL_DIR):
        for d in dirnames:
            shutil.rmtree(d, True)
        _ = [os.remove(f) for f in filenames if os.path.splitext(f)[1] in ['.py', '.pyc', '.pyo'] ]
    exit()

for idl in glob(os.path.join(HERE, r'idl\*.idl')):
    idl_py = os.path.splitext(idl)[0] + '_idl.py'
    if not os.path.isfile(idl_py):
        os.system(' '.join([OMNIIDL, '-bpython', os.path.basename(idl)]))
