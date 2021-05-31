#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

# (C) COPYRIGHT © Preston Landers 2010
# Released under the same license as Python 2.6.5

# Import relevant libraries to use it for admin status get and set functions

import sys, os, traceback, types, ctypes, win32api, win32con, win32event, win32process

# Import shell execute module
from win32com.shell.shell import ShellExecuteEx

# Import shell connection module
from win32com.shell import shellcon

def is_admin():

    # is_admin function will return a boolean value which represent
    # what a program is running in admin mode or normal

    try:

        # try to use python ctypes api to get result

        # this function will return boolean value about a program is running in admin or not

        return ctypes.windll.shell32.IsUserAnAdmin()
    except:

        # if their have any problem it will false it can be return True but it will be wrong into
        # and dangerous also

        return False

def run_as_admin(python_exe=sys.executable, cmdLine=None, wait=True):

    # run_as_admin function will try to run this program in an admin mode

    # it is expecting to getting up to three parameters

    # python_exe is executable path or instance to execute command for program
    # cmdline is need to be in sequence, it's not necessary yet,
    # but it will be used in future version

    # check if cmdline is used or not, because we are not allowing it now

    # wait=False if you don't want to wait, instead just want to force

    if cmdLine is None:

        # build cmdline to handle execute python command with system command arguments

        cmdLine = [python_exe] + sys.argv

    elif type(cmdLine) not in (types.TupleType,types.ListType):

        raise ValueError("cmdLine is not a sequence.")

    # build cmdline to a cmd string
    cmd         = '"%s"' % (cmdLine[0],) # get first command from cmdline

    # build params to pass some extra params to cmd call
    params      = " ".join(['"%s"' % (x,) for x in cmdLine[1:]]) # join params in a string

    # hide cmd shell window from window
    showCmd     = win32con.SW_HIDE

    # set ip verb to runas admin
    lpVerb      = 'runas'


    # it's another way to call program to run in admin mode but it will start a shell window
    # cmdDir = ''
    # showCmd = win32con.SW_SHOWNORMAL
    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)


    # finally call to ShellExecuteEx with all params
    # to get interective yes no question window
    # to run this program in admin mode

    procInfo = ShellExecuteEx(
        nShow=showCmd,  # show cmd or not
        fMask=shellcon.SEE_MASK_NOCLOSEPROCESS, # mask processes
        lpVerb=lpVerb, # ip verb
        lpFile=cmd, # cmd command with args
        lpParameters=params # pass extra parameters
    )

    # check if waiting True or False
    if wait:

        # get hProcess from procInfo object
        procHandle  = procInfo['hProcess']

        # pass hProcess to event object to get event result
        obj         = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)

        # pass hProcess to process object to get process result
        rc          = win32process.GetExitCodeProcess(procHandle)
    else:

        # if wait is False set process to None
        rc          = None

    # return True if everything is alright
    return True
