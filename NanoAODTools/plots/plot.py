from ROOT import *
from MCsampleList import *
import os

#Select signal sample root files here
ttbar1 = 'outDir2016AnalysisSR/ttbarDM/data_2016/ttbarDM_Mchi1Mphi100_scalar_full1'
ttbar2 = 'outDir2016AnalysisSR/ttbarDM/data_2016/ttbarDM_Mchi1Mphi100_scalar_full2'
tChan = 'outDir2016AnalysisSR/tDM_tChan/data_2016/tDM_tChan_Mchi1Mphi100_scalar_full'
tWChan = 'outDir2016AnalysisSR/tDM_tWChan/data_2016/tDM_tWChan_Mchi1Mphi100_scalar_full'

#Set sameCanvas to True for all nbjets = 1 on same Canvas and nbjets >= 2 plots on same Canvas, False if you want seperate plots
sameCanvas = False

#Set save directory and date for file names
saveDirectory = 'plots/SL_optimization/'
date = '02_13_2020'

if not os.path.exists( saveDirectory + date + '/' ) : os.makedirs( saveDirectory + date + '/' )

#Define selections here
passMETfilters = lambda t : t.Flag_goodVertices and t.Flag_HBHENoiseFilter and t.Flag_HBHENoiseIsoFilter and t.Flag_EcalDeadCellTriggerPrimitiveFilter and t.Flag_eeBadScFilter and t.Flag_globalTightHalo2016Filter and t.Flag_BadPFMuonFilter and t.Flag_chargedHadronTrackResolutionFilter
singleIsoEle = lambda t : t.HLT_Ele27_eta2p1_WPTight_Gsf or t.HLT_Ele32_WPTight_Gsf or t.HLT_Ele32_eta2p1_WPTight_Gsf or t.HLT_Ele27_WPLoose_Gsf or t.HLT_Ele27_WPTight_Gsf
singleEle = lambda t : t.HLT_Ele105_CaloIdVT_GsfTrkIdT or t.HLT_Ele115_CaloIdVT_GsfTrkIdT
singleIsoMu = lambda t : t.HLT_IsoMu27 or t.HLT_IsoTkMu27 or t.HLT_IsoMu24 or t.HLT_IsoTkMu24
SL1e = lambda t : t.nTightElectrons == 1 and t.nVetoElectrons == 1 and t.nLooseMuons == 0 and t.njets >= 2 and t.nbjets >= 1 and t.MET_pt >= 160 and passMETfilters(t) and (singleIsoEle(t) or singleEle(t))
SL1e0f = lambda t : SL1e(t) and t.nbjets == 1 and t.nfjets == 0

#Set signal sample cross sections here
ttbarXSec = 672.3
tChanXSec = 268.3
tWChanXSec = 55.49

#Set lum  and overall scale factor here
lumi = 35.9
scaleFactor = 20

#Set total number of events in signal samples here
nEvents_ttbar = 363143.0 
nEvents_tChan = 500000.0
nEvents_tWChan = 200000.0

#Single sample weights are calculated here
ttbarWeight = ttbarXSec*lumi*scaleFactor/nEvents_ttbar
tChanWeight = tChanXSec*lumi*scaleFactor/nEvents_tChan
tWChanWeight = tWChanXSec*lumi*scaleFactor/nEvents_tWChan
#print ttbarWeight, tChanWeight, tWChanWeight

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Define list of suffixes to use and dictionary of files for ttbar, tChan, and tWChan
#suffixList = ['_SL1e0fSR', '_SL1m0fSR', '_SL1e1fSR', '_SL1m1fSR', '_SL1e2bSR', '_SL1m2bSR']
suffixList = ['_SL1e0fSR', '_SL1e2bSR']
ttbarFiles = {}
tChanFiles = {}
tWChanFiles = {}

#Load MC signal root files 
print("Loading MC signal root files...")
for suffix in suffixList:
    ttbarFiles['f_ttbar1' + suffix] = TFile.Open(ttbar1 + suffix + '.root', '')
    ttbarFiles['f_ttbar2' + suffix] = TFile.Open(ttbar2 + suffix + '.root', '')
    tChanFiles['f_tChan' + suffix] = TFile.Open(tChan + suffix + '.root', '')
    tWChanFiles['f_tWChan' + suffix] = TFile.Open(tWChan + suffix + '.root', '')

    ttbarFiles['f_ttbar1' + suffix + '_MT'] = TFile.Open(ttbar1 + suffix + '_MT' + '.root', '')
    ttbarFiles['f_ttbar2' + suffix + '_MT'] = TFile.Open(ttbar2 + suffix + '_MT' + '.root', '')
    tChanFiles['f_tChan' + suffix + '_MT'] = TFile.Open(tChan + suffix + '_MT' + '.root', '')
    tWChanFiles['f_tWChan' + suffix + '_MT'] = TFile.Open(tWChan + suffix + '_MT' + '.root', '')

    ttbarFiles['f_ttbar1' + suffix + '_MTandMT2W'] = TFile.Open(ttbar1 + suffix + '_MTandMT2W' + '.root', '')
    ttbarFiles['f_ttbar2' + suffix + '_MTandMT2W'] = TFile.Open(ttbar2 + suffix + '_MTandMT2W' + '.root', '')
    tChanFiles['f_tChan' + suffix + '_MTandMT2W'] = TFile.Open(tChan + suffix + '_MTandMT2W' + '.root', '')
    tWChanFiles['f_tWChan' + suffix + '_MTandMT2W'] = TFile.Open(tWChan + suffix + '_MTandMT2W' + '.root', '')
print("MC signal Root files loaded")

#Get MC signal event trees
ttbarEvents = {}
tChanEvents = {}
tWChanEvents = {}

print("Getting MC signal event trees...")
for suffix in suffixList:
    ttbarEvents['ttbar1' + suffix + '_eventTree'] = ttbarFiles['f_ttbar1' + suffix].Get('Events')
    ttbarEvents['ttbar2' + suffix + '_eventTree'] = ttbarFiles['f_ttbar2' + suffix].Get('Events')
    tChanEvents['tChan' + suffix + '_eventTree'] = tChanFiles['f_tChan' + suffix].Get('Events')
    tWChanEvents['tWChan' + suffix + '_eventTree'] = tWChanFiles['f_tWChan' + suffix].Get('Events')

    ttbarEvents['ttbar1' + suffix + '_MT_eventTree'] = ttbarFiles['f_ttbar1' + suffix + '_MT'].Get('Events')
    ttbarEvents['ttbar2' + suffix + '_MT_eventTree'] = ttbarFiles['f_ttbar2' + suffix + '_MT'].Get('Events')
    tChanEvents['tChan' + suffix + '_MT_eventTree'] = tChanFiles['f_tChan' + suffix + '_MT'].Get('Events')
    tWChanEvents['tWChan' + suffix + '_MT_eventTree'] = tWChanFiles['f_tWChan' + suffix + '_MT'].Get('Events')

    ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'] = ttbarFiles['f_ttbar1' + suffix + '_MTandMT2W'].Get('Events')
    ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'] = ttbarFiles['f_ttbar2' + suffix + '_MTandMT2W'].Get('Events')
    tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'] = tChanFiles['f_tChan' + suffix + '_MTandMT2W'].Get('Events')
    tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'] = tWChanFiles['f_tWChan' + suffix + '_MTandMT2W'].Get('Events')
print("Got MC signal event trees")

#Get MC background root files and event trees
print("Loading MC background root files and event trees...")
for process in samples2016:
    for dataset in samples2016[process]:
        samples2016[process][dataset]['TFile'] = TFile.Open(samples2016[process][dataset]['filepath'],'')
        samples2016[process][dataset]['Events'] = samples2016[process][dataset]['TFile'].Get('Events')
        samples2016[process][dataset]['nevents'] = samples2016[process][dataset]['Events'].GetEntries()

print("Got MC background root files and event trees")

##Create SL optimization plots for nbjets = 1 signal regions
##-----------------------------------------------------------------------------------------------

print("Creating SL1b histograms..")
#Define SL nbjets = 1 histograms
h_ttbarSL1b_MT = TH1F('h_ttbarSL1b_MT', 'SL1b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)
h_tbarSL1b_MT = TH1F('h_tbarSL1b_MT', 'SL1b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)
h_TTTo2L2Nu_MT = TH1F('h_TTTo2L2Nu_MT', 'SL1b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)
h_TTToSemiLepton_MT = TH1F('h_TTToSemiLepton_MT', 'SL1b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)
h_singleTop_MT = TH1F('h_singleTop_MT', 'SL1b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)


#Fill histograms
print("Filling MC signal histograms...")
for suffix in suffixList:
    if '2b' in suffix: continue
    #Fill h_ttbarSL1b_MT
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL1b_MT.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].M_T, ttbarWeight)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL1b_MT.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].M_T, ttbarWeight)
    #Fill h_tbarSL1b_MT
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL1b_MT.Fill(tChanEvents['tChan' + suffix + '_eventTree'].M_T, tChanWeight)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL1b_MT.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].M_T, tWChanWeight)
print("Finished filling MC signal histograms")

count = 0
print("Filling MC background histograms...")
for process in samples2016:
    for dataset in samples2016[process]:
        for i in range(samples2016[process][dataset]['nevents']):
            samples2016[process][dataset]['Events'].GetEntry(i)
            count += 1
            if count % 1000 == 0:
                print count
            if SL1e0f(samples2016[process][dataset]['Events']):
                weight = samples2016[process][dataset]['xsec']*lumi*samples2016[process][dataset]['Events'].eventWeight/samples2016[process][dataset]['nevents']
                if dataset == 'TTTo2L2Nu':
                    h_TTTo2L2Nu_MT.Fill(samples2016[process][dataset]['Events'].M_T, weight)
                elif dataset == 'TTToSemiLepton':
                    h_TTTo2L2Nu_MT.Fill(samples2016[process][dataset]['Events'].M_T, weight)
                elif process == 'singleTop':
                    h_singleTop_MT.Fill(samples2016[process][dataset]['Events'].M_T, weight)
print("Finished filling MC background histograms")

#Add up MC background histos into stacked histogram
print("Creating stacked MC background histogram...")
h_MCbackground_MT = THStack('h_MCbackground_MT', 'SL1b M_{T}^{W} distribution')
h_TTTo2L2Nu_MT.SetFillColor(kYellow)
h_MCbackground_MT.Add(h_TTTo2L2Nu_MT)
h_TTToSemiLepton_MT.SetFillColor(kOrange)
h_MCbackground_MT.Add(h_TTToSemiLepton_MT)
h_singleTop_MT.SetFillColor(kOrange+7)
h_MCbackground_MT.Add(h_singleTop_MT)
print("Finished stacking MC background histograms.")
        
#Draw SL1b  M_T distribution plot
print("Creating SL1b M_T distribution plot...")
if sameCanvas:
    c1b = TCanvas('c1b', 'SL1b optimization distributions')
    c1b.Divide(2,2)
    c1b.cd(1)
else:
    c1b_MT = TCanvas('c1b_MT', 'SL1b M_{T} distribution')
h_ttbarSL1b_MT.Draw('hist')
h_tbarSL1b_MT.Draw('hist same')
h_MCbackground_MT.Draw('noclear')
#Set tbar histogram options
h_tbarSL1b_MT.SetLineColor(kBlue)
h_tbarSL1b_MT.SetLineWidth(1)
h_tbarSL1b_MT.SetFillColor(kBlue)
h_tbarSL1b_MT.SetFillStyle(3003)
h_tbarSL1b_MT.SetMinimum(0)
h_tbarSL1b_MT.SetMaximum(18000)
#Set ttbar histogram options
h_ttbarSL1b_MT.SetLineColor(kRed)
h_ttbarSL1b_MT.SetLineStyle(2)
h_ttbarSL1b_MT.SetLineWidth(1)
h_ttbarSL1b_MT.SetFillColor(kRed)
h_ttbarSL1b_MT.SetFillStyle(3003)
h_ttbarSL1b_MT.SetMinimum(0)
h_ttbarSL1b_MT.SetMaximum(18000)
#Add legend
legend_SL1bMT = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL1bMT.AddEntry(h_tbarSL1b_MT, 'Scalar, t+DM', 'l')
legend_SL1bMT.AddEntry(h_ttbarSL1b_MT, 'Scalar, tt+DM', 'l')
legend_SL1bMT.AddEntry(h_TTTo2L2Nu_MT, 'tt(2l)', 'f')
legend_SL1bMT.AddEntry(h_TTToSemiLepton_MT, 'tt(1l)', 'f')
legend_SL1bMT.AddEntry(h_singleTop_MT, 't+X', 'f')
legend_SL1bMT.Draw('same')
legend_SL1bMT.SetBorderSize(0)
legend_SL1bMT.SetFillStyle(0)
#Save SL1b M_T distribution plot individually if desired
if not sameCanvas:
    c1b_MT.SaveAs(saveDirectory + date + "/SL1b_MT_histo" + date + "_test.pdf")
print("Finished creating SL1b M_T distribution plot")

#Save SL1b distribution plots on same canvas if desired
if sameCanvas:
    c1b.SaveAs(saveDirectory + date + "/SL1b_allOptimizations_histo" + date + ".pdf")
