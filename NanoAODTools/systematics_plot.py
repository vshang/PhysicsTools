from ROOT import *
gROOT.SetBatch(True)
import os
import datetime
import re
from utils import *

#Select year and cut to plot for systematic variation
year = 2016
cutName = 'AH'

gStyle.SetOptStat(0)
f=TFile.Open('ttbarPlusJets_Run'+str(year)+'_v7_ModuleCommon09242022.root','')
t=f.Get('Events')

#Define selection cuts and filters here
cuts = {}

if year == 2016:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter'
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight'
elif (year == 2017) or (year == 2018):
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2'# && Flag_eeBadScFilter'
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'

cuts['PV'] = 'PV_npvsGood > 0 && PV_ndof > 4 && abs(PV_z) < 24 && sqrt(pow(PV_x,2)+pow(PV_y,2)) < 2'

#cuts['AH'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' + ' && ' + cuts['PV']
cuts['AH'] = 'njets >= 3 && METcorrected_pt >= 250'

cuts['AH0l0fSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1') + ' && nfjets == 0 && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['AH0l1fSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1') + ' && nfjets >= 1 && minDeltaPhi12 >= 0.8 && M_Tb >= 140' #+ ' && ((Jet_pt[index_forwardJets[0]] < Jet_pt[index_centralJets[0]]) || min(abs(Jet_phi[index_forwardJets[0]]-METcorrected_phi),2*pi-abs(Jet_phi[index_forwardJets[0]]-METcorrected_phi)) < 2.8)'
cuts['AH0l2bSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets >= 2') + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140 && jet1p_TH_T <= 0.5' #+ ' && nfjets == 0' #+ ' && ((nfjets == 0) || (nfjets >= 1 && Jet_pt[index_forwardJets[0]] < Jet_pt[index_centralJets[0]]))'

jesUnc = ['','AbsoluteMPFBias', 'AbsoluteScale', 'AbsoluteStat', 'FlavorQCD', 'Fragmentation', 'PileUpDataMC', 'PileUpPtBB', 'PileUpPtEC1', 'PileUpPtEC2', 'PileUpPtHF', 'PileUpPtRef', 'RelativeFSR', 'RelativeJEREC1', 'RelativeJEREC2', 'RelativeJERHF', 'RelativePtBB', 'RelativePtEC1', 'RelativePtEC2', 'RelativePtHF', 'RelativeBal', 'RelativeSample', 'RelativeStatEC', 'RelativeStatFSR', 'RelativeStatHF', 'SinglePionECAL', 'SinglePionHCAL', 'TimePtEta']

def addSys(sysName, cut):
    cutUp = cutDown = cut

    #Systematics
    for unc in jesUnc:
        if sysName == 'CMS_scale'+unc+'_j':
        
            cutUp = cut.replace('METcorrected_pt ','METcorrected_ptScale'+unc+'Up ')
            cutUp = cutUp.replace('njets ','njetsScale'+unc+'Up ')
            cutUp = cutUp.replace('nfjets ','nfjetsScale'+unc+'Up ')
            cutUp = cutUp.replace('nbjets ','nbjetsScale'+unc+'Up ')
            cutUp = cutUp.replace('minDeltaPhi ','minDeltaPhiScale'+unc+'Up ')
            cutUp = cutUp.replace('minDeltaPhi12 ','minDeltaPhi12Scale'+unc+'Up ')
            cutUp = cutUp.replace('M_Tb ','M_TbScale'+unc+'Up ')
            cutUp = cutUp.replace('M_T ','M_TScale'+unc+'Up ')
            cutUp = cutUp.replace('M_T2W ','M_T2WScale'+unc+'Up ')
            cutUp = cutUp.replace('M_T2ll ','M_T2llScale'+unc+'Up ')
            cutUp = cutUp.replace('jet1p_TH_T ','jet1p_TH_TScale'+unc+'Up ')
            cutUp = cutUp.replace('modified_topness ','modified_topnessScale'+unc+'Up ')
            cutUp = cutUp.replace('full_topness ','full_topnessScale'+unc+'Up ')

            cutDown = cut.replace('METcorrected_pt ','METcorrected_ptScale'+unc+'Down ')
            cutDown = cutDown.replace('njets ','njetsScale'+unc+'Down ')
            cutDown = cutDown.replace('nfjets ','nfjetsScale'+unc+'Down ')
            cutDown = cutDown.replace('nbjets ','nbjetsScale'+unc+'Down ')
            cutDown = cutDown.replace('minDeltaPhi ','minDeltaPhiScale'+unc+'Down ')
            cutDown = cutDown.replace('minDeltaPhi12 ','minDeltaPhi12Scale'+unc+'Down ')
            cutDown = cutDown.replace('M_Tb ','M_TbScale'+unc+'Down ')
            cutDown = cutDown.replace('M_T ','M_TScale'+unc+'Down ')
            cutDown = cutDown.replace('M_T2W ','M_T2WScale'+unc+'Down ')
            cutDown = cutDown.replace('M_T2ll ','M_T2llScale'+unc+'Down ')
            cutDown = cutDown.replace('jet1p_TH_T ','jet1p_TH_TScale'+unc+'Down ')
            cutDown = cutDown.replace('modified_topness ','modified_topnessScale'+unc+'Down ')
            cutDown = cutDown.replace('full_topness ','full_topnessScale'+unc+'Down ')

    if sysName == 'CMS_res_j':
        
        cutUp = cut.replace('METcorrected_pt ','METcorrected_ptResUp ')
        cutUp = cutUp.replace('njets ','njetsResUp ')
        cutUp = cutUp.replace('nfjets ','nfjetsResUp ')
        cutUp = cutUp.replace('nbjets ','nbjetsResUp ')
        cutUp = cutUp.replace('minDeltaPhi ','minDeltaPhiResUp ')
        cutUp = cutUp.replace('minDeltaPhi12 ','minDeltaPhi12ResUp ')
        cutUp = cutUp.replace('M_Tb ','M_TbResUp ')
        cutUp = cutUp.replace('M_T ','M_TResUp ')
        cutUp = cutUp.replace('M_T2W ','M_T2WResUp ')
        cutUp = cutUp.replace('M_T2ll ','M_T2llResUp ')
        cutUp = cutUp.replace('jet1p_TH_T ','jet1p_TH_TResUp ')
        cutUp = cutUp.replace('modified_topness ','modified_topnessResUp ')
        cutUp = cutUp.replace('full_topness ','full_topnessResUp ')

        cutDown = cut.replace('METcorrected_pt ','METcorrected_ptResDown ')
        cutDown = cutDown.replace('njets ','njetsResDown ')
        cutDown = cutDown.replace('nfjets ','nfjetsResDown ')
        cutDown = cutDown.replace('nbjets ','nbjetsResDown ')
        cutDown = cutDown.replace('minDeltaPhi ','minDeltaPhiResDown ')
        cutDown = cutDown.replace('minDeltaPhi12 ','minDeltaPhi12ResDown ')
        cutDown = cutDown.replace('M_Tb ','M_TbResDown ')
        cutDown = cutDown.replace('M_T ','M_TResDown ')
        cutDown = cutDown.replace('M_T2W ','M_T2WResDown ')
        cutDown = cutDown.replace('M_T2ll ','M_T2llResDown ')
        cutDown = cutDown.replace('jet1p_TH_T ','jet1p_TH_TResDown ')
        cutDown = cutDown.replace('modified_topness ','modified_topnessResDown ')
        cutDown = cutDown.replace('full_topness ','full_topnessResDown ')

    if sysName == 'CMS_UncMET':
        
        cutUp = cut.replace('METcorrected_pt ','METcorrected_ptUnclustUp ')
        cutUp = cutUp.replace('M_Tb ','M_TbUnclustUp ')
        cutUp = cutUp.replace('M_T ','M_TUnclustUp ')
        cutUp = cutUp.replace('M_T2W ','M_T2WUnclustUp ')
        cutUp = cutUp.replace('M_T2ll ','M_T2llUnclustUp ')
        cutUp = cutUp.replace('modified_topness ','modified_topnessUnclustUp ')
        cutUp = cutUp.replace('full_topness ','full_topnessUnclustUp ')
        cutUp = cutUp.replace('recoilPtMiss ', 'recoilPtMissUnclustUp ')

        cutDown = cut.replace('METcorrected_pt ','METcorrected_ptUnclustDown ')
        cutDown = cutDown.replace('M_Tb ','M_TbUnclustDown ')
        cutDown = cutDown.replace('M_T ','M_TUnclustDown ')
        cutDown = cutDown.replace('M_T2W ','M_T2WUnclustDown ')
        cutDown = cutDown.replace('M_T2ll ','M_T2llUnclustDown ')
        cutDown = cutDown.replace('modified_topness ','modified_topnessUnclustDown ')
        cutDown = cutDown.replace('full_topness ','full_topnessUnclustDown ')
        cutDown = cutDown.replace('recoilPtMiss ','recoildPtMissUnclustDown ')

    if sysName == 'CMS_pdf':
        cutUp = '(' + cutUp + ')' + '*pdfWeightUp'
        cutDown = '(' + cutDown + ')' + '*pdfWeightDown'

    return [cutUp, cutDown]

#cuts['AH'] = cuts['AH'].replace('minDeltaPhi > 0.4 && ','')

#Select systematic variable to plot
cut = cuts[cutName]
sys = 'CMS_UncMET'
var = 'recoilPtMiss'
varUp = var + 'UnclustUp'
varDown = var + 'UnclustDown'
cut_Up = addSys(sys, cut)[0]
cut_Down = addSys(sys, cut)[1]
print 'cut = ', cut
print 'cut_Up = ', cut_Up
print 'cut_Down = ', cut_Down

nbins = 15
xmin = 250
xmax = 550

histLabel = '; ; Events'

ratioLabel = '; p_{T}^{miss} (GeV); Events'
#ratioLabel = '; min#Delta#phi(jet_{1,2},p_{T}^{miss}) distribution; Events'
#ratioLabel = '; M_{T}^{b} (GeV); Events'
#ratioLabel = '; jet_{1} p_{T}/H_{T}; Events'
#ratioLabel = '; bjet_{1} #phi; Events'

hist=TH1F('hist',histLabel,nbins,xmin,xmax)
histUp=TH1F('histUp',histLabel,nbins,xmin,xmax)
histDown=TH1F('histDown',histLabel,nbins,xmin,xmax)
t.Draw(var+'>>hist', cut)
t.Draw(varUp+'>>histUp', cut_Up)
t.Draw(varDown+'>>histDown', cut_Down)

print 'hist integral = ', hist.Integral()
print 'histUp integral = ', histUp.Integral()
print 'histDown integral = ', histDown.Integral()

hist.SetBinContent(nbins,hist.GetBinContent(nbins)+hist.GetBinContent(nbins+1))
histUp.SetBinContent(nbins,histUp.GetBinContent(nbins)+histUp.GetBinContent(nbins+1))
histDown.SetBinContent(nbins,histDown.GetBinContent(nbins)+histDown.GetBinContent(nbins+1))

c1=TCanvas('c1','c1',800,800)
c1.Divide(1,2)
setTopPad(c1.GetPad(1),4)
setBotPad(c1.GetPad(2),4)
c1.cd(1)
c1.GetPad(1).SetLogy(1)
hist.Draw('hist')
histUp.Draw('hist same')
histDown.Draw('hist same')

ymin = max(0.5*min(min(histUp.GetBinContent(histUp.GetMinimumBin()), histDown.GetBinContent(histDown.GetMinimumBin())), hist.GetBinContent(hist.GetMinimumBin())),5.e-1)
#ymin = 0
ymax = 1.25*max(max(histUp.GetBinContent(histUp.GetMaximumBin()), histDown.GetBinContent(histDown.GetMaximumBin())), hist.GetBinContent(hist.GetMaximumBin()))

setHistStyle(hist)
hist.GetXaxis().SetLabelOffset(999)
hist.GetXaxis().SetLabelSize(0)
setHistStyle(histUp)
setHistStyle(histDown)

hist.SetFillColor(kGray)
hist.SetMinimum(ymin)
hist.SetMaximum(ymax)
histUp.SetLineColor(kRed)
histDown.SetLineColor(kBlue)

legend=TLegend(0.4,0.65,0.85,0.85)
legend.AddEntry(histUp,sys+'Up','l')
legend.AddEntry(histDown,sys+'Down','l')
legend.Draw('same')
legend.SetBorderSize(0)
legend.SetFillStyle(0)

c1.cd(2)
h_err = TH1F('h_ratio', ratioLabel, nbins, xmin, xmax)
h_ratioUp = TH1F('h_ratioUp', ratioLabel, nbins, xmin, xmax)
h_ratioDown = TH1F('h_ratioDown', ratioLabel, nbins, xmin, xmax)
setHistStyle(h_ratioUp)
setHistStyle(h_ratioDown)
for i in range(1, nbins+1):
    if hist.GetBinContent(i) > 0:
        h_ratioUp.SetBinContent(i,histUp.GetBinContent(i)/hist.GetBinContent(i))
        h_ratioDown.SetBinContent(i,histDown.GetBinContent(i)/hist.GetBinContent(i))
        h_err.SetBinContent(i,hist.GetBinContent(i)/hist.GetBinContent(i))
        h_err.SetBinError(i,hist.GetBinError(i)/hist.GetBinContent(i))
setBotStyle(h_err)
h_err.Draw('e2')
h_ratioUp.Draw('hist same')
h_ratioDown.Draw('hist same')
#Set settings for MC statistical error ratio histogram
h_err.SetFillStyle(3002)
h_err.SetFillColor(1)
#Set sysUp/down ratio histogram marker options
h_ratioUp.SetLineColor(kRed)
h_ratioDown.SetLineColor(kBlue)

c1.SaveAs(cutName + '_'+str(year)+'_' + var + '_' + sys + '.png')
