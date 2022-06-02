#!/bin/sh
#Script to run combine to produce expected limits

set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_8_0_26_patch1
tar -zxvf Analysis_test.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf HiggsAnalysis.tar.gz
cd CMSSW_8_0_26_patch1/src
scram b
eval `scram runtime -sh`
cd ../../condor_Analysis_test
chmod +x submit*.txt
./submit_ALL.txt
mv *.root ../
mv limitOutput_*/*.txt ../
