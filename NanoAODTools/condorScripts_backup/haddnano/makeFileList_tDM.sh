#!/bin/sh
rm -f filelist_tDM.txt
for FILE in  /hdfs/store/user/vshang//tDM_Run*/*/ModuleCommonSkim_03092022/rootFiles/NANOAOD_*.root; do

  # if no file matched the wildcards, do not output anything
  if ! [ -e "$FILE" ]; then continue; fi


  # trim off leading /hdfs

  FILE=$(echo $FILE | sed 's|^/hdfs||')


  echo root://cmsxrootd.hep.wisc.edu/$FILE >> filelist_tDM.txt
done
