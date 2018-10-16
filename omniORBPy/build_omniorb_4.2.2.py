#
# build_omniorb_4.2.2.py
#

import os
import os.path
import tarfile
import wget

OMNIORB_NAME = 'omniORB'
OMNIORB_VERSION = '4.2.2'
OMNIORB_FULLNAME = '-'.join([OMNIORB_NAME, OMNIORB_VERSION])
OMNIORB_FULLNAME_TAR_BZ2 = '{}.tar.bz2'.format(OMNIORB_FULLNAME)
OMNIORB_FULLNAME_TAR_BZ2_URL = r'https://sourceforge.net/projects/omniorb/files/omniORB/omniORB-4.2.2/omniORB-4.2.2.tar.bz2'
HERE = os.path.dirname(os.path.realpath(__file__))
OMNIORB_FOLDER =  os.path.join(HERE, OMNIORB_FULLNAME)
OMNIORB_FULLNAME_TAR_BZ2_FILE = os.path.join(HERE, OMNIORB_FULLNAME_TAR_BZ2)

os.chdir(HERE)

def download(url):
    wget.download(url)

def unzip(dir, name):
    tar = tarfile.open(os.path.join(dir, name))
    names = tar.getnames()
    for name in names:
        tar.extract(name, path=dir)
    tar.close()

def is_omniorb_folder_exist():
    return os.path.isdir(OMNIORB_FOLDER)

def is_omniorb_tar_gz_exist():
    return os.path.isfile(OMNIORB_FULLNAME_TAR_BZ2_FILE)

if not is_omniorb_folder_exist():
    if not is_omniorb_tar_gz_exist():
        try:
            print('Downloading {} from {} ...'.format(OMNIORB_FULLNAME_TAR_BZ2, OMNIORB_FULLNAME_TAR_BZ2_URL))
            download(OMNIORB_FULLNAME_TAR_BZ2_URL)
            print('')
        except:
            print('Download failed')
            exit()
    try:
        print('Unzip {} ...'.format(OMNIORB_FULLNAME_TAR_BZ2))
        unzip(HERE, OMNIORB_FULLNAME_TAR_BZ2)
    except:
        print('Unzip failed')
        exit()

# now prepaire to compile
