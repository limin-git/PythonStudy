# encoding: utf-8
from use_ta_idl import omniorb, TA_Base_Core

def resolve_system_controller():
    try:
        corbaloc = 'corbaloc::179.90.10.11:6666/SystemControllerAdmin'
        admin = omniorb.string_to_object(corbaloc)._narrow(TA_Base_Core.ISystemControllerAdminCorbaDef)
        print admin.getProcessData()
    except: pass

resolve_system_controller()
