#Script to write and save json files for MC and Data sample lists containing number of gen events (taking into account genWeightSign)
from ROOT import *
from MCsampleListv2 import *
from DataSampleListv2 import *
import json

MCsampleList = [samples2016, samples2017, samples2018]
DataSampleList = [data2016, data2017, data2018]

#Get MC background root files and event trees
signal = ['ttbar scalar', 'ttbar pseudoscalar', 'tbar scalar', 'tbar pseudoscalar']
year = 2016
for MCSamples in MCsampleList:
    print('Loading MC sample root files and event trees for ' + str(year) + '...')
    for process in MCSamples:
        print 'Loading process: ', process
        for dataset in MCSamples[process]:
            nevents = 0
            print '    ----Loading', dataset
            for filepath in MCSamples[process][dataset]['filepaths']:
                #Add events with positive genWeight and subtract events with negative genWeight
                File = TFile.Open(filepath,'')
                Events = File.Get('Events')
                if (process in signal) and ('ttbar' in process) and ('MPhi125_scalar' not in dataset) and ('MPhi10_' not in dataset):
                    skimFile = TFile.Open(filepath.replace('ModuleCommonSkim_02092023','countEvents_02092023'),'')
                    Mchi = MCSamples[process][dataset]['mchi']
                    Mphi = MCSamples[process][dataset]['mphi']
                    MediatorType = MCSamples[process][dataset]['mediatorType']
                    signalType = 'TTbarDMJets'
                    nevents += skimFile.Get('Events').GetEntries('GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8&&(genWeight>0)') - skimFile.Get('Events').GetEntries('GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8&&(genWeight<0)')   
                elif (process in ['tbar scalar','tbar pseudoscalar']):
                    runsTree = File.Get('Runs')
                    nRuns = runsTree.GetEntries()
                    for i in range(nRuns):
                        runsTree.GetEntry(i)
                        nevents += runsTree.genEventCount
                else:
                    skimFile = TFile.Open(filepath.replace('ModuleCommonSkim_02092023', 'countEvents_02092023'),'')
                    nevents += skimFile.Get('Events').GetEntries('genWeight>0') - skimFile.Get('Events').GetEntries('genWeight<0')
            MCSamples[process][dataset]['nevents'] = nevents
            print '    nevents in ', process, ' ', dataset, ': ', nevents
    print('Got MC sample root files and event trees for ' + str(year))
    with open('samples'+str(year)+'v2.json','w') as f:
        json.dump(MCSamples, f)
    print('Wrote MC sample json file for ' + str(year))
    year += 1

year = 2016
for dataSamples in DataSampleList:
    print('Loading data sample root files and event trees for ' + str(year) + '...')
    for dataset in dataSamples:
        nevents = 0
        for filepath in dataSamples[dataset]['filepaths']:
            print '    ----Loading', filepath
            File = TFile.Open(filepath,'')
            Events = File.Get('Events')
            dataset_nevents = Events.GetEntries()
            nevents += dataset_nevents
            print '    nevents in filepath = ' + filepath + ': ' + str(dataset_nevents)
        dataSamples[dataset]['nevents'] = nevents
        print '    total nevents in ', dataset, ': ', nevents
    print('Got data sample root files and event trees')
    with open('data'+str(year)+'v2.json','w') as f:
        json.dump(dataSamples, f)
    print('Wrote Data sample json file for ' + str(year))
    year += 1
