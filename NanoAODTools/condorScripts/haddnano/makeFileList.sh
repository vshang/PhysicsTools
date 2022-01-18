#!/bin/sh
rm -f filelist.txt
for FILE in  /hdfs/store/user/vshang/*/*/ModuleCommonSkim_11292021/*/0000/*.root; do

  # if no file matched the wildcards, do not output anything
  if ! [ -e "$FILE" ]; then continue; fi


  # trim off leading /hdfs

  FILE=$(echo $FILE | sed 's|^/hdfs||')


  echo root://cmsxrootd.hep.wisc.edu/$FILE >> filelist.txt
done
