#!/bin/sh
#Script to merge nanoAOD root files using haddnano.py
set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
scram project CMSSW CMSSW_10_6_9
cd CMSSW_10_6_9
eval `scram runtime -sh`
cd ..
chmod u+x ./haddnano.py
#./haddnano.py tree__Run2017.root /hdfs/store/user/vshang/WW_Run2016//ModuleCommonSkim_03182021/*/*/tree*.root

./haddnano.py tree_MET_RunUL2017B_all.root /hdfs/store/user/vshang/MET_RunUL2017B/MET/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_MET_RunUL2017C_all.root /hdfs/store/user/vshang/MET_RunUL2017C/MET/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_MET_RunUL2017D_all.root /hdfs/store/user/vshang/MET_RunUL2017D/MET/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_MET_RunUL2017E_all.root /hdfs/store/user/vshang/MET_RunUL2017E/MET/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_MET_RunUL2017F_all.root /hdfs/store/user/vshang/MET_RunUL2017F/MET/ModuleCommonSkim_09222021/*/*/tree*.root

./haddnano.py tree_QCD_Pt_15to30_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_30to50_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_50to80_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_80to120_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_120to170_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_170to300_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_300to470_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_470to600_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_600to800_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_800to1000_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1000to1400_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1400to1800_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1800to2400_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_2400to3200_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root
./haddnano.py tree_QCD_Pt_3200toInf_RunUL2017_all.root /hdfs/store/user/vshang/QCD_RunUL2017/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/*/*/tree*.root

#Copy output files directly to hdfs
#env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Single_Run2017/MET/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2017B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2017B/MET/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2017C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2017C/MET/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2017D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2017D/MET/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2017E_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2017E/MET/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_RunUL2017F_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_RunUL2017F/MET/ModuleCommonSkim_09222021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_15to30_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_30to50_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_50to80_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_80to120_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_120to170_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_170to300_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_300to470_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_470to600_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_600to800_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_800to1000_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1000to1400_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1400to1800_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1800to2400_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_2400to3200_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_3200toInf_RunUL2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_RunUL2017/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/ModuleCommonSkim_09222021/tree_all.root

#prevent condor from also transferring the output files back to the submit directory:
rm *.root
