#!/bin/sh
# cleandir.sh
# Script to remove directories and files from previous jobs to prepare for new job submission
echo "Removing submit directories..."
rm -rf ModuleCommon*
rm -rf */tChan*
rm -rf */tWChan*
rm -rf */ttDM*
rm -rf */ttH*
echo "DONE removing submit directories."
