#!/bin/sh
# cleandir.sh
# Script to remove directories and files from previous jobs to prepare for new job submission
echo "Removing rootfiles..."
rm */*.root
echo "DONE removing rootfiles."
echo "Removing other files (text, pdf, png)..."
rm */*.txt
rm */*.pdf
rm */*.png
rm */*~
rm *~
echo "DONE removing text files."
echo "Removing submit directories..."
rm -rf */scalar*
rm -rf */pseudo*
echo "DONE removing submit directories."
