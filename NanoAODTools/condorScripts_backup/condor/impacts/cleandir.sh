#!/bin/sh
# cleandir.sh
# Script to remove directories and files from previous jobs to prepare for new job submission
echo "Removing temporary files..."
rm -rf *tDM*
rm *~
echo "DONE removing other files."
