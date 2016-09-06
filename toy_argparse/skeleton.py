#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
import shutil
import subprocess
import sys

def has_fortune():

    # check for command presence
    if not shutil.which('fortune'):
        print('error: Missing `fortune` binary.')
        return False

    return True


def fortune(fortunefile):
    """ runs fortune against fortunefile

    Args:
        fortunefile (str): name of fortunefile

    Raises:
        ValueError: if the url is malformed or ping cannot be performed on it.
    Returns:
        dict: A dictionary containing ping information.

    """

    #print(fortunefile)
    if not has_fortune():
        return

    try:
        fortune = subprocess.check_output(['fortune', fortunefile]).decode("utf-8")
    except subprocess.CalledProcessError:
        raise ValueError('fortune failed on database name' + fortunefile)
    # = fortune.decode(UTF-8)
    print(fortune)
    return

if __name__ == '__main__':

    fortunefile = sys.argv[1]
    data = fortune(fortunefile)

