from ROOT import *
import os
import datetime
import re

gStyle.SetOptStat(0)
year = 2016
f=TFile.Open('ttbarPlusJets_Run'+str(year)+'_ModuleCommon_'+str(year)+'MC.root','')
t=f.Get('Events')

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

cuts['SL1e'] = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 160 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))'
cuts['SL1m'] = 'nTightMuons == 1 && nLooseMuons == 1 && nVetoElectrons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 160 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'

#Signal region definitions
cuts['SL1e0fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL1e1fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets >= 1' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL1e2bSR'] = cuts['SL1e'] + ' && ' + 'nbjets >= 2' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'

cuts['SL1m0fSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL1m1fSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1 && nfjets >= 1' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL1m2bSR'] = cuts['SL1m'] + ' && ' + 'nbjets >= 2' + ' && M_T >= 160' + ' && M_T2W >= 200' + ' && minDeltaPhi12 >= 1.2 && M_Tb >= 180'

cuts['SL1bSR'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + ')) && nbjets == 1 && M_T >= 160 && M_T2W >= 200 && minDeltaPhi12 >= 1.2 && M_Tb >= 180'
cuts['SL2bSR'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + ')) && nbjets >= 2 && M_T >= 160 && M_T2W >= 200 && minDeltaPhi12 >= 1.2 && M_Tb >= 180'

cuts['AH'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && jet1_jetId >= 3 && jet1_chHEF > 0.1 &&' + cuts['passMETfilters'] 
cuts['AH0l0fSR'] = cuts['AH'] + ' && nbjets == 1 && nfjets == 0'
cuts['AH0l2bSR'] = cuts['AH'] + ' && nbjets >= 2'

cuts['AH1bSR'] = cuts['AH'] + ' && nbjets == 1 && minDeltaPhi12 >= 1 && M_Tb >= 180'
cuts['AH1b0fSR'] = cuts['AH'] + ' && nbjets == 1 && nfjets == 0 && minDeltaPhi12 >= 1 && M_Tb >= 180'
cuts['AH1b1fSR'] = cuts['AH'] + ' && nbjets == 1 && nfjets >= 1 && minDeltaPhi12 >= 1 && M_Tb >= 180'
cuts['AH2bSR'] = cuts['AH'] + ' && nbjets >= 2 && minDeltaPhi12 >= 1 && M_Tb >= 180 && jet1p_TH_T <= 0.5'

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

#cut = 'SL1e0fSR' #Signal region cuts
#cut = 'SL1e1fSR'
#cut = 'SL1e2bSR'
#cut = 'SL1bSR'
#cut = 'SL2bSR'
#cut = 'AH0l0fSR'
#cut = 'AH0l2bSR'
#cut = 'AH1bSR'
#cut = 'AH1b0fSR'
#cut = 'AH1b1fSR'
#cut = 'AH2bSR'
#cut = 'SL1m0fSR'
#cut = 'SL1m1fSR'
#cut = 'SL1m2bSR'

cut = 'SL2eTR' #Control region cuts
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

#Select systematic variable to plot
var = 'leptonWeight'

nbins = 9
xmin = 160
xmax = 520

hist=TH1F('hist',var + ' Systematics; p_{T}^{miss} (GeV); Events',nbins,xmin,xmax)
histup=TH1F('histup',var + ' Systematics; p_{T}^{miss} (GeV); Events',nbins,xmin,xmax)
histdown=TH1F('histdown',var + ' Systematics; p_{T}^{miss} (GeV); Events',nbins,xmin,xmax)
t.Draw('METcorrected_pt>>hist',var+'*('+cuts[cut]+')')
t.Draw('METcorrected_pt>>histup',var+'Up*('+cuts[cut]+')')
t.Draw('METcorrected_pt>>histdown',var+'Down*('+cuts[cut]+')')

hist.SetBinContent(nbins,hist.GetBinContent(nbins)+hist.GetBinContent(nbins+1))
histup.SetBinContent(nbins,histup.GetBinContent(nbins)+histup.GetBinContent(nbins+1))
histdown.SetBinContent(nbins,histdown.GetBinContent(nbins)+histdown.GetBinContent(nbins+1))

c1=TCanvas('c1','c1',800,800)
hist.Draw('hist')
histup.Draw('hist same')
histdown.Draw('hist same')

ymin = 0
ymax = 1.25*max(max(histup.GetBinContent(histup.GetMaximumBin()), histdown.GetBinContent(histdown.GetMaximumBin())), hist.GetBinContent(hist.GetMaximumBin()))

hist.SetFillColor(kGray)
hist.SetMinimum(ymin)
hist.SetMaximum(ymax)
histup.SetLineColor(kRed)
histdown.SetLineColor(kBlue)

legend=TLegend(0.4,0.65,0.85,0.85)
legend.AddEntry(histup,var+'Up','l')
legend.AddEntry(histdown,var+'Down','l')
legend.Draw('same')
legend.SetBorderSize(0)
legend.SetFillStyle(0)

for i in range(nbins):
    if hist.GetBinContent(i) > histup.GetBinContent(i):
        print 'Bin ' + str(i) + ': ' + var + ' > ' + var + 'Up'
    if hist.GetBinContent(i) < histdown.GetBinContent(i):
        print 'Bin ' + str(i) + ': ' + var + ' < ' + var + 'Down'

c1.SaveAs(cut + '_' + str(year) + '_' + var + 'Sys.png')
