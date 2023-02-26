#Script to check and compare genEventCounts between default samples (ModuleCommonSkim) and samples used for normalization (countEvents)
from ROOT import *
from plots.MCsampleListv2 import *

#Set year 
year = 2018

if year == 2016:
    MCSamples = samples2016
elif year == 2017:
    MCSamples = samples2017
elif year == 2018:
    MCSamples = samples2018

#Get MC background root files and event trees
signal = ['ttbar scalar', 'ttbar pseudoscalar', 'tbar scalar', 'tbar pseudoscalar']
print('Loading MC sample root files and event trees...')
for process in MCSamples:
    print 'Loading process: ', process
    for dataset in MCSamples[process]:
        nevents_ModuleCommonSkimNeg = 0
        nevents_countEvents = 0
        print '    ----Loading', dataset
        for filepath in MCSamples[process][dataset]['filepaths']:
            MCSamples[process][dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            MCSamples[process][dataset][filepath+'_Events'] = MCSamples[process][dataset][filepath+'_TFile'].Get('Events')
            if (process in signal) and ('ttbar' in process) and ('MPhi125_scalar' not in dataset) and ('MPhi10_' not in dataset):
                skimFile = TFile.Open(filepath.replace('ModuleCommonSkim_02092023', 'countEvents_02092023'),'')
                Mchi = MCSamples[process][dataset]['mchi']
                Mphi = MCSamples[process][dataset]['mphi']
                MediatorType = MCSamples[process][dataset]['mediatorType']
                signalType = 'TTbarDMJets'
                nevents_countEvents += skimFile.Get('Events').GetEntries('GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8&&(genWeight<0)')
                nevents_ModuleCommonSkimNeg += MCSamples[process][dataset][filepath+'_Events'].GetEntries('GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8&&(genWeightSign<0)')
            #elif process not in signal:
            elif process not in ['tbar scalar', 'tbar pseudoscalar']:
                skimFile = TFile.Open(filepath.replace('ModuleCommonSkim_02092023', 'countEvents_02092023'),'')
                nevents_countEvents += skimFile.Get('Events').GetEntries('genWeight<0')
                nevents_ModuleCommonSkimNeg += MCSamples[process][dataset][filepath+'_Events'].GetEntries('genWeightSign<0')
            else:
                nevents_countEvents = -1
                nevents_ModuleCommonSkimNeg += MCSamples[process][dataset][filepath+'_Events'].GetEntries('genWeightSign<0')
        print '    nevents with negative genWeight using countEvents in ', process, ' ', dataset, ': ', nevents_countEvents
        print '    nevents with negative genWeightSign using ModuleCommonSkim in ', process, ' ', dataset, ': ', nevents_ModuleCommonSkimNeg
        if nevents_countEvents > 0 or nevents_ModuleCommonSkimNeg > 0:
            print '    WARNING: NEGATIVE GENWEIGHTSIGN SPOTTED'
print('Got MC sample root files and event trees')
