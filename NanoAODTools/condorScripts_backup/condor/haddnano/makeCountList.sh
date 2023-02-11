#!/bin/sh
rm -f countlist.txt
for FILE in  /hdfs/store/user/vshang/*/*/countEvents_12242022/*/0000/*.root; do

  # if no file matched the wildcards, do not output anything
  if ! [ -e "$FILE" ]; then continue; fi


  # trim off leading /hdfs

  FILE=$(echo $FILE | sed 's|^/hdfs||')


  echo root://cmsxrootd.hep.wisc.edu/$FILE >> countlist.txt
done
