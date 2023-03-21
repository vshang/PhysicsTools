#!/bin/sh
rm -f filelist_signal.txt
#Add tDM signal samples first
for FILE in  /hdfs/store/user/vshang/tDM_Run*/*/ModuleCommonSkim_12242022/rootFiles/*Skim.root; do

  # if no file matched the wildcards, do not output anything
  if ! [ -e "$FILE" ]; then continue; fi


  # trim off leading /hdfs

  FILE=$(echo $FILE | sed 's|^/hdfs||')


  echo root://cmsxrootd.hep.wisc.edu/$FILE >> filelist_signal.txt
done
#Then add Mphi1_Mchi10 ttbarDM signal samples
for FILE in  /hdfs/store/user/vshang/ttbarDM_Run*/ttbardm*/ModuleCommonSkim_12242022/rootFiles/*Skim.root; do

  # if no file matched the wildcards, do not output anything
  if ! [ -e "$FILE" ]; then continue; fi


  # trim off leading /hdfs

  FILE=$(echo $FILE | sed 's|^/hdfs||')


  echo root://cmsxrootd.hep.wisc.edu/$FILE >> filelist_signal.txt
done
#Finally add nanoAODv7 ttH 2016 signal samples
for FILE in  /hdfs/store/user/vshang/ttH_Run2016/ttH_*nanoAODv7/ModuleCommonSkim_12242022/rootFiles/*Skim.root; do

  # if no file matched the wildcards, do not output anything
  if ! [ -e "$FILE" ]; then continue; fi


  # trim off leading /hdfs

  FILE=$(echo $FILE | sed 's|^/hdfs||')


  echo root://cmsxrootd.hep.wisc.edu/$FILE >> filelist_signal.txt
done