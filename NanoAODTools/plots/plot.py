from ROOT import *
from MCsampleList import *
from DataSampleList import *
from utils import *
import os

#Set save directory and date for file names
saveDirectory = 'plots/data_plots/'
date = '05_18_2020'

if not os.path.exists( saveDirectory + date + '/' ) : os.makedirs( saveDirectory + date + '/' )

#Define selection cuts and filters here
cuts = {}

cuts['passMETfilters'] = 'Flag_goodVertices && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_globalTightHalo2016Filter && Flag_muonBadTrackFilter && Flag_chargedHadronTrackResolutionFilter'
cuts['singleIsoEle'] = 'HLT_Ele27_eta2p1_WPTight_Gsf || HLT_Ele32_eta2p1_WPTight_Gsf || HLT_Ele27_WPTight_Gsf'# || HLT_Ele27_WPLoose_Gsf || HLT_Ele32_WPTight_Gsf'
cuts['singleEle'] = 'HLT_Ele105_CaloIdVT_GsfTrkIdT || HLT_Ele115_CaloIdVT_GsfTrkIdT'
cuts['singleIsoMu'] = 'HLT_IsoMu27 || HLT_IsoTkMu27 || HLT_IsoMu24 || HLT_IsoTkMu24'

cuts['SL1e'] = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && njets >= 2 && nbjets >= 1 && MET_pt >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SL1m'] = 'nTightMuons == 1 && nLooseMuons == 1 && nVetoElectrons == 0 && njets >= 2 && nbjets >= 1 && MET_pt >= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['SL1e0fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 160' #+ ' && M_T2W >= 200'
cuts['SL1e2bSR'] = cuts['SL1e'] + ' && ' + 'nbjets >= 2' #+ ' && M_T >= 160' #+ ' && M_T2W >= 200'

cuts['SL1bSR'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + ')) && nbjets == 1 && M_T >= 160 && M_T2W >= 200 && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL2bSR'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + ')) && nbjets >= 2 && M_T >= 160 && M_T2W >= 200 && minDeltaPhi12 >= 1.2 && M_Tb >= 180'

cuts['AH'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && MET_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && jet1_jetId >= 3 && jet1_chHEF > 0.1 &&' + cuts['passMETfilters'] 
cuts['AH0l0fSR'] = cuts['AH'] + ' && nbjets == 1 && nfjets == 0'
cuts['AH0l2bSR'] = cuts['AH'] + ' && nbjets >= 2'

cuts['AH1bSR'] = cuts['AH'] + ' && nbjets == 1 && minDeltaPhi12 >= 1 && M_Tb >= 180'
cuts['AH2bSR'] = cuts['AH'] + ' && nbjets >= 2 && minDeltaPhi12 >= 1 && M_Tb >= 180 && jet1p_TH_T <= 0.5'


cuts['SL2eTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && MET_pt >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SL2mTR'] = 'njets >= 2 && nbjets >= 1 && nVetoElectrons  == 0 && nTightMuons == 2 && nLooseMuons == 2 && MET_pt >= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['SL1e1mTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 1 && nVetoElectrons == 1 && nTightMuons == 1 && nLooseMuons == 1 && MET_pt >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' + ' && (' + cuts['singleIsoMu'] + ')'
cuts['SL1eWR'] = 'njets >= 2 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && MET_pt >= 160 && M_T >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SL1mWR'] = 'njets >= 2 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && MET_pt >= 160 && M_T >= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'

cuts['AH1eTR'] = 'njets >= 3 && nbjets >= 1 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && MET_pt >= 250 && M_T <= 160 && minDeltaPhi12 >= 1.0 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['AH1mTR'] = 'njets >= 3 && nbjets >= 1 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && MET_pt >= 250 && M_T <= 160 && minDeltaPhi12 >= 1.0 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['AH1eWR'] = 'njets >= 3 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && MET_pt >= 250 && M_T <= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['AH1mWR'] = 'njets >= 3 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && MET_pt >= 250 && M_T <= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'

#Select selection cut and variable to be plotted here by uncommenting

cut = 'SL1e' #Pre-selection cuts
#cut = 'SL1m'
#cut = 'AH'

#cut = 'SL1e0fSR' #Signal region cuts
#cut = 'SL1e2bSR'
#cut = 'SL1bSR'
#cut = 'SL2bSR'
#cut = 'AH0l0fSR'
#cut = 'AH0l2bSR'
#cut = 'AH1bSR'
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

cuts['data'] = cuts[cut] + ' && Flag_eeBadScFilter && Flag_BadPFMuonSummer16Filter'
#cut['data'] = cut['data'].replace(' || HLT_Ele27_WPLoose_Gsf', '')
#cut['data'] = cut['data'].replace(' || HLT_Ele32_WPTight_Gsf', '')

#var = 'M_T'
#var = 'M_T2W'
#var = 'minDeltaPhi12'
#var = 'M_Tb'
#var = 'jet1p_TH_T'
#var = 'njets'
#var = 'nfjets'
var = 'MET_pt'

#Select dataset to use based on cut
datasetNames = []
if 'e' in cut or 'm' in cut:
    if 'e' in cut:
        datasetNames.append('SingleElectron')
    if 'm' in cut:
        datasetNames.append('SingleMuon')
else:
    datasetNames.append('MET')

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

print 'Cut name = ', cut
print 'MC Selection Cuts = ', cuts[cut]
print 'Data Selection Cuts = ', cuts['data']
print 'var = ', var
#print 'saveDirectory = ', saveDirectory
print 'date = ', date
print("Creating histograms..")
#Set histogram options
nbins = 9
xmin = 160
xmax = 520
auto_y = True
#auto_y = False
#doLogPlot = True
doLogPlot = False
if not auto_y:
    ymin = 60
    ymax = 20000

#Automatically activate storage of the sum of squares of errors for all new histograms
#TH1.SetDefaultSumw2() 

#histoLabel = 'SL1e2b M_{T} distribution; M_{T} (GeV); Events'
#histoLabel = 'Sl1e0f M_{T2}^{W} distribution; M_{T2}^{W} (GeV); Events'
#histoLabel = 'AH0l0f min#Delta#phi(jet_{1,2},p_{T}^{miss}) distribution; min#Delta#phi(_{1,2},p_{T}^{miss}); Events'
#histoLabel = 'AH0l2b M_{T}^{b} distribution; M_{T}^b (GeV); Events'
#histoLabel = 'AH0l2b jet_{1} p_{T}/H_{T} distribution; jet_{1} p_{T}/H_{T}; Events'
#histoLabel = 'SL1b central n_{jet} distribution; number of AK4 jets; Events'
#histoLabel = 'AH2b forward n_{jet} distribution; number of forward AK4 jets; Events'
histoLabel = 'SL2eTR p_{T}^{miss} distribution; ; Events'

ratioLabel = '; p_{T}^{miss} (GeV); Data / Bkg'

#Define histograms
signal = ['ttbar','tbar']
back = ['QCD','ZTo2L','VV','singleTop','WPlusJets','TTV','TTTo2L2Nu','TTToSemiLepton','ZTo2Nu']
hists = {}
for name in ['data','bkgSum'] + signal + back:
    hists[name] = TH1F(name, histoLabel, nbins, xmin, xmax)

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
for dataset in data2016:
    if dataset in datasetNames:
        print '  Dataset = ', dataset, ' ||   nEvents = ', data2016[dataset]['nevents']
        for filepath in data2016[dataset]['filepaths']:
            hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
            data2016[dataset][filepath+'_Events'].Draw(var+'>>hist',cuts['data'])
            print '    hist nEntries = ', hist.GetEntries()
            print '    hist integral = ', hist.Integral()
            hists['data'] += hist
            print '    hist_data nEntries = ', hists['data'].GetEntries()
            print '    hist_data integral = ', hists['data'].Integral()
for process in samples2016:
    print '  Process = ', process
    for dataset in samples2016[process]:
        print '      Dataset = ', dataset, ' ||   nEvents = ', samples2016[process][dataset]['nevents']
        weight = str(samples2016[process][dataset]['xsec']*lumi/samples2016[process][dataset]['nevents']) + '*eventWeight'
        if process == 'WPlusJets' or process == 'ZTo2L' or process == 'ZTo2Nu':
            weight = weight + '*qcdWeight*ewkWeight'
            print 'Applied qcd/ewk Weights correctly'
        for filepath in samples2016[process][dataset]['filepaths']:
            hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
            samples2016[process][dataset][filepath+'_Events'].Draw(var+'>>hist',weight+'*('+cuts[cut]+')')
            print '          hist nEntries = ', hist.GetEntries()
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
#Call Sumw2() to propagate errors for MC background correctly
for name in back:
    #hists[name].Sumw2()
    hists['bkgSum'] += hists[name]
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
c.Divide(1,2)
setTopPad(c.GetPad(1),4)
setBotPad(c.GetPad(2),4)
c.cd(1)
if doLogPlot:
    c.GetPad(1).SetLogy(1)
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
        ymax = 5.*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['data'].GetBinContent(hists['data'].GetMaximumBin())+hists['data'].GetBinError(hists['data'].GetMaximumBin()))
    else:
        ymin = 0
        ymax = 1.25*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['data'].GetBinContent(hists['data'].GetMaximumBin())+hists['data'].GetBinError(hists['data'].GetMaximumBin()))
h_MCStack.SetMinimum(ymin)
h_MCStack.SetMaximum(ymax)
#Set settings for data and MC background histogram title/labels
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

#Create and draw ratio plot histogram
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
        
#Save histograms
c.SaveAs(saveDirectory + date + "/SL1e_" + var + "_test_" + date + ".png")
#c.SaveAs("AH1mWR_" + var + "_testSingleTreeAll_" + date + ".png")
