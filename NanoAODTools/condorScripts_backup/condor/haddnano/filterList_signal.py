#!/bin/env python
import sys

if len(sys.argv) != 2:
    print("Syntax: filterList_signal.py filename")
filename = sys.argv[1]

f = open("filelist_signal.txt","r")
#f = open("countlist_signal.txt","r")
mylines = f.readlines()

for line in mylines:
    if filename in line:
        print line
