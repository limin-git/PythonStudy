#
# build_omniorb_4.2.2.py
#

import os
import os.path
import tarfile
import wget
import zipfile

HERE = os.path.dirname(os.path.realpath(__file__))
ACE_HOME = r'C:\cots_ng\ACE'
ACE_VERSION = '6.5.0'
ACE_NAME = 'ACE-{}'.format(ACE_VERSION)
ACE_PACKAGE = 'ACE-{}.zip'.format(ACE_VERSION)
ACE_PACKAGE_URL = r'http://download.dre.vanderbilt.edu/previous_versions/{}'.format(ACE_PACKAGE)
ACE_FOLDER =  os.path.join(ACE_HOME, ACE_NAME)
ACE_PACKAGE_FILE = os.path.join(ACE_HOME, ACE_PACKAGE)

# TODO
VS2017_COMMAND_LINE = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2017\Visual Studio Tools\VC\x86 Native Tools Command Prompt for VS 2017'

os.chdir(ACE_HOME)

def download(url, out=None):
    wget.download(url, out)

def unpackage(package, where):
    zf = zipfile.ZipFile(package, 'r')
    zf.extractall(path=where)

def is_folder_exist():
    return os.path.isdir(ACE_FOLDER)

def is_package_exist():
    return os.path.isfile(ACE_PACKAGE_FILE)

if not is_folder_exist():
    if not is_package_exist():
        try:
            print('Downloading {} from {} ...'.format(ACE_PACKAGE, ACE_PACKAGE_URL))
            download(ACE_PACKAGE_URL, ACE_HOME)
            print('')
        except:
            print('Download failed')
            exit()
    try:
        print('unpackage {} ...'.format(ACE_PACKAGE))
        unpackage(ACE_PACKAGE_FILE, ACE_FOLDER)
    except:
        print('unpackage failed')
        exit()

# now prepaire to build
# os.system(r'%comspec% /k "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvars32.bat"')
