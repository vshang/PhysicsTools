#Script to check and compare genEventCounts between default samples (ModuleCommonSkim) and samples used for normalization (countEvents)
from ROOT import *
from plots.MCsampleList import *

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
        nevents_ModuleCommonSkim = 0
        nevents_countEvents = 0
        print '    ----Loading', dataset
        for filepath in MCSamples[process][dataset]['filepaths']:
            MCSamples[process][dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            MCSamples[process][dataset][filepath+'_Events'] = MCSamples[process][dataset][filepath+'_TFile'].Get('Events')
            if (process in signal) and ('ttbar' in process) and ('MPhi125_scalar' not in dataset) and ('MPhi10_' not in dataset):
                skimFile = TFile.Open(filepath.replace('ModuleCommonSkim_02062024', 'countEvents_02062024'))#.replace('ModuleCommonSkim_12242022', 'countEvents_12242022'),'')
                Mchi = MCSamples[process][dataset]['mchi']
                Mphi = MCSamples[process][dataset]['mphi']
                MediatorType = MCSamples[process][dataset]['mediatorType']
                signalType = 'TTbarDMJets'
                nevents_ModuleCommonSkim += skimFile.Get('Events').GetEntries('GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8')
                nevents_countEvents += skimFile.Get('Events').GetEntries('GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8')
            elif process not in ['tbar scalar', 'tbar pseudoscalar']:
                runsTree = MCSamples[process][dataset][filepath+'_TFile'].Get('Runs')
                nRuns = runsTree.GetEntries()
                for i in range(nRuns):
                    runsTree.GetEntry(i)
                    nevents_ModuleCommonSkim += runsTree.genEventCount
                skimFile = TFile.Open(filepath.replace('ModuleCommonSkim_02062024', 'countEvents_02062024'))#.replace('ModuleCommonSkim_12242022', 'countEvents_12242022'),'')
                nevents_countEvents += skimFile.Get('Events').GetEntries()
            else:
                runsTree = MCSamples[process][dataset][filepath+'_TFile'].Get('Runs')
                nRuns = runsTree.GetEntries()
                for i in range(nRuns):
                    runsTree.GetEntry(i)
                    nevents_ModuleCommonSkim += runsTree.genEventCount
                nevents_countEvents = -1
        print '    nevents_ModuleCommonSkim in ', process, ' ', dataset, ': ', nevents_ModuleCommonSkim
        print '    nevents_countEvents in ', process, ' ', dataset, ': ', nevents_countEvents
        print '    DIFFERENCE: ', nevents_countEvents - nevents_ModuleCommonSkim
        if ((nevents_countEvents - nevents_ModuleCommonSkim) != 0) and nevents_countEvents > -1:
            print '    ERROR: nevents in ModuleCommonSkim and countEvents do not match!'
print('Got MC sample root files and event trees')
