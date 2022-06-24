#!/bin/sh
#Script to merge nanoAOD root files using haddnano.py
set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
scram project CMSSW CMSSW_10_6_9
cd CMSSW_10_6_9
eval `scram runtime -sh`
cd ..
chmod u+x haddnano.py
#./haddnano.py tree_DMScalar_top_tChan_Mchi1_all.root /hdfs/store/user/vshang/_Run2017//ModuleCommonSkim_06102022/*/*/tree*.root

./haddnano.py tree_ttbardm_10GeV_scalar_all.root $(./filterList_signal.py "ttbarDM_Run2017/ttbardm_10GeV_scalar_incl_2017_nanoaod")
./haddnano.py tree_ttbardm_10GeV_pseudo_all.root $(./filterList_signal.py "ttbarDM_Run2017/ttbardm_10GeV_pseudo_incl_2017_nanoaod")

#Copy output files directly to hdfs
#env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Single_Run2017/MET/ModuleCommonSkim_06102022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbardm_10GeV_scalar_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2017/ttbardm_10GeV_scalar_incl_2017_nanoaod/ModuleCommonSkim_06102022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbardm_10GeV_pseudo_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2017/ttbardm_10GeV_pseudo_incl_2017_nanoaod/ModuleCommonSkim_06102022/tree_all.root

#prevent condor from also transferring the output files back to the submit directory:
rm *.root
