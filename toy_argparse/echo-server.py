#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import subprocess

def has_echo():

    # check for command presence
    if not shutil.which('echo'):
        print('error: Missing `echo` binary.')
        return False

    return True


def echo():
    """ runs echo with --request

    """

    #print(fortunefile)
    if not has_echo():
        return

    try:
        echo = subprocess.check_output(['echo', 'foo']).decode("utf-8")
    except subprocess.CalledProcessError:
        raise ValueError('echo did not run')
    print(echo)
    return

if __name__ == '__main__':

    echo()

