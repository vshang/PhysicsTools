# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM --fileout file:tDM_tChan_Mchi1Mphi100_scalar_full.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 102X_mcRun2_asymptotic_v7 --step NANO --nThreads 2 --era Run2_2016,run2_miniAOD_80XLegacy --python_filename tDM_tChan_Mchi1Mphi100_scalar_full_cfg.py --no_exec --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False))) -n -1
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
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/CAB746AF-20A1-E711-A4F3-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/240EB337-A2A2-E711-B9EF-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/74A700EF-C2A2-E711-BE95-008CFAC93D6C.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/56EABC2C-E9A3-E711-99AC-008CFAE45080.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/6CFB0FAF-A7A2-E711-92E9-00259022277E.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/661D0373-4EA1-E711-9F58-FA163E84E4DC.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/50C65BA9-8FA2-E711-A41A-FA163EF56B4F.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/E83E1784-A7A2-E711-B8A8-FA163E81A06D.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/FC056439-A2A2-E711-9625-0CC47A7C3410.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/9A3207FC-ADA2-E711-ABDE-0CC47A4D762A.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/0E657944-5BA3-E711-9389-3417EBE51CDF.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/78225C44-5BA3-E711-A227-3417EBE51CDF.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/000A3D35-A2A2-E711-BB96-0CC47AF9B2D2.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/C0F6A787-549F-E711-B85F-02163E011C75.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/20FA5463-BAA2-E711-84FE-D4856459AC30.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/AA089F4C-A8A2-E711-B982-02163E01A2C7.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/BEA0BA35-71A6-E711-B2F2-0090FAA57F74.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/224D425D-74A7-E711-AC2D-FA163E487DBA.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/084ACB6E-74A7-E711-9865-FA163EA1B59C.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/CE8E66A1-73A7-E711-BFDC-FA163E2BF056.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/6200AD22-C9A2-E711-AE06-0242AC110002.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/5E5E3A43-ADA2-E711-ADC1-0CC47A1DF800.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/6E1E90AD-B3A2-E711-914A-001E675817A4.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/C0C59993-8DA3-E711-87E4-D8D385AF8B7A.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/02692C94-E8A2-E711-86B8-008CFAF74780.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/C4DBA75D-A1A2-E711-B4EC-001E67E6F760.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/6248BD7A-AAA2-E711-9AAB-1CB72C1B649A.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/CE5F15C0-8EA2-E711-AC32-003048CB7B30.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/1E6484EC-94A2-E711-99A3-002590E2DDC8.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/A4781363-2EA5-E711-97F4-FA163E3EE588.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/90EFBC10-62A3-E711-B2A4-3417EBE64BBE.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/F68909C0-6FA3-E711-80F5-FA163EF96018.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/BE9D1624-7DA3-E711-83F8-FA163E4934DD.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/7429899C-92A2-E711-9124-A0369FC5ED30.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/56697158-90A2-E711-9B98-90B11C12E856.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/56813580-91A2-E711-B0F4-0CC47A5FBE31.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/18312E5E-8AA2-E711-9903-1866DAEECF18.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/DE9739BB-4BA1-E711-B9F5-24BE05C6C7E1.root', 
        '/store/mc/RunIISummer16MiniAODv2/TopDMJets_scalar_tChan_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/70000/182F11D5-96A2-E711-BDA6-24BE05C6E571.root'
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
    fileName = cms.untracked.string('file:tDM_tChan_Mchi1Mphi100_scalar_full.root'),
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
