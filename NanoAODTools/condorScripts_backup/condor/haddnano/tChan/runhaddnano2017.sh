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
#./haddnano.py tree_DMScalar_top_tChan_Mchi1_all.root /hdfs/store/user/vshang/_Run2017//countEvents_02092023/*/*/tree*.root

./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi10_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi10_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi50_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi50_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi100_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi100_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi150_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi150_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi200_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi200_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi250_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi250_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi300_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi300_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi350_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi350_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi400_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi400_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi450_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi450_")
./haddnano.py tree_DMScalar_top_tChan_Mchi1_Mphi500_all.root $(./filterList_signal.py "tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi500_")

./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi10_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi10_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi50_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi50_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi100_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi100_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi150_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi150_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi200_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi200_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi250_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi250_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi300_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi300_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi350_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi350_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi400_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi400_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi450_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi450_")
./haddnano.py tree_DMPseudo_top_tChan_Mchi1_Mphi500_all.root $(./filterList_signal.py "tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi500_")

#Copy output files directly to hdfs
#env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Single_Run2017/MET/countEvents_02092023/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi10_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi10_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi50_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi50_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi100_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi100_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi150_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi150_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi200_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi200_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi250_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi250_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi300_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi300_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi350_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi350_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi400_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi400_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi450_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi450_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMScalar_top_tChan_Mchi1_Mphi500_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMScalar_top_tChan_Mchi1_Mphi500_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi10_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi10_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi50_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi50_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi100_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi100_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi150_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi150_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi200_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi200_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi250_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi250_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi300_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi300_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi350_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi350_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi400_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi400_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi450_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi450_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DMPseudo_top_tChan_Mchi1_Mphi500_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/tDM_Run2017/DMPseudo_top_tChan_Mchi1_Mphi500_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02092023/tree_all.root

#prevent condor from also transferring the output files back to the submit directory:
rm *.root
