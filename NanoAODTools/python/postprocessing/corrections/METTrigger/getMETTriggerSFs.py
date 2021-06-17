from ROOT import *
from METTriggerSampleList import *
import os
import datetime
import re
import math
import numpy as np

gErrorIgnoreLevel = kError
date = '06_16_2021'
year = 2017
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
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight'
elif year == 2017:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2'
    cuts['singleIsoEle'] = 'passEle32WPTightGsf2017'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
    cuts['singleIsoMu'] = 'HLT_IsoMu27' 
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'
elif year == 2018:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2'
    cuts['singleIsoEle'] = 'HLT_Ele32_WPTight_Gsf'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
    cuts['singleIsoMu'] = 'HLT_IsoMu24' 
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'

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
nbins = 40
xmin = 250
xmax = 650
#edges = np.array([160., 170., 180., 190., 200., 210., 220., 230., 240., 250., 260., 270., 280., 290., 300., 320., 340., 360., 380., 400., 420., 440., 460., 480., 500., 520., 540., 560., 580., 600.], dtype='float64')
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
TH1.SetDefaultSumw2()
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
    if dataset == 'SingleElectron':
        prefix = '1e'
    elif dataset == 'SingleMuon':
        prefix = '1m'
    for filepath in samples[dataset]['filepaths']:
        #Only apply ee badSC noise filter to data (https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2)
        datacutNum = cuts[prefix+'Num'] + ' && Flag_eeBadScFilter'
        datacutDenom = cuts[prefix+'Denom'] + ' && Flag_eeBadScFilter'
        if 'Run2017B' in filepath: #HLT_Ele115_CaloIdVT_GsfTrkIdT trigger path not available in Run2017B (https://hypernews.cern.ch/HyperNews/CMS/get/b2g-selections/346.html?inline=-1)
            datacutNum = datacutNum.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || ','')
            datacutDenom = datacutDenom.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || ','')
            #MET trigger paths also missing from Run2017B (https://hypernews.cern.ch/HyperNews/CMS/get/top-trigger/247/1.html)
            datacutNum = datacutNum.replace(' || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60','')
        histNum = TH1F('histNum', histoLabel, nbins, xmin, xmax)
        histDenom = TH1F('histDenom', histoLabel, nbins, xmin, xmax)
        samples[dataset][filepath+'_Events'].Draw(var+'>>histNum',datacutNum)
        samples[dataset][filepath+'_Events'].Draw(var+'>>histDenom',datacutDenom)
        hists[prefix+'NumData'] += histNum
        hists[prefix+'DenomData'] += histDenom
    hists[prefix+'EffData'].Divide(hists[prefix+'NumData'], hists[prefix+'DenomData'])
    print '    ' + prefix + 'NumData Bin 1 Content = ', hists[prefix+'NumData'].GetBinContent(1)
    print '    ' + prefix + 'NumData Bin 1 Error = ', hists[prefix+'NumData'].GetBinError(1)
    print '    ' + prefix + 'DenomData Bin 1 Content = ', hists[prefix+'DenomData'].GetBinContent(1)
    print '    ' + prefix + 'DenomData Bin 1 Error = ', hists[prefix+'DenomData'].GetBinError(1)
    print '    ' + prefix + 'EffData Bin 1 Content = ', hists[prefix+'EffData'].GetBinContent(1)
    print '    ' + prefix + 'EffData Bin 1 Error = ', hists[prefix+'EffData'].GetBinError(1)
    print '    ------------------------------------------------------------------------------------'
    print '    ' + prefix + 'NumData Bin 40 Content = ', hists[prefix+'NumData'].GetBinContent(40)
    print '    ' + prefix + 'NumData Bin 40 Error = ', hists[prefix+'NumData'].GetBinError(40)
    print '    ' + prefix + 'DenomData Bin 40 Content = ', hists[prefix+'DenomData'].GetBinContent(40)
    print '    ' + prefix + 'DenomData Bin 40 Error = ', hists[prefix+'DenomData'].GetBinError(40)
    print '    ' + prefix + 'EffData Bin 40 Content = ', hists[prefix+'EffData'].GetBinContent(40)
    print '    ' + prefix + 'EffData Bin 40 Error = ', hists[prefix+'EffData'].GetBinError(40)
    print '    ------------------------------------------------------------------------------------'

#Loop through each root file for each HTbin
for prefix in ['1e', '1m']:
    MCcutNum = cuts[prefix+'Num']
    MCcutDenom = cuts[prefix+'Denom']
    for HTbin in samples['WPlusJets']:
        weight = str(samples['WPlusJets'][HTbin]['xsec']*lumi/samples['WPlusJets'][HTbin]['nevents']) + '*leptonWeight*bjetWeight*puWeight*muonTriggerWeight*EE_L1_prefire_Weight*qcdWWeight*ewkWWeight'#*electronTriggerWeight'
        for filepath in samples['WPlusJets'][HTbin]['filepaths']:
            histNum = TH1F('histNum', histoLabel, nbins, xmin, xmax)
            histDenom = TH1F('histDenom', histoLabel, nbins, xmin, xmax)
            samples['WPlusJets'][HTbin][filepath+'_Events'].Draw(var+'>>histNum',MCcutNum)
            samples['WPlusJets'][HTbin][filepath+'_Events'].Draw(var+'>>histDenom',MCcutDenom)
            hists[prefix+'NumMC'] += histNum
            hists[prefix+'DenomMC'] += histDenom
    hists[prefix+'EffMC'].Divide(hists[prefix+'NumMC'], hists[prefix+'DenomMC'])
    print '    ' + prefix + 'NumMC Bin 1 Content = ', hists[prefix+'NumMC'].GetBinContent(1)
    print '    ' + prefix + 'NumMC Bin 1 Error = ', hists[prefix+'NumMC'].GetBinError(1)
    print '    ' + prefix + 'DenomMC Bin 1 Content = ', hists[prefix+'DenomMC'].GetBinContent(1)
    print '    ' + prefix + 'DenomMC Bin 1 Error = ', hists[prefix+'DenomMC'].GetBinError(1)
    print '    ' + prefix + 'EffMC Bin 1 Content = ', hists[prefix+'EffMC'].GetBinContent(1)
    print '    ' + prefix + 'EffMC Bin 1 Error = ', hists[prefix+'EffMC'].GetBinError(1)
    print '    ------------------------------------------------------------------------------------'
    print '    ' + prefix + 'NumMC Bin 40 Content = ', hists[prefix+'NumMC'].GetBinContent(40)
    print '    ' + prefix + 'NumMC Bin 40 Error = ', hists[prefix+'NumMC'].GetBinError(40)
    print '    ' + prefix + 'DenomMC Bin 40 Content = ', hists[prefix+'DenomMC'].GetBinContent(40)
    print '    ' + prefix + 'DenomMC Bin 40 Error = ', hists[prefix+'DenomMC'].GetBinError(40)
    print '    ' + prefix + 'EffMC Bin 40 Content = ', hists[prefix+'EffMC'].GetBinContent(40)
    print '    ' + prefix + 'EffMC Bin 40 Error = ', hists[prefix+'EffMC'].GetBinError(40)
    print '    ------------------------------------------------------------------------------------'

#Get Data/MC efficiency histograms
for prefix in ['1e', '1m']:
    hists[prefix+'EffRatio'].Divide(hists[prefix+'EffData'], hists[prefix+'EffMC'])
    print prefix + 'EffRatio Bin 1 Content = ', hists[prefix+'EffRatio'].GetBinContent(1)
    print prefix + 'EffRatio Bin 1 Error = ', hists[prefix+'EffRatio'].GetBinError(1)
    print prefix + 'EffRatio Bin 40 Content = ', hists[prefix+'EffRatio'].GetBinContent(40)
    print prefix + 'EffRatio Bin 40 Error = ', hists[prefix+'EffRatio'].GetBinError(40)

##-----------------------------------------------------------------------------------------------

#Save root files with SFs if saveRootFiles == True
if saveRootFiles:
    rootFile = TFile('MET_Trigger_SFs_'+str(year)+'.root', 'RECREATE')
    ratioHist = TH1F('SF', histoLabel, nbins, xmin, xmax)
    for i in range(1,nbins+2):
        binContent = hists['1eEffRatio'].GetBinContent(i)
        binError = hists['1eEffRatio'].GetBinError(i)
        ratioHist.SetBinContent(i, binContent)
        ratioHist.SetBinError(i, binError)
    ratioHist.Write()

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
    #Draw legend
    legend_data1e = TLegend(0.5, 0.1, 0.7, 0.4)
    legend_data1e.AddEntry(hists['1eEffData'], 'SingleElectron', 'lep')
    legend_data1e.Draw('same')
    legend_data1e.SetBorderSize(0)
    legend_data1e.SetFillStyle(0)
    legend_data1e.SetTextSize(0.04)
    #Draw title with lumi and beam energy
    title_data1e = TLatex()
    title_data1e.SetTextSize(0.03)
    title_data1e_x = .7
    title_data1e_y = .91
    if year == 2016:
        title_data1e.DrawLatexNDC(title_data1e_x, title_data1e_y, "#bf{35.9 fb^{-1} (13 TeV)}")
    elif year == 2017:
        title_data1e.DrawLatexNDC(title_data1e_x, title_data1e_y, "#bf{41.5 fb^{-1} (13 TeV)}")
    elif year == 2018:
        title_data1e.DrawLatexNDC(title_data1e_x, title_data1e_y, "#bf{59.8 fb^{-1} (13 TeV)}")
    #Set "CMS preliminary" text
    pt_data1e = TPaveText(0.23, 0.65, 0.4, 0.75, "NDC")
    pt_data1e.SetTextSize(0.04)
    pt_data1e.SetFillColor(0)
    pt_data1e.SetTextAlign(11)
    pt_data1e.AddText('#splitline{CMS}{#bf{#it{Preliminary}}}')
    pt_data1e.Draw('same')

#######

    #Draw SingleElectron MC efficiencies
    c_MC1e = TCanvas('c_MC1e', 'c_MC1e', 800, 800)
    hists['1eEffMC'].Draw('ep')
    hists['1eEffMC'].SetMinimum(0)
    hists['1eEffMC'].SetMaximum(1)
    hists['1eEffMC'].SetMarkerStyle(20)
    hists['1eEffMC'].SetMarkerSize(1.25)
    hists['1eEffMC'].SetLineColor(1)
    #Draw legend
    legend_MC1e = TLegend(0.5, 0.1, 0.7, 0.4)
    legend_MC1e.AddEntry(hists['1eEffMC'], 'SingleElectron', 'lep')
    legend_MC1e.Draw('same')
    legend_MC1e.SetBorderSize(0)
    legend_MC1e.SetFillStyle(0)
    legend_MC1e.SetTextSize(0.04)
    #Draw title with lumi and beam energy
    title_MC1e = TLatex()
    title_MC1e.SetTextSize(0.03)
    title_MC1e_x = .7
    title_MC1e_y = .91
    if year == 2016:
        title_MC1e.DrawLatexNDC(title_MC1e_x, title_MC1e_y, "#bf{35.9 fb^{-1} (13 TeV)}")
    elif year == 2017:
        title_MC1e.DrawLatexNDC(title_MC1e_x, title_MC1e_y, "#bf{41.5 fb^{-1} (13 TeV)}")
    elif year == 2018:
        title_MC1e.DrawLatexNDC(title_MC1e_x, title_MC1e_y, "#bf{59.8 fb^{-1} (13 TeV)}")
    #Set "CMS preliminary" text
    pt_MC1e = TPaveText(0.23, 0.65, 0.4, 0.75, "NDC")
    pt_MC1e.SetTextSize(0.04)
    pt_MC1e.SetFillColor(0)
    pt_MC1e.SetTextAlign(11)
    pt_MC1e.AddText('#splitline{CMS}{#bf{#it{Preliminary}}}')
    pt_MC1e.Draw('same')

#######

    #Draw SingleElectron Data/MC efficiencies
    c_ratio1e = TCanvas('c_ratio1e', 'c_ratio1e', 800, 800)
    hists['1eEffRatio'].Draw('ep')
    hists['1eEffRatio'].SetMinimum(0)
    hists['1eEffRatio'].SetMaximum(2)
    hists['1eEffRatio'].SetMarkerStyle(20)
    hists['1eEffRatio'].SetMarkerSize(1.25)
    hists['1eEffRatio'].SetLineColor(1)
    #Draw legend
    legend_ratio1e = TLegend(0.5, 0.1, 0.7, 0.4)
    legend_ratio1e.AddEntry(hists['1eEffRatio'], 'SingleElectron', 'lep')
    legend_ratio1e.Draw('same')
    legend_ratio1e.SetBorderSize(0)
    legend_ratio1e.SetFillStyle(0)
    legend_ratio1e.SetTextSize(0.04)
    #Draw title with lumi and beam energy
    title_ratio1e = TLatex()
    title_ratio1e.SetTextSize(0.03)
    title_ratio1e_x = .7
    title_ratio1e_y = .91
    if year == 2016:
        title_ratio1e.DrawLatexNDC(title_ratio1e_x, title_ratio1e_y, "#bf{35.9 fb^{-1} (13 TeV)}")
    elif year == 2017:
        title_ratio1e.DrawLatexNDC(title_ratio1e_x, title_ratio1e_y, "#bf{41.5 fb^{-1} (13 TeV)}")
    elif year == 2018:
        title_ratio1e.DrawLatexNDC(title_ratio1e_x, title_ratio1e_y, "#bf{59.8 fb^{-1} (13 TeV)}")
    #Set "CMS preliminary" text
    pt_ratio1e = TPaveText(0.23, 0.65, 0.4, 0.75, "NDC")
    pt_ratio1e.SetTextSize(0.04)
    pt_ratio1e.SetFillColor(0)
    pt_ratio1e.SetTextAlign(11)
    pt_ratio1e.AddText('#splitline{CMS}{#bf{#it{Preliminary}}}')
    pt_ratio1e.Draw('same')

#######

    #Draw SingleMuon Data efficiencies
    c_data1m = TCanvas('c_data1m', 'c_data1m', 800, 800)
    hists['1mEffData'].Draw('ep')
    hists['1mEffData'].SetMinimum(0)
    hists['1mEffData'].SetMaximum(1)
    hists['1mEffData'].SetMarkerStyle(20)
    hists['1mEffData'].SetMarkerSize(1.25)
    hists['1mEffData'].SetLineColor(1)
    #Draw legend
    legend_data1m = TLegend(0.5, 0.1, 0.7, 0.4)
    legend_data1m.AddEntry(hists['1mEffData'], 'SingleMuon', 'lep')
    legend_data1m.Draw('same')
    legend_data1m.SetBorderSize(0)
    legend_data1m.SetFillStyle(0)
    legend_data1m.SetTextSize(0.04)
    #Draw title with lumi and beam energy
    title_data1m = TLatex()
    title_data1m.SetTextSize(0.03)
    title_data1m_x = .7
    title_data1m_y = .91
    if year == 2016:
        title_data1m.DrawLatexNDC(title_data1m_x, title_data1m_y, "#bf{35.9 fb^{-1} (13 TeV)}")
    elif year == 2017:
        title_data1m.DrawLatexNDC(title_data1m_x, title_data1m_y, "#bf{41.5 fb^{-1} (13 TeV)}")
    elif year == 2018:
        title_data1m.DrawLatexNDC(title_data1m_x, title_data1m_y, "#bf{59.8 fb^{-1} (13 TeV)}")
    #Set "CMS preliminary" text
    pt_data1m = TPaveText(0.23, 0.65, 0.4, 0.75, "NDC")
    pt_data1m.SetTextSize(0.04)
    pt_data1m.SetFillColor(0)
    pt_data1m.SetTextAlign(11)
    pt_data1m.AddText('#splitline{CMS}{#bf{#it{Preliminary}}}')
    pt_data1m.Draw('same')

#######

    #Draw SingleMuon MC efficiencies
    c_MC1m = TCanvas('c_MC1m', 'c_MC1m', 800, 800)
    hists['1mEffMC'].Draw('ep')
    hists['1mEffMC'].SetMinimum(0)
    hists['1mEffMC'].SetMaximum(1)
    hists['1mEffMC'].SetMarkerStyle(20)
    hists['1mEffMC'].SetMarkerSize(1.25)
    hists['1mEffMC'].SetLineColor(1)
    #Draw legend
    legend_MC1m = TLegend(0.5, 0.1, 0.7, 0.4)
    legend_MC1m.AddEntry(hists['1mEffMC'], 'SingleMuon', 'lep')
    legend_MC1m.Draw('same')
    legend_MC1m.SetBorderSize(0)
    legend_MC1m.SetFillStyle(0)
    legend_MC1m.SetTextSize(0.04)
    #Draw title with lumi and beam energy
    title_MC1m = TLatex()
    title_MC1m.SetTextSize(0.03)
    title_MC1m_x = .7
    title_MC1m_y = .91
    if year == 2016:
        title_MC1m.DrawLatexNDC(title_MC1m_x, title_MC1m_y, "#bf{35.9 fb^{-1} (13 TeV)}")
    elif year == 2017:
        title_MC1m.DrawLatexNDC(title_MC1m_x, title_MC1m_y, "#bf{41.5 fb^{-1} (13 TeV)}")
    elif year == 2018:
        title_MC1m.DrawLatexNDC(title_MC1m_x, title_MC1m_y, "#bf{59.8 fb^{-1} (13 TeV)}")
    #Set "CMS preliminary" text
    pt_MC1m = TPaveText(0.23, 0.65, 0.4, 0.75, "NDC")
    pt_MC1m.SetTextSize(0.04)
    pt_MC1m.SetFillColor(0)
    pt_MC1m.SetTextAlign(11)
    pt_MC1m.AddText('#splitline{CMS}{#bf{#it{Preliminary}}}')
    pt_MC1m.Draw('same')

#######

    #Draw SingleMuon Data/MC efficiencies
    c_ratio1m = TCanvas('c_ratio1m', 'c_ratio1m', 800, 800)
    hists['1mEffRatio'].Draw('ep')
    hists['1mEffRatio'].SetMinimum(0)
    hists['1mEffRatio'].SetMaximum(2)
    hists['1mEffRatio'].SetMarkerStyle(20)
    hists['1mEffRatio'].SetMarkerSize(1.25)
    hists['1mEffRatio'].SetLineColor(1)
    #Draw legend
    legend_ratio1m = TLegend(0.5, 0.1, 0.7, 0.4)
    legend_ratio1m.AddEntry(hists['1mEffRatio'], 'SingleMuon', 'lep')
    legend_ratio1m.Draw('same')
    legend_ratio1m.SetBorderSize(0)
    legend_ratio1m.SetFillStyle(0)
    legend_ratio1m.SetTextSize(0.04)
    #Draw title with lumi and beam energy
    title_ratio1m = TLatex()
    title_ratio1m.SetTextSize(0.03)
    title_ratio1m_x = .7
    title_ratio1m_y = .91
    if year == 2016:
        title_ratio1m.DrawLatexNDC(title_ratio1m_x, title_ratio1m_y, "#bf{35.9 fb^{-1} (13 TeV)}")
    elif year == 2017:
        title_ratio1m.DrawLatexNDC(title_ratio1m_x, title_ratio1m_y, "#bf{41.5 fb^{-1} (13 TeV)}")
    elif year == 2018:
        title_ratio1m.DrawLatexNDC(title_ratio1m_x, title_ratio1m_y, "#bf{59.8 fb^{-1} (13 TeV)}")
    #Set "CMS preliminary" text
    pt_ratio1m = TPaveText(0.23, 0.65, 0.4, 0.75, "NDC")
    pt_ratio1m.SetTextSize(0.04)
    pt_ratio1m.SetFillColor(0)
    pt_ratio1m.SetTextAlign(11)
    pt_ratio1m.AddText('#splitline{CMS}{#bf{#it{Preliminary}}}')
    pt_ratio1m.Draw('same')
    
    #Save histograms
    if not os.path.exists(str(year)+'/'+date+'/') : os.makedirs(str(year)+'/'+date+'/')
    c_data1e.SaveAs(str(year)+'/'+date+'/MET_Trigger_efficiency_Data_1e.png')
    c_MC1e.SaveAs(str(year)+'/'+date+'/MET_Trigger_efficiency_MC_1e.png')
    c_ratio1e.SaveAs(str(year)+'/'+date+'/MET_Trigger_efficiency_Ratio_1e.png')
    c_data1m.SaveAs(str(year)+'/'+date+'/MET_Trigger_efficiency_Data_1m.png')
    c_MC1m.SaveAs(str(year)+'/'+date+'/MET_Trigger_efficiency_MC_1m.png')
    c_ratio1m.SaveAs(str(year)+'/'+date+'/MET_Trigger_efficiency_Ratio_1m.png')

print 'Code end time:', datetime.datetime.now()
