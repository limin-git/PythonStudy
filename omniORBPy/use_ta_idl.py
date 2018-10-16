# encoding: utf-8
#
# use_ta_idl.py
#

import sys
import os
import os.path
from use_omniorb import omniorb

HERE = os.path.dirname(os.path.realpath(__file__))
TA_IDL_PATH = os.path.join(HERE, 'idl')

sys.path.insert(0, TA_IDL_PATH)

import TA_Base_Core
