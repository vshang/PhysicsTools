#!/bin/env python
import sys

if len(sys.argv) != 2:
    print("Syntax: filterList.py filename")
filename = sys.argv[1]

f = open("filelist.txt","r")
mylines = f.readlines()

for line in mylines:
    if filename in line:
        print line
