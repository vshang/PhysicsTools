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

cuts['AHSR'] = cuts['AH'] + ' && nbjets >= 1 && minDeltaPhi12 >= 1 && M_Tb >= 180'
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
cut = 'AHSR'
#cut = 'AHminSR'

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

#var = 'M_T'
#var = 'M_T2W'
#var = 'minDeltaPhi12'
#var = 'M_Tb'
#var = 'jet1p_TH_T'
var = 'njets'
#var = 'nfjets'
#var = 'nbjets'
#var = 'MET_pt'
#var = 'METcorrected_pt'
#var = 'PuppiMET_pt'
#var = 'recoilPtMiss_puppi'
#var = 'Electron_pt[1]'
#var = 'Muon_pt[1]'
#var = 'Jet_pt[0]'
#var = 'Electron_eta[1]'
#var = 'Muon_eta[1]'
#var = 'nTightElectrons'
#var = 'nTightMuons'
#var = 'nTightElectrons + nTightMuons'
#var = 'm_ll'
#var = 'MET_phi'
#var = 'METcorrected_phi'
#var = 'M_T2ll'

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
print 'var = ', var
print 'year = ', str(year)
print 'lumi = ', str(lumi)
print 'saveDirectory = ', saveDirectory
print 'date = ', date
print("Creating histograms..")

#Set histogram options
nbins = 12
xmin = 0
xmax = 12
auto_y = True
#auto_y = False
#doLogPlot = True
doLogPlot = False
drawData = False
#drawData = False
if not auto_y:
    ymin = 60
    ymax = 20000

#histoLabel = cut + ' M_{T} distribution; M_{T} (GeV); Events'
#histoLabel = cut + ' M_{T2}^{W} distribution; M_{T2}^{W} (GeV); Events'
#histoLabel = cut + ' min#Delta#phi(jet_{1,2},p_{T}^{miss}) distribution; min#Delta#phi(jet_{1,2},p_{T}^{miss}); Events'
#histoLabel = cut + ' M_{T}^{b} distribution; M_{T}^{b} (GeV); Events'
#histoLabel = cut + ' jet_{1} p_{T}/H_{T} distribution; jet_{1} p_{T}/H_{T}; Events'
histoLabel = cut + ' central n_{jet} distribution; number of AK4 jets; Events'
#histoLabel = cut + ' n_{bjets} distribution; number of b-tagged jets; Events'
#histoLabel = cut + ' forward n_{jet} distribution; number of forward AK4 jets; Events'
#histoLabel = cut + ' p_{T}^{miss} distribution; p_{T}^{miss} (GeV); Events'
#histoLabel = cut + ' Hadronic recoil distribution; Hadronic recoil (GeV); Events'
#histoLabel = cut + ' Electron_pt[1] distribution; Electron_pt[1]; Events'
#histoLabel = cut + ' Muon_pt[1] distribution; Muon_pt[1]; Events'
#histoLabel = cut + ' Jet_pt[0] distribution; Jet_pt[0]; Events'
#histoLabel = cut + ' Electron_eta[1] distribution; Electron_eta[1]; Events'
#histoLabel = cut + ' Muon_eta[1] distribution; Muon_eta[1]; Events'
#histoLabel = cut + ' nTightElectrons distribution; number of tight electrons; Events'
#histoLabel = cut + ' nTightMuons distribution; number of tight muons; Events'
#histoLabel = cut + ' nTightLeptons distribution; number of tight leptons; Events'
#histoLabel = cut + ' m_{ll} distribution; m_{ll} (GeV); Events'
#histoLabel = cut + ' #phi^{miss} distribution; #phi^{miss} (GeV); Events'
#histoLabel = cut + ' M_{ll}^{T2} distribution; M_{ll}^{T2} (GeV); Events'

if drawData:
    ratioLabel = re.sub('.*distribution;', ';', histoLabel).replace('Events','Data / Bkg')
    histoLabel = re.sub(';.*;', '; ;', histoLabel)

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Select dataset to use based on cut
datasetNames = []
if drawData:
    print("Drawing data and ratio plot...")
    if 'm' in cut:
        datasetNames.append('SingleMuon')
        print("Selected SingleMuon dataset")
    elif 'e' in cut:
        datasetNames.append('SingleElectron')
        print("Selected SingleElectron dataset")
    else:
        datasetNames.append('MET')
        print("Selected MET dataset")

#Get data root files and event trees
print("Loading data sample root files and event trees...")
for dataset in dataSamples:
    if dataset in datasetNames:
        nevents = 0
        for filepath in dataSamples[dataset]['filepaths']:
            dataSamples[dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            dataSamples[dataset][filepath+'_Events'] = dataSamples[dataset][filepath+'_TFile'].Get('Events')
            nevents += dataSamples[dataset][filepath+'_Events'].GetEntries()
        dataSamples[dataset]['nevents'] = nevents
print("Got data sample root files and event trees")

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
    hists[name] = TH1F(name, histoLabel, nbins, xmin, xmax)

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
count = 0
print("Filling histograms...")
#Loop through each root file for each dataset
for dataset in dataSamples:
    if dataset in datasetNames:
        print '  Dataset = ', dataset, ' ||   nEvents = ', dataSamples[dataset]['nevents']
        for filepath in dataSamples[dataset]['filepaths']:
            hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
            #HLT_Ele32_WPTight_Gsf and HLT_Ele115_CaloIdVT_GsfTrkIdT triggers missing in 2017 Run B, make appropriate replacements
            if year == 2017 and 'tree_allB' in filepath: 
                datacut = cuts['data'].replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200', 'HLT_Photon200')
                datacut = datacut.replace('HLT_Ele32_WPTight_Gsf || HLT_Ele35_WPTight_Gsf', 'HLT_Ele32_WPTight_Gsf_L1DoubleEG || HLT_Ele35_WPTight_Gsf')
            else:
                datacut = cuts['data']
            dataSamples[dataset][filepath+'_Events'].Draw(var+'>>hist',datacut)
            print '    hist nEntries = ', hist.GetEntries()
            print '    hist integral = ', hist.Integral(1,nbins+1)
            hists['data'] += hist
            print '    hist_data nEntries = ', hists['data'].GetEntries()
            print '    hist_data integral = ', hists['data'].Integral(1,nbins+1)
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
            hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
            MCSamples[process][dataset][filepath+'_Events'].Draw(var+'>>hist',weight+'*('+cuts[cut]+')')
            print '          hist nEntries = ', hist.GetEntries()
            print '          hist integral = ', hist.Integral(1,nbins+1)
            if process in signal:
                hists[process] += scaleFactor*hist
            elif process == 'ttbarPlusJets':
                if dataset == 'TTTo2L2Nu':
                    hists['TTTo2L2Nu'] += hist
                elif dataset == 'TTToSemiLepton':
                    hists['TTToSemiLepton'] += hist
            elif process == 'singleTop':
                hists['singleTop'] += hist
            elif process == 'WPlusJets':
                hists['WPlusJets'] += hist
            elif process == 'ZTo2L':
                hists['ZTo2L'] += hist
            elif process == 'ZTo2Nu':
                hists['ZTo2Nu'] += hist
            elif (process == 'WW' or process == 'WZ' or process == 'ZZ'):
                hists['VV'] += hist
            elif process == 'TTV':
                hists['TTV'] += hist
            elif process == 'QCD':
                hists['QCD'] += hist

#Fill background sum histogram for calculating ratio plot
for name in back:
    hists['bkgSum'] += hists[name]
print 'Total data background nEvents = ', hists['data'].GetEntries()
print 'Total data background integral = ', hists['data'].Integral(1,nbins+1)
print 'Total MC background nEvents = ', hists['bkgSum'].GetEntries()
print 'Total MC background integral = ', hists['bkgSum'].Integral(1,nbins+1)
print("Finished filling histograms")

#Add overflow bins to histograms
for name in hists:
    hists[name].SetBinContent(nbins, hists[name].GetBinContent(nbins) + hists[name].GetBinContent(nbins+1))

#Add up MC background histos into stacked histogram
print("Creating stacked MC background histogram...")
h_MCStack = THStack('h_MCbackground', histoLabel)
for name in back:
    h_MCStack.Add(hists[name])
print("Finished stacking MC background histograms.")
        
#Draw histograms
print("Drawing histograms...")
c = TCanvas('c', 'c', 800, 800)
if drawData:
    c.Divide(1,2)
    setTopPad(c.GetPad(1),4)
    setBotPad(c.GetPad(2),4)
    c.cd(1)
    if doLogPlot:
        c.GetPad(1).SetLogy(1)
else:
    setCanvas(c)
    if doLogPlot:
        c.SetLogy(1)
h_MCStack.Draw('hist')
hists['ttbar'].Draw('hist same')
hists['tbar'].Draw('hist same')
hists['data'].Draw('ep same')
hists['bkgSum'].Draw('e2 same')
#Set MC background histogram options 
hists['QCD'].SetFillColor(kGray+1)
hists['ZTo2L'].SetFillColor(kGreen+1)
hists['VV'].SetFillColor(kBlue+2)
hists['singleTop'].SetFillColor(kOrange+7)
hists['WPlusJets'].SetFillColor(kViolet-1)
hists['TTV'].SetFillColor(kOrange+4)
hists['TTTo2L2Nu'].SetFillColor(kOrange-2)
hists['TTToSemiLepton'].SetFillColor(kOrange-3)
hists['ZTo2Nu'].SetFillColor(kAzure-4)

hists['QCD'].SetLineWidth(0)
hists['ZTo2L'].SetLineWidth(0)
hists['VV'].SetLineWidth(0)
hists['singleTop'].SetLineWidth(0)
hists['WPlusJets'].SetLineWidth(0)
hists['TTV'].SetLineWidth(0)
hists['TTTo2L2Nu'].SetLineWidth(0)
hists['TTToSemiLepton'].SetLineWidth(0)
hists['ZTo2Nu'].SetLineWidth(0)

if auto_y:
    if doLogPlot:
        ymin = max(min(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMinimumBin()), hists['data'].GetBinContent(hists['data'].GetMinimumBin())), 5.e-1)
        ymax = 5.*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['data'].GetBinContent(hists['data'].GetMaximumBin())+hists['data'].GetBinError(hists['data'].GetMaximumBin()), hists['tbar'].GetBinContent(hists['tbar'].GetMaximumBin()), hists['ttbar'].GetBinContent(hists['ttbar'].GetMaximumBin()))
    else:
        ymin = 0
        ymax = 1.25*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['data'].GetBinContent(hists['data'].GetMaximumBin())+hists['data'].GetBinError(hists['data'].GetMaximumBin()), hists['tbar'].GetBinContent(hists['tbar'].GetMaximumBin()), hists['ttbar'].GetBinContent(hists['ttbar'].GetMaximumBin()))
h_MCStack.SetMinimum(ymin)
h_MCStack.SetMaximum(ymax)
#Set settings for data and MC background histogram title/labels
if drawData:
    setHistStyle(h_MCStack)
    h_MCStack.GetXaxis().SetLabelOffset(999)
    h_MCStack.GetXaxis().SetLabelSize(0)
    setHistStyle(hists['ttbar'])
    setHistStyle(hists['tbar'])
    setHistStyle(hists['data'])
    setHistStyle(hists['bkgSum'])
#Set tbar histogram options
hists['tbar'].SetLineColor(kRed)
hists['tbar'].SetLineWidth(3)
#Set ttbar histogram options
hists['ttbar'].SetLineColor(kRed)
hists['ttbar'].SetLineStyle(2)
hists['ttbar'].SetLineWidth(3)
#Set data histogram options
hists['data'].SetMarkerStyle(20)
hists['data'].SetMarkerSize(1.25)
hists['data'].SetLineColor(1)
#Set bkgSum histogram options
hists['bkgSum'].SetFillStyle(3002)
hists['bkgSum'].SetFillColor(1)
#Add legend
legend = TLegend(0.4, 0.65, 0.85, 0.85)
legend.SetNColumns(3)
legend.AddEntry(hists['data'], 'Data', 'pe')
legend.AddEntry(hists['ZTo2Nu'], 'Z(#nu#nu) + jets', 'f')
legend.AddEntry(hists['TTToSemiLepton'], 't#bar{t}(1l)', 'f')
legend.AddEntry(hists['TTTo2L2Nu'], 't#bar{t}(2l)', 'f')
legend.AddEntry(hists['TTV'], 't#bar{t}+V', 'f')
legend.AddEntry(hists['WPlusJets'], 'W(l#nu) + jets', 'f')
legend.AddEntry(hists['singleTop'], 't+X', 'f')
legend.AddEntry(hists['VV'], 'VV,VH', 'f')
legend.AddEntry(hists['ZTo2L'], 'Z(ll) + jets', 'f')
legend.AddEntry(hists['QCD'], 'multijet', 'f')
legend.AddEntry(hists['bkgSum'], 'MC stat.', 'f')
if scaleFactor != 1: 
    legend.AddEntry(hists['ttbar'], 'Scalar, t#bar{t}+DM (x'+str(scaleFactor)+')', 'l')
    legend.AddEntry(hists['tbar'], 'Scalar, t+DM (x'+str(scaleFactor)+')', 'l')
else:
    legend.AddEntry(hists['ttbar'], 'Scalar, t#bar{t}+DM', 'l')
    legend.AddEntry(hists['tbar'], 'Scalar, t+DM', 'l')
legend.Draw('same')
legend.SetBorderSize(0)
legend.SetFillStyle(0)
print("Finished drawing histograms")

#Create and draw ratio plot histogram if drawData = True
if drawData:
    print("Drawing ratio plot...")
    c.cd(2)
    h_ratio = TH1F('h_ratio', ratioLabel, nbins, xmin, xmax)
    setHistStyle(h_ratio) #Set settings for ratio histogram title/labels
    h_err = hists['bkgSum'].Clone('err')
    #h_MCsum = hists['QCD'] + hists['ZTo2L'] + hists['VV'] + hists['singleTop'] + hists['WPlusJets'] + hists['TTV'] + hists['TTTo2L2Nu'] + hists['TTToSemiLepton'] + hists['ZTo2Nu']
    for i in range(1, nbins+1):
        if hists['bkgSum'].GetBinContent(i) > 0:
            h_ratio.SetBinContent(i,hists['data'].GetBinContent(i)/hists['bkgSum'].GetBinContent(i))
            h_err.SetBinContent(i,hists['bkgSum'].GetBinContent(i)/hists['bkgSum'].GetBinContent(i))
            h_ratio.SetBinError(i,hists['data'].GetBinError(i)/hists['bkgSum'].GetBinContent(i))
            h_err.SetBinError(i,hists['bkgSum'].GetBinError(i)/hists['bkgSum'].GetBinContent(i))
    #Set settings for ratio histogram axes/labels
    setBotStyle(h_ratio) 
    h_ratio.Draw('pe0')
    h_err.Draw('e2 same')

    #Set settings for MC statistical error ratio histogram
    h_err.SetFillStyle(3002)
    h_err.SetFillColor(1)
    #Set ratio histogram marker options
    h_ratio.SetMarkerStyle(20)
    h_ratio.SetMarkerSize(1.25)
    h_ratio.SetLineColor(1)
    print("Finished drawing ratio plot")
        
#Save histogram
if useCondor:
    c.SaveAs(cut + str(year) + "_" + var + "_" + date + ".png")
    #c.SaveAs(cut + str(year) + "_" + var + "_" + date + ".root")
else:
    c.SaveAs(saveDirectory + date + "/" + cut + str(year) + "_" + var + "_" + date + ".png")
#c.SaveAs("test.png")

print 'Plotting end time:', datetime.datetime.now()
