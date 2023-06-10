from ROOT import *
gROOT.SetBatch(True)
from utils import *
import os
import datetime
import re
import math
import json

import optparse
usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
parser.add_option('-c', '--cutName', action='store', type='string', default='', dest='cutName')
parser.add_option('-f', '--sysFirstHalf', action='store_true', default=False, dest='sysFirstHalf')
parser.add_option('-s', '--sysSecondHalf', action='store_true', default=False, dest='sysSecondHalf')
parser.add_option('-y', '--year', action='store', type='int', default=0, dest='optionYear')
parser.add_option('-p', '--plot', action='store_true', default=False, dest='optionPlot')
(options, args) = parser.parse_args()

condor_cut = options.cutName
condor_sysFirstHalf = options.sysFirstHalf
condor_sysSecondHalf = options.sysSecondHalf
condor_year = options.optionYear
condor_plot = options.optionPlot

global counter
counter = True

#Set date, year, and other global settings
gErrorIgnoreLevel = kError
date = '06_10_2023'
year = 2016
useUL = False
useCondor = True
applyHEMfix = True
partialUnblind = False

#Set save directory
saveDirectory = 'plots/systematics/CMS_eff_b_light_2018/'
#saveDirectory = 'plots/SR_2016/METcorrected_pt/'
#saveDirectory = 'plots/AN/modtopness/'
#saveDirectory = 'plots/EEl1prefire_studies/'

#If cut and year options are specified, use those instead
if condor_year != 0:
    year = condor_year
    saveDirectory = saveDirectory.replace('2016',str(year)).replace('2017',str(year)).replace('2018',str(year))
if condor_cut != '':
    if 'SR' in condor_cut:
        saveDirectory = saveDirectory.replace('CR','SR')
    else:
        saveDirectory = saveDirectory.replace('SR','CR')

#Choose samples to use based on run year (stored in MCsampleList.py and DataSampleList.py)
if useCondor:
    with open('data'+str(year)+'.json') as json_data:
        dataSamples = json.load(json_data)
    with open('samples'+str(year)+'.json') as json_mc:
        MCSamples = json.load(json_mc)
else:
    with open('plots/data'+str(year)+'v2.json') as json_data:
        dataSamples = json.load(json_data)
    with open('plots/samples'+str(year)+'v2.json') as json_mc:
        MCSamples = json.load(json_mc)

#Make sure save directory is available if not using Condor
if False:#not useCondor:
    try:
        if not os.path.exists( saveDirectory + date + '/' ) : os.makedirs( saveDirectory + date + '/' )
        #if not os.path.exists( saveDirectory ) : os.makedirs( saveDirectory )
    except OSError, e:
        if e.errno != 17:
            print("Error:", e)

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
    if useUL:
        cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilter && Flag_eeBadScFilter'
        cuts['singleIsoEle'] = 'passEle32WPTightGsf2017'
        cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
        cuts['singleIsoMu'] = 'HLT_IsoMu27' 
        cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'
    else:
        cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2'
        cuts['singleIsoEle'] = 'passEle32WPTightGsf2017'
        cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
        cuts['singleIsoMu'] = 'HLT_IsoMu27' 
        cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'
elif year == 2018:
    if useUL:
        cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilter && Flag_eeBadScFilter'
        cuts['singleIsoEle'] = 'HLT_Ele32_WPTight_Gsf'
        cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
        cuts['singleIsoMu'] = 'HLT_IsoMu24' 
        cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'
    else:
        cuts['passMETfilters'] = 'Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilterV2'
        cuts['singleIsoEle'] = 'HLT_Ele32_WPTight_Gsf'
        cuts['singleEle'] = 'HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200'
        cuts['singleIsoMu'] = 'HLT_IsoMu24' 
        cuts['MET'] = 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60'

#Primary vertex cut definitions
cuts['PV'] = 'PV_npvsGood > 0 && PV_ndof > 4 && abs(PV_z) < 24 && sqrt(pow(PV_x,2)+pow(PV_y,2)) < 2'

#Pre-selection cut definitions
preselect_cuts = ['SL1e', 'SL1m', 'AH', 'AH1', 'AH2', 'AH3', 'AH4']
cuts['SL1e'] = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 250 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' + ' && ' + cuts['PV']
cuts['SL1m'] = 'nTightMuons == 1 && nLooseMuons == 1 && nVetoElectrons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 250 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' + ' && ' + cuts['PV']
cuts['AH'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' + ' && ' + cuts['PV']

cuts['AH1'] = '(nVetoElectrons + nLooseMuons) == 0 && METcorrected_pt >= 250 && ntaus == 0 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' + ' && ' + cuts['PV']
cuts['AH1v2'] = '(nVetoElectrons + nLooseMuons) == 0 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' + ' && ' + cuts['PV']
cuts['AH1v3'] = '(nVetoElectrons + nLooseMuons) == 0 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && minDeltaPhi12 >= 0.8 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' + ' && ' + cuts['PV']
cuts['AH2'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && METcorrected_pt >= 250 && ntaus == 0 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' + ' && ' + cuts['PV']
cuts['AH3'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' + ' && ' + cuts['PV']
cuts['AH4'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi > 0.4 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' + ' && ' + cuts['PV']

cuts['SL1ev1'] = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && ' + cuts['passMETfilters']  + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['SL1mv1'] = 'nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['SL1lv1'] =  '((' + cuts['SL1ev1'] + ') || (' + cuts['SL1mv1'] + '))'

#Apply HEM fix to SR for 2018 if applyHEMfix == True
if (year == 2018) and applyHEMfix:
    for cut in preselect_cuts:
        cuts[cut] = cuts[cut] + ' && ((METcorrected_phi <= -1.62) || (METcorrected_phi >= -0.82))'

cuts['SL'] = '((' + cuts['SL1e'] + ') || (' + cuts['SL1m'] + '))' 
cuts['SL1b'] = cuts['SL'].replace('nbjets >= 1', 'nbjets == 1') 
cuts['SL2b'] = cuts['SL'].replace('nbjets >= 1', 'nbjets >= 2') 
cuts['AH1b'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1')
cuts['AH2b'] = cuts['AH'].replace('nbjets >= 1', 'nbjets >= 2')

#Signal region definitions
cuts['SL1e0fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1e1fSR'] = cuts['SL1e'] + ' && ' + 'nbjets == 1 && nfjets >= 1' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140' 
cuts['SL1e2bSR'] = cuts['SL1e'] + ' && ' + 'nbjets >= 2' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140' 

cuts['SL1m0fSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1 && nfjets == 0' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['SL1m1fSR'] = cuts['SL1m'] + ' && ' + 'nbjets == 1 && nfjets >= 1' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140' 
cuts['SL1m2bSR'] = cuts['SL1m'] + ' && ' + 'nbjets >= 2' + ' && M_T >= 140' + ' && M_T2W >= 180' + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140'

cuts['AH0l0fSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1') + ' && nfjets == 0 && minDeltaPhi12 >= 0.8 && M_Tb >= 140'
cuts['AH0l1fSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets == 1') + ' && nfjets >= 1 && minDeltaPhi12 >= 0.8 && M_Tb >= 140 && noB2Bleadingfjet' 
cuts['AH0l2bSR'] = cuts['AH'].replace('nbjets >= 1', 'nbjets >= 2') + ' && minDeltaPhi12 >= 0.8 && M_Tb >= 140 && jet1p_TH_T <= 0.5 && noB2Bleadingfjet'

cuts['SL1l0fSR'] = '(' + cuts['SL1e0fSR'] + ') || (' + cuts['SL1m0fSR'] + ')'
cuts['SL1l1fSR'] = '(' + cuts['SL1e1fSR'] + ') || (' + cuts['SL1m1fSR'] + ')'
cuts['SL1l2bSR'] = '(' + cuts['SL1e2bSR'] + ') || (' + cuts['SL1m2bSR'] + ')'

#modified topness categories
cuts['SL1e0fT1SR'] = cuts['SL1e0fSR'] + ' && modified_topness <= 0'
cuts['SL1e0fT2SR'] = cuts['SL1e0fSR'] + ' && modified_topness > 0'
cuts['SL1e1fT1SR'] = cuts['SL1e1fSR'] + ' && modified_topness <= 0'
cuts['SL1e1fT2SR'] = cuts['SL1e1fSR'] + ' && modified_topness > 0'
cuts['SL1e2bT1SR'] = cuts['SL1e2bSR'] + ' && modified_topness <= 0'
cuts['SL1e2bT2SR'] = cuts['SL1e2bSR'] + ' && modified_topness > 0'

cuts['SL1m0fT1SR'] = cuts['SL1m0fSR'] + ' && modified_topness <= 0'
cuts['SL1m0fT2SR'] = cuts['SL1m0fSR'] + ' && modified_topness > 0'
cuts['SL1m1fT1SR'] = cuts['SL1m1fSR'] + ' && modified_topness <= 0'
cuts['SL1m1fT2SR'] = cuts['SL1m1fSR'] + ' && modified_topness > 0'
cuts['SL1m2bT1SR'] = cuts['SL1m2bSR'] + ' && modified_topness <= 0'
cuts['SL1m2bT2SR'] = cuts['SL1m2bSR'] + ' && modified_topness > 0'

cuts['SL1l0fT1SR'] = '(' + cuts['SL1e0fT1SR'] + ') || (' + cuts['SL1m0fT1SR'] + ')'
cuts['SL1l0fT2SR'] = '(' + cuts['SL1e0fT2SR'] + ') || (' + cuts['SL1m0fT2SR'] + ')'
cuts['SL1l1fT1SR'] = '(' + cuts['SL1e1fT1SR'] + ') || (' + cuts['SL1m1fT1SR'] + ')'
cuts['SL1l1fT2SR'] = '(' + cuts['SL1e1fT2SR'] + ') || (' + cuts['SL1m1fT2SR'] + ')'
cuts['SL1l2bT1SR'] = '(' + cuts['SL1e2bT1SR'] + ') || (' + cuts['SL1m2bT1SR'] + ')'
cuts['SL1l2bT2SR'] = '(' + cuts['SL1e2bT2SR'] + ') || (' + cuts['SL1m2bT2SR'] + ')'


#Control region definitions
controlRegion_cuts = ['SL2eTR', 'SL2mTR', 'SL1e1mTR', 'SL1eWR', 'SL1mWR', 'AH1eTR', 'AH1mTR', 'AH1eWR', 'AH1mWR', 'AH2eZR', 'AH2mZR', 'AH0lQR', 'AH0lZR', 'AH2eZRv2', 'AH2mZRv2', 'AH2e1bZR', 'AH2m1bZR', 'AH2e2bZR', 'AH2m2bZR']
# cuts['SL2eTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
# cuts['SL2mTR'] = 'njets >= 2 && nbjets >= 1 && nVetoElectrons  == 0 && nTightMuons == 2 && nLooseMuons == 2 && METcorrected_pt >= 250 && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['SL2eTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && METcorrected_pt >= 250 && ((m_ll < 60) || (m_ll > 120)) && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['SL2mTR'] = 'njets >= 2 && nbjets >= 1 && nVetoElectrons  == 0 && nTightMuons == 2 && nLooseMuons == 2 && METcorrected_pt >= 250 && ((m_ll < 60) || (m_ll > 120)) && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['SL1e1mTR'] = 'njets >= 2 && nbjets >= 1 && nTightElectrons  == 1 && nVetoElectrons == 1 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T2ll <= 80 && tightElectron1_charge != tightMuon1_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['SL1eWR'] = 'njets >= 2 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T >= 140 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['SL1mWR'] = 'njets >= 2 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T >= 140 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 

cuts['AH1eTR'] = 'njets >= 3 && nbjets >= 1 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T <= 140 && minDeltaPhi12 >= 0.8 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH1mTR'] = 'njets >= 3 && nbjets >= 1 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T <= 140 && minDeltaPhi12 >= 0.8 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['AH1eWR'] = 'njets >= 3 && nbjets == 0 && nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && METcorrected_pt >= 250 && M_T <= 140 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH1mWR'] = 'njets >= 3 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 1 && nLooseMuons == 1 && METcorrected_pt >= 250 && M_T <= 140 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['AH2eZR'] = 'njets >= 3 && nbjets == 0 && nTightElectrons == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH2mZR'] = 'njets >= 3 && nbjets == 0 && nVetoElectrons == 0 && nTightMuons == 2 && nLooseMuons == 2 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
# cuts['AH2eZR'] = 'njets >= 3 && nbjets >= 1 && nTightElectrons == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && lepton1_charge == -lepton2_charge && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
# cuts['AH2mZR'] = 'njets >= 3 && nbjets >= 1 && nVetoElectrons == 0 && nTightMuons == 2 && nLooseMuons == 2 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && lepton1_charge == -lepton2_charge && M_T2ll <= 80 && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')'
cuts['AH0lQR'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets >= 1 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi12 <= 0.8 && noB2Bleadingfjet && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')' 

#Test control region for Z->2Nu in AH channel
cuts['AH0lZR'] = '(nVetoElectrons + nLooseMuons) == 0 && njets >= 3 && nbjets == 0 && METcorrected_pt >= 250 && ntaus == 0 && minDeltaPhi12 >= 0.8 && ' + cuts['passMETfilters']  + ' && (' + cuts['MET'] + ')'

#Test control region for 1b/2b categories of Z->2l
cuts['AH2eZRv2'] = 'njets >= 3 && nbjets >= 1 && nTightElectrons == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && M_T2ll <= 80 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH2mZRv2'] = 'njets >= 3 && nbjets >= 1 && nVetoElectrons == 0 && nTightMuons == 2 && nLooseMuons == 2 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && M_T2ll <= 80 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['AH2lZRv2'] = '(' + cuts['AH2eZRv2'] + ') || (' + cuts['AH2mZRv2'] + ')'

cuts['AH2e1bZR'] = 'njets >= 3 && nbjets == 1 && nTightElectrons == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && M_T2ll <= 80 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH2m1bZR'] = 'njets >= 3 && nbjets == 1 && nVetoElectrons == 0 && nTightMuons == 2 && nLooseMuons == 2 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && M_T2ll <= 80 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['AH2l1bZR'] = '(' + cuts['AH2e1bZR'] + ') || (' + cuts['AH2m1bZR'] + ')'

cuts['AH2e2bZR'] = 'njets >= 3 && nbjets >= 2 && nTightElectrons == 2 && nVetoElectrons == 2 && nLooseMuons == 0 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && M_T2ll <= 80 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && ((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))' 
cuts['AH2m2bZR'] = 'njets >= 3 && nbjets >= 2 && nVetoElectrons == 0 && nTightMuons == 2 && nLooseMuons == 2 && m_ll >= 60 && m_ll <= 120 && recoilPtMiss >= 250 && M_T2ll <= 80 && lepton1_charge == -lepton2_charge && ' + cuts['passMETfilters'] + ' && (' + cuts['singleIsoMu'] + ')' 
cuts['AH2l2bZR'] = '(' + cuts['AH2e2bZR'] + ') || (' + cuts['AH2m2bZR'] + ')'

#Apply primary vertex selection cuts
for cut in controlRegion_cuts:
    cuts[cut] = cuts[cut] + ' && ' + cuts['PV']

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
#cut = 'AH'

#cut = 'AH0l0fSR' #Signal region cuts
#cut = 'AH0l1fSR'
#cut = 'AH0l2bSR'

#cut = 'SL1l0fT1SR'
#cut = 'SL1l0fT2SR'
#cut = 'SL1l1fT1SR'
#cut = 'SL1l1fT2SR'
#cut = 'SL1l2bT1SR'
#cut = 'SL1l2bT2SR'

#cut = 'SL2lTR'#Control region cuts
#cut = 'SL1lWR'
#cut = 'AH1lTR'
#cut = 'AH1lWR'
#cut = 'AH2lZR'
#cut = 'AH0lQR'
#cut = 'AH0lZR'

#cuts['AH'] = cuts['AH'].replace('&& nbjets >= 1 ','') + ' && minDeltaPhi12 >= 0.8'
#cuts['AH'] = cuts['AH'].replace('&& njets >= 3 ','')
#cuts['AH'] = cuts['AH'] + ' && minDeltaPhi12 >= 0.8'
#cuts['AH0lQR'] = cuts['AH0lQR'] + ' && nfjets == 0'
#cuts[cut] = cuts[cut].replace(' && M_T2ll <= 80', '')
#cuts[cut] = cuts[cut].replace('METcorrected_pt >= 250', 'METcorrected_pt >= 160')
#cuts['AH0lQR'] = cuts['AH0lQR'].replace('&& minDeltaPhi12 <= 0.8 ', '')

# cuts['AH0lQR'] = cuts['AH0lQR'] + ' && nfjets >= 1 && Jet_pt[index_forwardJets[0]] > Jet_pt[index_centralJets[0]]'
# cuts['AH0l1fSR'] = cuts['AH0l1fSR'] + ' && Jet_pt[index_forwardJets[0]] < Jet_pt[index_centralJets[0]]'
# cuts['AH0l2bSR'] = cuts['AH0l2bSR'] + ' && nfjets >= 1 && Jet_pt[index_forwardJets[0]] < Jet_pt[index_centralJets[0]]'

# cuts['AH0lQR'] = cuts['AH0lQR'] + ' && nfjets >= 1 && ((Jet_pt[index_forwardJets[0]] < Jet_pt[index_centralJets[0]]) || min(abs(Jet_phi[index_forwardJets[0]]-METcorrected_phi),2*pi-abs(Jet_phi[index_forwardJets[0]]-METcorrected_phi)) < 2.8)'
# cuts['AH0l1fSR'] = cuts['AH0l1fSR'] + ' && ((Jet_pt[index_forwardJets[0]] < Jet_pt[index_centralJets[0]]) || min(abs(Jet_phi[index_forwardJets[0]]-METcorrected_phi),2*pi-abs(Jet_phi[index_forwardJets[0]]-METcorrected_phi)) < 2.8)'
# cuts['AH0l2bSR'] = cuts['AH0l2bSR'] + ' && nfjets >= 1'# && ((Jet_pt[index_forwardJets[0]] < Jet_pt[index_centralJets[0]]) || min(abs(Jet_phi[index_forwardJets[0]]-METcorrected_phi),2*pi-abs(Jet_phi[index_forwardJets[0]]-METcorrected_phi)) < 2.8)'

var = 'METcorrected_pt'
#var = 'recoilPtMiss'
#var = 'METcorrected_phi'
#var = 'M_T'
#var = 'M_T2W'
#var = 'minDeltaPhi12'
#var = 'M_Tb'
#var = 'jet1p_TH_T'
#var = 'nbjets'
#var = 'MET_pt'
#var = 'Electron_pt[1]'
#var = 'Muon_pt[1]'
#var = 'Jet_pt'
#var = 'Jet_phi[index_centralJets[2]]'
#var = 'Jet_pt[index_centralJets[0]]/Jet_pt[index_forwardJets[0]]'
#var = 'Jet_chEmEF[index_forwardJets[0]]'
#var = 'min(abs(Jet_phi[index_centralJets[2]]-METcorrected_phi),2*pi-abs(Jet_phi[index_centralJets[2]]-METcorrected_phi))'
#var = 'min(abs(TkMET_phi-METcorrected_phi),2*pi-abs(TkMET_phi-METcorrected_phi))'
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

#If cut option is not empty, use that instead
if condor_cut != '':
    cut = condor_cut
    if ('ZR' in cut and 'AH0lZR' not in cut) and (var == 'METcorrected_pt'):
        var = 'recoilPtMiss'

#Set lumi (fb^-1) and overall signal sample scale factor here
if year == 2016:
    lumi = 36.31
elif year == 2017:
    lumi = 41.53
elif year == 2018:
    lumi = 59.74
    #lumi = 21.08 #Before HEM 15/16 Issue
    #lumi = 38.75 #After HEM 15/16 Issue
    #lumi = 14.03 #Run A
    #lumi = 7.07 #Run B
    #lumi = 6.90 #Run C
    #lumi = 31.84 #Run D
if partialUnblind:
    lumi = lumi/5.0
if 'SR' in cut:
    scaleFactor = 1
else:
    scaleFactor = 1

##Create histograms
##-----------------------------------------------------------------------------------------------

print 'Cut name = ', cut
print 'MC Selection Cuts = ', cuts[cut]
print 'Data Selection Cuts = ', cuts[cut] + ' && Flag_eeBadScFilter'
print 'var = ', var
print 'year = ', str(year)
print 'lumi = ', str(lumi)
print 'saveDirectory = ', saveDirectory
print 'date = ', date
if useUL:
    print 'using UL samples...'
if applyHEMfix:
    print 'applying HEM fix for 2018...'
if partialUnblind:
    print 'partially unblinding 1/5 data...'
print('Creating histograms..')

#Set histogram options
nbins = 15
xmin = 250
xmax = 550
auto_y = True
doLogPlot = False
drawData = True
mediatorType = 'scalar'
mchi = 1
mphi = 100
normalizePlots = False
doBinned = True
savePlots = False
combineEleMu = True
doSys = False
doSysFirstHalf = False
doSysSecondHalf = False
drawOverflow = True
drawUnderflow = False
plotSys = False
plotSysVar = 'CMS_eff_b_light_2018'
plotSysSignal = False
TH1.SetDefaultSumw2()

#If using Condor, use command line option instead
if useCondor:
    doSysFirstHalf = condor_sysFirstHalf
    doSysSecondHalf = condor_sysSecondHalf
    if 'SL' in condor_cut:
        nbins = 5
        xmin = 250
        xmax = 400
    elif 'AH' in condor_cut:
        nbins = 15
        xmin = 250
        xmax = 550
if doSysFirstHalf or doSysSecondHalf:
    doSys = True
if doBinned:
    scaleFactor = 1
    savePlots = False
if not auto_y:
    ymin = 60
    ymax = 20000

#If plot and cut option enabled, use those instead
if (condor_cut != '') and condor_plot:
    savePlots = True
    if 'SL' in condor_cut:
        nbins = 5
        xmin = 250
        xmax = 400
        doLogPlot = False
    elif 'AH' in condor_cut:
        nbins = 17
        xmin = 250
        xmax = 590
        doLogPlot = True

histoLabel = '; p_{T}^{miss} (GeV); Events'
#histoLabel = '; Hadronic recoil (GeV); Events'
#histoLabel = '; #phi^{miss}; Events'
#histoLabel = '; M_{T} (GeV); Events'
#histoLabel = '; M_{T2}^{W} (GeV); Events'
#histoLabel = '; min#Delta#phi(jet_{1,2},p_{T}^{miss}); Events'
#histoLabel = '; M_{T}^{b} (GeV); Events'
#histoLabel = '; jet_{1} p_{T}/H_{T}; Events'
#histoLabel = '; central jet_{3} #phi; Events'
#histoLabel = '; central jet_{2} #eta; Events'
#histoLabel = '; b-tagged jet_{1} p_{T}; Events'
#histoLabel = '; central jet_{1} p_{T}/forward jet_{1} p_{T}; Events'
#histoLabel = '; #Delta#phi(jet_{3},p_{T}^{miss}); Events'
#histoLabel = '; #Delta#phi(TrkMET,p_{T}^{miss}); Events'
#histoLabel = '; forward jet_{1} charged Electromagnetic Energy Fraction; Events'
#histoLabel = '; DeepAK8 top tag discriminant value; Events'
#histoLabel = '; leading electron #eta; Events'
#histoLabel = '; number of b-tagged jets; Events'
#histoLabel = '; modified topness; Events'

if ('ZR' in condor_cut and 'AH0lZR' not in condor_cut) and (var == 'METcorrected_pt'): 
    histoLabel = '; Hadronic recoil (GeV); Events'

if drawData:
    ratioLabel = re.sub('.*distribution;', ';', histoLabel).replace('Events','Data / Bkg')
    histoLabel = re.sub(';.*;', '; ;', histoLabel)
if plotSys:
    ratioLabel = re.sub('.*distribution;', ';', histoLabel).replace('Events','Var / Nom')
    histoLabel = re.sub(';.*;', '; ;', histoLabel)

#Print histogram options
print 'Histogram options: '
print '    nbins = ', nbins
print '    xmin = ', xmin
print '    xmax = ', xmax
print '    auto_y = ', str(auto_y)
print '    doLogPlot = ', str(doLogPlot)
print '    drawData = ', str(drawData)
print '    mediatorType = ', mediatorType
print '    mchi = ', str(mchi)
print '    mphi = ', str(mphi)
print '    normalizePlots = ', str(normalizePlots)
print '    doBinned = ', str(doBinned)
print '    savePlots = ', str(savePlots)
print '    combineEleMu = ', str(combineEleMu)
print '    doSys = ', str(doSys)
print '    doSysFirstHalf = ', str(doSysFirstHalf)
print '    doSysSecondHalf = ', str(doSysSecondHalf)
print '    drawOverflow = ', str(drawOverflow)
print '    drawUnderflow = ', str(drawUnderflow)
print '    plotSys = ', str(plotSys)
print '    plotSysVar = ', plotSysVar
print '    plotSysSignal = ', str(plotSysSignal)

#Remove stats box from histograms
gStyle.SetOptStat(0)


#Define signal and background histograms
signalMassPoints = ['MChi1_MPhi10', 'MChi1_MPhi50', 'MChi1_MPhi100', 'MChi1_MPhi150', 'MChi1_MPhi200', 'MChi1_MPhi250', 'MChi1_MPhi300', 'MChi1_MPhi350', 'MChi1_MPhi400', 'MChi1_MPhi450', 'MChi1_MPhi500']
if doBinned:
    signal = ['ttbar scalar', 'ttbar pseudoscalar', 'tbar scalar', 'tbar pseudoscalar']
else:
    signal = ['ttbar ' + mediatorType,'tbar ' + mediatorType]
back = ['QCD','ZTo2L','VV','singleTop','WPlusJets','TTV','TTTo2L2Nu','TTToSemiLepton','ZTo2Nu']
hists = {}
if doSysFirstHalf or plotSys:
    sys = ['CMS_res_j_'+str(year),'CMS_pdf','CMS_eff_b_corr','CMS_eff_b_light_corr','CMS_eff_b_'+str(year),'CMS_eff_b_light_'+str(year),'CMS_scale_pu','CMS_eff_met_trigger','CMS_trig_m','CMS_trig_e','CMS_eff_e','CMS_eff_m','QCDScale_ren_TT','QCDScale_fac_TT','QCDScale_ren_VV','QCDScale_fac_VV','preFire','CMS_UncMET_'+str(year),'CMS_WewkWeight','CMS_ZewkWeight','CMS_WqcdWeightRen','CMS_WqcdWeightFac','CMS_ZqcdWeightRen','CMS_ZqcdWeightFac']
else:
    sys = []
jesUnc = ['','AbsoluteMPFBias','AbsoluteScale','AbsoluteStat','FlavorQCD','Fragmentation','PileUpDataMC','PileUpPtBB','PileUpPtEC1','PileUpPtEC2','PileUpPtHF','PileUpPtRef','RelativeFSR','RelativeJEREC1','RelativeJEREC2','RelativeJERHF','RelativePtBB','RelativePtEC1','RelativePtEC2','RelativePtHF','RelativeBal','RelativeSample','RelativeStatEC','RelativeStatFSR','RelativeStatHF','SinglePionECAL','SinglePionHCAL','TimePtEta']
if doSysSecondHalf or plotSys:
    for unc in jesUnc:
        sys.append('CMS_scale'+unc+'_j')
for name in ['data','bkgSum'] + signal + back:
    hists[name] = TH1F(name, histoLabel, nbins, xmin, xmax)
if doBinned:
    hists['TTbarSL'] = TH1F('ttbarSL', histoLabel, nbins, xmin, xmax)
    for massCombination in signalMassPoints:
        for mediator in ['scalar', 'pseudo']:
            hists['tDM_'+massCombination+'_'+mediator] = TH1F('tDM_'+massCombination+'_'+mediator, histoLabel, nbins, xmin, xmax)
            hists['tttDM_'+massCombination+'_'+mediator] = TH1F('tDM_'+massCombination+'_'+mediator, histoLabel, nbins, xmin, xmax)
    for process in ['ttbar scalar', 'ttbar pseudoscalar']:
        for dataset in MCSamples[process]:
            hists[dataset] = TH1F(dataset, histoLabel, nbins, xmin, xmax)
syshists = {}
if doSys:
    print 'Making systematic histogram dictionary for binned histograms...'
    for sysName in sys:
        for name in hists:
            for suffix in ['Up', 'Down']:
                if name != 'data':
                    syshists[name + '_' + sysName + suffix] = TH1F(name + '_' + sysName + suffix, histoLabel, nbins, xmin, xmax)
                    print '    ' + name + '_' + sysName + suffix + ' histogram made'
    print 'Finished making systematic histogram dictionary'
if plotSys:
    print 'Adding background up/down variation histograms...'
    for name in back + ['bkgSum'] + signal:
        for suffix in ['Up', 'Down']:
            syshists[name + '_sys' + suffix] = TH1F(name + '_sys' + suffix, histoLabel, nbins, xmin, xmax)
            print '    ' + name + '_sys' + suffix + ' histogram made'

########################################################

#Helper function to fill histograms for systematics
def addSys(histName, eventTree, var, weightedcut, sysName, addHist=True):
    # print '        Adding systematic histograms for ' + histName + '_' + sysName + '...'
    if addHist:
        histUp = TH1F('histUp', histoLabel, nbins, xmin, xmax)
        histDown = TH1F('histDown', histoLabel, nbins, xmin, xmax)
    varUp = varDown = var
    weightedcutUp = weightedcutDown = weightedcut

    #Systematics
    for unc in jesUnc:
        if sysName == 'CMS_scale'+unc+'_j':
            if var == 'METcorrected_pt':
                varUp = var.replace('METcorrected_pt','METcorrected_ptScale'+unc+'Up')
                varDown = var.replace('METcorrected_pt','METcorrected_ptScale'+unc+'Down')
            elif var == 'recoilPtMiss':
                varUp = var.replace('recoilPtMiss','recoilPtMissScale'+unc+'Up')
                varDown = var.replace('recoilPtMiss','recoilPtMissScale'+unc+'Down')
        
            weightedcutUp = weightedcut.replace('METcorrected_pt ','METcorrected_ptScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('recoilPtMiss ','recoilPtMissScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('njets ','njetsScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('nfjets ','nfjetsScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('nbjets ','nbjetsScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('minDeltaPhi ','minDeltaPhiScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('minDeltaPhi12 ','minDeltaPhi12Scale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('M_Tb ','M_TbScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('M_T ','M_TScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('M_T2W ','M_T2WScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('M_T2ll ','M_T2llScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('jet1p_TH_T ','jet1p_TH_TScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('modified_topness ','modified_topnessScale'+unc+'Up ')
            weightedcutUp = weightedcutUp.replace('full_topness ','full_topnessScale'+unc+'Up ')

            weightedcutDown = weightedcut.replace('METcorrected_pt ','METcorrected_ptScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('recoilPtMiss ','recoilPtMissScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('njets ','njetsScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('nfjets ','nfjetsScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('nbjets ','nbjetsScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('minDeltaPhi ','minDeltaPhiScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('minDeltaPhi12 ','minDeltaPhi12Scale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('M_Tb ','M_TbScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('M_T ','M_TScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('M_T2W ','M_T2WScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('M_T2ll ','M_T2llScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('jet1p_TH_T ','jet1p_TH_TScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('modified_topness ','modified_topnessScale'+unc+'Down ')
            weightedcutDown = weightedcutDown.replace('full_topness ','full_topnessScale'+unc+'Down ')

    if 'CMS_res_j' in sysName:
        if var == 'METcorrected_pt':
            varUp = var.replace('METcorrected_pt','METcorrected_ptResUp')
            varDown = var.replace('METcorrected_pt','METcorrected_ptResDown')
        elif var == 'recoilPtMiss':
            varUp = var.replace('recoilPtMiss','recoilPtMissResUp')
            varDown = var.replace('recoilPtMiss','recoilPtMissResDown')
        
        weightedcutUp = weightedcut.replace('METcorrected_pt ','METcorrected_ptResUp ')
        weightedcutUp = weightedcutUp.replace('recoilPtMiss ','recoilPtMissResUp ')
        weightedcutUp = weightedcutUp.replace('njets ','njetsResUp ')
        weightedcutUp = weightedcutUp.replace('nfjets ','nfjetsResUp ')
        weightedcutUp = weightedcutUp.replace('nbjets ','nbjetsResUp ')
        weightedcutUp = weightedcutUp.replace('minDeltaPhi ','minDeltaPhiResUp ')
        weightedcutUp = weightedcutUp.replace('minDeltaPhi12 ','minDeltaPhi12ResUp ')
        weightedcutUp = weightedcutUp.replace('M_Tb ','M_TbResUp ')
        weightedcutUp = weightedcutUp.replace('M_T ','M_TResUp ')
        weightedcutUp = weightedcutUp.replace('M_T2W ','M_T2WResUp ')
        weightedcutUp = weightedcutUp.replace('M_T2ll ','M_T2llResUp ')
        weightedcutUp = weightedcutUp.replace('jet1p_TH_T ','jet1p_TH_TResUp ')
        weightedcutUp = weightedcutUp.replace('modified_topness ','modified_topnessResUp ')
        weightedcutUp = weightedcutUp.replace('full_topness ','full_topnessResUp ')

        weightedcutDown = weightedcut.replace('METcorrected_pt ','METcorrected_ptResDown ')
        weightedcutDown = weightedcutDown.replace('recoilPtMiss ','recoilPtMissResDown ')
        weightedcutDown = weightedcutDown.replace('njets ','njetsResDown ')
        weightedcutDown = weightedcutDown.replace('nfjets ','nfjetsResDown ')
        weightedcutDown = weightedcutDown.replace('nbjets ','nbjetsResDown ')
        weightedcutDown = weightedcutDown.replace('minDeltaPhi ','minDeltaPhiResDown ')
        weightedcutDown = weightedcutDown.replace('minDeltaPhi12 ','minDeltaPhi12ResDown ')
        weightedcutDown = weightedcutDown.replace('M_Tb ','M_TbResDown ')
        weightedcutDown = weightedcutDown.replace('M_T ','M_TResDown ')
        weightedcutDown = weightedcutDown.replace('M_T2W ','M_T2WResDown ')
        weightedcutDown = weightedcutDown.replace('M_T2ll ','M_T2llResDown ')
        weightedcutDown = weightedcutDown.replace('jet1p_TH_T ','jet1p_TH_TResDown ')
        weightedcutDown = weightedcutDown.replace('modified_topness ','modified_topnessResDown ')
        weightedcutDown = weightedcutDown.replace('full_topness ','full_topnessResDown ')

    elif 'CMS_UncMET' in sysName:
        if var == 'METcorrected_pt':
            varUp = var.replace('METcorrected_pt','METcorrected_ptUnclustUp')
            varDown = var.replace('METcorrected_pt','METcorrected_ptUnclustDown')
        elif var == 'recoilPtMiss':
            varUp = var.replace('recoilPtMiss','recoilPtMissUnclustUp')
            varDown = var.replace('recoilPtMiss','recoilPtMissUnclustDown')

        weightedcutUp = weightedcut.replace('METcorrected_pt ','METcorrected_ptUnclustUp ')
        weightedcutUp = weightedcutUp.replace('recoilPtMiss ','recoilPtMissUnclustUp ')
        weightedcutUp = weightedcutUp.replace('M_Tb ','M_TbUnclustUp ')
        weightedcutUp = weightedcutUp.replace('M_T ','M_TUnclustUp ')
        weightedcutUp = weightedcutUp.replace('M_T2W ','M_T2WUnclustUp ')
        weightedcutUp = weightedcutUp.replace('M_T2ll ','M_T2llUnclustUp ')
        weightedcutUp = weightedcutUp.replace('modified_topness ','modified_topnessUnclustUp ')
        weightedcutUp = weightedcutUp.replace('full_topness ','full_topnessUnclustUp ')

        weightedcutDown = weightedcut.replace('METcorrected_pt ','METcorrected_ptUnclustDown ')
        weightedcutDown = weightedcutDown.replace('recoilPtMiss ','recoilPtMissUnclustDown ')
        weightedcutDown = weightedcutDown.replace('M_Tb ','M_TbUnclustDown ')
        weightedcutDown = weightedcutDown.replace('M_T ','M_TUnclustDown ')
        weightedcutDown = weightedcutDown.replace('M_T2W ','M_T2WUnclustDown ')
        weightedcutDown = weightedcutDown.replace('M_T2ll ','M_T2llUnclustDown ')
        weightedcutDown = weightedcutDown.replace('modified_topness ','modified_topnessUnclustDown ')
        weightedcutDown = weightedcutDown.replace('full_topness ','full_topnessUnclustDown ')

    elif sysName == 'CMS_WqcdWeightRen':
        weightedcutUp = weightedcut.replace('qcdWWeight','qcdWWeightRenUp')
        weightedcutDown = weightedcut.replace('qcdWWeight','qcdWWeightRenDown')

    elif sysName == 'CMS_WqcdWeightFac':
        weightedcutUp = weightedcut.replace('qcdWWeight','qcdWWeightFacUp')
        weightedcutDown = weightedcut.replace('qcdWWeight','qcdWWeightFacDown')

    elif sysName == 'CMS_ZqcdWeightRen':
        weightedcutUp = weightedcut.replace('qcdZTo2LWeight','qcdZTo2LWeightRenUp')
        weightedcutUp = weightedcutUp.replace('qcdZTo2NuWeight','qcdZTo2NuWeightRenUp')
        weightedcutDown = weightedcut.replace('qcdZTo2LWeight','qcdZTo2LWeightRenDown')
        weightedcutDown = weightedcutDown.replace('qcdZTo2NuWeight','qcdZTo2NuWeightRenDown')

    elif sysName == 'CMS_ZqcdWeightFac':
        weightedcutUp = weightedcut.replace('qcdZTo2LWeight','qcdZTo2LWeightFacUp')
        weightedcutUp = weightedcut.replace('qcdZTo2NuWeight','qcdZTo2NuWeightFacUp')
        weightedcutDown = weightedcut.replace('qcdZTo2LWeight','qcdZTo2LWeightFacDown')
        weightedcutDown = weightedcut.replace('qcdZTo2NuWeight','qcdZTo2NuWeightFacDown')

    elif sysName == 'CMS_WewkWeight':
        weightedcutUp = weightedcut.replace('ewkWWeight', '1')
        weightedcutDown = weightedcut

    elif sysName == 'CMS_ZewkWeight':
        weightedcutUp = weightedcut.replace('ewkZWeight', '1')
        weightedcutDown = weightedcut

    elif sysName == 'CMS_pdf':
        if year == 2016:
            if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName): 
                weightedcutUp = weightedcut + '*pdfWeightUp'
                weightedcutDown = weightedcut + '*pdfWeightDown'
        elif (year == 2017) or (year == 2018):
            if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName)  and ('QCD' not in histName): 
                weightedcutUp = weightedcut + '*pdfWeightUp'
                weightedcutDown = weightedcut + '*pdfWeightDown'

    elif sysName == 'CMS_HF':
        if ('WPlusJets' in histName) or ('ZTo2L' in histName) or ('ZTo2Nu' in histName):
            weightedcutUp = weightedcut + '*1.20'
            weightedcutDown = weightedcut + '*0.8'

    elif sysName == 'CMS_HF_V':
        if ('WPlusJets' in histName) or ('ZTo2L' in histName) or ('ZTo2Nu' in histName):
            weightedcutUp = weightedcut + '*(nbjets >= 1 ? 1.2 : 1.)'
            weightedcutDown = weightedcut + '*(nbjets >= 1 ? 0.8 : 1.)'

    elif sysName == 'CMS_HF_W':
        if ('WPlusJets' in histName):
            weightedcutUp = weightedcut + '*(nbjets >= 1 ? 1.2 : 1.)'
            weightedcutDown = weightedcut + '*(nbjets >= 1 ? 0.8 : 1.)'

    elif sysName == 'CMS_HF_Z':
        if ('ZTo2L' in histName) or ('ZTo2Nu' in histName):
            weightedcutUp = weightedcut + '*(nbjets >= 1 ? 1.2 : 1.)'
            weightedcutDown = weightedcut + '*(nbjets >= 1 ? 0.8 : 1.)'

    elif sysName == 'CMS_eff_b_corr':
        weightedcutUp = weightedcut.replace('bjetWeight','bjetWeightbcUpCorrelated')
        weightedcutDown = weightedcut.replace('bjetWeight','bjetWeightbcDownCorrelated')
    
    elif sysName == 'CMS_eff_b_light_corr':
        weightedcutUp = weightedcut.replace('bjetWeight','bjetWeightlightUpCorrelated')
        weightedcutDown = weightedcut.replace('bjetWeight','bjetWeightlightDownCorrelated')

    elif sysName == 'CMS_eff_b_'+str(year):
        weightedcutUp = weightedcut.replace('bjetWeight','bjetWeightbcUpUncorrelated')
        weightedcutDown = weightedcut.replace('bjetWeight','bjetWeightbcDownUncorrelated')

    elif sysName == 'CMS_eff_b_light_'+str(year):
        weightedcutUp = weightedcut.replace('bjetWeight','bjetWeightlightUpUncorrelated')
        weightedcutDown = weightedcut.replace('bjetWeight','bjetWeightlightDownUncorrelated')

    elif sysName == 'CMS_scale_pu':
        weightedcutUp = weightedcut.replace('puWeight','puWeightUp')
        weightedcutDown = weightedcut.replace('puWeight','puWeightDown')

    elif sysName == 'CMS_eff_lep_trigger':
        weightedcutUp = weightedcut.replace('electronTriggerWeight','electronTriggerWeightUp')
        weightedcutUp = weightedcutUp.replace('muonTriggerWeight','muonTriggerWeightUp')
        weightedcutDown = weightedcut.replace('electronTriggerWeight','electronTriggerWeightDown')
        weightedcutDown = weightedcutDown.replace('muonTriggerWeight','muonTriggerWeightDown')

    elif sysName == 'CMS_trig_e':
        weightedcutUp = weightedcut.replace('electronTriggerWeight','electronTriggerWeightUp')
        weightedcutDown = weightedcut.replace('electronTriggerWeight','electronTriggerWeightDown')
        # if ('e' in cut) or ('1l' in cut) or ('2l' in cut):
        #     weightedcutUp = weightedcutUp + '*1.020'
        #     weightedcutDown = weightedcutDown + '*0.980'

    elif sysName == 'CMS_trig_m':
        weightedcutUp = weightedcut.replace('muonTriggerWeight','muonTriggerWeightUp')
        weightedcutDown = weightedcut.replace('muonTriggerWeight','muonTriggerWeightDown')
        # if ('m' in cut) or ('1l' in cut) or ('2l' in cut):
        #     weightedcutUp = weightedcutUp + '*1.002'
        #     weightedcutDown = weightedcutDown + '*0.998'

    elif sysName == 'CMS_eff_met_trigger':
        if ('e' not in cut) and ('m' not in cut) and ('1l' not in cut) and ('2l' not in cut):
            weightedcutUp = weightedcut + '*1.02'
            weightedcutDown = weightedcut + '*0.98'

    elif sysName == 'CMS_eff_lep':
        weightedcutUp = weightedcut.replace('leptonWeight','leptonWeightUp')
        weightedcutDown = weightedcut.replace('leptonWeight','leptonWeightDown')

    elif sysName == 'CMS_eff_e_old':
        weightedcutUp = weightedcut.replace('leptonWeight','leptonWeightUp')
        weightedcutDown = weightedcut.replace('leptonWeight','leptonWeightDown')
        
    elif sysName == 'CMS_eff_m_old':
        weightedcutUp = weightedcut.replace('leptonWeight','leptonWeightUp')
        weightedcutDown = weightedcut.replace('leptonWeight','leptonWeightDown')

    elif sysName == 'CMS_eff_e':
        weightedcutUp = weightedcut.replace('leptonWeight','electronWeightUp*muonWeight')
        weightedcutDown = weightedcut.replace('leptonWeight','electronWeightDown*muonWeight')
        # if ('e' in cut) or ('1l' in cut) or ('2l' in cut):
        #     weightedcutUp = weightedcutUp + '*1.010'
        #     weightedcutDown = weightedcutDown + '*0.990'

    elif sysName == 'CMS_eff_m':
        weightedcutUp = weightedcut.replace('leptonWeight','electronWeight*muonWeightUp')
        weightedcutDown = weightedcut.replace('leptonWeight','electronWeight*muonWeightDown')
        # if ('m' in cut) or ('1l' in cut) or ('2l' in cut):
        #     weightedcutUp = weightedcutUp + '*1.014'
        #     weightedcutDown = weightedcutDown + '*0.986'
    
    elif ('QCDScale' in sysName) and ('ren' in sysName):
        if year == 2016:
            if ('TT' in sysName) and ('TT' in histName):
                weightedcutUp = weightedcut + '*qcdRenWeightUp'
                weightedcutDown = weightedcut + '*qcdRenWeightDown'
            elif ('VV' in sysName) and ('VV' in histName):
                weightedcutUp = weightedcut + '*qcdRenWeightUp'
                weightedcutDown = weightedcut + '*qcdRenWeightDown'
            elif ('O' in sysName) and (('QCD' in histName) or ('singleTop' in histName)):
                weightedcutUp = weightedcut + '*qcdRenWeightUp'
                weightedcutDown = weightedcut + '*qcdRenWeightDown'
            elif sysName == 'QCDScale_ren':
                if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName):
                    weightedcutUp = weightedcut + '*qcdRenWeightUp'
                    weightedcutDown = weightedcut + '*qcdRenWeightDown'
        elif (year == 2017) or (year == 2018):
            if ('TT' in sysName) and ('TT' in histName):
                weightedcutUp = weightedcut + '*qcdRenWeightUp'
                weightedcutDown = weightedcut + '*qcdRenWeightDown'
            elif ('VV' in sysName) and ('VV' in histName):
                weightedcutUp = weightedcut + '*qcdRenWeightUp'
                weightedcutDown = weightedcut + '*qcdRenWeightDown'
            elif ('O' in sysName) and ('singleTop' in histName):
                weightedcutUp = weightedcut + '*qcdRenWeightUp'
                weightedcutDown = weightedcut + '*qcdRenWeightDown'
            elif sysName == 'QCDScale_ren':
                if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName) and ('QCD' not in histName):
                    weightedcutUp = weightedcut + '*qcdRenWeightUp'
                    weightedcutDown = weightedcut + '*qcdRenWeightDown'

    elif ('QCDScale' in sysName) and ('fac' in sysName):
        if year == 2016:
            if ('TT' in sysName) and ('TT' in histName):
                weightedcutUp = weightedcut + '*qcdFacWeightUp'
                weightedcutDown = weightedcut + '*qcdFacWeightDown'
            elif ('VV' in sysName) and ('VV' in histName):
                weightedcutUp = weightedcut + '*qcdFacWeightUp'
                weightedcutDown = weightedcut + '*qcdFacWeightDown'
            elif ('O' in sysName) and (('QCD' in histName) or ('singleTop' in histName)):
                weightedcutUp = weightedcut + '*qcdFacWeightUp'
                weightedcutDown = weightedcut + '*qcdFacWeightDown'
            elif sysName == 'QCDScale_fac':
                if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName):
                    weightedcutUp = weightedcut + '*qcdFacWeightUp'
                    weightedcutDown = weightedcut + '*qcdFacWeightDown'
        elif (year == 2017) or (year == 2018):
            if ('TT' in sysName) and ('TT' in histName):
                weightedcutUp = weightedcut + '*qcdFacWeightUp'
                weightedcutDown = weightedcut + '*qcdFacWeightDown'
            elif ('VV' in sysName) and ('VV' in histName):
                weightedcutUp = weightedcut + '*qcdFacWeightUp'
                weightedcutDown = weightedcut + '*qcdFacWeightDown'
            elif ('O' in sysName) and ('singleTop' in histName):
                weightedcutUp = weightedcut + '*qcdFacWeightUp'
                weightedcutDown = weightedcut + '*qcdFacWeightDown'
            elif sysName == 'QCDScale_fac':
                if (histName not in signal) and ('tDM' not in histName) and ('Chan' not in histName) and ('QCD' not in histName):
                    weightedcutUp = weightedcut + '*qcdFacWeightUp'
                    weightedcutDown = weightedcut + '*qcdFacWeightDown'

    elif sysName == 'pdf_accept_2l':
        if ('2e' in cut) or ('2m' in cut) or ('2l' in cut):
            weightedcutUp = weightedcut + '*1.060'
            weightedcutDown = weightedcut + '*0.940'
    
    elif sysName == 'pdf_accept_1l':
        if ('1e' in cut) or ('1m' in cut) or ('1l' in cut):
            weightedcutUp = weightedcut + '*1.030'
            weightedcutDown = weightedcut + '*0.970'

    elif sysName == 'pdf_accept_0l':
        if ('e' not in cut) and ('m' not in cut) and ('1l' not in cut) and ('2l' not in cut):
            weightedcutUp = weightedcut + '*1.060'
            weightedcutDown = weightedcut + '*0.940'

    elif sysName == 'preFire':
        weightedcutUp = weightedcut.replace('EE_L1_prefire_Weight','EE_L1_prefire_WeightUp')
        weightedcutDown = weightedcut.replace('EE_L1_prefire_Weight','EE_L1_prefire_WeightDown')

    elif sysName == 'CMS_PSisr':
        weightedcutUp = weightedcutUp + '*PSWeightISRUp'
        weightedcutDown = weightedcutDown + '*PSWeightISRDown'

    elif sysName == 'CMS_PSfsr':
        weightedcutUp = weightedcutUp + '*PSWeightFSRUp'
        weightedcutDown = weightedcutDown + '*PSWeightFSRDown'

    if addHist:
        eventTree.Draw(varUp+'>>histUp',weightedcutUp)
        eventTree.Draw(varDown+'>>histDown',weightedcutDown)
        # print '        ' + name + '_' + sysName + 'Up hist entries = ', histUp.GetEntries()
        # print '        ' + name + '_' + sysName + 'Up hist integral = ', histUp.Integral(1,nbins+1)
        # print '        ' + name + '_' + sysName + 'Down hist entries = ', histUp.GetEntries()
        # print '        ' + name + '_' + sysName + 'Down hist integral = ', histDown.Integral(1,nbins+1)
        syshists[histName + '_' + sysName + 'Up'] += histUp
        syshists[histName + '_' + sysName + 'Down'] += histDown
        # print '        Finished adding systematic histograms for ' + histName + '_' + sysName
    else:
        return [weightedcutUp, weightedcutDown]

#Helper function to add systematic up/down variation histograms for background
def addSysPlot(process, eventTree, var, weightedcut):
    histSysUp = TH1F('histSysUp', histoLabel, nbins, xmin, xmax)
    histSysDown = TH1F('histSysDown', histoLabel, nbins, xmin, xmax)
    weightedcutUpPlot = weightedcutDownPlot = weightedcut
    varSysUp = varSysDown = var

    #Substitute systematic up/down variations into cut
    weightedcutUp_temp = addSys(process, eventTree, var, weightedcut, plotSysVar, addHist=False)[0]
    weightedcutDown_temp = addSys(process, eventTree, var, weightedcut, plotSysVar, addHist=False)[1]
    weightedcutUpPlot = weightedcutUp_temp
    weightedcutDownPlot = weightedcutDown_temp

    #Check to see if var needs to be modified for up/down variation
    if 'CMS_scale' in plotSysVar and plotSysVar != 'CMS_scale_pu':
        unc = plotSysVar.replace('CMS_scale','').replace('_j','')
        varSysUp = var+'Scale'+unc+'Up'
        varSysDown = var+'Scale'+unc+'Down'
    if 'CMS_res_j' in plotSysVar:
        varSysUp = var+'ResUp'
        varSysDown = var+'ResDown'
    if 'CMS_UncMET' in plotSysVar:
        varSysUp = var+'UnclustUp'
        varSysDown = var+'UnclustDown'
    #print '          varSysUp = ', varSysUp
    #print '          varSysDown = ', varSyDown

    #Add to histograms for background
    eventTree.Draw(varSysUp+'>>histSysUp',weightedcutUpPlot)
    eventTree.Draw(varSysDown+'>>histSysDown',weightedcutDownPlot)
    #print '          histUpTemp nEntries = ', syshists[process + '_sysUp'].GetEntries()
    #print '          histUpTemp integral = ', syshists[process + '_sysUp'].Integral(1,nbins+1)
    #print '          histDownTemp nEntries = ', syshists[process + '_sysDown'].GetEntries()
    #print '          histDownTemp integral = ', syshists[process + '_sysDown'].Integral(1,nbins+1)

    syshists[process + '_sysUp'] += histSysUp
    syshists[process + '_sysDown'] += histSysDown
    #print '          histUp nEntries = ', syshists[process + '_sysUp'].GetEntries()
    #print '          histUp integral = ', syshists[process + '_sysUp'].Integral(1,nbins+1)
    #print '          histDown nEntries = ', syshists[process + '_sysDown'].GetEntries()
    #print '          histDown integral = ', syshists[process + '_sysDown'].Integral(1,nbins+1)

    if process == 'WPlusJets' and counter:
    #if 'ZTo2' in process and counter:
        print 'DEBUG OUTPUT HERE: '
        print 'weightedcut = ', weightedcut
        print 'weightedcutUp = ', weightedcutUpPlot
        print 'weightedcutDown = ', weightedcutDownPlot
        print 'var = ', var
        print 'varUp = ', varSysUp
        print 'varDown = ', varSysDown
        global counter
        counter = False
    

########################################################

#Select dataset to use based on cut
datasetNames = []
if drawData:
    print('Drawing data and ratio plot...')
if combineEleMu:
    if ('1l' in cut) or ('2l' in cut) or (cut == 'SL'):
        datasetNames.append('SingleMuon')
        datasetNames.append('SingleElectron')
        if (year == 2016) or (year == 2017):
            datasetNames.append('SinglePhoton')
            print 'Selected SingleMuon, SingleElectron, and SinglePhoton dataset'
        else:
            print 'Selected both SingleMuon and SingleElectron dataset'
    else:
        datasetNames.append('MET')
        print 'Selected MET dataset'
else:
    if 'm' in cut:
        datasetNames.append('SingleMuon')
        print('Selected SingleMuon dataset')
    elif 'e' in cut:
        datasetNames.append('SingleElectron')
        if (year == 2016) or (year == 2017):
            datasetNames.append('SinglePhoton')
            print('Selected both SingleElectron and SinglePhoton dataset')
        else:
            print('Selected SingleElectron dataset')
    else:
        datasetNames.append('MET')
        print('Selected MET dataset')

#Get data root files and event trees
print('Loading data sample root files and event trees...')
for dataset in dataSamples:
    if dataset in datasetNames:
        for filepath in dataSamples[dataset]['filepaths']:
            print '    ----Loading', filepath
            dataSamples[dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            dataSamples[dataset][filepath+'_Events'] = dataSamples[dataset][filepath+'_TFile'].Get('Events')
        print '    total nevents in ', dataset, ': ', dataSamples[dataset]['nevents']
print('Got data sample root files and event trees')

#Get MC background root files and event trees
print('Loading MC sample root files and event trees...')
for process in MCSamples:
    print 'Loading process: ', process
    for dataset in MCSamples[process]:
        print '    ----Loading', dataset
        for filepath in MCSamples[process][dataset]['filepaths']:
            MCSamples[process][dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            MCSamples[process][dataset][filepath+'_Events'] = MCSamples[process][dataset][filepath+'_TFile'].Get('Events')
        print '    nevents in ', process, ' ', dataset, ': ', MCSamples[process][dataset]['nevents']
print('Got MC sample root files and event trees')

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
print('Filling data histograms...')
#Loop through each root file for each dataset
for dataset in dataSamples:
    if (dataset in datasetNames) and drawData:
        print '  Dataset = ', dataset, ' ||   nEvents = ', dataSamples[dataset]['nevents']
        for filepath in dataSamples[dataset]['filepaths']:
            hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
            #Only apply ee badSC noise filter to data (https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2)
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
                    if year == 2016:
                        datacut = datacut.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon175', 'HLT_Ele115_CaloIdVT_GsfTrkIdT')
                    if year == 2017:
                        datacut = datacut.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200', 'HLT_Ele115_CaloIdVT_GsfTrkIdT')
                    print '  Using cut = ', datacut
                elif dataset == 'SinglePhoton':
                    datacut = cuts[cut.replace('l','e')] + ' && Flag_eeBadScFilter'
                    if year == 2016:
                        datacut = datacut.replace('((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))', '((!'+cuts['singleIsoEle']+') && (!HLT_Ele115_CaloIdVT_GsfTrkIdT) && HLT_Photon175)')
                    if year == 2017:
                        datacut = datacut.replace('((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))', '((!'+cuts['singleIsoEle']+') && (!HLT_Ele115_CaloIdVT_GsfTrkIdT) && HLT_Photon200)')
                    print '  Using cut = ', datacut
                else:
                    datacut = cuts[cut] + ' && Flag_eeBadScFilter'
            else:
                datacut = cuts[cut] + ' && Flag_eeBadScFilter'
                if dataset == 'SingleElectron':
                    if year == 2016:
                        datacut = datacut.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon175', 'HLT_Ele115_CaloIdVT_GsfTrkIdT')
                    if year == 2017:
                        datacut = datacut.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200', 'HLT_Ele115_CaloIdVT_GsfTrkIdT')
                if dataset== 'SinglePhoton':
                    if year == 2016:
                        datacut = datacut.replace('((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))', '((!'+cuts['singleIsoEle']+') && (!HLT_Ele115_CaloIdVT_GsfTrkIdT) && HLT_Photon175)')
                    if year == 2017:
                        datacut = datacut.replace('((' + cuts['singleIsoEle'] + ') || (' + cuts['singleEle'] + '))', '((!'+cuts['singleIsoEle']+') && (!HLT_Ele115_CaloIdVT_GsfTrkIdT) && HLT_Photon200)')
                        
            if 'SingleElectron_Run2017B' in filepath: #HLT_Ele115_CaloIdVT_GsfTrkIdT trigger path not available in Run2017B (https://hypernews.cern.ch/HyperNews/CMS/get/b2g-selections/346.html?inline=-1)
                datacut = datacut.replace('HLT_Ele115_CaloIdVT_GsfTrkIdT || ','')
                print '   Using cut = ', datacut
            if 'MET_Run2017B' in filepath: #MET trigger paths also missing from Run2017B (https://hypernews.cern.ch/HyperNews/CMS/get/top-trigger/247/1.html)
                datacut = datacut.replace(' || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60','')
                print '   Using cut = ', datacut
            #datacut = datacut + ' && run >= 319077' #Uncomment to only include runs post-HEM 15/16 failure (2018)
            if partialUnblind:
                datacut = datacut + ' && (event%5 == 0)' 
            dataSamples[dataset][filepath+'_Events'].Draw(var+'>>hist',datacut)
            print '    hist nEntries = ', hist.GetEntries()
            print '    hist integral = ', hist.Integral(1,nbins+1)
            hists['data'] += hist
            print '    hist_data nEntries = ', hists['data'].GetEntries()
            print '    hist_data integral = ', hists['data'].Integral(1,nbins+1)

print('Filling MC histograms...')
for process in MCSamples:
    print '  Process = ', process
    for dataset in MCSamples[process]:
        print '      Dataset = ', dataset, ' ||   nEvents = ', MCSamples[process][dataset]['nevents']
        weight = str(MCSamples[process][dataset]['xsec']*lumi/MCSamples[process][dataset]['nevents']) + '*leptonWeight*bjetWeight*puWeight*muonTriggerWeight*EE_L1_prefire_Weight*electronTriggerWeight*genWeightSign'
        if datasetNames == ['MET']:
            weight = weight + '*METTriggerWeight'
        #Apply appropriate NLO k-factors
        if process == 'WPlusJets':
            if year == 2016:
                weight = weight + '*qcdWWeight*ewkWWeight'
                print 'Applied WPlusJets qcd/ewk Weights correctly'
            else:
                weight = weight + '*qcdWWeight*ewkWWeight*0.9135'
                if 'AH' in cut:
                    if year == 2017:
                        weight = weight + '*(nbjets == 0 ? 0.891 : 1.)'
                    elif year == 2018:
                        weight = weight + '*(nbjets == 0 ? 0.870 : 1.)'
                print 'Applied WPlusJets ewk Weights correctly'
        elif process == 'ZTo2L':
            if year == 2016:
                weight = weight + '*qcdZTo2LWeight*ewkZWeight'
                print 'Applied ZTo2L qcd/ewk Weights correctly'
            else:
                weight = weight + '*qcdZTo2LWeight*ewkZWeight*0.934'
                if 'AH' in cut:
                    if year == 2017:
                        weight = weight + '*(nbjets == 0 ? 0.801 : 1.)'
                    elif year == 2018:
                        weight = weight + '*(nbjets == 0 ? 0.802 : 1.)'
                print 'Applied ZTo2L ewk Weights correctly'
        elif process == 'ZTo2Nu':
            if year == 2016:
                weight = weight + '*qcdZTo2NuWeight*ewkZWeight'
                print 'Applied ZTo2Nu qcd/ewk Weights correctly'
            else:
                weight = weight + '*qcdZTo2NuWeight*ewkZWeight*0.934'
                print 'Applied ZTo2Nu ewk Weights correctly'
        if (process in signal) and ('ttbar' in process) and ('MPhi125_scalar' not in dataset) and ('MPhi10_' not in dataset):
            Mchi = MCSamples[process][dataset]['mchi']
            Mphi = MCSamples[process][dataset]['mphi']
            MediatorType = MCSamples[process][dataset]['mediatorType']
            signalType = 'TTbarDMJets'
            weight = weight + '*GenModel__'+signalType+'_Inclusive_'+MediatorType+'_LO_Mchi_'+str(Mchi)+'_Mphi_'+str(Mphi)+'_TuneCP5_13TeV_madgraph_mcatnlo_pythia8'
        #Exclude single QCD events in 2016 and 2017 with large weights
        if (process == 'QCD') and (dataset == 'HT300To500') and (year == 2016):
            weight = weight + '*(event!=159953384)'
        if (process == 'QCD') and (dataset == 'Pt120to170') and (year == 2017):
            weight = weight + '*(event!=3468768)'
        for filepath in MCSamples[process][dataset]['filepaths']:
            hist = TH1F('hist', histoLabel, nbins, xmin, xmax)
            MCSamples[process][dataset][filepath+'_Events'].Draw(var+'>>hist',weight+'*('+cuts[cut]+')')
            print '          hist weight = ', weight
            print '          hist nEntries = ', hist.GetEntries()
            print '          hist integral = ', hist.Integral(1,nbins+1)
            if process in signal:
                hists[process] += scaleFactor*hist
                if doBinned:
                    if (process == 'tbar scalar') or (process == 'tbar pseudoscalar'):
                        hists[dataset.replace('tChan','tDM').replace('tWChan','tDM')] += hist
                        hists[dataset.replace('tChan','tttDM').replace('tWChan','tttDM')] += hist
                    if (process == 'ttbar scalar') or (process == 'ttbar pseudoscalar'):
                        hists[dataset] += hist
                        if 'MPhi125_scalar' not in dataset:
                            hists[dataset.replace('ttDM','tttDM')] += hist
            elif process == 'ttbarPlusJets':
                hists[dataset] += hist
                if doBinned:
                    hists['TTbarSL'] += hist
            elif (process == 'WW' or process == 'WZ' or process == 'ZZ'):
                hists['VV'] += hist
            elif process == 'TTV':
                hists['TTV'] += hist
                if doBinned:
                    hists['TTbarSL'] += hist
            else:
                hists[process] += hist
            #Add MC histograms for systematics for binned histograms
            if doSys:
                print '          Adding systematics to binned histograms...'
                for sysName in sys:
                    if process in signal:
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                        if doBinned:
                            if (process == 'tbar scalar') or (process == 'tbar pseudoscalar'):
                                addSys(dataset.replace('tChan','tDM').replace('tWChan','tDM'), MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                                addSys(dataset.replace('tChan','tttDM').replace('tWChan','tttDM'), MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                            if (process == 'ttbar scalar') or (process == 'ttbar pseudoscalar'):
                                addSys(dataset, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                                if 'MPhi125_scalar' not in dataset:
                                    addSys(dataset.replace('ttDM','tttDM'), MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'ttbarPlusJets':
                        addSys(dataset, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                        if doBinned:
                            addSys('TTbarSL', MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif (process == 'WW' or process == 'WZ' or process == 'ZZ'):
                        addSys('VV', MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    elif process == 'TTV':
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                        if doBinned:
                            addSys('TTbarSL', MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
                    else:
                        addSys(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')', sysName)
            #Add MC histograms for total systematic up/down variations for plotting
            if plotSys:
                print '          Adding up/down varations for systematic given by plotSysVar to MC background histograms...'
                if process in signal:
                    addSysPlot(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')')
                elif process == 'ttbarPlusJets':
                    addSysPlot(dataset, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')')
                elif (process == 'WW' or process == 'WZ' or process == 'ZZ'):
                    addSysPlot('VV', MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')')
                else:
                    addSysPlot(process, MCSamples[process][dataset][filepath+'_Events'], var, weight+'*('+cuts[cut]+')')
                    

#Fill background sum histogram for calculating ratio plot
for name in back:
    hists['bkgSum'] += hists[name]
    if doSys:
        for sysName in sys:
            for suffix in ['Up','Down']:
                syshists['bkgSum_'+sysName + suffix] += syshists[name + '_' + sysName + suffix]
    if plotSys:
        for suffix in ['Up','Down']:
            syshists['bkgSum_sys' + suffix] += syshists[name + '_sys' + suffix]

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
print 'Total t+DM signal nEvents = ', hists['tbar ' + mediatorType].GetEntries()/scaleFactor
print 'Total t+DM signal integral = ', hists['tbar ' + mediatorType].Integral(1,nbins+1)/scaleFactor
print '-----------------------------'
print 'FOM for tt+DM signal = ', (hists['ttbar ' + mediatorType].Integral(1,nbins+1)/scaleFactor)/((hists['ttbar ' + mediatorType].Integral(1,nbins+1)/scaleFactor)+math.sqrt(hists['bkgSum'].Integral(1,nbins+1)))
print 'FOM for t+DM signal = ', (hists['tbar ' + mediatorType].Integral(1,nbins+1)/scaleFactor)/((hists['tbar ' + mediatorType].Integral(1,nbins+1)/scaleFactor)+math.sqrt(hists['bkgSum'].Integral(1,nbins+1)))
print '-----------------------------'

print 'Data bin content:'
for i in range(nbins+2):
    bin_content = hists['data'].GetBinContent(i)
    print '    bin ' + str(i) + ': ' + str(bin_content)
print '-----------------------------'
print 'MC background bin content:'
for i in range(nbins+2):
    bin_content = hists['bkgSum'].GetBinContent(i)
    print '    bin ' + str(i) + ': ' + str(bin_content)
print '-----------------------------'
print 'tt+DM bin content:'
for i in range(nbins+2):
    bin_content = hists['ttbar ' + mediatorType].GetBinContent(i)
    print '    bin ' + str(i) + ': ' + str(bin_content)
print '-----------------------------'
print 't+DM bin content:'
for i in range(nbins+2):
    bin_content = hists['tbar ' + mediatorType].GetBinContent(i)
    print '    bin ' + str(i) + ': ' + str(bin_content)
print '-----------------------------'

print 'Data bin errors:'
for i in range(nbins+2):
    bin_error = hists['data'].GetBinError(i)
    print '    bin ' + str(i) + ': ' + str(bin_error)
print '-----------------------------'
print 'MC background bin errors:'
for i in range(nbins+2):
    bin_error = hists['bkgSum'].GetBinError(i)
    print '    bin ' + str(i) + ': ' + str(bin_error)
print '-----------------------------'
print 'tt+DM bin errors:'
for i in range(nbins+2):
    bin_error = hists['ttbar ' + mediatorType].GetBinError(i)
    print '    bin ' + str(i) + ': ' + str(bin_error)
print '-----------------------------'
print 't+DM bin errors:'
for i in range(nbins+2):
    bin_error = hists['tbar ' + mediatorType].GetBinError(i)
    print '    bin ' + str(i) + ': ' + str(bin_error)
print '-----------------------------'
for name in hists:
    print name + ' hist info:'
    if name in signal:
        print '    nEvents = ', hists[name].GetEntries()/scaleFactor
        print '    integral = ', hists[name].Integral(1,nbins+1)/scaleFactor
    else:
        print '    nEvents = ', hists[name].GetEntries()
        print '    integral = ', hists[name].Integral(1,nbins+1)
    if plotSys and (name in back + ['bkgSum'] + signal):
        print name + ' histUp info:'
        print '    nEvents = ', syshists[name + '_sysUp'].GetEntries()
        print '    integral = ', syshists[name + '_sysUp'].Integral(1,nbins+1)
        print name + ' histDown info:'
        print '    nEvents = ', syshists[name + '_sysDown'].GetEntries()
        print '    integral = ', syshists[name + '_sysDown'].Integral(1,nbins+1)
print('Finished filling histograms')

#Add overflow and underflow bins to histograms
for name in hists:
    if drawOverflow:
        hists[name].SetBinContent(nbins, hists[name].GetBinContent(nbins) + hists[name].GetBinContent(nbins+1))
        hists[name].SetBinError(nbins, math.sqrt(math.pow(hists[name].GetBinError(nbins),2)+math.pow(hists[name].GetBinError(nbins+1),2)))
    if drawUnderflow:
        hists[name].SetBinContent(1, hists[name].GetBinContent(0) + hists[name].GetBinContent(1))
        hists[name].SetBinError(1, math.sqrt(math.pow(hists[name].GetBinError(0),2)+math.pow(hists[name].GetBinError(1),2)))
for name in syshists:
    if drawOverflow:
        syshists[name].SetBinContent(nbins, syshists[name].GetBinContent(nbins) + syshists[name].GetBinContent(nbins+1))
        syshists[name].SetBinError(nbins, math.sqrt(math.pow(syshists[name].GetBinError(nbins),2)+math.pow(syshists[name].GetBinError(nbins+1),2)))
    if drawUnderflow:
        syshists[name].SetBinContent(1, syshists[name].GetBinContent(0) + syshists[name].GetBinContent(1))
        syshists[name].SetBinError(1, math.sqrt(math.pow(syshists[name].GetBinError(0),2)+math.pow(syshists[name].GetBinError(1),2)))

#Add up MC background histos into stacked histogram
print('Creating stacked MC background histogram...')
h_MCStack = THStack('h_MCbackground', histoLabel)
for name in back:
#for name in ['WPlusJets']: #Edit here
    h_MCStack.Add(hists[name])
print('Finished stacking MC background histograms.')

#Create binned histogram root files if doBinned == True
if doBinned:
    print('Creating binned histogram root files...')
    savePrefix = saveDirectory + date + '/' + str(year) + '/'
    stepSize = (xmax-xmin)/nbins
    for i in range(1,nbins+1):
        print '--------------------------'
        print '    Bin ' + str(i)
        print '    ---------'
        leftbin = xmin + (i-1)*stepSize
        rightbin = xmin + i*stepSize
        if doSysFirstHalf:
            binnedRootFile = TFile(cut+'bin_'+str(leftbin)+'_'+str(rightbin)+'v1.root', 'RECREATE')
        elif doSysSecondHalf:
            binnedRootFile = TFile(cut+'bin_'+str(leftbin)+'_'+str(rightbin)+'v2.root', 'RECREATE')
        else:
            binnedRootFile = TFile(cut+'bin_'+str(leftbin)+'_'+str(rightbin)+'.root', 'RECREATE')
        if doSysFirstHalf:
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
            for massCombination in signalMassPoints:
                for mediator in ['scalar','pseudo']:
                    for signalType in ['tDM','tttDM']:
                        binContent = hists[signalType+'_'+massCombination+'_'+mediator].GetBinContent(i)
                        binError = hists[signalType+'_'+massCombination+'_'+mediator].GetBinError(i)
                        binnedHist = TH1F(signalType+'_'+massCombination+'_'+mediator, '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                        binnedHist.SetBinContent(1, binContent)
                        binnedHist.SetBinError(1, binError)
                        binnedHist.Write()
                        print '    ' + signalType+'_'+massCombination+'_'+mediator + ' bin content: ' + str(binContent) + ', ' + signalType+'_'+massCombination+'_'+mediator + ' bin error: ' + str(binError)
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
                    for massCombination in signalMassPoints:
                        for mediator in ['scalar','pseudo']:
                            for signalType in ['tDM','tttDM']:
                                binContent = syshists[signalType+'_'+massCombination+'_'+mediator + '_' + sysName + suffix].GetBinContent(i)
                                binError = syshists[signalType+'_'+massCombination+'_'+mediator + '_' + sysName + suffix].GetBinError(i)
                                binnedHist = TH1F(signalType+'_'+massCombination+'_'+mediator, '; p_{T}^{miss} (GeV); Events', 1, leftbin, rightbin)
                                binnedHist.SetBinContent(1, binContent)
                                binnedHist.SetBinError(1, binError)
                                binnedHist.Write()
                                print '    ' + signalType+'_'+massCombination+'_'+mediator + '_' + sysName + suffix + ' bin content: ' + str(binContent) + ', ' + signalType+'_'+massCombination+'_'+mediator + '_' + sysName + suffix + ' bin error: ' + str(binError)
    print('Finished creating binned histogram root files...')

#Normalize plots to area 1 if normalizePlots == True
if normalizePlots:
    for name in back:
        hists[name].Scale(1/hists['bkgSum'].Integral())
        if plotSys:
            syshists[name + '_sysUp'].Scale(1/hists['bkgSum'].Integral())
            syshists[name + '_sysDown'].Scale(1/hists['bkgSum'].Integral())
    for process in signal:
        hists[process].Scale(1./hists[process].Integral())
    if drawData:
        hists['data'].Scale(1./hists['data'].Integral())
    hists['bkgSum'].Scale(1./hists['bkgSum'].Integral())
    if plotSys:
            syshists['bkgSum_sysUp'].Scale(1/hists['bkgSum'].Integral())
            syshists['bkgSum_sysDown'].Scale(1/hists['bkgSum'].Integral())
    print('Normalized plots')

#Uncomment to set bkgSum hist to signal hist for plotting purposes if needed
if plotSysSignal:
    hists['bkgSum'] = hists['ttbar '+mediatorType]
    syshists['bkgSum_sysUp'] = syshists['ttbar '+mediatorType+'_sysUp']
    syshists['bkgSum_sysDown'] = syshists['ttbar '+mediatorType+'_sysDown']
        
#Draw histograms and save if savePlots == True
if savePlots:
    print('Drawing histograms...')
    c = TCanvas('c', 'c', 800, 800)
    #Make two canvases if drawing data for ratio plot or plotting systematics, otherwise make one canvas
    if drawData or plotSys:
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
    #Draw relevant histograms depending on if plotting systematics or not
    if not plotSys:
        h_MCStack.Draw('hist')
        hists['ttbar '+mediatorType].Draw('hist same') #Edit here
        hists['tbar '+mediatorType].Draw('hist same')
        hists['data'].Draw('ep same')
        hists['bkgSum'].Draw('e2 same')
    elif plotSys:
        hists['bkgSum'].Draw('hist')
        syshists['bkgSum_sysUp'].Draw('hist same')
        syshists['bkgSum_sysDown'].Draw('hist same')
    #Draw title with lumi and beam energy
    title = TLatex()
    if drawData or plotSys:
        title.SetTextSize(0.035)
        title_x = .76
        title_y = .91
    else:
        title.SetTextSize(0.03)
        title_x = .74
        title_y = .91
    if year == 2016:
        if partialUnblind:
            title.DrawLatexNDC(title_x, title_y, '#bf{7.2 fb^{-1} (13 TeV)}')
        else:
            title.DrawLatexNDC(title_x, title_y, '#bf{36.3 fb^{-1} (13 TeV)}')
    elif year == 2017:
        if partialUnblind:
            title.DrawLatexNDC(title_x, title_y, '#bf{8.3 fb^{-1} (13 TeV)}')
        else:
            title.DrawLatexNDC(title_x, title_y, '#bf{41.5 fb^{-1} (13 TeV)}')
    elif year == 2018:
        if partialUnblind:
            title.DrawLatexNDC(title_x, title_y, '#bf{12.0 fb^{-1} (13 TeV)}')
        else:
            title.DrawLatexNDC(title_x, title_y, '#bf{59.7 fb^{-1} (13 TeV)}')
            #title.DrawLatexNDC(title_x, title_y, '#bf{31.84 fb^{-1} (13 TeV)}') #RunD
            #title.DrawLatexNDC(title_x, title_y, '#bf{21.1 fb^{-1} (13 TeV)}') #preHEM
            #title.DrawLatexNDC(title_x, title_y, '#bf{38.8 fb^{-1} (13 TeV)}') #postHEM
            #title.DrawLatexNDC(title_x, title_y, '#bf{12.0 fb^{-1} (13 TeV)}') #1/5 partial unblind
            #title.DrawLatexNDC(title_x, title_y, '#bf{4.2 fb^{-1} (13 TeV)}')   #1/5 partial unblind preHEM
            #title.DrawLatexNDC(title_x, title_y, '#bf{7.8 fb^{-1} (13 TeV)}')  #1/5 partial unblind postHEM
    #Set 'CMS, Preliminary' text
    pt = TPaveText(0.18, 0.75, 0.35, 0.85, 'NDC')
    if drawData or plotSys:
        pt.SetTextSize(0.04)
    else:
        pt.SetTextSize(0.03)
    pt.SetFillColor(0)
    pt.SetTextAlign(11)
    pt.AddText('#splitline{CMS}{#bf{#it{Preliminary}}}')
    pt.Draw('same')
    #Set MC background histogram options 
    if not plotSys:
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

    #Automatically scale y-axis based on largest histogram bins
    if auto_y:
        if doLogPlot:
            if drawData:
                ymin = max(min(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMinimumBin()), hists['data'].GetBinContent(hists['data'].GetMinimumBin())), 5.e-1)
                ymax = 5.*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['data'].GetBinContent(hists['data'].GetMaximumBin())+hists['data'].GetBinError(hists['data'].GetMaximumBin()), hists['ttbar '+mediatorType].GetBinContent(hists['ttbar '+mediatorType].GetMaximumBin()), hists['tbar '+mediatorType].GetBinContent(hists['tbar '+mediatorType].GetMaximumBin()))
            else:
                ymin = max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMinimumBin()), 5.e-1)
                ymax = 5.*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['ttbar '+mediatorType].GetBinContent(hists['ttbar '+mediatorType].GetMaximumBin()), hists['tbar '+mediatorType].GetBinContent(hists['tbar '+mediatorType].GetMaximumBin()))
        else:
            ymin = 0
            if drawData:
                ymax = 1.25*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['data'].GetBinContent(hists['data'].GetMaximumBin())+hists['data'].GetBinError(hists['data'].GetMaximumBin()), hists['ttbar '+mediatorType].GetBinContent(hists['ttbar '+mediatorType].GetMaximumBin()), hists['tbar '+mediatorType].GetBinContent(hists['tbar '+mediatorType].GetMaximumBin()))
            else:
                ymax = 1.25*max(hists['bkgSum'].GetBinContent(hists['bkgSum'].GetMaximumBin()), hists['ttbar '+mediatorType].GetBinContent(hists['ttbar '+mediatorType].GetMaximumBin()), hists['tbar '+mediatorType].GetBinContent(hists['tbar '+mediatorType].GetMaximumBin()))
    if normalizePlots:
        ymin = 5.e-4
    if not plotSys:
        h_MCStack.SetMinimum(ymin)
        h_MCStack.SetMaximum(ymax)
    elif plotSys:
        hists['bkgSum'].SetMinimum(ymin)
        hists['bkgSum'].SetMaximum(ymax)
    #Set settings for data and MC background histogram title/labels
    if drawData and not plotSys:
        setHistStyle(h_MCStack)
        h_MCStack.GetXaxis().SetLabelOffset(999)
        h_MCStack.GetXaxis().SetLabelSize(0)
        setHistStyle(hists['ttbar '+mediatorType])
        setHistStyle(hists['tbar '+mediatorType])
        setHistStyle(hists['data'])
        setHistStyle(hists['bkgSum'])
    elif plotSys:
        setHistStyle(hists['bkgSum'])
        hists['bkgSum'].GetXaxis().SetLabelOffset(999)
        hists['bkgSum'].GetXaxis().SetLabelSize(0)
        setHistStyle(syshists['bkgSum_sysUp'])
        setHistStyle(syshists['bkgSum_sysDown'])
    if not plotSys:
        #Set tbar histogram options
        hists['tbar '+mediatorType].SetLineColor(kRed)
        hists['tbar '+mediatorType].SetLineWidth(3)
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
    #Set up/down systematic variation of bkgSum histogram options
    elif plotSys:
        if plotSysSignal:
            hists['bkgSum'].SetLineColor(kRed)
            hists['bkgSum'].SetLineWidth(3)
        else:
            hists['bkgSum'].SetFillColor(kOrange-5)
            hists['bkgSum'].SetLineWidth(0)
        syshists['bkgSum_sysUp'].SetLineColor(kBlue)
        syshists['bkgSum_sysDown'].SetLineColor(kGreen)
        syshists['bkgSum_sysUp'].SetLineWidth(2)
        syshists['bkgSum_sysDown'].SetLineWidth(2)
    #Add legend
    legend = TLegend(0.4, 0.65, 0.85, 0.85)
    legend.SetNColumns(3)
    if drawData:
        legend.AddEntry(hists['data'], 'Data', 'pe')
    if not plotSys:
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
            legend.AddEntry(hists['tbar '+mediatorType], '#splitline{'+mediatorType + ', t+DM (x'+str(scaleFactor)+')}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
        else:
            legend.AddEntry(hists['ttbar '+mediatorType], '#splitline{'+mediatorType + ', t#bar{t}+DM}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
            legend.AddEntry(hists['tbar '+mediatorType], '#splitline{'+mediatorType + ', t+DM}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
    elif plotSys:
        if plotSysSignal:
            legend.AddEntry(hists['bkgSum'], '#splitline{'+mediatorType + ', t#bar{t}+DM}{m_{#chi} = '+str(mchi)+', m_{#phi} = '+str(mphi)+'}', 'l')
        else:
            legend.AddEntry(hists['bkgSum'], 'MC background', 'f')
        legend.AddEntry(syshists['bkgSum_sysUp'], plotSysVar+'Up', 'l')
        legend.AddEntry(syshists['bkgSum_sysDown'], plotSysVar+'Down', 'l')
    legend.Draw('same')
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    print('Finished drawing histograms')

#Create and draw ratio plot histogram if drawData == True and savePlots == True
if drawData and savePlots:
    print('Drawing ratio plot...')
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

#Add ratio plot for up/down systematic variation of bkgSum if plotSys == True and savePlots == True
elif plotSys and savePlots:
    print('Drawing ratio plot...')
    c.cd(2)
    h_err = TH1F('h_ratio', ratioLabel, nbins, xmin, xmax)
    h_ratioUp = TH1F('h_ratioUp', ratioLabel, nbins, xmin, xmax)
    h_ratioDown = TH1F('h_ratioDown', ratioLabel, nbins, xmin, xmax)
    setHistStyle(h_ratioUp)
    setHistStyle(h_ratioDown)
    for i in range(1, nbins+1):
        if hists['bkgSum'].GetBinContent(i) > 0:
            h_ratioUp.SetBinContent(i,syshists['bkgSum_sysUp'].GetBinContent(i)/hists['bkgSum'].GetBinContent(i))
            h_ratioDown.SetBinContent(i,syshists['bkgSum_sysDown'].GetBinContent(i)/hists['bkgSum'].GetBinContent(i))
            h_err.SetBinContent(i,hists['bkgSum'].GetBinContent(i)/hists['bkgSum'].GetBinContent(i))
            h_err.SetBinError(i,hists['bkgSum'].GetBinError(i)/hists['bkgSum'].GetBinContent(i))
    #Set settings for sysUp/down ratio histograms 
    setBotStyle(h_err)
    h_err.Draw('e2')
    h_ratioUp.Draw('hist same')
    h_ratioDown.Draw('hist same')
    #Set settings for MC statistical error ratio histogram
    h_err.SetFillStyle(3002)
    h_err.SetFillColor(1)
    #Set sysUp/down ratio histogram marker options
    h_ratioUp.SetLineColor(kBlue)
    h_ratioDown.SetLineColor(kGreen)

    print('Finished drawing ratio plot')
        
#Save histogram if savePlots == True
if savePlots:
    if useCondor:
        suffix = date
        nameYear = str(year)
        if (year == 2018) and applyHEMfix:
            suffix += '_withHEMfix'
        if useUL:
            nameYear = 'UL'+str(year)
        if partialUnblind:
            suffix += '_partialUnblind'
        c.SaveAs(cut + nameYear + '_' + var.replace('/','over') + '_' + suffix + '.png')
        #c.SaveAs(cut + str(year) + '_' + var + '_' + date + '.root')
    else:
        suffix = date
        nameYear = str(year)
        if plotSys:
            suffix = plotSysVar + '_' + date
        if (year == 2018) and applyHEMfix:
            suffix += '_withHEMfix'
        if useUL:
            nameYear = 'UL'+str(year)
        if partialUnblind:
            suffix += '_partialUnblind'
        if plotSysSignal:
            c.SaveAs(saveDirectory + date + '/' + cut + nameYear + '_' + var.replace('/','over') + '_' + suffix + '_ttDM_scalar_Mchi'+str(mchi)+'_Mphi'+str(mphi)+'.png')
        else:
            #c.SaveAs(saveDirectory + date + '/' + cut + nameYear + '_' + var.replace('/','over') + '_' + suffix + '_NLO.png')
            #c.SaveAs(saveDirectory + date + '/' + cut + str(year) + '_' + var + '_' + date + '.png')
            #c.SaveAs(saveDirectory + cut + str(year) + '_' + var + '_' + date + '_withHEMfixv5_postHEM.png')
            c.SaveAs(cut + nameYear + '_' + var.replace('/','over') + '_' + suffix + '.png')
            #c.SaveAs(cut + nameYear + '_deltaPhiJet3MET_' + suffix + '.png')

print 'Plotting end time:', datetime.datetime.now()
