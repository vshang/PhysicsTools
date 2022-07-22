#!/bin/sh
#Script to run combine to produce expected limits

set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_8_0_26_patch1
tar -zxvf Analysis_ttDM.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf HiggsAnalysis.tar.gz
cd CMSSW_8_0_26_patch1/src
scram b
eval `scram runtime -sh`
cd ../../condor_Analysis
chmod +x submit*.txt
./submit_ALL_pseudo350.txt
mv *.root ../
mv limitOutput_ModuleCommonSkim_06102022_*/*.txt ../
