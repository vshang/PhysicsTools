#!/bin/sh
# cleandir.sh
# Script to remove directories and files from previous jobs to prepare for new job submission
echo "Removing rootfiles..."
rm *.root
rm */*.root
echo "DONE removing rootfiles."
echo "Removing submit directories..."
rm -rf */*v1
rm -rf */*v2
echo "DONE removing submit directories."
