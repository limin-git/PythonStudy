import os
import os.path
import wget

HERE = os.path.dirname(os.path.realpath(__file__))

os.chdir(HERE)

omniORB_422_tar_bz2 = r'https://sourceforge.net/projects/omniorb/files/omniORB/omniORB-4.2.2/omniORB-4.2.2.tar.bz2'
wget.download(omniORB_422_tar_bz2)
