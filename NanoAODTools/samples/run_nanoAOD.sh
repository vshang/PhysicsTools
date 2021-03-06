#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_15/src ] ; then 
 echo release CMSSW_10_2_15 already exists
else
scram p CMSSW CMSSW_10_2_15
fi
cd CMSSW_10_2_15/src
eval `scram runtime -sh`

scram b
cd ../../
cmsDriver.py step1 --filein "dbs:/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM" --fileout file:tDM_tWChan_Mchi1Mphi100_scalar_fullv2.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 102X_mcRun2_asymptotic_v7 --step NANO --nThreads 2 --era Run2_2016,run2_miniAOD_80XLegacy --python_filename tDM_tWChan_Mchi1Mphi100_scalar_fullv2_cfg.py --no_exec --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))" -n -1 || exit $? ; 
