#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

# (C) COPYRIGHT © Preston Landers 2010
# Released under the same license as Python 2.6.5


import sys, os, traceback, types, win32api, win32con, win32event, win32process, ctypes
from win32com.shell.shell import ShellExecuteEx
from win32com.shell import shellcon

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def run_as_admin(python_exe, cmdLine=None, wait=True):
    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType,types.ListType):
        raise ValueError("cmdLine is not a sequence.")

    cmd         = '"%s"' % (cmdLine[0],)
    # XXX TODO: isn't there a function or something we can call to massage command line params?
    params      = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir      = ''
    # showCmd = win32con.SW_SHOWNORMAL
    showCmd     = win32con.SW_HIDE
    lpVerb      = 'runas'  # causes UAC elevation prompt.

    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

    procInfo = ShellExecuteEx(nShow=showCmd, fMask=shellcon.SEE_MASK_NOCLOSEPROCESS, lpVerb=lpVerb, lpFile=cmd, lpParameters=params)

    if wait:
        procHandle  = procInfo['hProcess']
        obj         = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc          = win32process.GetExitCodeProcess(procHandle)
    else:
        rc          = None

    return True
