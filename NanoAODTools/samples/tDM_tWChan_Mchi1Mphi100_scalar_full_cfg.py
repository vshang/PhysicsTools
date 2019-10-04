# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM --fileout file:tDM_tWChan_Mchi1Mphi100_scalar_full.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 102X_mcRun2_asymptotic_v7 --step NANO --nThreads 2 --era Run2_2016,run2_miniAOD_80XLegacy --python_filename tDM_tWChan_Mchi1Mphi100_scalar_full_cfg.py --no_exec --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False))) -n -1
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2016,eras.run2_miniAOD_80XLegacy)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/9EE0DD92-4CEE-E711-AAD9-FA163E8AA331.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/C4DF6B92-C4F0-E711-9327-FA163E4483B6.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/BE999CBD-0CF3-E711-8A1E-0025905C9726.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/28A66DC6-0CF3-E711-A2CD-2047478D3CC8.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/F019C4E3-0CF3-E711-96BB-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/340AA1AA-0CF3-E711-953B-0425C5923ACA.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/88BB40DD-0CF3-E711-A3A1-0CC47A2B0700.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/36F911A4-BFF3-E711-B753-E0071B7AC750.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/A09305FB-0CF3-E711-91A6-008CFAC94220.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/08BA56AD-0CF3-E711-90ED-001E67E6F904.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/5C3226B2-0CF3-E711-929B-008CFAF74750.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/5A8B5049-0DF3-E711-9C02-001E67580724.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/148E64BA-0CF3-E711-9A6E-0026B94DBDD6.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/2EF2D308-0DF3-E711-9B1C-0025905B8606.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/AE6073E4-0CF3-E711-A505-B083FED42A6D.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/E4978DB2-0CF3-E711-9610-D4AE5269F5FF.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/A4280CE9-29F3-E711-95F8-002590747D9C.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/9E47A884-0BF3-E711-B5E6-FA163EB03992.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/00000/96D6BA8E-0DF3-E711-AE52-002481DE47D0.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tWChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/10000/FE5060FE-F4F5-E711-A38D-1866DA890B94.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:tDM_tWChan_Mchi1Mphi100_scalar_full.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mcRun2_asymptotic_v7', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(2)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# End of customisation functions

# Customisation from command line

process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
