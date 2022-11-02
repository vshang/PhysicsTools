#!/bin/sh
# cleandir.sh
# Script to remove directories and files from previous jobs to prepare for new job submission
echo "Removing rootfiles..."
rm */*.root
echo "DONE removing rootfiles."
echo "Removing other files (text, pdf, png)..."
rm *.out
rm *.err
rm *.log
echo "DONE removing other files."
