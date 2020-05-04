from ROOT import *
from MCsampleList import *
from DataSampleList import *
from utils import *
import os

#Set save directory and date for file names
#saveDirectory = 'plots/SL_optimization/'
#saveDirectory = 'plots/AH_optimization/'
#saveDirectory = 'plots/optimized_jets/'
date = '05_03_2020'

#if not os.path.exists( saveDirectory + date + '/' ) : os.makedirs( saveDirectory + date + '/' )

#Define selection cuts and filters here
passMETfilters = 'Flag_goodVertices && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_globalTightHalo2016Filter && Flag_muonBadTrackFilter && Flag_chargedHadronTrackResolutionFilter'
singleIsoEle = 'HLT_Ele27_eta2p1_WPTight_Gsf || HLT_Ele32_eta2p1_WPTight_Gsf || HLT_Ele27_WPTight_Gsf'# || HLT_Ele27_WPLoose_Gsf || HLT_Ele32_WPTight_Gsf'
singleEle = 'HLT_Ele105_CaloIdVT_GsfTrkIdT || HLT_Ele115_CaloIdVT_GsfTrkIdT'
singleIsoMu = 'HLT_IsoMu27 || HLT_IsoTkMu27 || HLT_IsoMu24 || HLT_IsoTkMu24'

SL1e = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && njets >= 2 && nbjets >= 1 && MET_pt >= 160 && ' + passMETfilters + ' && ((' + singleIsoEle + ') || (' + singleEle + '))'
SL1m = 'nTightMuons == 1 && nLooseMuons == 1 && nVetoElectrons == 0 && njets >= 2 && nbjets >= 1 && MET_pt >= 160 && ' + passMETfilters + ' && (' + singleIsoMu + ')'
SL1e0f = SL1e + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 160' #+ ' && M_T2W >= 200'
SL1e2b = SL1e + ' && ' + 'nbjets >= 2' #+ ' && M_T >= 160' #+ ' && M_T2W >= 200'

SL1b = '((' + SL1e + ') || (' + SL1m + ')) && nbjets == 1 && M_T >= 160 && M_T2W >= 200 && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
SL2b = '((' + SL1e + ') || (' + SL1m + ')) && nbjets >= 2 && M_T >= 160 && M_T2W >= 200 && minDeltaPhi12 >= 1.2 && M_Tb >= 180'

AH = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && MET_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && jet1_jetId >= 3 && jet1_chHEF > 0.1 &&' + passMETfilters 
AH0l0f = AH + ' && nbjets == 1 && nfjets == 0'
AH0l2b = AH + ' && nbjets >= 2'

AH1b = AH + ' && nbjets == 1 && minDeltaPhi12 >= 1 && M_Tb >= 180'
AH2b = AH + ' && nbjets >= 2 && minDeltaPhi12 >= 1 && M_Tb >= 180 && jet1p_TH_T <= 0.5'


SL2eTR = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && MET_pt >= 160 && ' + passMETfilters + ' && ((' + singleIsoEle + ') || (' + singleEle + '))'
SL2mTR = 'njets >= 2 && nbjets >= 1 && nVetoElectrons  == 0 && nTightMuons == 2 && nLooseMuons == 2 && MET_pt >= 160 && ' + passMETfilters + ' && (' + singleIsoMu + ')'
SL1e1mTR = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 1 && nVetoElectrons == 1 && nTightMuons == 1 && nLooseMuons == 1 && MET_pt >= 160 && ' + passMETfilters + ' && ((' + singleIsoEle + ') || (' + singleEle + '))' + ' && (' + singleIsoMu + ')'
SL1eWR = 'njets >= 2 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && MET_pt >= 160 && M_T >= 160 && ' + passMETfilters + ' && ((' + singleIsoEle + ') || (' + singleEle + '))'
SL1mWR = 'njets >= 2 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && MET_pt >= 160 && M_T >= 160 && ' + passMETfilters + ' && (' + singleIsoMu + ')'

AH1eTR = 'njets >= 3 && nbjets >= 1 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && MET_pt >= 250 && M_T <= 160 && minDeltaPhi12 >= 1.0 && ' + passMETfilters + ' && ((' + singleIsoEle + ') || (' + singleEle + '))'
AH1mTR = 'njets >= 3 && nbjets >= 1 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && MET_pt >= 250 && M_T <= 160 && minDeltaPhi12 >= 1.0 && ' + passMETfilters + ' && (' + singleIsoMu + ')'
AH1eWR = 'njets >= 3 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && MET_pt >= 250 && M_T <= 160 && ' + passMETfilters + ' && ((' + singleIsoEle + ') || (' + singleEle + '))'
AH1mWR = 'njets >= 3 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && MET_pt >= 250 && M_T <= 160 && ' + passMETfilters + ' && (' + singleIsoMu + ')'

#Select selection cut and variable to be plotted here
#cut = SL1e0f
#cut = SL1e2b
#cut = SL1b
#cut = SL2b
#cut = AH0l0f
#cut = AH0l2b
#cut = AH1b
#cut = AH2b

#cut = SL2eTR
#cut = SL2mTR
#cut = SL1e1mTR
#cut = SL1eWR
#cut = SL1mWR
#cut = AH1eTR
#cut = AH1mTR
cut = AH1mWR
#cut = AH1mWR

cut_data = cut + ' && Flag_eeBadScFilter && Flag_BadPFMuonFilter'
#cut_data = cut_data.replace(' || HLT_Ele27_WPLoose_Gsf', '')
#cut_data = cut_data.replace(' || HLT_Ele32_WPTight_Gsf', '')

#var = 'M_T'
#var = 'M_T2W'
#var = 'minDeltaPhi12'
#var = 'M_Tb'
#var = 'jet1p_TH_T'
#var = 'njets'
#var = 'nfjets'
var = 'MET_pt'

#Set lum (fb^-1) and overall signal sample scale factor here
lumi = 35.9
scaleFactor = 20

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Get data root files and event trees
print("Loading data sample root files and event trees...")
for dataset in data2016:
    nevents = 0
    for filepath in data2016[dataset]['filepaths']:
            data2016[dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            data2016[dataset][filepath+'_Events'] = data2016[dataset][filepath+'_TFile'].Get('Events')
            nevents += data2016[dataset][filepath+'_Events'].GetEntries()
    data2016[dataset]['nevents'] = nevents
print("Got data sample root files and event trees")

#Get MC background root files and event trees
print("Loading MC sample root files and event trees...")
for process in samples2016:
    for dataset in samples2016[process]:
        nevents = 0
        for filepath in samples2016[process][dataset]['filepaths']:
            samples2016[process][dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            samples2016[process][dataset][filepath+'_Events'] = samples2016[process][dataset][filepath+'_TFile'].Get('Events')
            nevents += samples2016[process][dataset][filepath+'_Events'].GetEntries()
        samples2016[process][dataset]['nevents'] = nevents
print("Got MC sample root files and event trees")

##Create histograms
##-----------------------------------------------------------------------------------------------

print 'Cut = ', cut
print 'Cut_data = ', cut_data
print 'var = ', var
#print 'saveDirectory = ', saveDirectory
print 'date = ', date
print("Creating histograms..")
#Set histogram options
nbins = 15
xmin = 250
xmax = 550
ymin = 80
ymax = 30000

doLogPlot = True
#doLogPlot = False

#histoLabel = 'SL1e2b M_{T} distribution; M_{T} (GeV); Events'
#histoLabel = 'Sl1e0f M_{T2}^{W} distribution; M_{T2}^{W} (GeV); Events'
#histoLabel = 'AH0l0f min#Delta#phi(jet_{1,2},p_{T}^{miss}) distribution; min#Delta#phi(_{1,2},p_{T}^{miss}); Events'
#histoLabel = 'AH0l2b M_{T}^{b} distribution; M_{T}^b (GeV); Events'
#histoLabel = 'AH0l2b jet_{1} p_{T}/H_{T} distribution; jet_{1} p_{T}/H_{T}; Events'
#histoLabel = 'SL1b central n_{jet} distribution; number of AK4 jets; Events'
#histoLabel = 'AH2b forward n_{jet} distribution; number of forward AK4 jets; Events'
histoLabel = 'AH1mWR p_{T}^{miss} distribution; ; Events'

ratioLabel = '; p_{T}^{miss} (GeV); Data / Bkg'

#Define histograms
h_data = TH1F('h_data', histoLabel, nbins, xmin, xmax)
h_ttbar = TH1F('h_ttbar', histoLabel, nbins, xmin, xmax)
h_tbar = TH1F('h_tbar', histoLabel, nbins, xmin, xmax)
h_TTTo2L2Nu = TH1F('h_TTTo2L2Nu', histoLabel, nbins, xmin, xmax)
h_TTToSemiLepton = TH1F('h_TTToSemiLepton', histoLabel, nbins, xmin, xmax)
h_singleTop = TH1F('h_singleTop', histoLabel, nbins, xmin, xmax)
h_WPlusJets = TH1F('h_WPlusJets', histoLabel, nbins, xmin, xmax)
h_ZTo2L = TH1F('h_ZTo2L', histoLabel, nbins, xmin, xmax)
h_ZTo2Nu = TH1F('h_ZTo2Nu', histoLabel, nbins, xmin, xmax)
h_VV = TH1F('h_VV', histoLabel, nbins, xmin, xmax)
h_TTV = TH1F('h_TTV', histoLabel, nbins, xmin, xmax)
h_QCD = TH1F('h_QCD', histoLabel, nbins, xmin, xmax)

# for i in range(1,nbins+1):
#     h_TTTo2L2Nu.SetBinContent(i,200)
#     h_TTToSemiLepton.SetBinContent(i,200)
#     h_singleTop.SetBinContent(i,200)
#     h_WPlusJets.SetBinContent(i,200)
#     h_ZTo2L.SetBinContent(i,200)
#     h_ZTo2Nu.SetBinContent(i,200)
#     h_VV.SetBinContent(i,200)
#     h_TTV.SetBinContent(i,200)
#     h_QCD.SetBinContent(i,200)

#Fill histograms
count = 0
print("Filling histograms...")
hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
#Loop through each root file for each dataset
for dataset in data2016:
    if dataset == 'SingleMuon':
        print '  Dataset = ', dataset, ' ||   nEvents = ', data2016[dataset]['nevents']
        for filepath in data2016[dataset]['filepaths']:
            data2016[dataset][filepath+'_Events'].Draw(var+'>>hist',cut_data)
            print '    hist nEntries = ', hist.GetEntries()
            h_data += hist
for process in samples2016:
    print '  Process = ', process
    for dataset in samples2016[process]:
        print '      Dataset = ', dataset, ' ||   nEvents = ', samples2016[process][dataset]['nevents']
        weight = str(samples2016[process][dataset]['xsec']*lumi/samples2016[process][dataset]['nevents']) + '*eventWeight'
        if process == 'WPlusJets' or process == 'ZTo2L' or process == 'ZTo2Nu':
            weight = weight + '*qcdWeight*ewkWeight'
            print 'Applied qcd/ewk Weights correctly'
        for filepath in samples2016[process][dataset]['filepaths']:
            samples2016[process][dataset][filepath+'_Events'].Draw(var+'>>hist',weight+'*('+cut+')')
            print '          hist nEntries = ', hist.GetEntries()
            if process == 'ttbarDM':
                h_ttbar += scaleFactor*hist
            elif process == 'tDM':
                h_tbar += scaleFactor*hist
            elif process == 'ttbarPlusJets':
                if dataset == 'TTTo2L2Nu':
                    h_TTTo2L2Nu += hist
                elif dataset == 'TTToSemiLepton':
                    h_TTToSemiLepton += hist
            elif process == 'singleTop':
                h_singleTop += hist
            elif process == 'WPlusJets':
                h_WPlusJets += hist
            elif process == 'ZTo2L':
                h_ZTo2L += hist
            elif process == 'ZTo2Nu':
                h_ZTo2Nu += hist
            elif (process == 'WW' or process == 'WZ' or process == 'ZZ'):
                h_VV += hist
            elif process == 'TTV':
                h_TTV += hist
            elif process == 'QCD':
                h_QCD += hist
print("Finished filling histograms")

#Add up MC background histos into stacked histogram
print("Creating stacked MC background histogram...")
h_MCbackground = THStack('h_MCbackground', histoLabel)
h_MCbackground.Add(h_QCD)
h_MCbackground.Add(h_ZTo2L)
h_MCbackground.Add(h_VV)
h_MCbackground.Add(h_singleTop)
h_MCbackground.Add(h_WPlusJets)
h_MCbackground.Add(h_TTV)
h_MCbackground.Add(h_TTTo2L2Nu)
h_MCbackground.Add(h_TTToSemiLepton)
h_MCbackground.Add(h_ZTo2Nu)
print("Finished stacking MC background histograms.")
        
#Draw histograms
print("Drawing histograms...")
c = TCanvas('c', 'c', 800, 800)
c.Divide(1,2)
setTopPad(c.GetPad(1),4)
setBotPad(c.GetPad(2),4)
c.cd(1)
if doLogPlot:
    c.GetPad(1).SetLogy(1)
h_MCbackground.Draw('hist')
h_ttbar.Draw('hist same')
h_tbar.Draw('hist same')
h_data.Draw('ep same')
#Set MC background histogram options 
h_QCD.SetFillColor(kGray+1)
h_ZTo2L.SetFillColor(kGreen+1)
h_VV.SetFillColor(kBlue+2)
h_singleTop.SetFillColor(kOrange+7)
h_WPlusJets.SetFillColor(kViolet-1)
h_TTV.SetFillColor(kOrange+4)
h_TTTo2L2Nu.SetFillColor(kOrange-2)
h_TTToSemiLepton.SetFillColor(kOrange-3)
h_ZTo2Nu.SetFillColor(kAzure-4)

h_QCD.SetLineWidth(0)
h_ZTo2L.SetLineWidth(0)
h_VV.SetLineWidth(0)
h_singleTop.SetLineWidth(0)
h_WPlusJets.SetLineWidth(0)
h_TTV.SetLineWidth(0)
h_TTTo2L2Nu.SetLineWidth(0)
h_TTToSemiLepton.SetLineWidth(0)
h_ZTo2Nu.SetLineWidth(0)

h_MCbackground.SetMinimum(ymin)
h_MCbackground.SetMaximum(ymax)
#Set settings for data and MC background histogram title/labels
setHistStyle(h_MCbackground)
h_MCbackground.GetXaxis().SetLabelOffset(999)
h_MCbackground.GetXaxis().SetLabelSize(0)
setHistStyle(h_ttbar)
setHistStyle(h_tbar)
setHistStyle(h_data)
#Set tbar histogram options
h_tbar.SetLineColor(kRed)
h_tbar.SetLineWidth(3)
#Set ttbar histogram options
h_ttbar.SetLineColor(kRed)
h_ttbar.SetLineStyle(2)
h_ttbar.SetLineWidth(3)
#Set data histogram options
h_data.SetMarkerStyle(20)
h_data.SetMarkerSize(1.25)
#Add legend
legend = TLegend(0.4, 0.65, 0.85, 0.85)
legend.SetNColumns(3)
legend.AddEntry(h_data, 'Data', 'pe')
legend.AddEntry(h_ZTo2Nu, 'Z(#nu#nu) + jets', 'f')
legend.AddEntry(h_TTToSemiLepton, 't#bar{t}(1l)', 'f')
legend.AddEntry(h_TTTo2L2Nu, 't#bar{t}(2l)', 'f')
legend.AddEntry(h_TTV, 't#bar{t}+V', 'f')
legend.AddEntry(h_WPlusJets, 'W(l#nu) + jets', 'f')
legend.AddEntry(h_singleTop, 't+X', 'f')
legend.AddEntry(h_VV, 'VV,VH', 'f')
legend.AddEntry(h_ZTo2L, 'Z(ll) + jets', 'f')
legend.AddEntry(h_QCD, 'multijet', 'f')
legend.AddEntry(h_ttbar, 'Scalar, t#bar{t}+DM', 'l')
legend.AddEntry(h_tbar, 'Scalar, t+DM', 'l')
legend.Draw('same')
legend.SetBorderSize(0)
legend.SetFillStyle(0)
print("Finished drawing histograms")

#Create and draw ratio plot histogram
print("Drawing ratio plot...")
c.cd(2)
h_ratio = TH1F('h_ratio', ratioLabel, nbins, xmin, xmax)
setHistStyle(h_ratio) #Set settings for ratio histogram title/labels
h_errLine = h_ratio.Clone('errLine')
h_MCsum = h_QCD + h_ZTo2L + h_VV + h_singleTop + h_WPlusJets + h_TTV + h_TTTo2L2Nu + h_TTToSemiLepton + h_ZTo2Nu
for i in range(1, nbins+1):
    h_errLine.SetBinContent(i,1)
    if h_MCsum.GetBinContent(i) > 0:
        h_ratio.SetBinContent(i,h_data.GetBinContent(i)/h_MCsum.GetBinContent(i))
#Set settings for ratio histogram axes/labels
setBotStyle(h_ratio) 
h_ratio.Draw('p')
h_errLine.Draw('hist same')

#Set settings for ratio axis at y=1
h_errLine.SetLineWidth(1)
h_errLine.SetFillStyle(0)
#Set ratio histogram marker options
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerSize(1.25)
print("Finished drawing ratio plot")
        
#Save histograms
#c.SaveAs(saveDirectory + date + "/AH0l0f_" + var + "_allhisto_" + date + ".png")ls
c.SaveAs("AH1mWR_" + var + "_withRatioPlot_" + date + ".png")
