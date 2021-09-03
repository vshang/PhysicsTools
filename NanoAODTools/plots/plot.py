from ROOT import *
from MCsampleList import *
from DataSampleList import *
from utils import *
import os
import datetime
import re
import math

gErrorIgnoreLevel = kError
#Set save directory and date for file names
saveDirectory = 'plots/CR_2017/METcorrected_pt/'
date = '08_27_2021'
year = 2017
useCondor = True
applyHEMfix = True
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
    #if not os.path.exists( saveDirectory ) : os.makedirs( saveDirectory )

print 'Plotting start time:', datetime.datetime.now()

#Define selection cuts and filters here
cuts = {}

if year == 2016:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter'
    cuts['singleIsoEle'] = 'HLT_Ele27_WPTight_Gsf'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon175'
    cuts['singleIsoMu'] = 'HLT_IsoMu24 || HLT_IsoTkMu24'
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight'
elif year == 2017:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2 && Flag_eeBadScFilter'
    cuts['singleIsoEle'] = 'passEle32WPTightGsf2017'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
    cuts['singleIsoMu'] = 'HLT_IsoMu27' 
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'
elif year == 2018:
    cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2 && Flag_eeBadScFilter'
    cuts['singleIsoEle'] = 'HLT_Ele32_WPTight_Gsf'
    cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
    cuts['singleIsoMu'] = 'HLT_IsoMu24' 
    cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'

#Pre-selection cut definitions
preselect_cuts = ['SL1e', 'SL1m', 'AH']
cuts['SL1e'] = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 250 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['SL1m'] = 'nTightMuons == 1 && nLooseMuons == 1 && nVetoElectrons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 250 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['SL'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + '))' 
cuts['SL1b'] = cuts['SL'].replace('nbjets >= 1', 'nbjets == 1')
cuts['SL2b'] = cuts['SL'].replace('nbjets >= 1', 'nbjets >= 2')
cuts['AH'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' 
cuts['AH1b'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1')
cuts['AH2b'] = cuts['AH'].replace('nbjets >= 1', 'nbjets >= 2')

#Apply HEM fix to SR for 2018 if applyHEMfix == True
if (year == 2018) and applyHEMfix:
    for cut in preselect_cuts:
        cuts[cut] = cuts[cut] + ' && ((METcorrected_phi <= -1.62) || (METcorrected_phi >= -0.82))'

cuts['SL1e1b1FJ'] = cuts['SL1e'].replace('nbjets >= 1', 'nbjets == 1') + ' && nFatJet <= 1'
cuts['SL1e2b1FJ'] = cuts['SL1e'].replace('nbjets >= 1', 'nbjets >= 2') + ' && nFatJet <= 1'
cuts['SL1m1b1FJ'] = cuts['SL1m'].replace('nbjets >= 1', 'nbjets == 1') + ' && nFatJet <= 1'
cuts['SL1m2b1FJ'] = cuts['SL1m'].replace('nbjets >= 1', 'nbjets >= 2') + ' && nFatJet <= 1'
cuts['AH1b1FJ'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1') + ' && nFatJet <= 1'
cuts['AH2b1FJ'] = cuts['AH'].replace('nbjets >= 1', 'nbjets >= 2') + ' && nFatJet <= 1'

cuts['SL1e1b2FJ'] = cuts['SL1e'].replace('nbjets >= 1', 'nbjets == 1') + ' && nFatJet >= 2'
cuts['SL1e2b2FJ'] = cuts['SL1e'].replace('nbjets >= 1', 'nbjets >= 2') + ' && nFatJet >= 2'
cuts['SL1m1b2FJ'] = cuts['SL1m'].replace('nbjets >= 1', 'nbjets == 1') + ' && nFatJet >= 2'
cuts['SL1m2b2FJ'] = cuts['SL1m'].replace('nbjets >= 1', 'nbjets >= 2') + ' && nFatJet >= 2'
cuts['AH1b2FJ'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1') + ' && nFatJet >= 2'
cuts['AH2b2FJ'] = cuts['AH'].replace('nbjets >= 1', 'nbjets >= 2') + ' && nFatJet >= 2'

cuts['AHminSR'] = '(nVetoElectrons + nLooseMuons) == 0 && METcorrected_pt >= 250'
cuts['AH2j0bSR'] = cuts['AHminSR'] + ' && njets >= 2 && nbjets == 0'
cuts['AH2j1bSR'] = cuts['AHminSR'] + ' && njets >= 2 && nbjets == 1'
cuts['AH2j2bSR'] = cuts['AHminSR'] + ' && njets >= 2 && nbjets >= 2'

#Signal region definitions
cuts['SL1e0fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1e1fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets >= 1' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1e2bSR'] = cuts['SL1e'] + ' && ' + 'nbjets >= 2' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'

cuts['SL1m0fSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1m1fSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1 && nfjets >= 1' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1m2bSR'] = cuts['SL1m'] + ' && ' + 'nbjets >= 2' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'

cuts['AH0l0fSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1') + ' && nfjets == 0 && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['AH0l1fSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1') + ' && nfjets >= 1 && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['AH0l2bSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets >= 2') + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140 && jet1p_TH_T <= 0.5'

cuts['SL1e1bSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1eSR'] = cuts['SL1e'] + ' && ' + 'nbjets >= 1' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1m1bSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1mSR'] = cuts['SL1m'] + ' && ' + 'nbjets >= 1' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1l1bSR'] = '(' + cuts['SL1e1bSR'] + ') || (' + cuts['SL1m1bSR'] + ')'
cuts['SL1lSR'] = '(' + cuts['SL1eSR'] + ') || (' + cuts['SL1mSR'] + ')'

cuts['SL1bSR'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + ')) && nbjets == 1 && M_T >= 140 && M_T2W >= 180 && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL2bSR'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + ')) && nbjets >= 2 && M_T >= 140 && M_T2W >= 180 && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1l0fSR'] = cuts['SL1bSR'] + ' && nfjets == 0'
cuts['SL1l1fSR'] = cuts['SL1bSR'] + ' && nfjets >= 1'
cuts['SL1l2bSR'] = cuts['SL2bSR']

#modified topness categories
cuts['SL1e0fT1SR'] = cuts['SL1e0fSR'] + ' && modified_topness <= 0'
cuts['SL1e0fT2SR'] = cuts['SL1e0fSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1e0fT3SR'] = cuts['SL1e0fSR'] + ' && modified_topness > 10'
cuts['SL1e1fT1SR'] = cuts['SL1e1fSR'] + ' && modified_topness <= 0'
cuts['SL1e1fT2SR'] = cuts['SL1e1fSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1e1fT3SR'] = cuts['SL1e1fSR'] + ' && modified_topness > 10'
cuts['SL1e2bT1SR'] = cuts['SL1e2bSR'] + ' && modified_topness <= 0'
cuts['SL1e2bT2SR'] = cuts['SL1e2bSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1e2bT3SR'] = cuts['SL1e2bSR'] + ' && modified_topness > 10'

cuts['SL1m0fT1SR'] = cuts['SL1m0fSR'] + ' && modified_topness <= 0'
cuts['SL1m0fT2SR'] = cuts['SL1m0fSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1m0fT3SR'] = cuts['SL1m0fSR'] + ' && modified_topness > 10'
cuts['SL1m1fT1SR'] = cuts['SL1m1fSR'] + ' && modified_topness <= 0'
cuts['SL1m1fT2SR'] = cuts['SL1m1fSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1m1fT3SR'] = cuts['SL1m1fSR'] + ' && modified_topness > 10'
cuts['SL1m2bT1SR'] = cuts['SL1m2bSR'] + ' && modified_topness <= 0'
cuts['SL1m2bT2SR'] = cuts['SL1m2bSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1m2bT3SR'] = cuts['SL1m2bSR'] + ' && modified_topness > 10'

cuts['SL1l0fT1SR'] = cuts['SL1l0fSR'] + ' && modified_topness <= 0'
cuts['SL1l0fT2SR'] = cuts['SL1l0fSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1l0fT3SR'] = cuts['SL1l0fSR'] + ' && modified_topness > 10'
cuts['SL1l1fT1SR'] = cuts['SL1l1fSR'] + ' && modified_topness <= 0'
cuts['SL1l1fT2SR'] = cuts['SL1l1fSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1l1fT3SR'] = cuts['SL1l1fSR'] + ' && modified_topness > 10'
cuts['SL1l2bT1SR'] = cuts['SL1l2bSR'] + ' && modified_topness <= 0'
cuts['SL1l2bT2SR'] = cuts['SL1l2bSR'] + ' && modified_topness > 0 && modified_topness <= 10'
cuts['SL1l2bT3SR'] = cuts['SL1l2bSR'] + ' && modified_topness > 10'

#nFatJet categories
cuts['AHSR'] = cuts['AH'] + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['AH1bSR'] = cuts['AHSR'].replace('nbjets >= 1', 'nbjets ==1')
cuts['AH2bSR'] = cuts['AHSR'].replace('nbjets >= 1', 'nbjets >= 2') + ' && jet1p_TH_T <= 0.5'
cuts['AH1b1FJSR'] = cuts['AH1bSR'] + ' && nFatJet <= 1'
cuts['AH1b2FJSR'] = cuts['AH1bSR'] + ' && nFatJet >= 2'
cuts['AH2b1FJSR'] = cuts['AH0l2bSR'] + ' && nFatJet <= 1'
cuts['AH2b2FJSR'] = cuts['AH0l2bSR'] + ' && nFatJet >= 2'

cuts['AH1b0f1FJSR'] = cuts['AH0l0fSR'] + ' && nFatJet <= 1'
cuts['AH1b0f2FJSR'] = cuts['AH0l0fSR'] + ' && nFatJet >= 2'
cuts['AH1b1f1FJSR'] = cuts['AH0l1fSR'] + ' && nFatJet <= 1'
cuts['AH1b1f2FJSR'] = cuts['AH0l1fSR'] + ' && nFatJet >= 2'


#Control region definitions
controlRegion_cuts = ['SL2eTR', 'SL2mTR', 'SL1e1mTR', 'SL1eWR', 'SL1mWR', 'AH1eTR', 'AH1mTR', 'AH1eWR', 'AH1mWR', 'AH2eZR', 'AH2mZR', 'AH0lQR']
cuts['SL2eTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['SL2mTR'] = 'njets >= 2 && nbjets >= 1 && nVetoElectrons  == 0 && nTightMuons == 2 && nLooseMuons == 2 && METcorrected_pt >= 250 && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['SL1e1mTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 1 && nVetoElectrons == 1 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T2ll <= 80 && tightElectron1_charge != tightMuon1_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['SL1eWR'] = 'njets >= 2 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T >= 140 && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['SL1mWR'] = 'njets >= 2 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T >= 140 && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 

cuts['AH1eTR'] = 'njets >= 3 && nbjets >= 1 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T <= 140 && minDeltaPhi12 >= 0.8 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH1mTR'] = 'njets >= 3 && nbjets >= 1 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T <= 140 && minDeltaPhi12 >= 0.8 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['AH1eWR'] = 'njets >= 3 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T <= 140 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH1mWR'] = 'njets >= 3 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T <= 140 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['AH2eZR'] = 'njets >= 3 && nbjets == 0 && nTightElectrons == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH2mZR'] = 'njets >= 3 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 2 && nLooseMuons == 2 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['AH0lQR'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi12 <= 0.8 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')'  

#Apply HEM fix to CR for 2018 if applyHEMfix == True
if (year == 2018) and applyHEMfix:
    for cut in controlRegion_cuts:
        cuts[cut] = cuts[cut] + ' && ((METcorrected_phi <= -1.62) || (METcorrected_phi >= -0.82))'

cuts['SL2lTR'] = '(' + cuts['SL2eTR'] + ') || (' + cuts['SL2mTR'] + ') || (' + cuts['SL1e1mTR'] + ')'
cuts['SL1lWR'] = '(' + cuts['SL1eWR'] + ') || (' + cuts['SL1mWR'] + ')'
cuts['AH1lTR'] = '(' + cuts['AH1eTR'] + ') || (' + cuts['AH1mTR'] + ')'
cuts['AH1lWR'] = '(' + cuts['AH1eWR'] + ') || (' + cuts['AH1mWR'] + ')'
cuts['AH2lZR'] = '(' + cuts['AH2eZR'] + ') || (' + cuts['AH2mZR'] + ')'

#Select selection cut and variable to be plotted here by uncommenting

#cut = 'SL1e' #Pre-selection cuts
#cut = 'SL1m'
#cut = 'SL'
#cut = 'SL1b'
#cut = 'SL2b'
#cut = 'AH'
#cut = 'AH1b'
#cut = 'AH2b'

#cut = 'SL1e1b1FJ'
#cut = 'SL1e2b1FJ'
#cut = 'SL1m1b1FJ'
#cut = 'SL1m2b1FJ'
#cut = 'SL1e1b2FJ'
#cut = 'SL1e2b2FJ'
#cut = 'SL1m1b2FJ'
#cut = 'SL1m2b2FJ'
#cut = 'AH1b1FJ'
#cut = 'AH2b1FJ'
#cut = 'AH1b2FJ'
#cut = 'AH2b2FJ'

#cut = 'SL1e0fSR' #Signal region cuts
#cut = 'SL1e1fSR'
#cut = 'SL1e2bSR'
#cut = 'SL1m0fSR'
#cut = 'SL1m1fSR'
#cut = 'SL1m2bSR'
#cut = 'AH0l0fSR'
#cut = 'AH0l1fSR'
#cut = 'AH0l2bSR'

#cut = 'SL1l0fSR'
#cut = 'SL1l1fSR'
#cut = 'SL1l2bSR'

#cut = 'SL1l1bSR'
#cut = 'SL1lSR'

#cut = 'SL1e1bSR'
#cut = 'SL1eSR'

#cut = 'SL1l0fT1SR'
#cut = 'SL1l0fT2SR'
#cut = 'SL1l0fT3SR'
#cut = 'SL1l1fT1SR'
#cut = 'SL1l1fT2SR'
#cut = 'SL1l1fT3SR'
#cut = 'SL1l2bT1SR'
#cut = 'SL1l2bT2SR'
#cut = 'SL1l2bT3SR'

#cut = 'AH1b1FJSR'
#cut = 'AH1b2FJSR'

#cut = 'AH1b0f1FJSR'
#cut = 'AH1b0f2FJSR'
#cut = 'AH1b1f1FJSR'
#cut = 'AH1b1f2FJSR'
#cut = 'AH2b1FJSR'
#cut = 'AH2b2FJSR'

#cut = 'SL2eTR' #Control region cuts
#cut = 'SL2mTR'
#cut = 'SL1e1mTR'
cut = 'SL1eWR'
#cut = 'SL1mWR'
#cut = 'AH1eTR'
#cut = 'AH1mTR'
#cut = 'AH1eWR'
#cut = 'AH1mWR'
#cut = 'AH2eZR'
#cut = 'AH2mZR'

#cut = 'SL2lTR'
#cut = 'SL1lWR'
#cut = 'AH1lTR'
#cut = 'AH1lWR'
#cut = 'AH2lZR'
#cut = 'AH0lQR'

#cut = 'SLeCR'
#cut = 'SLmCR'
#cut = 'SL1eCR'
#cut = 'SL1mCR'
#cut = 'SL1e0bCR'
#cut = 'SL1m0bCR'

#cut = 'SL1e1bCR'
#cut = 'SL1m1bCR'

#cuts[cut] = cuts[cut].replace('&& M_T >= 140 ', '')
#cuts[cut] = cuts[cut].replace(' && M_T2ll <= 80', '')
#cuts[cut] = cuts[cut].replace('METcorrected_pt >= 250', 'METcorrected_pt >= 160')
#cuts['AH0lQR'] = cuts['AH0lQR'].replace('&& minDeltaPhi12 <= 0.8 ', '')
#cuts['AH0lQR'] = cuts['AH0lQR'] + ' && Flag_eeBadScFilter'

#Only apply ee badSC noise filter to data (https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2)
cuts['data'] = cuts[cut] + ' && Flag_eeBadScFilter'

var = 'METcorrected_pt'
#var = 'recoilPtMiss'
#var = 'METcorrected_phi'
#var = 'M_T'
#var = 'M_T2W'
#var = 'minDeltaPhi12'
#var = 'M_Tb'
#var = 'jet1p_TH_T'
#var = 'njets'
#var = 'nfjets'
#var = 'nbjets'
#var = 'MET_pt'
#var = 'Electron_pt[1]'
#var = 'Muon_pt[1]'
#var = 'Jet_pt'
#var = 'Jet_eta[index_centralJets[0]]'
#var = 'Electron_eta[index_tightElectrons[0]]'
#var = 'Muon_eta[1]'
#var = 'nTightElectrons'
#var = 'nTightMuons'
#var = 'nTightElectrons + nTightMuons'
#var = 'm_ll'
#var = 'MET_phi'
#var = 'M_T2ll'
#var = 'deltaPhij3'
#var = 'nFatJet'
#var = 'FatJet_deepTag_TvsQCD[0]'
#var = 'Jet_qgl'
#var = 'FatJet_pt[2]'
#var = 'modified_topness'
#var = 'full_topness'

#Set lumi (fb^-1) and overall signal sample scale factor here
if year == 2016:
    lumi = 35.92
elif year == 2017:
    lumi = 41.53
elif year == 2018:
    lumi = 59.83
    #lumi = 21.08 #Before HEM 15/16 Issue
    #lumi = 38.75 #After HEM 15/16 Issue
    # lumi = 14.03 #Run A
    # lumi = 7.07 #Run B
    # lumi = 6.90 #Run C
    # lumi = 31.84 #Run D
if 'SR' in cut:
    scaleFactor = 20
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
nbins = 9
xmin = 250
xmax = 610
auto_y = True
doLogPlot = False
drawData = True
mediatorType = 'scalar'
mchi = 1
mphi = 100
normalizePlots = False
useCentralSamples = True
doBinned = False
savePlots = True
combineEleMu = False
doSys = False
drawOverflow = True
drawUnderflow = False
if doBinned:
    useCentralSamples = True
    scaleFactor = 1
    savePlots = False
if not auto_y:
    ymin = 60
    ymax = 20000

histoLabel = '; p_{T}^{miss} (GeV); Events'
#histoLabel = '; Hadronic recoil (GeV); Events'
#histoLabel = '; #phi^{miss}; Events'
#histoLabel = '; M_{T} (GeV); Events'
#histoLabel = '; M_{T2}^{W} (GeV); Events'
#histoLabel = '; min#Delta#phi(jet_{1,2},p_{T}^{miss}); Events'
#histoLabel = '; M_{T}^{b} (GeV); Events'
#histoLabel = '; jet_{1} p_{T}/H_{T}; Events'
#histoLabel = '; jet_{1} #eta; Events'
#histoLabel = '; jet_{2} p_{T}; Events'
#histoLabel = '; DeepAK8 top tag discriminant value; Events'
#histoLabel = '; electron #eta; Events'
#histoLabel = '; number of b-tagged jets; Events'

#histoLabel = cut + ' M_{T} distribution; M_{T} (GeV); Events'
#histoLabel = cut + ' M_{T2}^{W} distribution; M_{T2}^{W} (GeV); Events'
#histoLabel = cut + ' min#Delta#phi(jet_{1,2},p_{T}^{miss}) distribution; min#Delta#phi(jet_{1,2},p_{T}^{miss}); Events'
#histoLabel = cut + ' M_{T}^{b} distribution; M_{T}^{b} (GeV); Events'
#histoLabel = cut + ' jet_{1} p_{T}/H_{T} distribution; jet_{1} p_{T}/H_{T}; Events'
#histoLabel = cut + ' central n_{jet} distribution; number of AK4 jets; Events'
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
#histoLabel = cut + ' #Delta#phi(jet_{3},p_{T}^{miss}) distribution; #Delta#phi(jet_{3},p_{T}^{miss}); Events'
#histoLabel = cut + ' n_{AK8 jets} distribution; number of AK8 jets; Events'
#histoLabel = cut + ' DeepAK8 top tag discriminant distribution; DeepAK8 top tag discriminant value; Events'
#histoLabel = cut + ' DeepAK8 W tag discriminant distribution; DeepAK8 W tag discriminant value; Events'
#histoLabel = cut + ' jet_{2} Quark/Gluon likelihood distribution; jet_{2} Quark/Gluon likelihood; Events'
#histoLabel = cut + ' FatJet_{3} phi^{miss} distribution; FatJet_{3} phi^{miss} (GeV); Events'
#histoLabel = cut + ' Modified topness distribution; modified topness; Events'
#histoLabel = cut + ' Full topness distribution; full topness; Events'


if drawData:
    ratioLabel = re.sub('.*distribution;', ';', histoLabel).replace('Events','Data / Bkg')
    histoLabel = re.sub(';.*;', '; ;', histoLabel)

#Remove stats box from histograms
gStyle.SetOptStat(0)


#Define signal and background histograms
if doBinned:
    if year == 2016:
        signal = ['ttbar scalar', 'ttbar pseudoscalar', 'tbar scalar']
    else:
        signal = ['ttbar scalar', 'ttbar pseudoscalar']
else:
    if year == 2016:
        signal = ['ttbar ' + mediatorType,'tbar ' + mediatorType]
    else:
        signal = ['ttbar ' + mediatorType,'ttbar pseudoscalar']
back = ['QCD','ZTo2L','VV','singleTop','WPlusJets','TTV','TTTo2L2Nu','TTToSemiLepton','ZTo2Nu']
hists = {}
sys = ['CMS_res_j','CMS_WqcdWeightRen','CMS_WqcdWeightFac','CMS_WewkWeight','CMS_pdf','CMS_HF','CMS_HF_V','CMS_eff_b', 'CMS_scale_pu', 'CMS_eff_met_trigger', 'CMS_eff_lep_trigger','CMS_trig_m','CMS_trig_e', 'pdf_accept_2l','pdf_accept_1l','pdf_accept_0l','CMS_eff_e', 'CMS_eff_m','CMS_eff_e_old', 'CMS_eff_m_old','CMS_HF_Z','CMS_HF_W','CMS_ZqcdWeightRen','CMS_ZqcdWeightFac','CMS_ZewkWeight','QCDscale_ren', 'QCDscale_fac', 'QCDscale_ren_TT', 'QCDscale_fac_TT', 'QCDscale_ren_VV', 'QCDscale_fac_VV', 'QCDscale_ren_O', 'QCDscale_fac_O',]
jesUnc = ["","AbsoluteMPFBias", "AbsoluteScale", "AbsoluteStat", "FlavorQCD", "Fragmentation", "PileUpDataMC", "PileUpPtBB", "PileUpPtEC1", "PileUpPtEC2", "PileUpPtHF", "PileUpPtRef", "RelativeFSR", "RelativeJEREC1", "RelativeJEREC2", "RelativeJERHF", "RelativePtBB", "RelativePtEC1", "RelativePtEC2", "RelativePtHF", "RelativeBal", "RelativeSample", "RelativeStatEC", "RelativeStatFSR", "RelativeStatHF", "SinglePionECAL", "SinglePionHCAL", "TimePtEta"]
for unc in jesUnc:
    sys.append('CMS_scale'+unc+'_j')
for name in ['data','bkgSum'] + signal + back:
    hists[name] = TH1F(name, histoLabel, nbins, xmin, xmax)
if doBinned:
    hists['TTbarSL'] = TH1F('ttbarSL', histoLabel, nbins, xmin, xmax)
    hists['tttDM_MChi1_MPhi100_scalar'] = TH1F('tttDM_MChi1_MPhi100_scalar', histoLabel, nbins, xmin, xmax)
    for process in signal:
        for dataset in MCSamples[process]:
            hists[dataset] = TH1F(dataset, histoLabel, nbins, xmin, xmax)
if doSys:
    print 'Making systematic histogram dictionary...'
    syshists = {}
    for sysName in sys:
        for name in hists:
            for suffix in ['Up', 'Down']:
                if name != 'data':
                    syshists[name + '_' + sysName + suffix] = TH1F(dataset, histoLabel, nbins, xmin, xmax)
                    print '    ' + name + '_' + sysName + suffix + ' histogram made'
print 'Finished making systematic histogram dictionary'

########################################################

#Helper function to fill histograms for systematics
def addSys(histName, eventTree, var, cut, sysName):
    # print '        Adding systematic histograms for ' + histName + '_' + sysName + '...'
    histUp = TH1F('histUp', histoLabel, nbins, xmin, xmax)
    histDown = TH1F('histDown', histoLabel, nbins, xmin, xmax)
    varUp = varDown = var
    cutUp = cutDown = cut

    #Systematics
    for unc in jesUnc:
        if sysName == 'CMS_scale'+unc+'_j':
            if var == 'METcorrected_pt':
                varUp = var.replace('METcorrected_pt','METcorrected_ptScale'+unc+'Up')
                varDown = var.replace('METcorrected_pt','METcorrected_ptScale'+unc+'Down')
            elif var == 'recoilPtMiss':
                varUp = var.replace('recoilPtMiss','recoilPtMissScale'+unc+'Up')
                varDown = var.replace('recoilPtMiss','recoilPtMissScale'+unc+'Down')
        
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
        if var == 'METcorrected_pt':
            varUp = var.replace('METcorrected_pt','METcorrected_ptResUp')
            varDown = var.replace('METcorrected_pt','METcorrected_ptResDown')
        elif var == 'recoilPtMiss':
            varUp = var.replace('recoilPtMiss','recoilPtMissResUp')
            varDown = var.replace('recoilPtMiss','recoilPtMissResDown')
        
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

    elif sysName == 'CMS_WqcdWeightRen':
        cutUp = cut.replace('qcdWWeight','qcdWWeightRenUp')
        cutDown = cut.replace('qcdWWeight','qcdWWeightRenDown')

    elif sysName == 'CMS_WqcdWeightFac':
        cutUp = cut.replace('qcdWWeight','qcdWWeightFacUp')
        cutDown = cut.replace('qcdWWeight','qcdWWeightFacDown')

    elif sysName == 'CMS_ZqcdWeightRen':
        cutUp = cut.replace('qcdZTo2LWeight','qcdZWeightRenUp')
        cutUp = cutUp.replace('qcdZTo2NuWeight','qcdZWeightRenUp')
        cutDown = cut.replace('qcdZTo2LWeight','qcdZWeightRenDown')
        cutDown = cutDown.replace('qcdZTo2NuWeight','qcdZWeightRenDown')

    elif sysName == 'CMS_ZqcdWeightFac':
        cutUp = cut.replace('qcdZTo2LWeight','qcdZWeightFacUp')
        cutUp = cut.replace('qcdZTo2NuWeight','qcdZWeightFacUp')
        cutDown = cut.replace('qcdZTo2LWeight','qcdZWeightFacDown')
        cutDown = cut.replace('qcdZTo2NuWeight','qcdZWeightFacDown')

    elif sysName == 'CMS_WewkWeight':
        cutUp = cut.replace('ewkWWeight', '')
        cutDown = cut

    elif sysName == 'CMS_ZewkWeight':
        cutUp = cut.replace('ewkZWeight', '')
        cutDown = cut

    elif sysName == 'CMS_pdf':
        if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName):
            cutUp = cut + '*pdfWeightUp'
            cutDown = cut + '*pdfWeightDown'

    elif sysName == 'CMS_HF':
        if ('WPlusJets' in histName) or ('ZTo2L' in histName) or ('ZTo2Nu' in histName):
            cutUp = cut + '*1.20'
            cutDown = cut + '*0.8'

    elif sysName == 'CMS_HF_V':
        if ('WPlusJets' in histName) or ('ZTo2L' in histName) or ('ZTo2Nu' in histName):
            cutUp = cut + '*(nbjets >= 1 ? 1.2 : 1.)'
            cutDown = cut + '*(nbjets >= 1 ? 1.2 : 1.)'

    elif sysName == 'CMS_HF_W':
        if ('WPlusJets' in histName):
            cutUp = cut + '*(nbjets >= 1 ? 1.2 : 1.)'
            cutDown = cut + '*(nbjets >= 1 ? 1.2 : 1.)'

    elif sysName == 'CMS_HF_Z':
        if ('ZTo2L' in histName) or ('ZTo2Nu' in histName):
            cutUp = cut + '*(nbjets >= 1 ? 1.2 : 1.)'
            cutDown = cut + '*(nbjets >= 1 ? 1.2 : 1.)'

    elif sysName == 'CMS_eff_b':
        cutUp = cut.replace('bjetWeight','bjetWeightUp')
        cutDown = cut.replace('bjetWeight','bjetWeightDown')

    elif sysName == 'CMS_scale_pu':
        cutUp = cut.replace('puWeight','puWeightUp')
        cutDown = cut.replace('puWeight','puWeightDown')

    elif sysName == 'CMS_eff_lep_trigger':
        cutUp = cut.replace('electronTriggerWeight','electronTriggerWeightUp')
        cutUp = cutUp.replace('muonTriggerWeight','muonTriggerWeightUp')
        cutDown = cut.replace('electronTriggerWeight','electronTriggerWeightDown')
        cutDown = cutDown.replace('muonTriggerWeight','muonTriggerWeightDown')

    elif sysName == 'CMS_trig_e':
        cutUp = cut.replace('electronTriggerWeight','electronTriggerWeightUp')
        cutDown = cut.replace('electronTriggerWeight','electronTriggerWeightDown')
        if ('e' in cut) or ('1l' in cut) or ('2l' in cut):
            cutUp = cutUp + '*1.020'
            cutDown = cutDown + '*0.980'

    elif sysName == 'CMS_trig_m':
        cutUp = cut.replace('muonTriggerWeight','muonTriggerWeightUp')
        cutDown = cut.replace('muonTriggerWeight','muonTriggerWeightDown')
        if ('m' in cut) or ('1l' in cut) or ('2l' in cut):
            cutUp = cutUp + '*1.002'
            cutDown = cutDown + '*0.998'

    elif sysName == 'CMS_eff_met_trigger':
        if ('e' not in cut) and ('m' not in cut) and ('1l' not in cut) and ('2l' not in cut):
            cutUp = cut + '*1.02'
            cutDown = cut + '*0.98'

    elif sysName == 'CMS_eff_e_old':
        cutUp = cut.replace('leptonWeight','leptonWeightUp')
        cutDown = cut.replace('leptonWeight','leptonWeightDown')
        
    elif sysName == 'CMS_eff_m_old':
        cutUp = cut.replace('leptonWeight','leptonWeightUp')
        cutDown = cut.replace('leptonWeight','leptonWeightDown')

    elif sysName == 'CMS_eff_e':
        cutUp = cut.replace('leptonWeight','leptonWeightUp')
        cutDown = cut.replace('leptonWeight','leptonWeightDown')
        if ('e' in cut) or ('1l' in cut) or ('2l' in cut):
            cutUp = cutUp + '*1.010'
            cutDown = cutDown + '*0.990'

    elif sysName == 'CMS_eff_m':
        cutUp = cut.replace('leptonWeight','leptonWeightUp')
        cutDown = cut.replace('leptonWeight','leptonWeightDown')
        if ('m' in cut) or ('1l' in cut) or ('2l' in cut):
            cutUp = cutUp + '*1.014'
            cutDown = cutDown + '*0.986'
    
    elif ('QCDscale' in sysName) and ('ren' in sysName):
        if ('TT' in sysName) and ('TT' in histName):
            cutUp = cut + '*qcdRenWeightUp'
            cutDown = cut + '*qcdRenWeightDown'
        elif ('VV' in sysName) and ('VV' in histName):
            cutUp = cut + '*qcdRenWeightUp'
            cutDown = cut + '*qcdRenWeightDown'
        elif ('O' in sysName) and (('QCD' in histName) or ('singleTop' in histName)):
            cutUp = cut + '*qcdRenWeightUp'
            cutDown = cut + '*qcdRenWeightDown'
        elif sysName == 'QCDscale_ren':
            if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName):
                cutUp = cut + '*qcdRenWeightUp'
                cutDown = cut + '*qcdRenWeightDown'

    elif ('QCDscale' in sysName) and ('fac' in sysName):
        if ('TT' in sysName) and ('TT' in histName):
            cutUp = cut + '*qcdFacWeightUp'
            cutDown = cut + '*qcdFacWeightDown'
        elif ('VV' in sysName) and ('VV' in histName):
            cutUp = cut + '*qcdFacWeightUp'
            cutDown = cut + '*qcdFacWeightDown'
        elif ('O' in sysName) and (('QCD' in histName) or ('singleTop' in histName)):
            cutUp = cut + '*qcdFacWeightUp'
            cutDown = cut + '*qcdFacWeightDown'
        elif sysName == 'QCDscale_fac':
            if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName):
                cutUp = cut + '*qcdFacWeightUp'
                cutDown = cut + '*qcdFacWeightDown'

    elif sys == 'pdf_accept_2l':
        if ('2e' in cut) or ('2m' in cut) or ('2l' in cut):
            cutUp = cut + '*1.060'
            cutDown = cut + '*0.940'
    
    elif sys == 'pdf_accept_1l':
        if ('1e' in cut) or ('1m' in cut) or ('1l' in cut):
            cutUp = cut + '*1.030'
            cutDown = cut + '*0.970'

    elif sys == 'pdf_accept_0l':
        if ('e' not in cut) and ('m' not in cut) and ('1l' not in cut) and ('2l' not in cut):
            cutUp = cut + '*1.060'
            cutDown = cut + '*0.940'

    eventTree.Draw(varUp+'>>histUp',cutUp)
    eventTree.Draw(varDown+'>>histDown',cutDown)
    # print '        ' + name + '_' + sysName + 'Up hist entries = ', histUp.GetEntries()
    # print '        ' + name + '_' + sysName + 'Up hist integral = ', histUp.Integral(1,nbins+1)
    # print '        ' + name + '_' + sysName + 'Down hist entries = ', histUp.GetEntries()
    # print '        ' + name + '_' + sysName + 'Down hist integral = ', histDown.Integral(1,nbins+1)
    syshists[histName + '_' + sysName + 'Up'] += histUp
    syshists[histName + '_' + sysName + 'Down'] += histDown
    # print '        Finished adding systematic histograms for ' + histName + '_' + sysName

########################################################

#Select dataset to use based on cut
datasetNames = []
if drawData:
    print("Drawing data and ratio plot...")
    if combineEleMu:
        if ('1l' in cut) or ('2l' in cut) or (cut == 'SL'):
            datasetNames.append('SingleMuon')
            datasetNames.append('SingleElectron')
            print 'Selected both SingleMuon and SingleElectron dataset'
        else:
            datasetNames.append('MET')
            print 'Selected MET dataset'
    else:
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
            dataset_nevents = dataSamples[dataset][filepath+'_Events'].GetEntries()
            nevents += dataset_nevents
            print '    nevents in filepath = ' + filepath + ': ' + str(dataset_nevents)
        dataSamples[dataset]['nevents'] = nevents
        print '    total nevents in ', dataset, ': ', nevents
print("Got data sample root files and event trees")

#Get MC background root files and event trees
print("Loading MC sample root files and event trees...")
for process in MCSamples:
    for dataset in MCSamples[process]:
        nevents = 0
        for filepath in MCSamples[process][dataset]['filepaths']:
            print 'getting events from filepath ', filepath
            MCSamples[process][dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            MCSamples[process][dataset][filepath+'_Events'] = MCSamples[process][dataset][filepath+'_TFile'].Get('Events')
            if (process in signal) and useCentralSamples and ('ttbar' in process):
                skimFile = TFile.Open(filepath.replace('ModuleCommonSkim_07152021', 'countEvents_03182021'),'')
                Mchi = MCSamples[process][dataset]['mchi']
                Mphi = MCSamples[process][dataset]['mphi']
                MediatorType = MCSamples[process][dataset]['mediatorType']
                if 'ttbar' in process:
                    signalType = 'TTbarDMJets'
                else:
                    signalType = 'TTbarDMJets'
                nevents += skimFile.Get('Events').GetEntries('GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8')
            else:
                runsTree = MCSamples[process][dataset][filepath+'_TFile'].Get('Runs')
                nRuns = runsTree.GetEntries()
                for i in range(nRuns):
                    runsTree.GetEntry(i)
                    nevents += runsTree.genEventCount
        MCSamples[process][dataset]['nevents'] = nevents
        print '    nevents in ', process, ' ', dataset, ': ', nevents
print("Got MC sample root files and event trees")

# #Uncomment this section for quickly testing plot settings
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
for dataset in dataSamples:
    if dataset in datasetNames:
        print '  Dataset = ', dataset, ' ||   nEvents = ', dataSamples[dataset]['nevents']
        for filepath in dataSamples[dataset]['filepaths']:
            hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
            if combineEleMu:
                if dataset == 'SingleMuon':
                    if cut == 'SL2lTR':
                        datacut = '((' + cuts['SL2mTR'] + ') || (' + cuts['SL1e1mTR'] + '))' + ' && Flag_eeBadScFilter'
                        print '  Using cut = ', datacut
                    else:
                        datacut = cuts[cut.replace('l','m')] + ' && Flag_eeBadScFilter'
                        print '  Using cut = ', datacut
                elif dataset == 'SingleElectron':
                    datacut = cuts[cut.replace('l','e')] + ' && Flag_eeBadScFilter'
                    print '  Using cut = ', datacut
                else:
                    datacut = cuts['data']
            else:
                datacut = cuts['data']
            if 'SingleElectron_Run2017B' in filepath: #HLT_Ele115_CaloIdVT_GsfTrkIdT trigger path not available in Run2017B (https://hypernews.cern.ch/HyperNews/CMS/get/b2g-selections/346.html?inline=-1)
                datacut = datacut.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || ','')
                print '   Using cut = ', datacut
            if 'MET_Run2017B' in filepath: #MET trigger paths also missing from Run2017B (https://hypernews.cern.ch/HyperNews/CMS/get/top-trigger/247/1.html)
                datacut = datacut.replace(' || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60','')
                print '   Using cut = ', datacut
            #datacut = datacut + ' && run < 319077'
            #datacut = datacut + ' && (event%5 == 0)' 
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
        weight = str(MCSamples[process][dataset]['xsec']*lumi/MCSamples[process][dataset]['nevents']) + '*leptonWeight*bjetWeight*puWeight*muonTriggerWeight*EE_L1_prefire_Weight*electronTriggerWeight'
        if datasetNames == ['MET']:
            weight = weight + '*METTriggerWeight'
        #Apply appropriate NLO k-factors
        # if process == 'WPlusJets':
        #     weight = weight + '*qcdWWeight*ewkWWeight'
        #     print 'Applied WPlusJets qcd/ewk Weights correctly'
        # elif process == 'ZTo2L':
        #     weight = weight + '*qcdZTo2LWeight*ewkZWeight'
        #     print 'Applied ZTo2L qcd/ewk Weights correctly'
        # elif process == 'ZTo2Nu':
        #     weight = weight + '*qcdZTo2NuWeight*ewkZWeight'
        #     print 'Applied ZTo2Nu qcd/ewk Weights correctly'
        if (process in signal) and useCentralSamples and ('ttbar' in process):
            Mchi = MCSamples[process][dataset]['mchi']
            Mphi = MCSamples[process][dataset]['mphi']
            MediatorType = MCSamples[process][dataset]['mediatorType']
            if 'ttbar' in process:
                signalType = 'TTbarDMJets'
            else:
                signalType = 'TTbarDMJets'
            weight = weight + '*GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8'
        for filepath in MCSamples[process][dataset]['filepaths']:
            hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
            MCSamples[process][dataset][filepath+'_Events'].Draw(var+'>>hist',weight+'*('+cuts[cut]+')')
            print '          hist nEntries = ', hist.GetEntries()
            print '          hist integral = ', hist.Integral(1,nbins+1)
            if process in signal:
                hists[process] += scaleFactor*hist
                if doBinned:
                    hists[dataset] += hist
                    if (dataset == 'ttDM_MChi1_MPhi100_scalar') or (process == 'tbar scalar'):
                        hists['tttDM_MChi1_MPhi100_scalar'] += hist
            elif process == 'ttbarPlusJets':
                if doBinned:
                    hists['TTbarSL'] += hist
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
                if doBinned:
                    hists['TTbarSL'] += hist
            elif process == 'QCD':
                hists['QCD'] += hist
            #Add MC histograms for systematics
            if doSys:
                for sysName in sys:
                    if process in signal:
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                        if doBinned:
                            addSys(dataset, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                            if (dataset == 'ttDM_MChi1_MPhi100_scalar') or (process == 'tbar scalar'):
                                addSys('tttDM_MChi1_MPhi100_scalar', MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'ttbarPlusJets':
                        if doBinned:
                            addSys('TTbarSL', MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                        if dataset == 'TTTo2L2Nu':
                            addSys(dataset, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                        elif dataset == 'TTToSemiLepton':
                            addSys(dataset, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'singleTop':
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'WPlusJets':
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'ZTo2L':
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'ZTo2Nu':
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif (process == 'WW' or process == 'WZ' or process == 'ZZ'):
                        addSys('VV', MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'TTV':
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                        if doBinned:
                            addSys('TTbarSL', MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'QCD':
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    

#Fill background sum histogram for calculating ratio plot
for name in back:
    hists['bkgSum'] += hists[name]
    if doSys:
        for sysName in sys:
            for suffix in ['Up','Down']:
                syshists['bkgSum_'+sysName + suffix] += syshists[name + '_' + sysName + suffix]

#Print signal and background yields and FOM
print '-----------------------------'
print 'Total data background nEvents = ', hists['data'].GetEntries()
print 'Total data background integral = ', hists['data'].Integral(1,nbins+1)
print '-----------------------------'
print 'Total MC background nEvents = ', hists['bkgSum'].GetEntries()
print 'Total MC background integral = ', hists['bkgSum'].Integral(1,nbins+1)
print '-----------------------------'
print 'Total tt+DM signal nEvents = ', hists['ttbar ' + mediatorType].GetEntries()/scaleFactor
print 'Total tt+DM signal integral = ', hists['ttbar ' + mediatorType].Integral(1,nbins+1)/scaleFactor
print '-----------------------------'
if year == 2016:
    print 'Total t+DM signal nEvents = ', hists['tbar ' + mediatorType].GetEntries()/scaleFactor
    print 'Total t+DM signal integral = ', hists['tbar ' + mediatorType].Integral(1,nbins+1)/scaleFactor
print '-----------------------------'
print 'FOM for tt+DM signal = ', hists['ttbar ' + mediatorType].Integral(1,nbins+1)/(math.sqrt(hists['bkgSum'].Integral(1,nbins+1))*scaleFactor)
if year == 2016:
    print 'FOM for t+DM signal = ', hists['tbar ' + mediatorType].Integral(1,nbins+1)/(math.sqrt(hists['bkgSum'].Integral(1,nbins+1))*scaleFactor)
print '-----------------------------'
print 'Data bin errors:'
for i in range(nbins+1):
    bin_error = hists['data'].GetBinError(i)
    print '    bin ' + str(i) + ': ' + str(bin_error)
print '-----------------------------'
print 'MC background bin errors:'
for i in range(nbins+1):
    bin_error = hists['bkgSum'].GetBinError(i)
    print '    bin ' + str(i) + ': ' + str(bin_error)
print '-----------------------------'
print 'tt+DM bin errors:'
for i in range(nbins+1):
    bin_error = hists['ttbar ' + mediatorType].GetBinError(i)
    print '    bin ' + str(i) + ': ' + str(bin_error)
print '-----------------------------'
if year == 2016:
    print 't+DM bin errors:'
    for i in range(nbins+1):
        bin_error = hists['tbar ' + mediatorType].GetBinError(i)
        print '    bin ' + str(i) + ': ' + str(bin_error)
print '-----------------------------'
for name in hists:
    print name + ' hist info:'
    print '    nEvents = ', hists[name].GetEntries()
    print '    integral = ', hists[name].Integral(1,nbins+1)
print("Finished filling histograms")

#Add overflow and underflow bins to histograms
for name in hists:
    if drawOverflow:
        hists[name].SetBinContent(nbins, hists[name].GetBinContent(nbins) + hists[name].GetBinContent(nbins+1))
    if drawUnderflow:
        hists[name].SetBinContent(1, hists[name].GetBinContent(0) + hists[name].GetBinContent(1))

#Add up MC background histos into stacked histogram
print("Creating stacked MC background histogram...")
h_MCStack = THStack('h_MCbackground', histoLabel)
for name in back:
    h_MCStack.Add(hists[name])
print("Finished stacking MC background histograms.")

#Create binned histogram root files if doBinned == True
if doBinned:
    print("Creating binned histogram root files...")
    savePrefix = saveDirectory + date + '/' + str(year) + '/'
    stepSize = (xmax-xmin)/nbins
    for i in range(1,nbins+1):
        print '--------------------------'
        print '    Bin ' + str(i)
        print '    ---------'
        leftbin = xmin + (i-1)*stepSize
        rightbin = xmin + i*stepSize
        binnedRootFile = TFile(cut+'bin_'+str(leftbin)+'_'+str(rightbin)+'.root', 'RECREATE')
        #First fill in bkgSum binned histogram
        binContent = hists['bkgSum'].GetBinContent(i)
        binError = hists['bkgSum'].GetBinError(i)
        binnedHist = TH1F('BkgSum', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
        binnedHist.SetBinContent(1, binContent)
        binnedHist.SetBinError(1, binError)
        binnedHist.Write()
        print '    bkgSum bin content: ' + str(binContent) + ', bkgSum bin error: ' + str(binError)
        #Then fill in individual background binned histograms
        for name in back:
            binContent = hists[name].GetBinContent(i)
            binError = hists[name].GetBinError(i)
            if name == 'ZTo2L':
                binnedHist = TH1F('DYJetsToLL', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            elif name == 'ZTo2Nu':
                binnedHist = TH1F('DYJetsToNuNu', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            elif name == 'QCD':
                binnedHist = TH1F('QCD', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            elif name == 'singleTop':
                binnedHist = TH1F('ST', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            elif name == 'VV':
                binnedHist = TH1F('VV', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            elif name == 'WPlusJets':
                binnedHist = TH1F('WJetsToLNu', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            elif name == 'TTToSemiLepton':
                binnedHist = TH1F('TTToSemiLepton', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            elif name == 'TTTo2L2Nu':
                binnedHist = TH1F('TTTo2L2Nu', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            elif name == 'TTV':
                binnedHist = TH1F('TTV', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            binnedHist.SetBinContent(1, binContent)
            binnedHist.SetBinError(1, binError)
            binnedHist.Write()
            print '    ' + name + ' bin content: ' + str(binContent) + ', ' + name + ' bin error: ' + str(binError)
        binContent = hists['TTbarSL'].GetBinContent(i)
        binError = hists['TTbarSL'].GetBinError(i)
        binnedHist = TH1F('TTbarSL', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
        binnedHist.SetBinContent(1, binContent)
        binnedHist.SetBinError(1, binError)
        binnedHist.Write()
        print '    TTbarSL bin content: ' + str(binContent) + ', TTbarSL bin error: ' + str(binError)
        #Then fill in data binned histogram
        binContent = hists['data'].GetBinContent(i)
        binError = hists['data'].GetBinError(i)
        binnedHist = TH1F('data_obs', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
        binnedHist.SetBinContent(1, binContent)
        binnedHist.SetBinError(1, binError)
        binnedHist.Write()
        print '    data_obs bin content: ' + str(binContent) + ', data_obs bin error: ' + str(binError)
        #Finally fill in signal MC binned histograms
        for process in signal:
            if 'ttbar' in process:
                for dataset in MCSamples[process]:
                    binContent = hists[dataset].GetBinContent(i)
                    binError = hists[dataset].GetBinError(i)
                    binnedHist = TH1F(dataset, '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                    binnedHist.SetBinContent(1, binContent)
                    binnedHist.SetBinError(1, binError)
                    binnedHist.Write()
                    print '    ' + dataset + ' bin content: ' + str(binContent) + ', ' + dataset + ' bin error: ' + str(binError)
        if year == 2016:
            binContent = hists['tbar scalar'].GetBinContent(i)
            binError = hists['tbar scalar'].GetBinError(i)
            binnedHist = TH1F('tDM_MChi1_MPhi100_scalar', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            binnedHist.SetBinContent(1, binContent)
            binnedHist.SetBinError(1, binError)
            binnedHist.Write()
            print '    tDM_MChi1_MPhi100_scalar bin content: ' + str(binContent) + ', tDM_MChi1_MPhi100_scalar bin error: ' + str(binError)
            binContent = hists['tttDM_MChi1_MPhi100_scalar'].GetBinContent(i)
            binError = hists['tttDM_MChi1_MPhi100_scalar'].GetBinError(i)
            binnedHist = TH1F('tttDM_MChi1_MPhi100_scalar', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
            binnedHist.SetBinContent(1, binContent)
            binnedHist.SetBinError(1, binError)
            binnedHist.Write()
            print '    tttDM_MChi1_MPhi100_scalar bin content: ' + str(binContent) + ', tttDM_MChi1_MPhi100_scalar bin error: ' + str(binError)
        #Add systematics
        if doSys:
            directories = {}
            for sysName in sys:
                for suffix in ['Up','Down']:
                    directories[sysName+suffix] = binnedRootFile.mkdir(sysName+suffix)
                    directories[sysName+suffix].cd()
                    #First fill in bkgSum binned histogram systematics
                    print '    ---------'
                    print '    ' + sysName + suffix + ':'
                    print '    ---------'
                    binContent = syshists['bkgSum_' + sysName + suffix].GetBinContent(i)
                    binError = syshists['bkgSum_' + sysName + suffix].GetBinError(i)
                    binnedHist = TH1F('BkgSum', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                    binnedHist.SetBinContent(1, binContent)
                    binnedHist.SetBinError(1, binError)
                    binnedHist.Write()
                    print '    bkgSum_' + sysName + suffix + ' bin content: ' + str(binContent) + ', bkgSum_' + sysName + suffix + ' bin error: ' + str(binError)
                    #Then fill in individual background binned histogram systematics
                    for name in back:
                        binContent = syshists[name + '_' + sysName + suffix].GetBinContent(i)
                        binError = syshists[name + '_' + sysName + suffix].GetBinError(i)
                        if name == 'ZTo2L':
                            binnedHist = TH1F('DYJetsToLL', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        elif name == 'ZTo2Nu':
                            binnedHist = TH1F('DYJetsToNuNu', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        elif name == 'QCD':
                            binnedHist = TH1F('QCD', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        elif name == 'singleTop':
                            binnedHist = TH1F('ST', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        elif name == 'VV':
                            binnedHist = TH1F('VV', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        elif name == 'WPlusJets':
                            binnedHist = TH1F('WJetsToLNu', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        elif name == 'TTToSemiLepton':
                            binnedHist = TH1F('TTToSemiLepton', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        elif name == 'TTTo2L2Nu':
                            binnedHist = TH1F('TTTo2L2Nu', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        elif name == 'TTV':
                            binnedHist = TH1F('TTV', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        binnedHist.SetBinContent(1, binContent)
                        binnedHist.SetBinError(1, binError)
                        binnedHist.Write()
                        print '    ' + name + '_' + sysName + suffix + ' bin content: ' + str(binContent) + ', ' + name + '_' + sysName + suffix + ' bin error: ' + str(binError)
                    binContent = syshists['TTbarSL_' + sysName + suffix].GetBinContent(i)
                    binError = syshists['TTbarSL_' + sysName + suffix].GetBinError(i)
                    binnedHist = TH1F('TTbarSL', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                    binnedHist.SetBinContent(1, binContent)
                    binnedHist.SetBinError(1, binError)
                    binnedHist.Write()
                    print '    TTbarSL_' + sysName + suffix + ' bin content: ' + str(binContent) + ', TTbarSL_' + sysName + suffix + ' bin error: ' + str(binError)
                    #Finally fill in signal MC binned histogram systematics
                    for process in signal:
                        if 'ttbar' in process:
                            for dataset in MCSamples[process]:
                                binContent = syshists[dataset + '_' + sysName + suffix].GetBinContent(i)
                                binError = syshists[dataset + '_' + sysName + suffix].GetBinError(i)
                                binnedHist = TH1F(dataset, '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                                binnedHist.SetBinContent(1, binContent)
                                binnedHist.SetBinError(1, binError)
                                binnedHist.Write()
                                print '    ' + dataset + '_' + sysName + suffix + ' bin content: ' + str(binContent) + ', ' + dataset + '_' + sysName + suffix + ' bin error: ' + str(binError)
                    if year == 2016:
                        binContent = syshists['tbar scalar_' + sysName + suffix].GetBinContent(i)
                        binError = syshists['tbar scalar_' + sysName + suffix].GetBinError(i)
                        binnedHist = TH1F('tDM_MChi1_MPhi100_scalar', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        binnedHist.SetBinContent(1, binContent)
                        binnedHist.SetBinError(1, binError)
                        binnedHist.Write()
                        print '    tDM_MChi1_MPhi100_scalar_' + sysName + suffix + ' bin content: ' + str(binContent) + ', tDM_MChi1_MPhi100_scalar_' + sysName + suffix + ' bin error: ' + str(binError)
                        binContent = syshists['tttDM_MChi1_MPhi100_scalar_' + sysName + suffix].GetBinContent(i)
                        binError = syshists['tttDM_MChi1_MPhi100_scalar_' + sysName + suffix].GetBinError(i)
                        binnedHist = TH1F('tttDM_MChi1_MPhi100_scalar', '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        binnedHist.SetBinContent(1, binContent)
                        binnedHist.SetBinError(1, binError)
                        binnedHist.Write()
                        print '    tttDM_MChi1_MPhi100_scalar_' + sysName + suffix + ' bin content: ' + str(binContent) + ', tttDM_MChi1_MPhi100_scalar_' + sysName + suffix + ' bin error: ' + str(binError)
    print("Finished creating binned histogram root files...")

#Normalize plots to area 1 if normalizePlots == True
if normalizePlots:
    for name in back:
        hists[name].Scale(1/hists['bkgSum'].Integral())
    for process in signal:
        hists[process].Scale(1./hists[process].Integral())
    if drawData:
        hists['data'].Scale(1./hists['data'].Integral())
    hists['bkgSum'].Scale(1./hists['bkgSum'].Integral())
    print("Normalized plots")
        
#Draw histograms and save if savePlots == True
if savePlots:
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
    hists['ttbar '+mediatorType].Draw('hist same')
    if year == 2016:
        secondSignal = 'tbar '+mediatorType
    else:
        secondSignal = 'ttbar pseudoscalar'
    hists[secondSignal].Draw('hist same')
    hists['data'].Draw('ep same')
    hists['bkgSum'].Draw('e2 same')
    #Draw title with lumi and beam energy
    title = TLatex()
    if drawData:
        title.SetTextSize(0.035)
        title_x = .76
        title_y = .91
    else:
        title.SetTextSize(0.03)
        title_x = .74
        title_y = .91
    if year == 2016:
        title.DrawLatexNDC(title_x, title_y, "#bf{35.9 fb^{-1} (13 TeV)}")
    elif year == 2017:
        title.DrawLatexNDC(title_x, title_y, "#bf{41.5 fb^{-1} (13 TeV)}")
    elif year == 2018:
        title.DrawLatexNDC(title_x, title_y, "#bf{59.8 fb^{-1} (13 TeV)}")
        #title.DrawLatexNDC(title_x, title_y, "#bf{21.1 fb^{-1} (13 TeV)}") #preHEM
        #title.DrawLatexNDC(title_x, title_y, "#bf{38.8 fb^{-1} (13 TeV)}") #postHEM
        #title.DrawLatexNDC(title_x, title_y, "#bf{12.0 fb^{-1} (13 TeV)}") #1/5 partial unblind
        #title.DrawLatexNDC(title_x, title_y, "#bf{4.2 fb^{-1} (13 TeV)}")   #1/5 partial unblind preHEM
        #title.DrawLatexNDC(title_x, title_y, "#bf{7.8 fb^{-1} (13 TeV)}")  #1/5 partial unblind postHEM
    #Set "CMS, work in progress" text
    pt = TPaveText(0.18, 0.75, 0.35, 0.85, "NDC")
    if drawData:
        pt.SetTextSize(0.04)
    else:
        pt.SetTextSize(0.03)
    pt.SetFillColor(0)
    pt.SetTextAlign(11)
    pt.AddText('#splitline{CMS}{#bf{#it{work in progress}}}')
    pt.Draw('same')
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
            if drawData:
                ymin = max(min(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMinimumBin()), hists['data'].GetBinContent(hists['data'].GetMinimumBin())), 5.e-1)
                ymax = 5.*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['data'].GetBinContent(hists['data'].GetMaximumBin())+hists['data'].GetBinError(hists['data'].GetMaximumBin()), hists['ttbar '+mediatorType].GetBinContent(hists['ttbar '+mediatorType].GetMaximumBin()), hists[secondSignal].GetBinContent(hists[secondSignal].GetMaximumBin()))
            else:
                ymin = max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMinimumBin()), 5.e-1)
                ymax = 5.*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['ttbar '+mediatorType].GetBinContent(hists['ttbar '+mediatorType].GetMaximumBin()), hists[secondSignal].GetBinContent(hists[secondSignal].GetMaximumBin()))
        else:
            ymin = 0
            if drawData:
                ymax = 1.25*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['data'].GetBinContent(hists['data'].GetMaximumBin())+hists['data'].GetBinError(hists['data'].GetMaximumBin()), hists['ttbar '+mediatorType].GetBinContent(hists['ttbar '+mediatorType].GetMaximumBin()), hists[secondSignal].GetBinContent(hists[secondSignal].GetMaximumBin()))
            else:
                ymax = 1.25*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['ttbar '+mediatorType].GetBinContent(hists['ttbar '+mediatorType].GetMaximumBin()), hists[secondSignal].GetBinContent(hists[secondSignal].GetMaximumBin()))
    if normalizePlots:
        ymin = 5.e-4
    h_MCStack.SetMinimum(ymin)
    h_MCStack.SetMaximum(ymax)
    #Set settings for data and MC background histogram title/labels
    if drawData:
        setHistStyle(h_MCStack)
        h_MCStack.GetXaxis().SetLabelOffset(999)
        h_MCStack.GetXaxis().SetLabelSize(0)
        setHistStyle(hists['ttbar '+mediatorType])
        setHistStyle(hists[secondSignal])
        setHistStyle(hists['data'])
        setHistStyle(hists['bkgSum'])
    #Set tbar histogram options
    hists[secondSignal].SetLineColor(kRed)
    hists[secondSignal].SetLineWidth(3)
    #Set ttbar histogram options
    hists['ttbar '+mediatorType].SetLineColor(kRed)
    hists['ttbar '+mediatorType].SetLineStyle(2)
    hists['ttbar '+mediatorType].SetLineWidth(3)
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
    if drawData:
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
        legend.AddEntry(hists['ttbar '+mediatorType], '#splitline{'+mediatorType + ', t#bar{t}+DM (x'+str(scaleFactor)+')}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
        if year == 2016:
            legend.AddEntry(hists['tbar '+mediatorType], '#splitline{'+mediatorType + ', t+DM (x'+str(scaleFactor)+')}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
        else:
            legend.AddEntry(hists['ttbar pseudoscalar'], '#splitline{pseudoscalar, t#bar{t}+DM (x'+str(scaleFactor)+')}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
    else:
        legend.AddEntry(hists['ttbar '+mediatorType], '#splitline{'+mediatorType + ', t#bar{t}+DM}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
        if year == 2016:
            legend.AddEntry(hists['tbar '+mediatorType], '#splitline{'+mediatorType + ', t+DM}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
        else:
            legend.AddEntry(hists['ttbar pseudoscalar'], '#splitline{pseudoscalar, t#bar{t}+DM}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
    legend.Draw('same')
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    print("Finished drawing histograms")

#Create and draw ratio plot histogram if drawData == True and savePlots == True
if drawData and savePlots:
    print("Drawing ratio plot...")
    c.cd(2)
    h_ratio = TH1F('h_ratio', ratioLabel, nbins, xmin, xmax)
    setHistStyle(h_ratio) #Set settings for ratio histogram title/labels
    h_err = hists['bkgSum'].Clone('err')
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
        
#Save histogram if savePlots == True
if savePlots:
    if useCondor:
        c.SaveAs(cut + str(year) + "_" + var + "_" + date + "_NLO.png")
        #c.SaveAs(cut + str(year) + "_" + var + "_" + date + ".root")
    else:
        suffix = date
        if (year == 2018) and applyHEMfix:
            suffix += '_withHEMfix'
        c.SaveAs(saveDirectory + date + '/' + cut + str(year) + "_" + var + "_" + suffix + ".png")
        #c.SaveAs(saveDirectory + date + '/' + cut + str(year) + "_" + var + "_" + date + ".png")
        #c.SaveAs(saveDirectory + cut + str(year) + "_" + var + "_" + date + "_withHEMfixv5_postHEM.png")
        #c.SaveAs("test.png")

print 'Plotting end time:', datetime.datetime.now()
