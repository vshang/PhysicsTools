from ROOT import *
from MCsampleList import *
from DataSampleList import *
from utils import *
import os
import datetime
import re

#Set save directory and date for file names
saveDirectory = 'plots/CR_2016/nleptons/'
date = '11_11_2020'
year = 2016
useCondor = True
#Choose samples to use based on run year (stored in MCsampleList.py and DataSampleList.py)
if year == 2016:
    dataSamples = data2016
    MCSamples = samples2016
elif year == 2017:
    dataSamples = data2017
    MCSamples = samples2017
elif year == 2018:
    dataSamples = data2018
    MCSamples = samples2018
#Make sure save directory is available if not using Condor
if not useCondor:
    if not os.path.exists( saveDirectory + date + '/' ) : os.makedirs( saveDirectory + date + '/' )

print 'Plotting start time:', datetime.datetime.now()

#Define selection cuts and filters here
cuts = {}

cuts['passMETfilters'] = 'Flag_goodVertices && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_globalTightHalo2016Filter && Flag_muonBadTrackFilter && Flag_chargedHadronTrackResolutionFilter'
if year == 2016:
    cuts['singleIsoEle'] = 'HLT_Ele27_WPTight_Gsf'# || HLT_Ele32_eta2p1_WPTight_Gsf || HLT_Ele27_eta2p1_WPTight_Gsf' # || HLT_Ele27_WPLoose_Gsf || HLT_Ele32_WPTight_Gsf
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Ele105_CaloIdVT_GsfTrkIdT || HLT_Photon175'
    cuts['singleIsoMu'] = 'HLT_IsoMu27 || HLT_IsoMu24 || HLT_IsoTkMu24 || HLT_IsoTkMu27'
else:
    cuts['singleIsoEle'] = 'HLT_Ele32_WPTight_Gsf || HLT_Ele35_WPTight_Gsf'# || HLT_Ele32_WPTight_Gsf_L1DoubleEG'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200' # || HLT_Ele105_CaloIdVT_GsfTrkIdT
    cuts['singleIsoMu'] = 'HLT_IsoMu27 || HLT_IsoMu24' # || HLT_IsoTkMu24' #|| HLT_IsoTkMu27

#Pre-selection cut definitions
cuts['SL1e'] = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SL1m'] = 'nTightMuons == 1 && nLooseMuons == 1 && nVetoElectrons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['AH'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && jet1_jetId >= 3 && jet1_chHEF > 0.1 &&' + cuts['passMETfilters'] 
cuts['AHminSR'] = '(nVetoElectrons + nLooseMuons) == 0 && METcorrected_pt >= 250'

#Signal region definitions
cuts['SL1e0fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL1e1fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets >= 1' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL1e2bSR'] = cuts['SL1e'] + ' && ' + 'nbjets >= 2' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'

cuts['SL1m0fSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL1m1fSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1 && nfjets >= 1' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL1m2bSR'] = cuts['SL1m'] + ' && ' + 'nbjets >= 2' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['AH0l0fSR'] = cuts['AH'] + ' && nbjets == 1 && nfjets == 0 && minDeltaPhi12 >= 1 && M_Tb >= 180'
cuts['AH0l1fSR'] = cuts['AH'] + ' && nbjets == 1 && nfjets >= 1 && minDeltaPhi12 >= 1 && M_Tb >= 180'
cuts['AH0l2bSR'] = cuts['AH'] + ' && nbjets >= 2 && minDeltaPhi12 >= 1 && M_Tb >= 180 && jet1p_TH_T <= 0.5'

cuts['SL1bSR'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + ')) && nbjets == 1 && M_T >= 160 && M_T2W >= 200 && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL2bSR'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + ')) && nbjets >= 2 && M_T >= 160 && M_T2W >= 200 && minDeltaPhi12 >= 1.2 && M_Tb >= 180'

cuts['AH1b0fSR'] = cuts['AH'] + ' && nbjets == 1 && nfjets == 0'
cuts['AH2bSR'] = cuts['AH'] + ' && nbjets >= 2'
cuts['AH0l1bSR'] = cuts['AH'] + ' && nbjets == 1 && minDeltaPhi12 >= 1 && M_Tb >= 180'

#Control region definitions
cuts['SL2eTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && METcorrected_pt >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SL2mTR'] = 'njets >= 2 && nbjets >= 1 && nVetoElectrons  == 0 && nTightMuons == 2 && nLooseMuons == 2 && METcorrected_pt >= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['SL1e1mTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 1 && nVetoElectrons == 1 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 160 && tightElectron1_charge != tightMuon1_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['SL1eWR'] = 'njets >= 2 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 160 && M_T >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SL1mWR'] = 'njets >= 2 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 160 && M_T >= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'

cuts['AH1eTR'] = 'njets >= 3 && nbjets >= 1 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T <= 160 && minDeltaPhi12 >= 1.0 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['AH1mTR'] = 'njets >= 3 && nbjets >= 1 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T <= 160 && minDeltaPhi12 >= 1.0 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['AH1eWR'] = 'njets >= 3 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T <= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['AH1mWR'] = 'njets >= 3 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T <= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['AH2eZR'] = 'njets >= 3 && nbjets == 0 && nTightElectrons == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['AH2mZR'] = 'njets >= 3 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 2 && nLooseMuons == 2 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'

cuts['SLeCR'] = 'njets >= 2 && METcorrected_pt >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SLmCR'] = 'njets >= 2 && METcorrected_pt >= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['SL1eCR'] = 'njets >= 2 && METcorrected_pt >= 160 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SL1mCR'] = 'njets >= 2 && METcorrected_pt >= 160 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['SL1e0bCR'] = cuts['SL1eCR'] + ' && nbjets == 0'
cuts['SL1m0bCR'] = cuts['SL1mCR'] + ' && nbjets == 0'
cuts['SL1e1bCR'] = cuts['SL1eCR'] + ' && nbjets >= 1'
cuts['SL1m1bCR'] = cuts['SL1mCR'] + ' && nbjets >= 1'

#Select selection cut and variable to be plotted here by uncommenting

#cut = 'SL1e' #Pre-selection cuts
#cut = 'SL1m'
#cut = 'AH'
cut = 'AHminSR'

#cut = 'SL1e0fSR' #Signal region cuts
#cut = 'SL1e1fSR'
#cut = 'SL1e2bSR'
#cut = 'SL1m0fSR'
#cut = 'SL1m1fSR'
#cut = 'SL1m2bSR'
#cut = 'AH0l0fSR'
#cut = 'AH0l1fSR'
#cut = 'AH0l2bSR'
#cut = 'SL1bSR'
#cut = 'SL2bSR'
#cut = 'AH0l1bSR'
#cut = 'AH1b0fSR'
#cut = 'AH2bSR'

#cut = 'SL2eTR' #Control region cuts
#cut = 'SL2mTR'
#cut = 'SL1e1mTR'
#cut = 'SL1eWR'
#cut = 'SL1mWR'
#cut = 'AH1eTR'
#cut = 'AH1mTR'
#cut = 'AH1eWR'
#cut = 'AH1mWR'
#cut = 'AH2eZR'
#cut = 'AH2mZR'
#cut = 'SLeCR'
#cut = 'SLmCR'
#cut = 'SL1eCR'
#cut = 'SL1mCR'
#cut = 'SL1e0bCR'
#cut = 'SL1m0bCR'
#cut = 'SL1e1bCR'
#cut = 'SL1m1bCR'

#cuts[cut] += ' && Electron_pt[1] > 30 && Electron_cutBased_Sum16[1] == 4 && ((abs(Electron_eta[1]) < 1.4442) || (abs(Electron_eta[1]) > 1.566 && abs(Electron_eta[1]) < 2.1))'
#cuts[cut] += ' && Muon_pt[1] > 30 && Muon_tightId[1] && abs(Muon_eta[1]) < 2.4'
#cuts[cut] += ' && Jet_pt[0] > 30 && abs(Jet_eta[0]) < 2.4 && Jet_jetId[0] > 0'
#cuts[cut] = cuts[cut].replace('&& M_T >= 160 ', '')
#cuts[cut] = cuts[cut].replace('&& m_ll >= 60 && m_ll <= 120 ', '')
#cuts[cut] = cuts[cut] + ' && M_T2ll < 80'
#cuts[cut] = cuts[cut] + ' && ((m_ll < 76) || (m_ll > 106))'
#Uncomment replacements below to replace PFMET with PuppiMET variables
# cuts[cut] = cuts[cut].replace('METcorrected', 'PuppiMET')
# cuts[cut] = cuts[cut].replace('minDeltaPhi ', 'minDeltaPhi_puppi ')
# cuts[cut] = cuts[cut].replace('minDeltaPhi12 ', 'minDeltaPhi12_puppi ')
# cuts[cut] = cuts[cut].replace('M_Tb ', 'M_Tb_puppi ')
# cuts[cut] = cuts[cut].replace('M_T ', 'M_T_puppi ')
# cuts[cut] = cuts[cut].replace('M_T2W ', 'M_T2W_puppi ')
# cuts[cut] = cuts[cut].replace('M_T2ll ', 'M_T2ll_puppi ')
# cuts[cut] = cuts[cut].replace('m_llExists ', 'm_llExists_puppi ')
# cuts[cut] = cuts[cut].replace('recoilPtMiss ', 'recoilPtMiss_puppi ')

if year == 2016:
    cuts['data'] = cuts[cut] + ' && Flag_eeBadScFilter && Flag_BadPFMuonSummer16Filter'
else:
    cuts['data'] = cuts[cut] + ' && Flag_eeBadScFilter && Flag_BadPFMuonFilter'

#Select first variable to plot (y-axis)
var1 = 'nbjets'

#Select second variable to plot (x-axis)
var2 = 'njets'

#Set lum (fb^-1) and overall signal sample scale factor here
if year == 2016:
    lumi = 35.9
elif year == 2017:
    lumi = 41.5
    #lumi = 9.66
elif year == 2018:
    lumi = 59.7
if 'SR' in cut:
    scaleFactor = 100
else:
    scaleFactor = 1

##Create histograms
##-----------------------------------------------------------------------------------------------

print 'Cut name = ', cut
print 'MC Selection Cuts = ', cuts[cut]
print 'Data Selection Cuts = ', cuts['data']
print 'var1 (y-axis) = ', var1
print 'var2 (x-axis) = ', var2
print 'year = ', str(year)
print 'lumi = ', str(lumi)
print 'saveDirectory = ', saveDirectory
print 'date = ', date
print("Creating histograms..")

#Set histogram options
nbinsx = 12
xmin = 0
xmax = 12
nbinsy = 5
ymin = 0
ymax = 5

histoLabel = cut + ' n_{bjets} vs n_{jets} distribution; number of central jets; number of b-tagged jets'

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Select dataset to use based on cut
# datasetNames = []
# if drawData:
#     print("Drawing data and ratio plot...")
#     if 'm' in cut:
#         datasetNames.append('SingleMuon')
#         print("Selected SingleMuon dataset")
#     elif 'e' in cut:
#         datasetNames.append('SingleElectron')
#         print("Selected SingleElectron dataset")
#     else:
#         datasetNames.append('MET')
#         print("Selected MET dataset")

#Get data root files and event trees
# print("Loading data sample root files and event trees...")
# for dataset in dataSamples:
#     if dataset in datasetNames:
#         nevents = 0
#         for filepath in dataSamples[dataset]['filepaths']:
#             dataSamples[dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
#             dataSamples[dataset][filepath+'_Events'] = dataSamples[dataset][filepath+'_TFile'].Get('Events')
#             nevents += dataSamples[dataset][filepath+'_Events'].GetEntries()
#         dataSamples[dataset]['nevents'] = nevents
# print("Got data sample root files and event trees")

#Get MC background root files and event trees
print("Loading MC sample root files and event trees...")
for process in MCSamples:
    for dataset in MCSamples[process]:
        nevents = 0
        for filepath in MCSamples[process][dataset]['filepaths']:
            MCSamples[process][dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            MCSamples[process][dataset][filepath+'_Events'] = MCSamples[process][dataset][filepath+'_TFile'].Get('Events')
            nevents += MCSamples[process][dataset][filepath+'_Events'].GetEntries()
        MCSamples[process][dataset]['nevents'] = nevents
print("Got MC sample root files and event trees")

#Define signal and background histograms
signal = ['ttbar','tbar']
back = ['QCD','ZTo2L','VV','singleTop','WPlusJets','TTV','TTTo2L2Nu','TTToSemiLepton','ZTo2Nu']
hists = {}
for name in ['data','bkgSum'] + signal + back:
    hists[name] = TH2F(name, histoLabel, nbinsx, xmin, xmax, nbinsy, ymin, ymax)

#Uncomment this section for quickly testing plot settings
# counter = 1.
# for name in ['data'] + signal + back:
#     for i in range(1,nbins+1):
#         hists[name].SetBinContent(i,200)
#         hists[name].SetBinError(i,10.*counter)
#     counter += 1
# for i in range(1,nbins+1):
#     hists['data'].SetBinContent(i,2700)
#     hists['data'].SetBinError(i,300)

#Fill histograms
print("Filling histograms...")
#Loop through each root file for each dataset
# for dataset in dataSamples:
#     if dataset in datasetNames:
#         print '  Dataset = ', dataset, ' ||   nEvents = ', dataSamples[dataset]['nevents']
#         for filepath in dataSamples[dataset]['filepaths']:
#             hist = TH2F('hist', histoLabel, nbinsx, xmin, xmax, nbinsy, ymin, ymax)
#             #HLT_Ele32_WPTight_Gsf and HLT_Ele115_CaloIdVT_GsfTrkIdT triggers missing in 2017 Run B, make appropriate replacements
#             if year == 2017 and 'tree_allB' in filepath: 
#                 datacut = cuts['data'].replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200', 'HLT_Photon200')
#                 datacut = datacut.replace('HLT_Ele32_WPTight_Gsf || HLT_Ele35_WPTight_Gsf', 'HLT_Ele32_WPTight_Gsf_L1DoubleEG || HLT_Ele35_WPTight_Gsf')
#             else:
#                 datacut = cuts['data']
#             dataSamples[dataset][filepath+'_Events'].Draw(var1+':'+var2+'>>hist',datacut)
#             hists['data'].Add(hist)
for process in MCSamples:
    print '  Process = ', process
    for dataset in MCSamples[process]:
        print '      Dataset = ', dataset, ' ||   nEvents = ', MCSamples[process][dataset]['nevents']
        weight = str(MCSamples[process][dataset]['xsec']*lumi/MCSamples[process][dataset]['nevents']) + '*leptonWeight*bjetWeight*puWeight'
        #Apply appropriate NLO k-factors
        if process == 'WPlusJets':
            weight = weight + '*qcdWWeight*ewkWWeight'
            print 'Applied WPlusJets qcd/ewk Weights correctly'
        elif process == 'ZTo2L':
            weight = weight + '*qcdZTo2LWeight*ewkZWeight'
            print 'Applied ZTo2L qcd/ewk Weights correctly'
        elif process == 'ZTo2Nu':
            weight = weight + '*qcdZTo2NuWeight*ewkZWeight'
            print 'Applied ZTo2Nu qcd/ewk Weights correctly'
        for filepath in MCSamples[process][dataset]['filepaths']:
            hist = TH2F('hist', histoLabel, nbinsx, xmin, xmax, nbinsy, ymin, ymax)
            MCSamples[process][dataset][filepath+'_Events'].Draw(var1+':'+var2+'>>hist',weight+'*('+cuts[cut]+')')
            if process in signal:
                hists[process].Add(hist)
            elif process == 'ttbarPlusJets':
                if dataset == 'TTTo2L2Nu':
                    hists['TTTo2L2Nu'].Add(hist)
                elif dataset == 'TTToSemiLepton':
                    hists['TTToSemiLepton'].Add(hist)
            elif process == 'singleTop':
                hists['singleTop'].Add(hist)
            elif process == 'WPlusJets':
                hists['WPlusJets'].Add(hist)
            elif process == 'ZTo2L':
                hists['ZTo2L'].Add(hist)
            elif process == 'ZTo2Nu':
                hists['ZTo2Nu'].Add(hist)
            elif (process == 'WW' or process == 'WZ' or process == 'ZZ'):
                hists['VV'].Add(hist)
            elif process == 'TTV':
                hists['TTV'].Add(hist)
            elif process == 'QCD':
                hists['QCD'].Add(hist)

#Fill background sum histogram 
for name in back:
    hists['bkgSum'].Add(hists[name])

print("Finished filling histograms")

#Add overflow bins to histograms
for name in hists:
    hists[name].SetBinContent(0, nbinsy, hists[name].GetBinContent(0,nbinsy) + hists[name].GetBinContent(0,nbinsy+1))
    hists[name].SetBinContent(nbinsx, 0, hists[name].GetBinContent(nbinsx,0) + hists[name].GetBinContent(nbinsx+1,0))
    hists[name].SetBinContent(nbinsx, nbinsy, hists[name].GetBinContent(nbinsx,nbinsy) + hists[name].GetBinContent(nbinsx,nbinsy+1) + hists[name].GetBinContent(nbinsx+1,nbinsy))

        
#Draw histograms
print("Drawing histograms...")
c1 = TCanvas('c1', 'c1', 800, 800)
hists['bkgSum'].Draw('Colz')

c2 = TCanvas('c2', 'c2', 800, 800)
hists['tbar'].Draw('Colz')

c3 = TCanvas('c3', 'c3', 800, 800)
hists['ttbar'].Draw('Colz')
        
#Save histogram
if useCondor:
    c1.SaveAs(cut + str(year) + "_" + var1 + "_vs_" + var2 + '_' + date + "_bkg.png")
    c2.SaveAs(cut + str(year) + "_" + var1 + "_vs_" + var2 + '_' + date + "_tbar.png")
    c3.SaveAs(cut + str(year) + "_" + var1 + "_vs_" + var2 + '_' + date + "_ttbar.png")
else:
    c1.SaveAs(saveDirectory + date + "/" + cut + str(year) + "_" + var1 + "_vs_" + var2 + '_' + date + "_bkg.png")
    c2.SaveAs(saveDirectory + date + "/" + cut + str(year) + "_" + var2 + "_vs_" + var2 + '_' + date + "_tbar.png")
    c3.SaveAs(saveDirectory + date + "/" + cut + str(year) + "_" + var3 + "_vs_" + var2 + '_' + date + "_ttbar.png")

print 'Plotting end time:', datetime.datetime.now()
