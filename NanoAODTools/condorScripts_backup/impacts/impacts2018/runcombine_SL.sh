#!/bin/sh
#Script to run combine to produce expected limits

set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_8_0_26_patch1
tar -zxvf Analysis_test.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf HiggsAnalysis.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf CombineHarvester.tar.gz
cd CMSSW_8_0_26_patch1/src
scram b
eval `scram runtime -sh`
cd ../../condor_Analysis_test
chmod +x *.sh
./runImpacts.sh combinedCards_ModuleCommonSkim_06102022_2018 combinedCards_ModuleCommonSkim_06102022_2018/tttDM_MChi1_MPhi100_scalar1b2b_SL.txt
mv combinedCards_*/*.png ../
mv combinedCards_*/*.pdf ../
rm *.root
