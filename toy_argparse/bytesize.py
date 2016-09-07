# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:44:35 2016

@author: fred
"""
import subprocess
import sys

def fortune(fortunefile1, fortunefile2):
    result = subprocess.check_output(['fortune', fortunefile1, fortunefile2]).decode('utf-8')
    print(result)
    return fortune


if __name__ == '__main__':
    fortunefile1 = sys.argv[1]
    fortunefile2 = sys.argv[2]
    fortune(fortunefile1, fortunefile2)
