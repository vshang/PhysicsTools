#!/bin/sh
#Script to merge nanoAOD root files using haddnano.py
set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_10_6_9
cd CMSSW_10_6_9
eval `scram runtime -sh`
cd ..
chmod u+x ./haddnano.py
#./haddnano.py tree__Run2018.root /hdfs/store/user/vshang/WW_Run2018//ModuleCommonSkim_03182021/*/*/tree*.root

./haddnano.py tree_MET_RunUL2018A_all.root /hdfs/store/user/vshang/MET_RunUL2018A/MET/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_MET_RunUL2018B_all.root /hdfs/store/user/vshang/MET_RunUL2018B/MET/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_MET_RunUL2018C_all.root /hdfs/store/user/vshang/MET_RunUL2018C/MET/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_MET_RunUL2018D_all.root /hdfs/store/user/vshang/MET_RunUL2018D/MET/ModuleCommonSkim_09222021/*/*/tree*.root

./haddnano.py tree_QCD_Pt_15to30_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_30to50_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_50to80_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_80to120_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_120to170_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_170to300_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_300to470_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_470to600_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_600to800_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_800to1000_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1000to1400_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1400to1800_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1800to2400_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_2400to3200_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_3200toInf_RunUL2018_all.root /hdfs/store/user/vshang/QCD_RunUL2018/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root

#Copy output files directly to hdfs
#env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Single_Run2018/MET/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2018A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2018A/MET/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2018B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2018B/MET/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2018C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2018C/MET/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2018D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2018D/MET/ModuleCommonSkim_09222021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_15to30_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_30to50_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_50to80_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_80to120_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_120to170_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_170to300_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_300to470_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_470to600_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_600to800_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_800to1000_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1000to1400_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1400to1800_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1800to2400_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_2400to3200_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_3200toInf_RunUL2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2018/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root

#prevent condor from also transferring the output files back to the submit directory:
rm *.root
