from ROOT import *
from MCsampleList import *
import os

#Set save directory and date for file names
saveDirectory = 'plots/SL_optimization/'
#saveDirectory = 'plots/AH_optimization/'
date = '02_17_2020'

if not os.path.exists( saveDirectory + date + '/' ) : os.makedirs( saveDirectory + date + '/' )

#Define selection cuts and filters here
passMETfilters = 'Flag_goodVertices && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_eeBadScFilter && Flag_globalTightHalo2016Filter && Flag_BadPFMuonFilter && Flag_chargedHadronTrackResolutionFilter'
singleIsoEle = 'HLT_Ele27_eta2p1_WPTight_Gsf || HLT_Ele32_WPTight_Gsf || HLT_Ele32_eta2p1_WPTight_Gsf || HLT_Ele27_WPLoose_Gsf || HLT_Ele27_WPTight_Gsf'
singleEle = 'HLT_Ele105_CaloIdVT_GsfTrkIdT || HLT_Ele115_CaloIdVT_GsfTrkIdT'
singleIsoMu = 'HLT_IsoMu27 || HLT_IsoTkMu27 || HLT_IsoMu24 || HLT_IsoTkMu24'

SL1e = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && njets >= 2 && nbjets >= 1 && MET_pt >= 160 && ' + passMETfilters + ' && ((' + singleIsoEle + ') || (' + singleEle + '))'
SL1e0f = SL1e + ' && ' + 'nbjets == 1 && nfjets == 0'
SL1e2b = SL1e + ' && ' + 'nbjets >= 2'

AH = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && MET_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && ' + passMETfilters
AH0l0f = AH + ' && nbjets == 1 && nfjets == 0'
AH0l2b = AH + ' && nbjets >= 2'

#Select selection cut and variable to be plotted here
cut = SL1e0f
#cut = SL1e2b
#cut = AH0l0f
#cut = AH0l2b

var = 'M_T'
#var = 'minDeltaPhi12'
#var = 'M_Tb'
#var = 'jet1p_TH_T'

#Set lum  and overall signal sample scale factor here
lumi = 35.9
scaleFactor = 20

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Get MC background root files and event trees
print("Loading MC sample root files and event trees...")
for process in samples2016:
    for dataset in samples2016[process]:
        samples2016[process][dataset]['TFile'] = TFile.Open(samples2016[process][dataset]['filepath'],'')
        samples2016[process][dataset]['Events'] = samples2016[process][dataset]['TFile'].Get('Events')
        samples2016[process][dataset]['nevents'] = samples2016[process][dataset]['Events'].GetEntries()

print("Got MC sample root files and event trees")

##Create histograms
##-----------------------------------------------------------------------------------------------

print("Creating histograms..")
#Define histograms
nbins = 10
xmin = 0
xmax = 400
histoLabel = 'SL1e0f M_{T} distribution; M_{T} (GeV); Events'
#histoLabel = 'AH0l2b min#Delta#phi(_{1,2},p_{T}^{miss}) distribution; min#Delta#phi(_{1,2},p_{T}^{miss}), Events'
#histoLabel = 'AH0l2b M_{T}^b distribution; M_{T}^b (GeV); Events'
#histoLabel = 'AH0l2b jet_{1} p_{T}/H_{T} distribution; jet_{1} p_{T}/H_{T}; Events'
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

count = 0
print("Filling histograms...")
hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
for process in samples2016:
    for dataset in samples2016[process]:
        weight = str(samples2016[process][dataset]['xsec']*lumi/samples2016[process][dataset]['nevents']) + '*eventWeight'
        samples2016[process][dataset]['Events'].Draw(var+'>>hist',weight+'*('+cut+')')
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
c = TCanvas('c', 'SL1e0f M_{T} distribution')
#c = TCanvas('c', 'AH0l2b min#Delta#phi(_{1,2},p_{T}^{miss}) distribution')
#c = TCanvas('c', 'AH0l2b M_{T}^{b} distribution')
#c = TCanvas('c', 'jet_{1} p_{T}/H_{T} distribution')
#c.SetLogy(1)
h_MCbackground.Draw('hist')
h_ttbar.Draw('hist same')
h_tbar.Draw('hist same')
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

h_MCbackground.SetMinimum(0)
h_MCbackground.SetMaximum(18000)
#Set tbar histogram options
h_tbar.SetLineColor(kRed)
h_tbar.SetLineWidth(3)
#Set ttbar histogram options
h_ttbar.SetLineColor(kRed)
h_ttbar.SetLineStyle(2)
h_ttbar.SetLineWidth(3)
#Add legend
legend = TLegend(0.4, 0.65, 0.85, 0.85)
legend.SetNColumns(3)
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
#Save histograms
c.SaveAs(saveDirectory + date + "/SL1e0f_" + var + "_histo_" + date + ".pdf")
print("Finished drawing histograms")
