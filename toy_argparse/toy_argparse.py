# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 12:45:41 2016

@author: fred
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', help = "target file or directory for NER")
parser.add_argument('--outfile', help = "target file for output")
parser.add_argument('--uuid', help = "uuid")
args = parser.parse_args()

infile = args.path
outfile = args.outfile
uuid = args.uuid

print(infile)
print(outfile)
print(uuid)