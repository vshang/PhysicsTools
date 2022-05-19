#!/bin/sh
#Script to run combine to produce expected limits

set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_8_0_26_patch1
tar -zxvf Analysis.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf HiggsAnalysis.tar.gz
cd CMSSW_8_0_26_patch1/src
scram b
eval `scram runtime -sh`
cd ../../condor_Analysis
chmod +x submit*.txt
./submit_ALL_scalar450.txt
mv *.root ../
mv limitOutput_ModuleCommonSkim_03092022_RunIIFull/*.txt ../
