#!/bin/sh
#Script to run combine to produce expected limits

set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_8_0_26_patch1
tar -zxvf Analysis_pulls.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf HiggsAnalysis.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf CombineHarvester.tar.gz
cd CMSSW_8_0_26_patch1/src
scram b
eval `scram runtime -sh`
cd ../../condor_Analysis_pulls
chmod +x *.sh
./runPulls_Victor.sh
mv *.root ../
