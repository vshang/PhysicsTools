#!/bin/sh
# cleandir.sh
# Script to remove directories and files from previous jobs to prepare for new job submission
echo "Removing rootfiles..."
rm */*.root
echo "DONE removing rootfiles."
echo "Removing text files..."
rm */*.txt
echo "DONE removing text files."
echo "Removing submit directories..."
rm -rf */RunII*
echo "DONE removing submit directories."
