from ROOT import *
from METTriggerSampleList import *
import os
import datetime
import re
import math

gErrorIgnoreLevel = kError
year = 2016
#Choose samples to use based on run year (stored in MCsampleList.py and DataSampleList.py)
if year == 2016:
    samples = samples2016
elif year == 2017:
    samples = samples2017
elif year == 2018:
    samples = samples2018

print 'Code start time:', datetime.datetime.now()

#Define selection cuts and filters here
cuts = {}

if year == 2016:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter'
    cuts['singleIsoEle'] = 'HLT_Ele27_WPTight_Gsf'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon175'
    cuts['singleIsoMu'] = 'HLT_IsoMu24 || HLT_IsoTkMu24'
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMET120_PFMHT120_IDTight || HLT_PFMET170_HBHECleaned || HLT_PFMET170_BeamHaloCleaned'
elif year == 2017:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2'
    cuts['singleIsoEle'] = 'passEle32WPTightGsf2017'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
    cuts['singleIsoMu'] = 'HLT_IsoMu27' 
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60 || HLT_PFMET120_PFMHT120_IDTight || HLT_PFMET120_PFMHT120_IDTight_PFHT60 || HLT_PFMET200_HBHECleaned || HLT_PFMET200_HBHE_BeamHaloCleaned'
elif year == 2018:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2'
    cuts['singleIsoEle'] = 'HLT_Ele32_WPTight_Gsf'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
    cuts['singleIsoMu'] = 'HLT_IsoMu24' 
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60 || HLT_PFMET120_PFMHT120_IDTight || HLT_PFMET120_PFMHT120_IDTight_PFHT60 || HLT_PFMET200_HBHECleaned || HLT_PFMET200_HBHE_BeamHaloCleaned'

#Cut definitions
cuts['1eDenom'] = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['1mDenom'] = 'nTightMuons == 1 && nLooseMuons == 1 && nVetoElectrons == 0 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['1eNum'] = cuts['1eDenom'] + ' && (' + cuts['MET'] + ')'
cuts['1mNum'] = cuts['1mDenom'] + ' && (' + cuts['MET'] + ')'

#Set lum (fb^-1) here 
if year == 2016:
    lumi = 35.92
elif year == 2017:
    lumi = 41.53
elif year == 2018:
    lumi = 59.83

##Create histograms
##-----------------------------------------------------------------------------------------------

print("Creating histograms..")

#Set histogram options
var = 'METcorrected_pt'
nbins = 100
xmin = 150
xmax = 650
ymin = 0
ymax = 1
saveRootFiles = True
savePlots = True

histoLabel = '; p_{T}^{miss} (GeV); Efficiency'

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Define efficiency histograms
histNames = ['1eNumData', '1eDenomData', '1eEffData', '1mNumData', '1mDenomData', '1mEffData', '1eNumMC', '1eDenomMC', '1eEffMC', '1mEffData', '1mNumMC', '1mDenomMC', '1mEffMC', '1eEffRatio', '1mEffRatio']
hists = {}
for name in histNames:
    hists[name] = TH1F(name, histoLabel, nbins, xmin, xmax)

#Get data root files and event trees
dataSamples = ['SingleElectron', 'SingleMuon']
print("Loading data sample root files and event trees...")
for dataset in dataSamples:
    nevents = 0
    for filepath in samples[dataset]['filepaths']:
        samples[dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
        samples[dataset][filepath+'_Events'] = samples[dataset][filepath+'_TFile'].Get('Events')
        nevents += samples[dataset][filepath+'_Events'].GetEntries()
    samples[dataset]['nevents'] = nevents
    print '   nevents in ', dataset, ': ', nevents
print("Got data sample root files and event trees")

#Get WPlusJets MC root files and event trees
print("Loading WPlusJets MC sample root files and event trees...")
for HTbin in samples['WPlusJets']:
    nevents = 0
    for filepath in samples['WPlusJets'][HTbin]['filepaths']:
        samples['WPlusJets'][HTbin][filepath+'_TFile'] = TFile.Open(filepath,'')
        samples['WPlusJets'][HTbin][filepath+'_Events'] = samples['WPlusJets'][HTbin][filepath+'_TFile'].Get('Events')
        skimFile = TFile.Open(filepath.replace('ModuleCommonSkim_03182021', 'countEvents_03182021'),'')
        nevents += skimFile.Get('Events').GetEntries()
    samples['WPlusJets'][HTbin]['nevents'] = nevents
    print '    nevents in WPlusJets ', HTbin, ': ', nevents
print("Got WPlusJets MC sample root files and event trees")

#Fill histograms
print("Filling histograms...")
#Loop through each root file for each dataset
for dataset in dataSamples:
    print '  Dataset = ', dataset, ' ||   nEvents = ', samples[dataset]['nevents']
    if dataset == 'SingleElectron':
        prefix = '1e'
    elif dataset == 'SingleMuon':
        prefix = '1m'
    for filepath in samples[dataset]['filepaths']:
        #Only apply ee badSC noise filter to data (https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2)
        datacutNum = cuts[prefix+'Num'] + ' && Flag_eeBadScFilter'
        datacutDenom = cuts[prefix+'Denom'] + ' && Flag_eeBadScFilter'
        if 'SingleElectron_Run2017B' in filepath: #HLT_Ele115_CaloIdVT_GsfTrkIdT trigger path not available in Run2017B (https://hypernews.cern.ch/HyperNews/CMS/get/b2g-selections/346.html?inline=-1)
            datacutNum = datacutNum.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || ','')
            datacutDenom = datacutDenom.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || ','')
        if 'MET_Run2017B' in filepath: #MET trigger paths also missing from Run2017B (https://hypernews.cern.ch/HyperNews/CMS/get/top-trigger/247/1.html)
            datacutNum = datacutNum.replace('HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60 || ','')
            datacutNum = datacutNum.replace(' || HLT_PFMET120_PFMHT120_IDTight_PFHT60 || HLT_PFMET200_HBHECleaned || HLT_PFMET200_HBHE_BeamHaloCleaned','')
        histNum = TH1F('histNum', histoLabel, nbins, xmin, xmax)
        histDenom = TH1F('histDenom', histoLabel, nbins, xmin, xmax)
        samples[dataset][filepath+'_Events'].Draw(var+'>>histNum',datacutNum)
        samples[dataset][filepath+'_Events'].Draw(var+'>>histDenom',datacutDenom)
        hists[prefix+'NumData'] += histNum
        hists[prefix+'DenomData'] += histDenom
    print '    ' + prefix + 'histNumData integral = ', hists[prefix+'NumData'].Integral(1,nbins+1)
    print '    ' + prefix + 'histDenomData integral = ', hists[prefix+'DenomData'].Integral(1,nbins+1)
    hists[prefix+'EffData'].Divide(hists[prefix+'NumData'], hists[prefix+'DenomData'])
    print '    ' + prefix + 'EffData integral = ', hists[prefix+'EffData'].Integral(1,nbins+1)

#Loop through each root file for each HTbin
for prefix in ['1e', '1m']:
    MCcutNum = cuts[prefix+'Num']
    MCcutDenom = cuts[prefix+'Denom']
    for HTbin in samples['WPlusJets']:
        print '  process = WPlusJets ', HTbin, ' ||   nEvents = ', samples['WPlusJets'][HTbin]['nevents']
        weight = str(samples['WPlusJets'][HTbin]['xsec']*lumi/samples['WPlusJets'][HTbin]['nevents']) + '*leptonWeight*bjetWeight*puWeight*muonTriggerWeight*EE_L1_prefire_Weight*qcdWWeight*ewkWWeight'#*electronTriggerWeight'
        for filepath in samples['WPlusJets'][HTbin]['filepaths']:
            histNum = TH1F('histNum', histoLabel, nbins, xmin, xmax)
            histDenom = TH1F('histDenom', histoLabel, nbins, xmin, xmax)
            samples['WPlusJets'][HTbin][filepath+'_Events'].Draw(var+'>>histNum',MCcutNum)
            samples['WPlusJets'][HTbin][filepath+'_Events'].Draw(var+'>>histDenom',MCcutDenom)
            hists[prefix+'NumMC'] += histNum
            hists[prefix+'DenomMC'] += histDenom
    print '    ' + prefix + 'histNumMC integral = ', hists[prefix+'NumMC'].Integral(1,nbins+1)
    print '    ' + prefix + ' histDenomMC integral = ', hists[prefix+'DenomMC'].Integral(1,nbins+1)
    hists[prefix+'EffMC'].Divide(hists[prefix+'NumMC'], hists[prefix+'DenomMC'])
    print '    ' + prefix + 'EffMC integral = ', hists[prefix+'EffMC'].Integral(1,nbins+1)

#Get Data/MC efficiency histograms
for prefix in ['1e', '1m']:
    hists[prefix+'EffRatio'].Divide(hists[prefix+'EffData'], hists[prefix+'EffMC'])
    print prefix + 'EffRatio integral = ', hists[prefix+'EffRatio'].Integral(1,nbins+1)

#Add overflow bins to histograms
for name in hists:
    hists[name].SetBinContent(nbins, hists[name].GetBinContent(nbins) + hists[name].GetBinContent(nbins+1))

#Draw histograms if savePlots == True
if savePlots:
    print 'Drawing histograms...'
    #Draw SingleElectron Data efficiencies
    c_data1e = TCanvas('c_data1e', 'c_data1e', 800, 800)
    hists['1eEffData'].Draw('ep')
    hists['1eEffData'].SetMinimum(0)
    hists['1eEffData'].SetMaximum(1)
    hists['1eEffData'].SetMarkerStyle(20)
    hists['1eEffData'].SetMarkerSize(1.25)
    hists['1eEffData'].SetLineColor(1)
    legend_data1e = TLegend(0.6, 0.4, 0.9, 0.65)
    legend_data1e.AddEntry(hists['1eEffData'], 'SingleElectron', 'le')
    legend_data1e.Draw('same')
    legend_data1e.SetBorderSize(0)
    legend_data1e.SetFillStyle(0)
    #Draw SingleElectron MC efficiencies
    c_MC1e = TCanvas('c_MC1e', 'c_MC1e', 800, 800)
    hists['1eEffMC'].Draw('ep')
    hists['1eEffMC'].SetMinimum(0)
    hists['1eEffMC'].SetMaximum(1)
    hists['1eEffMC'].SetMarkerStyle(20)
    hists['1eEffMC'].SetMarkerSize(1.25)
    hists['1eEffMC'].SetLineColor(1)
    legend_MC1e = TLegend(0.6, 0.4, 0.9, 0.65)
    legend_MC1e.AddEntry(hists['1eEffMC'], 'SingleElectron', 'le')
    legend_MC1e.Draw('same')
    legend_MC1e.SetBorderSize(0)
    legend_MC1e.SetFillStyle(0)
    #Draw SingleElectron Data/MC efficiencies
    c_ratio1e = TCanvas('c_ratio1e', 'c_ratio1e', 800, 800)
    hists['1eEffRatio'].Draw('ep')
    hists['1eEffRatio'].SetMinimum(0)
    hists['1eEffRatio'].SetMaximum(2)
    hists['1eEffRatio'].SetMarkerStyle(20)
    hists['1eEffRatio'].SetMarkerSize(1.25)
    hists['1eEffRatio'].SetLineColor(1)
    legend_ratio1e = TLegend(0.6, 0.4, 0.9, 0.65)
    legend_ratio1e.AddEntry(hists['1eEffRatio'], 'SingleElectron', 'le')
    legend_ratio1e.Draw('same')
    legend_ratio1e.SetBorderSize(0)
    legend_ratio1e.SetFillStyle(0)
    #Draw SingleMuon Data efficiencies
    c_data1m = TCanvas('c_data1m', 'c_data1m', 800, 800)
    hists['1mEffData'].Draw('ep')
    hists['1mEffData'].SetMinimum(0)
    hists['1mEffData'].SetMaximum(1)
    hists['1mEffData'].SetMarkerStyle(20)
    hists['1mEffData'].SetMarkerSize(1.25)
    hists['1mEffData'].SetLineColor(1)
    legend_data1m = TLegend(0.6, 0.4, 0.9, 0.65)
    legend_data1m.AddEntry(hists['1mEffData'], 'SingleMuon', 'le')
    legend_data1m.Draw('same')
    legend_data1m.SetBorderSize(0)
    legend_data1m.SetFillStyle(0)
    #Draw SingleMuon MC efficiencies
    c_MC1m = TCanvas('c_MC1m', 'c_MC1m', 800, 800)
    hists['1mEffMC'].Draw('ep')
    hists['1mEffMC'].SetMinimum(0)
    hists['1mEffMC'].SetMaximum(1)
    hists['1mEffMC'].SetMarkerStyle(20)
    hists['1mEffMC'].SetMarkerSize(1.25)
    hists['1mEffMC'].SetLineColor(1)
    legend_MC1m = TLegend(0.6, 0.4, 0.9, 0.65)
    legend_MC1m.AddEntry(hists['1mEffMC'], 'SingleMuon', 'le')
    legend_MC1m.Draw('same')
    legend_MC1m.SetBorderSize(0)
    legend_MC1m.SetFillStyle(0)
    #Draw SingleMuon Data/MC efficiencies
    c_ratio1m = TCanvas('c_ratio1m', 'c_ratio1m', 800, 800)
    hists['1mEffRatio'].Draw('ep')
    hists['1mEffRatio'].SetMinimum(0)
    hists['1mEffRatio'].SetMaximum(2)
    hists['1mEffRatio'].SetMarkerStyle(20)
    hists['1mEffRatio'].SetMarkerSize(1.25)
    hists['1mEffRatio'].SetLineColor(1)
    legend_ratio1m = TLegend(0.6, 0.4, 0.9, 0.65)
    legend_ratio1m.AddEntry(hists['1mEffRatio'], 'SingleMuon', 'le')
    legend_ratio1m.Draw('same')
    legend_ratio1m.SetBorderSize(0)
    legend_ratio1m.SetFillStyle(0)
    
    #Save histograms
    c_data1e.SaveAs('MET_Trigger_efficiency_Data_1e.png')
    c_MC1e.SaveAs('MET_Trigger_efficiency_MC_1e.png')
    c_ratio1e.SaveAs('MET_Trigger_efficiency_Ratio_1e.png')
    c_data1m.SaveAs('MET_Trigger_efficiency_Data_1m.png')
    c_MC1m.SaveAs('MET_Trigger_efficiency_MC_1m.png')
    c_ratio1m.SaveAs('MET_Trigger_efficiency_Ratio_1m.png')

print 'Code end time:', datetime.datetime.now()
