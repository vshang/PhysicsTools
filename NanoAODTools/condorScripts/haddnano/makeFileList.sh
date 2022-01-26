#!/bin/sh
rm -f filelist.txt
for FILE in  /hdfs/store/user/vshang/*/*/ModuleCommonSkim_01182022/*/0000/*.root; do
#for FILE in  /hdfs/store/user/vshang/*/*/ModuleCommonSkim_01182021/; do

    # mv "${FILE}" "${FILE/ModuleCommonSkim_01182021/ModuleCommonSkim_01182022}"

  # if no file matched the wildcards, do not output anything
  if ! [ -e "$FILE" ]; then continue; fi


  # trim off leading /hdfs

  FILE=$(echo $FILE | sed 's|^/hdfs||')


  echo root://cmsxrootd.hep.wisc.edu/$FILE >> filelist.txt
done
