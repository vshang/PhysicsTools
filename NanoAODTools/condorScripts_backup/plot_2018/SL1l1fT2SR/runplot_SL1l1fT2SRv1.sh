#!/bin/sh
#Script to merge nanoAOD root files using haddnano.py
set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_10_6_9
cd CMSSW_10_6_9
eval `scram runtime -sh`
cd ..
python plot2018.py -c SL1l1fT2SR -f
rm MCsampleList.py*
rm DataSampleList.py*
rm utils.py*
