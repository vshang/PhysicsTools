#!/bin/sh
#Script to run combine to produce expected limits

set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
scram project CMSSW CMSSW_8_0_26_patch1
tar -zxvf Analysis2018_tttDM2b.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf HiggsAnalysis.tar.gz
cd CMSSW_8_0_26_patch1/src
scram b
eval `scram runtime -sh`
cd ../../condor_Analysis
chmod +x submit*.txt
./submit_AH_pseudo250.txt
mv *.root ../
mv limitOutput_ModuleCommonSkim_*/*.txt ../
