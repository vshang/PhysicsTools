import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.corrections.leptonSFs import *
from PhysicsTools.NanoAODTools.postprocessing.corrections.BTaggingTool import *
from PhysicsTools.NanoAODTools.postprocessing.corrections.kFactorTool import *
from PhysicsTools.NanoAODTools.postprocessing.corrections.PileupWeightTool import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *

#Load Mt2Com_bisect.o object file that contains C++ code to calculate M_T2W for SL region (runLocal = False if running jobs through CRAB)
#runLocal = False
runLocal = True

if runLocal:
    ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2w_bisect_cc.so")
    ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/MT2Utility_cc.so")
    ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2bl_bisect_cc.so")
    ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/Mt2Com_bisect_cc.so")
    ROOT.gROOT.ProcessLine(".L /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/lester_mt2_bisect.h")
    ROOT.gROOT.ProcessLine(".L /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/XYMETCorrection.h")
else:
    ROOT.gSystem.Load("mt2w_bisect_cc.so")
    ROOT.gSystem.Load("MT2Utility_cc.so")
    ROOT.gSystem.Load("mt2bl_bisect_cc.so")
    ROOT.gSystem.Load("Mt2Com_bisect_cc.so")
    ROOT.gROOT.ProcessLine(".L lester_mt2_bisect.h")
    ROOT.gROOT.ProcessLine(".L XYMETCorrection.h")

try:
    ROOT.asymm_mt2_lester_bisect.disableCopyrightMessage()
except:
    pass
Mt2Com_bisect = ROOT.Mt2Com_bisect()
asymm_mt2_lester_bisect = ROOT.asymm_mt2_lester_bisect()

class CommonAnalysis(Module):
    def __init__(self, signalRegion, year=2016, isData=False, isSignal=False, btag='DeepCSV'):
        self.signalRegion = signalRegion
        self.year = year
        self.isData = isData
        self.isMC = not self.isData
        self.isSignal = isSignal
        self.btag = btag
        self.nEvent = 0
        if self.isMC:
            self.eleSFs = ElectronSFs(self.year)
            self.muSFs = MuonSFs(self.year)
            self.btagTool = BTagWeightTool(tagger=self.btag,wp='medium',channel='ttbar',year=self.year)
            self.btagToolUp = BTagWeightTool(tagger=self.btag,wp='medium',sigma='up',channel='ttbar',year=self.year)
            self.btagToolDown = BTagWeightTool(tagger=self.btag,wp='medium',sigma='down',channel='ttbar',year=self.year)
            self.puTool = PileupWeightTool(year=self.year)
            self.puToolUp = PileupWeightTool(year=self.year,sigma='up')
            self.puToolDown = PileupWeightTool(year=self.year,sigma='down')
            self.kFactorTool = KFactorTool(year=self.year)

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        #Define output branches to check if preselection is working
        self.out = wrappedOutputTree
        self.out.branch("nTightElectrons","I");
        self.out.branch("nVetoElectrons","I");
        self.out.branch("nTightMuons","I");
        self.out.branch("nLooseMuons","I");
        self.out.branch("tightElectron1_charge","I")
        self.out.branch("tightMuon1_charge","I")

        self.out.branch("njets", "I")
        self.out.branch("nfjets", "I")
        self.out.branch("nbjets", "I")

        self.out.branch("METcorrected_pt", "F")
        self.out.branch("METcorrected_phi", "F")

        self.out.branch("minDeltaPhi", "F")
        self.out.branch("minDeltaPhi12", "F")
        self.out.branch("M_Tb", "F")
        self.out.branch("M_T", "F")
        self.out.branch("M_T2W", "F")
        self.out.branch("M_T2ll", "F")
        self.out.branch("jet1p_TH_T", "F")
        self.out.branch("jet1_jetId", "I")
        self.out.branch("jet1_chHEF", "F")
        self.out.branch("ntaus", "I")
        self.out.branch("m_llExists","I")
        self.out.branch("m_ll","F")
        self.out.branch("recoilPtMiss","F")

        self.out.branch("minDeltaPhi_puppi", "F")
        self.out.branch("minDeltaPhi12_puppi", "F")
        self.out.branch("M_Tb_puppi", "F")
        self.out.branch("M_T_puppi", "F")
        self.out.branch("M_T2W_puppi", "F")
        self.out.branch("M_T2ll_puppi", "F")
        self.out.branch("m_llExists_puppi","I")
        self.out.branch("recoilPtMiss_puppi","F")

        self.out.branch("lepton1_charge","I")
        self.out.branch("lepton2_charge","I")

        self.out.branch("index_vetoElectrons","I",lenVar="nVetoElectrons")
        self.out.branch("index_tightElectrons","I",lenVar="nTightElectrons")
        self.out.branch("index_looseMuons","I",lenVar="nLooseMuons")
        self.out.branch("index_tightMuons","I",lenVar="nTightMuons")
        self.out.branch("index_centralJets","I",lenVar="njets")
        self.out.branch("index_forwardJets","I",lenVar="nfjets")
        self.out.branch("index_bJets","I",lenVar="nbjets")

        #Systematics - JES, JER
        self.out.branch("njetsScaleUp", "I")
        self.out.branch("njetsScaleDown", "I")
        self.out.branch("njetsResUp", "I")
        self.out.branch("njetsResDown", "I")

        self.out.branch("nfjetsScaleUp", "I")
        self.out.branch("nfjetsScaleDown", "I")
        self.out.branch("nfjetsResUp", "I")
        self.out.branch("nfjetsResDown", "I")

        self.out.branch("nbjetsScaleUp", "I")
        self.out.branch("nbjetsScaleDown", "I")
        self.out.branch("nbjetsResUp", "I")
        self.out.branch("nbjetsResDown", "I")

        self.out.branch("METcorrected_ptScaleUp", "F")
        self.out.branch("METcorrected_ptScaleDown", "F")
        self.out.branch("METcorrected_ptResUp", "F")
        self.out.branch("METcorrected_ptResDown", "F")
        self.out.branch("METcorrected_phiScaleUp", "F")
        self.out.branch("METcorrected_phiScaleDown", "F")
        self.out.branch("METcorrected_phiResUp", "F")
        self.out.branch("METcorrected_phiResDown", "F")

        self.out.branch("minDeltaPhiScaleUp", "F")
        self.out.branch("minDeltaPhiScaleDown", "F")
        self.out.branch("minDeltaPhiResUp", "F")
        self.out.branch("minDeltaPhiResDown", "F")

        self.out.branch("minDeltaPhi12ScaleUp", "F")
        self.out.branch("minDeltaPhi12ScaleDown", "F")
        self.out.branch("minDeltaPhi12ResUp", "F")
        self.out.branch("minDeltaPhi12ResDown", "F")

        self.out.branch("M_TbScaleUp", "F")
        self.out.branch("M_TbScaleDown", "F")
        self.out.branch("M_TbResUp", "F")
        self.out.branch("M_TbResDown", "F")

        self.out.branch("M_TScaleUp", "F")
        self.out.branch("M_TScaleDown", "F")
        self.out.branch("M_TResUp", "F")
        self.out.branch("M_TResDown", "F")

        self.out.branch("M_T2WScaleUp", "F")
        self.out.branch("M_T2WScaleDown", "F")
        self.out.branch("M_T2WResUp", "F")
        self.out.branch("M_T2WResDown", "F")

        self.out.branch("M_T2llScaleUp", "F")
        self.out.branch("M_T2llScaleDown", "F")
        self.out.branch("M_T2llResUp", "F")
        self.out.branch("M_T2llResDown", "F")

        self.out.branch("jet1p_TH_TScaleUp", "F")
        self.out.branch("jet1p_TH_TScaleDown", "F")
        self.out.branch("jet1p_TH_TResUp", "F")
        self.out.branch("jet1p_TH_TResDown", "F")

        self.out.branch("jet1_chHEFScaleUp", "F")
        self.out.branch("jet1_chHEFScaleDown", "F")
        self.out.branch("jet1_chHEFResUp", "F")
        self.out.branch("jet1_chHEFResDown", "F")

        self.out.branch("m_llExistsScaleUp", "I")
        self.out.branch("m_llExistsScaleDown", "I")
        self.out.branch("m_llExistsResUp", "I")
        self.out.branch("m_llExistsResDown", "I")

        self.out.branch("recoilPtMissScaleUp", "F")
        self.out.branch("recoilPtMissScaleDown", "F")
        self.out.branch("recoilPtMissResUp", "F")
        self.out.branch("recoilPtMissResDown", "F")

        if self.isMC:
            #Systematics - PDF
            self.out.branch("pdfWeightUp", "F")
            self.out.branch("pdfWeightDown", "F")

            #Systematics - QCD Renormalization and Factorization scales
            self.out.branch("qcdRenWeightUp", "F")
            self.out.branch("qcdRenWeightDown", "F")
            self.out.branch("qcdFacWeightUp", "F")
            self.out.branch("qcdFacWeightDown", "F")

            self.out.branch("leptonWeight", "F")
            #Systematics - lepton weights
            self.out.branch("leptonWeightUp", "F")
            self.out.branch("leptonWeightDown", "F")

            self.out.branch("bjetWeight", "F")
            #Systematics - b-tagging weights
            self.out.branch("bjetWeightUp","F")
            self.out.branch("bjetWeightDown","F")

            self.out.branch("puWeight", "F")
            #Systematics - Pile-up
            self.out.branch("puWeightUp", "F")
            self.out.branch("puWeightDown", "F")

            self.out.branch("ewkWWeight", "F")
            self.out.branch("ewkZWeight", "F")
            self.out.branch("qcdWWeight", "F")
            self.out.branch("qcdZTo2NuWeight", "F")
            self.out.branch("qcdZTo2LWeight", "F")
            #Systematics - QCD Scale Factors
            self.out.branch("qcdWWeightRenUp", "F")
            self.out.branch("qcdWWeightRenDown", "F")
            self.out.branch("qcdWWeightFacUp", "F")
            self.out.branch("qcdWWeightFacDown", "F")
            self.out.branch("qcdZWeightRenUp", "F")
            self.out.branch("qcdZWeightRenDown", "F")
            self.out.branch("qcdZWeightFacUp", "F")
            self.out.branch("qcdZWeightFacDown", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go 
to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")

        #Tight/Veto electrons are defined and counted
        if self.year == 2016:
            vetoElectronsEnumerate = filter(lambda lep : lep[1].pt > 10 and lep[1].cutBased_Sum16 != 0 and (abs(lep[1].eta) < 1.4442 or 1.566 < abs(lep[1].eta) < 2.5), enumerate(electrons))
            tightElectronsEnumerate = filter(lambda lep : lep[1].pt > 40 and abs(lep[1].eta) < 2.1 and lep[1].cutBased_Sum16 == 4, vetoElectronsEnumerate)

        else:
            vetoElectronsEnumerate = filter(lambda lep : lep[1].pt > 10 and lep[1].cutBased != 0 and (abs(lep[1].eta) < 1.4442 or 1.566 < abs(lep[1].eta) < 2.5), enumerate(electrons))
            tightElectronsEnumerate = filter(lambda lep : lep[1].pt > 40 and abs(lep[1].eta) < 2.1 and lep[1].cutBased == 4, vetoElectronsEnumerate)
        
        nVetoElectrons = len(vetoElectronsEnumerate)
        nTightElectrons = len(tightElectronsEnumerate)

        vetoElectrons = [lep[1] for lep in vetoElectronsEnumerate]
        tightElectrons = [lep[1] for lep in tightElectronsEnumerate]

        #Also store index of each electron in collection
        index_vetoElectrons = [lep[0] for lep in vetoElectronsEnumerate]
        index_tightElectrons = [lep[0] for lep in tightElectronsEnumerate]
        
        #Tight/Loose muons are defined and counted
        looseMuonsEnumerate = filter(lambda lep : lep[1].pt > 10 and lep[1].looseId and lep[1].pfRelIso04_all < 0.25 and abs(lep[1].eta) < 2.4, enumerate(muons))
        tightMuonsEnumerate = filter(lambda lep : lep[1].pt > 30 and lep[1].tightId and lep[1].pfRelIso04_all < 0.15, looseMuonsEnumerate)

        nLooseMuons = len(looseMuonsEnumerate)
        nTightMuons = len(tightMuonsEnumerate)

        looseMuons = [lep[1] for lep in looseMuonsEnumerate]
        tightMuons = [lep[1] for lep in tightMuonsEnumerate]

        #Also store index of each muon in collection
        index_looseMuons = [lep[0] for lep in looseMuonsEnumerate]
        index_tightMuons = [lep[0] for lep in tightMuonsEnumerate]

        #Store charge of highest pT Tight electron/muon if possible
        tightElectron1_charge = 0
        tightMuon1_charge = 0
        if nTightElectrons > 0:
            tightElectron1_charge = tightElectrons[0].charge
        if nTightMuons > 0:
            tightMuon1_charge = tightMuons[0].charge

        #Jets (including tau jets) are not considered if they are within Delta R < 0.4 of a loose/veto lepton
        def cleanJet(jet):
            for vetoElectron in vetoElectrons:
                if vetoElectron.p4().DeltaR(jet.p4()) < 0.4:
                    return False
            for looseMuon in looseMuons:
                if looseMuon.p4().DeltaR(jet.p4()) < 0.4:
                    return False
            return True

        #Jet categories are defined and counted 
        if self.year == 2016:
            #Central jets  (2016)
            centralJetsEnumerate = filter(lambda j : ((30 < j[1].pt_nom < 50 and j[1].puId == 7) or j[1].pt_nom > 50) and abs(j[1].eta) < 2.4 and cleanJet(j[1]) and j[1].jetId == 7, enumerate(jets)) #Use tightLepVeto jet ID WP for 2016 with tight puId for jet_pt < 50
            #Systematics - JES, JER
            centralJetsScaleUp = filter(lambda j : ((30 < j.pt_jesTotalUp < 50 and j.puId == 7) or j.pt > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 7, jets)
            centralJetsScaleDown = filter(lambda j : ((30 < j.pt_jesTotalDown < 50 and j.puId == 7) or j.pt > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 7, jets)
            centralJetsResUp = filter(lambda j : ((30 < j.pt_jerUp < 50 and j.puId == 7) or j.pt > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 7, jets)
            centralJetsResDown = filter(lambda j : ((30 < j.pt_jerDown < 50 and j.puId == 7) or j.pt > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 7, jets)

            #Forward jets (2016)
            forwardJetsEnumerate = filter(lambda j : ((30 < j[1].pt_nom < 50 and j[1].puId == 7) or j[1].pt_nom > 50) and 2.4 < abs(j[1].eta) < 4 and cleanJet(j[1]) and j[1].jetId == 7, enumerate(jets))
            #Systematics - JES, JER
            forwardJetsScaleUp = filter(lambda j : ((30 < j.pt_jesTotalUp < 50 and j.puId == 7) or j.pt > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 7, jets)
            forwardJetsScaleDown = filter(lambda j : ((30 < j.pt_jesTotalDown < 50 and j.puId == 7) or j.pt > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 7, jets)
            forwardJetsResUp = filter(lambda j : ((30 < j.pt_jerUp < 50 and j.puId == 7) or j.pt > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 7, jets)
            forwardJetsResDown = filter(lambda j : ((30 < j.pt_jerDown < 50 and j.puId == 7) or j.pt > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 7, jets)

        else:
            #Central jets (2017, 2018)
            centralJetsEnumerate = filter(lambda j : ((30 < j[1].pt_nom < 50 and j[1].puId == 7) or j[1].pt_nom > 50) and abs(j[1].eta) < 2.4 and cleanJet(j[1]) and j[1].jetId == 6, enumerate(jets)) #Use tightLepVeto jet ID WP for 2017 and 2018 with tight puId for jet_pt < 50
            #Systematics - JES, JER
            centralJetsScaleUp = filter(lambda j : ((30 < j.pt_jesTotalUp < 50 and j.puId == 7) or j.pt > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 6, jets)
            centralJetsScaleDown = filter(lambda j : ((30 < j.pt_jesTotalDown < 50 and j.puId == 7) or j.pt > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 6, jets)
            centralJetsResUp = filter(lambda j : ((30 < j.pt_jerUp < 50 and j.puId == 7) or j.pt > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 6, jets)
            centralJetsResDown = filter(lambda j : ((30 < j.pt_jerDown < 50 and j.puId == 7) or j.pt > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 6, jets)

            #Forward jets (2017, 2018)
            forwardJetsEnumerate = filter(lambda j : ((30 < j[1].pt_nom < 50 and j[1].puId == 7) or j[1].pt_nom > 50) and 2.4 < abs(j[1].eta) < 4 and cleanJet(j[1]) and j[1].jetId == 6, enumerate(jets))
            #Systematics - JES, JER
            forwardJetsScaleUp = filter(lambda j : ((30 < j.pt_jesTotalUp < 50 and j.puId == 7) or j.pt > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 6, jets)
            forwardJetsScaleDown = filter(lambda j : ((30 < j.pt_jesTotalDown < 50 and j.puId == 7) or j.pt > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 6, jets)
            forwardJetsResUp = filter(lambda j : ((30 < j.pt_jerUp < 50 and j.puId == 7) or j.pt > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 6, jets)
            forwardJetsResUp = filter(lambda j : ((30 < j.pt_jerDown < 50 and j.puId == 7) or j.pt > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 6, jets)

        #B-jets
        btag_WP = getattr(BTagWPs(self.btag,self.year),'medium')
        if self.btag == 'CSVv2':
            bJetsEnumerate = filter(lambda j : j[1].btagCSVV2 > btag_WP, centralJetsEnumerate)
            #Systematics - JES, JER
            bJetsScaleUp = filter(lambda j : j.btagCSVV2 > btag_WP, centralJetsScaleUp)
            bJetsScaleDown = filter(lambda j : j.btagCSVV2 > btag_WP, centralJetsScaleDown)
            bJetsResUp = filter(lambda j : j.btagCSVV2 > btag_WP, centralJetsResUp)
            bJetsResDown = filter(lambda j : j.btagCSVV2 > btag_WP, centralJetsResDown)

        elif self.btag == 'DeepCSV':
            bJetsEnumerate = filter(lambda j : j[1].btagDeepB > btag_WP, centralJetsEnumerate)
            #Systematics - JES, JER
            bJetsScaleUp = filter(lambda j : j.btagDeepB > btag_WP, centralJetsScaleUp)
            bJetsScaleDown = filter(lambda j : j.btagDeepB > btag_WP, centralJetsScaleDown)
            bJetsResUp = filter(lambda j : j.btagDeepB > btag_WP, centralJetsResUp)
            bJetsResDown = filter(lambda j : j.btagDeepB > btag_WP, centralJetsResDown)

        #Define central, forward, and b-tagged jet collections
        centralJets = [j[1] for j in centralJetsEnumerate]
        forwardJets = [j[1] for j in forwardJetsEnumerate]
        bJets = [j[1] for j in bJetsEnumerate]

        #Count central, forward, and b-tagged jets
        njets = len(centralJetsEnumerate)
        nfjets = len(forwardJetsEnumerate)
        nbjets = len(bJetsEnumerate)

        #Also store index of each jet in collection
        index_centralJets = [j[0] for j in centralJetsEnumerate]
        index_forwardJets = [j[0] for j in forwardJetsEnumerate]
        index_bJets = [j[0] for j in bJetsEnumerate]
        
        #Systematics - JES, JER
        njetsScaleUp = len(centralJetsScaleUp)
        njetsScaleDown = len(centralJetsScaleDown)
        njetsResUp = len(centralJetsResUp)
        njetsResDown = len(centralJetsResDown)

        nfjetsScaleUp = len(forwardJetsScaleUp)
        nfjetsScaleDown = len(forwardJetsScaleDown)
        nfjetsResUp = len(forwardJetsResUp)
        nfjetsResDown = len(forwardJetsResDown)

        nbjetsScaleUp = len(bJetsScaleUp)
        nbjetsScaleDown = len(bJetsScaleDown)
        nbjetsResUp = len(bJetsResUp)
        nbjetsResDown = len(bJetsResDown)


        #Apply MET corrections (JEC, JER, METFixEE2017, xy-Shift)
        if self.year == 2017:
            #Apply EE noise fix for 2017 (https://twiki.cern.ch/twiki/bin/viewauth/CMS/ExoPreapprovalChecklist)
            METcorrected_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_pt, event.METFixEE2017_phi, event.run, 2017, self.isMC, event.PV_npvs)
            #Systematics - JES, JER
            METcorrected_pt_phiScaleUp = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_T1Smear_pt_jesTotalUp, event.METFixEE2017_T1Smear_phi_jesTotalUp, event.run, 2017, self.isMC, event.PV_npvs)
            METcorrected_pt_phiScaleDown = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_T1Smear_pt_jesTotalDown, event.METFixEE2017_T1Smear_phi_jesTotalDown, event.run, 2017, self.isMC, event.PV_npvs)
            METcorrected_pt_phiResUp = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_T1Smear_pt_jerUp, event.METFixEE2017_T1Smear_phi_jerUp, event.run, 2017, self.isMC, event.PV_npvs)
            METcorrected_pt_phiResDown = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_T1Smear_pt_jerDown, event.METFixEE2017_T1Smear_phi_jerDown, event.run, 2017, self.isMC, event.PV_npvs)

        else:
            METcorrected_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.MET_pt, event.MET_phi, event.run, self.year, self.isMC, event.PV_npvs)
            #Systematics - JES, JER
            METcorrected_pt_phiScaleUp = ROOT.METXYCorr_Met_MetPhi(event.MET_T1Smear_pt_jesTotalUp, event.MET_T1Smear_phi_jesTotalUp, event.run, 2017, self.isMC, event.PV_npvs)
            METcorrected_pt_phiScaleDown = ROOT.METXYCorr_Met_MetPhi(event.MET_T1Smear_pt_jesTotalDown, event.MET_T1Smear_phi_jesTotalDown, event.run, 2017, self.isMC, event.PV_npvs)
            METcorrected_pt_phiResUp = ROOT.METXYCorr_Met_MetPhi(event.MET_T1Smear_pt_jerUp, event.MET_T1Smear_phi_jerUp, event.run, 2017, self.isMC, event.PV_npvs)
            METcorrected_pt_phiResDown = ROOT.METXYCorr_Met_MetPhi(event.MET_T1Smear_pt_jerDown, event.MET_T1Smear_phi_jerDown, event.run, 2017, self.isMC, event.PV_npvs)

        METcorrected_pt = METcorrected_pt_phi[0]
        METcorrected_phi = METcorrected_pt_phi[1]

        #Systematics - JES, JER
        METcorrected_ptScaleUp = METcorrected_pt_phiScaleUp[0]
        METcorrected_phiScaleUp = METcorrected_pt_phiScaleUp[1]
        METcorrected_ptScaleDown = METcorrected_pt_phiScaleDown[0]
        METcorrected_phiScaleDown = METcorrected_pt_phiScaleDown[1]
        METcorrected_ptResUp = METcorrected_pt_phiResUp[0]
        METcorrected_phiResUp = METcorrected_pt_phiResUp[1]
        METcorrected_ptResDown = METcorrected_pt_phiResDown[0]
        METcorrected_phiResDown = METcorrected_pt_phiResDown[1]

        #Calculate minDeltaPhi and minDeltaPhi(j_(1,2), missing pt) preselection variable of all central jets 
        minDeltaPhi = minDeltaPhi12 = minDeltaPhi_puppi = minDeltaPhi12_puppi = -9 #If there is less than 2 jets, set value to -9 to indicate  minDeltaPhi cannot be calculated

        #Systematics - JES, JER
        minDeltaPhiScaleUp = minDeltaPhiScaleDown = minDeltaPhiResUp = minDeltaPhiResDown = -9 
        minDeltaPhi12ScaleUp = minDeltaPhi12ScaleDown = minDeltaPhi12ResUp = minDeltaPhi12ResDown = -9 

        if njets > 1: #Should always be true for both SL and AH signal regions
            jet1 = centralJets[0] #jet1 (jet2) is the jet with the largest (second-largest) pt
            jet2 = centralJets[1]
            deltaPhi1 = min(abs(jet1.phi - METcorrected_phi), 2 * math.pi - abs(jet1.phi - METcorrected_phi)) #phi angle between jet1 and missing pt
            #Systematics - JES, JER
            deltaPhi1ScaleUp = min(abs(jet1.phi - METcorrected_phiScaleUp), 2 * math.pi - abs(jet1.phi - METcorrected_phiScaleUp))
            deltaPhi1ScaleDown = min(abs(jet1.phi - METcorrected_phiScaleDown), 2 * math.pi - abs(jet1.phi - METcorrected_phiScaleDown))
            deltaPhi1ResUp = min(abs(jet1.phi - METcorrected_phiResUp), 2 * math.pi - abs(jet1.phi - METcorrected_phiResUp))
            deltaPhi1ResDown = min(abs(jet1.phi - METcorrected_phiResDown), 2 * math.pi - abs(jet1.phi - METcorrected_phiResDown))

            deltaPhi2 = min(abs(jet2.phi - METcorrected_phi), 2 * math.pi - abs(jet2.phi - METcorrected_phi)) #phi angle between jet2 and missing pt
            #Systematics - JES, JER
            deltaPhi2ScaleUp = min(abs(jet2.phi - METcorrected_phiScaleUp), 2 * math.pi - abs(jet2.phi - METcorrected_phiScaleUp))
            deltaPhi2ScaleDown = min(abs(jet2.phi - METcorrected_phiScaleDown), 2 * math.pi - abs(jet2.phi - METcorrected_phiScaleDown))
            deltaPhi2ResUp = min(abs(jet2.phi - METcorrected_phiResUp), 2 * math.pi - abs(jet2.phi - METcorrected_phiResUp))
            deltaPhi2ResDown = min(abs(jet2.phi - METcorrected_phiResDown), 2 * math.pi - abs(jet2.phi - METcorrected_phiResDown))

            minDeltaPhi12 = min(deltaPhi1, deltaPhi2) #First calculate minDeltaPhi12
            #Systematics - JES, JER
            minDeltaPhi12ScaleUp = min(deltaPhi1ScaleUp, deltaPhi2ScaleUp)
            minDeltaPhi12ScaleDown = min(deltaPhi1ScaleDown, deltaPhi2ScaleDown)
            minDeltaPhi12ResUp = min(deltaPhi1ResUp, deltaPhi2ResUp)
            minDeltaPhi12ResDown = min(deltaPhi1ResDown, deltaPhi2ResDown)

            deltaPhi1_puppi = min(abs(jet1.phi - event.PuppiMET_phi), 2 * math.pi - abs(jet1.phi - event.PuppiMET_phi)) #phi angle between jet1 and Puppi missing pt
            deltaPhi2_puppi = min(abs(jet2.phi - event.PuppiMET_phi), 2 * math.pi - abs(jet2.phi - event.PuppiMET_phi)) #phi angle between jet2 and Puppi missing pt
            minDeltaPhi12_puppi = min(deltaPhi1_puppi, deltaPhi2_puppi) #First calculate minDeltaPhi12_puppi 

            #Now calculate minDeltaPhi and minDeltaPhi_puppi
            minDeltaPhi = min(abs(jet1.phi - METcorrected_phi), 2 * math.pi - abs(jet1.phi - METcorrected_phi)) #phi angle between jet1 and missing pt
            minDeltaPhi_puppi = min(abs(jet1.phi - event.PuppiMET_phi), 2 * math.pi - abs(jet1.phi - event.PuppiMET_phi)) #phi angle between jet1 and Puppi missing pt
            #Systematics - JES, JER
            minDeltaPhiScaleUp = min(abs(jet1.phi - METcorrected_phiScaleUp), 2 * math.pi - abs(jet1.phi - METcorrected_phiScaleUp))
            minDeltaPhiScaleDown = min(abs(jet1.phi - METcorrected_phiScaleDown), 2 * math.pi - abs(jet1.phi - METcorrected_phiScaleDown))
            minDeltaPhiResUp = min(abs(jet1.phi - METcorrected_phiResUp), 2 * math.pi - abs(jet1.phi - METcorrected_phiResUp))
            minDeltaPhiResDown = min(abs(jet1.phi - METcorrected_phiResDown), 2 * math.pi - abs(jet1.phi - METcorrected_phiResDown))

            for i in range(1, njets):
                jeti = centralJets[i]
                minDeltaPhi_i = min(abs(jeti.phi - METcorrected_phi), 2 * math.pi - abs(jeti.phi - METcorrected_phi)) #phi angle between jeti and missing pt
                minDeltaPhi_puppi_i = min(abs(jeti.phi - event.PuppiMET_phi), 2 * math.pi - abs(jeti.phi - event.PuppiMET_phi)) #phi angle between jeti and Puppi missing pt
                if minDeltaPhi_i < minDeltaPhi: #Choose lowest minDeltaPhi out of all central jets
                    minDeltaPhi = minDeltaPhi_i
                if minDeltaPhi_puppi_i < minDeltaPhi_puppi: #Choose lowest minDeltaPhi_puppi out of all central jets
                    minDeltaPhi_puppi = minDeltaPhi_puppi_i

            #Systematics - JES, JER
            for i in range(1, njetsScaleUp):
                jetiScaleUp = centralJetsScaleUp[i]
                minDeltaPhiScaleUp_i = min(abs(jeti.phi - METcorrected_phiScaleUp), 2 * math.pi - abs(jeti.phi - METcorrected_phiScaleUp)) #phi angle between jeti and missing pt
                if minDeltaPhiScaleUp_i < minDeltaPhiScaleUp: #Choose lowest minDeltaPhi out of all central jets
                    minDeltaPhiScaleUp = minDeltaPhiScaleUp_i

            for i in range(1, njetsScaleDown):
                jetiScaleDown = centralJetsScaleDown[i]
                minDeltaPhiScaleDown_i = min(abs(jeti.phi - METcorrected_phiScaleDown), 2 * math.pi - abs(jeti.phi - METcorrected_phiScaleDown)) #phi angle between jeti and missing pt
                if minDeltaPhiScaleDown_i < minDeltaPhiScaleDown: #Choose lowest minDeltaPhi out of all central jets
                    minDeltaPhiScaleDown = minDeltaPhiScaleDown_i

            for i in range(1, njetsResUp):
                jetiResUp = centralJetsResUp[i]
                minDeltaPhiResUp_i = min(abs(jeti.phi - METcorrected_phiResUp), 2 * math.pi - abs(jeti.phi - METcorrected_phiResUp)) #phi angle between jeti and missing pt
                if minDeltaPhiResUp_i < minDeltaPhiResUp: #Choose lowest minDeltaPhi out of all central jets
                    minDeltaPhiResUp = minDeltaPhiResUp_i

            for i in range(1, njetsResDown):
                jetiResDown = centralJetsResDown[i]
                minDeltaPhiResDown_i = min(abs(jeti.phi - METcorrected_phiResDown), 2 * math.pi - abs(jeti.phi - METcorrected_phiResDown)) #phi angle between jeti and missing pt
                if minDeltaPhiResDown_i < minDeltaPhiResDown: #Choose lowest minDeltaPhi out of all central jets
                    minDeltaPhiResDown = minDeltaPhiResDown_i

        #Jet TLorentzVectors are constructed to calculate M_T2^W
        ljetVector = ROOT.vector("TLorentzVector")()
        bjetVector = ROOT.vector("TLorentzVector")()
        #Systematics - JES, JER
        ljetVectorScaleUp = ROOT.vector("TLorentzVector")()
        bjetVectorScaleUp = ROOT.vector("TLorentzVector")()
        ljetVectorScaleDown = ROOT.vector("TLorentzVector")()
        bjetVectorScaleDown = ROOT.vector("TLorentzVector")()
        ljetVectorResUp = ROOT.vector("TLorentzVector")()
        bjetVectorResUp = ROOT.vector("TLorentzVector")()
        ljetVectorResDown = ROOT.vector("TLorentzVector")()
        bjetVectorResDown = ROOT.vector("TLorentzVector")()

        #Calculate jet1p_T/H_T
        H_T = 0
        jet1p_TH_T = 9 #If there are no jets, set value to +9 to indicate jet1p_T/H_T cannnot be calculated
        #Systematics - JES, JER
        H_TScaleUp = H_TScaleDown = H_TResUp = H_TResDown = 0
        jet1p_TH_TScaleUp = jet1p_TH_TScaleDown = jet1p_TH_TResUp = jet1p_TH_TResDown = -9
        
        if njets > 0:
            for jet in centralJets:
                H_T += jet.pt_nom
                if self.btag == 'CSVv2':
                    jet_btag = jet.btagCSVV2
                elif self.btag == 'DeepCSV':
                    jet_btag = jet.btagDeepB
                if jet_btag < btag_WP:
                    ljetVector.push_back(jet.p4())                    
            jet1p_TH_T = centralJets[0].pt_nom/H_T

        #Systematics - JES, JER
        if njetsScaleUp > 0:
            for jetScaleUp in centralJetsScaleUp:
                H_TScaleUp += jetScaleUp.pt_nom
                if self.btag == 'CSVv2':
                    jetScaleUp_btag = jetScaleUp.btagCSVV2
                elif self.btag == 'DeepCSV':
                    jetScaleUp_btag = jetScaleUp.btagDeepB
                if jetScaleUp_btag < btag_WP:
                    ljetVectorScaleUp.push_back(jetScaleUp.p4()*(jetScaleUp.pt_jesTotalUp/jetScaleUp.pt_nom))
            jet1p_TH_TScaleUp = centralJetsScaleUp[0].pt_nom/H_TScaleUp

        if njetsScaleDown > 0:
            for jetScaleDown in centralJetsScaleDown:
                H_TScaleDown += jetScaleDown.pt_nom
                if self.btag == 'CSVv2':
                    jetScaleDown_btag = jetScaleDown.btagCSVV2
                elif self.btag == 'DeepCSV':
                    jetScaleDown_btag = jetScaleDown.btagDeepB
                if jetScaleDown_btag < btag_WP:
                    ljetVectorScaleDown.push_back(jetScaleDown.p4()*(jetScaleDown.pt_jesTotalDown/jetScaleDown.pt_nom))
            jet1p_TH_TScaleDown = centralJetsScaleDown[0].pt_nom/H_TScaleDown

        if njetsResUp > 0:
            for jetResUp in centralJetsResUp:
                H_TResUp += jetResUp.pt_nom
                if self.btag == 'CSVv2':
                    jetResUp_btag = jetResUp.btagCSVV2
                elif self.btag == 'DeepCSV':
                    jetResUp_btag = jetResUp.btagDeepB
                if jetResUp_btag < btag_WP:
                    if self.isMC:
                        ljetVectorResUp.push_back(jetResUp.p4()*(jetResUp.pt_jerUp/jetResUp.pt_nom))
                    else:
                        ljetVectorResUp.push_back(jetResUp.p4())
            jet1p_TH_TResUp = centralJetsResUp[0].pt_nom/H_TResUp

        if njetsResDown > 0:
            for jetResDown in centralJetsResDown:
                H_TResDown += jetResDown.pt_nom
                if self.btag == 'CSVv2':
                    jetResDown_btag = jetResDown.btagCSVV2
                elif self.btag == 'DeepCSV':
                    jetResDown_btag = jetResDown.btagDeepB
                if jetResDown_btag < btag_WP:
                    if self.isMC:
                        ljetVectorResDown.push_back(jetResDown.p4()*(jetResDown.pt_jerDown/jetResDown.pt_nom))
                    else:
                        ljetVectorResDown.push_back(jetResDown.p4())
            jet1p_TH_TResDown = centralJetsResDown[0].pt_nom/H_TResDown

        #Calculate jet1_jetId and jet1_chHEF
        jet1_jetId  = -9 #If there are no jets, set value to -9 to indicate jet1_jetId and jet1_chHEF cannot be calculated
        jet1_chHEF = -9
        if njets > 0:
            jet1_jetId = centralJets[0].jetId
            jet1_chHEF = centralJets[0].chHEF
        #Systematics - JES, JER
        jet1_chHEFScaleUp = jet1_chHEFScaleDown = jet1_chHEFResUp = jet1_chHEFResDown = -9
        if njetsScaleUp > 0:
            jet1_chHEFScaleUp = centralJetsScaleUp[0].chHEF
        if njetsScaleDown > 0:
            jet1_chHEFScaleDown = centralJetsScaleDown[0].chHEF
        if njetsResUp > 0:
            jet1_chHEFResUp = centralJetsResUp[0].chHEF
        if njetsResDown > 0:
            jet1_chHEFResDown = centralJetsResDown[0].chHEF

        #Calculate M_T^b
        M_Tb = -9 #If there are no bjets, set value to -9 to indicate M_Tb cannot be calculated
        M_Tb_puppi = -9
        #Systematics - JES, JER
        M_TbScaleUp = M_TbScaleDown = M_TbResUp = M_TbResDown = -9
        
        if nbjets > 0:
            bjet1 = bJets[0]
            for bjet in bJets:
                bjetVector.push_back(bjet.p4())
                if self.btag == 'CSVv2':
                    bjet_btag = bjet.btagCSVV2
                    bjet1_btag = bjet1.btagCSVV2
                elif self.btag == 'DeepCSV':
                    bjet_btag = bjet.btagDeepB
                    bjet1_btag = bjet.btagDeepB
                if bjet_btag > bjet1_btag:
                    bjet1 = bjet

            deltaPhiMTb = bjet1.phi - METcorrected_phi
            deltaPhiMTb_puppi = bjet1.phi - event.PuppiMET_phi
            M_Tb = math.sqrt(2 * METcorrected_pt * bjet1.pt * (1 - math.cos(deltaPhiMTb)))
            M_Tb_puppi = math.sqrt(2 * event.PuppiMET_pt * bjet1.pt * (1 - math.cos(deltaPhiMTb_puppi)))

        #Systematics - JES, JER
        if nbjetsScaleUp > 0:
            bjetScaleUp1 = bJetsScaleUp[0]
            for bjetScaleUp in bJetsScaleUp:
                bjetVectorScaleUp.push_back(bjetScaleUp.p4()*(bjetScaleUp.pt_jesTotalUp/bjetScaleUp.pt_nom))
                if self.btag == 'CSVv2':
                    bjetScaleUp_btag = bjetScaleUp.btagCSVV2
                    bjetScaleUp1_btag = bjetScaleUp1.btagCSVV2
                elif self.btag == 'DeepCSV':
                    bjetScaleUp_btag = bjetScaleUp.btagDeepB
                    bjetScaleUp1_btag = bjetScaleUp1.btagDeepB
                if bjetScaleUp_btag > bjetScaleUp1_btag:
                    bjetScaleUp1 = bjetScaleUp

            deltaPhiMTbScaleUp = bjetScaleUp1.phi - METcorrected_phiScaleUp
            M_TbScaleUp = math.sqrt(2 * METcorrected_ptScaleUp * bjetScaleUp1.pt_nom * (1 - math.cos(deltaPhiMTbScaleUp)))

        if nbjetsScaleDown > 0:
            bjetScaleDown1 = bJetsScaleDown[0]
            for bjetScaleDown in bJetsScaleDown:
                bjetVectorScaleDown.push_back(bjetScaleDown.p4()*(bjetScaleDown.pt_jesTotalDown/bjetScaleDown.pt_nom))
                if self.btag == 'CSVv2':
                    bjetScaleDown_btag = bjetScaleDown.btagCSVV2
                    bjetScaleDown1_btag = bjetScaleDown1.btagCSVV2
                elif self.btag == 'DeepCSV':
                    bjetScaleDown_btag = bjetScaleDown.btagDeepB
                    bjetScaleDown1_btag = bjetScaleDown1.btagDeepB
                if bjetScaleDown_btag > bjetScaleDown1_btag:
                    bjetScaleDown1 = bjetScaleDown

            deltaPhiMTbScaleDown = bjetScaleDown1.phi - METcorrected_phiScaleDown
            M_TbScaleDown = math.sqrt(2 * METcorrected_ptScaleDown * bjetScaleDown1.pt_nom * (1 - math.cos(deltaPhiMTbScaleDown)))

        if nbjetsResUp > 0:
            bjetResUp1 = bJetsResUp[0]
            for bjetResUp in bJetsResUp:
                if self.isMC:
                    bjetVectorResUp.push_back(bjetResUp.p4()*(bjetResUp.pt_jerUp/bjetResUp.pt_nom))
                else:
                    bjetVectorResUp.push_back(bjetResUp.p4())
                if self.btag == 'CSVv2':
                    bjetResUp_btag = bjetResUp.btagCSVV2
                    bjetResUp1_btag = bjetResUp1.btagCSVV2
                elif self.btag == 'DeepCSV':
                    bjetResUp_btag = bjetResUp.btagDeepB
                    bjetResUp1_btag = bjetResUp1.btagDeepB
                if bjetResUp_btag > bjetResUp1_btag:
                    bjetResUp1 = bjetResUp

            deltaPhiMTbResUp = bjetResUp1.phi - METcorrected_phiResUp
            M_TbResUp = math.sqrt(2 * METcorrected_ptResUp * bjetResUp1.pt_nom * (1 - math.cos(deltaPhiMTbResUp)))

        if nbjetsResDown > 0:
            bjetResDown1 = bJetsResDown[0]
            for bjetResDown in bJetsResDown:
                if self.isMC:
                    bjetVectorResDown.push_back(bjetResDown.p4()*(bjetResDown.pt_jerDown/bjetResDown.pt_nom))
                else:
                    bjetVectorResDown.push_back(bjetResDown.p4())
                if self.btag == 'CSVv2':
                    bjetResDown_btag = bjetResDown.btagCSVV2
                    bjetResDown1_btag = bjetResDown1.btagCSVV2
                elif self.btag == 'DeepCSV':
                    bjetResDown_btag = bjetResDown.btagDeepB
                    bjetResDown1_btag = bjetResDown1.btagDeepB
                if bjetResDown_btag > bjetResDown1_btag:
                    bjetResDown1 = bjetResDown
            
            deltaPhiMTbResDown = bjetResDown1.phi - METcorrected_phiResDown
            M_TbResDown = math.sqrt(2 * METcorrected_ptResDown * bjetResDown1.pt_nom * (1 - math.cos(deltaPhiMTbResDown)))

        #Calculate M_T, M_T2^W, and M_T2^ll using PFMET
        M_T = M_T2W = M_T2ll = M_T_puppi = M_T2W_puppi = M_T2ll_puppi = -9 #If there are not enough tight leptons, set value to -9 to indicate variable cannot be calculated
        #Systematics - JES, JER
        M_TScaleUp = M_TScaleDown = M_TResUp = M_TResDown = -9
        M_T2WScaleUp = M_T2WScaleDown = M_T2WResUp = M_T2WResDown = -9
        M_T2llScaleUp = M_T2llScaleDown = M_T2llResUp = M_T2llResDown = -9

        if nTightElectrons > 0 or nTightMuons > 0: #Default to using electron if both tight electron and muon exist
            if nTightElectrons > 0:
                lepton = tightElectrons[0] #Default to using tight electron with greatest pT
            elif nTightMuons > 0:
                lepton = tightMuons[0] #Default to using tight muon with greatest pT

            #Calculate M_T
            deltaPhiMT = lepton.phi - METcorrected_phi
            deltaPhiMT_puppi = lepton.phi - event.PuppiMET_phi
            M_T = math.sqrt(2 * METcorrected_pt * lepton.pt * (1 - math.cos(deltaPhiMT)))
            M_T_puppi = math.sqrt(2 * event.PuppiMET_pt * lepton.pt * (1 - math.cos(deltaPhiMT_puppi)))
            #Systematics - JES, JER
            deltaPhiMTScaleUp = lepton.phi - METcorrected_phiScaleUp
            M_TScaleUp = math.sqrt(2 * METcorrected_ptScaleUp * lepton.pt * (1 - math.cos(deltaPhiMTScaleUp)))
            deltaPhiMTScaleDown = lepton.phi - METcorrected_phiScaleDown
            M_TScaleDown = math.sqrt(2 * METcorrected_ptScaleDown * lepton.pt * (1 - math.cos(deltaPhiMTScaleDown)))
            deltaPhiMTResUp = lepton.phi - METcorrected_phiResUp
            M_TResUp = math.sqrt(2 * METcorrected_ptResUp * lepton.pt * (1 - math.cos(deltaPhiMTResUp)))
            deltaPhiMTResDown = lepton.phi - METcorrected_phiResDown
            M_TResDown = math.sqrt(2 * METcorrected_ptResDown * lepton.pt * (1 - math.cos(deltaPhiMTResDown)))

            #Calculate M_T2^W 
            leptonTLorentz = lepton.p4()
            metTVector2 = ROOT.TVector2(METcorrected_pt * math.cos(METcorrected_phi), METcorrected_pt * math.sin(METcorrected_phi))
            PuppimetTVector2 = ROOT.TVector2(event.PuppiMET_pt * math.cos(event.PuppiMET_phi), event.PuppiMET_pt * math.sin(event.PuppiMET_phi))
            M_T2W = Mt2Com_bisect.calculateMT2w(ljetVector, bjetVector, leptonTLorentz, metTVector2, "MT2w")
            M_T2W_puppi = Mt2Com_bisect.calculateMT2w(ljetVector, bjetVector, leptonTLorentz, PuppimetTVector2, "MT2w")
            #Systematics - JES, JER
            metTVector2ScaleUp = ROOT.TVector2(METcorrected_ptScaleUp * math.cos(METcorrected_phiScaleUp), METcorrected_ptScaleUp * math.sin(METcorrected_phiScaleUp))
            M_T2WScaleUp = Mt2Com_bisect.calculateMT2w(ljetVectorScaleUp, bjetVectorScaleUp, leptonTLorentz, metTVector2ScaleUp, "MT2w")
            metTVector2ScaleDown = ROOT.TVector2(METcorrected_ptScaleDown * math.cos(METcorrected_phiScaleDown), METcorrected_ptScaleDown * math.sin(METcorrected_phiScaleDown))
            M_T2WScaleDown = Mt2Com_bisect.calculateMT2w(ljetVectorScaleDown, bjetVectorScaleDown, leptonTLorentz, metTVector2ScaleDown, "MT2w")
            metTVector2ResUp = ROOT.TVector2(METcorrected_ptResUp * math.cos(METcorrected_phiResUp), METcorrected_ptResUp * math.sin(METcorrected_phiResUp))
            M_T2WResUp = Mt2Com_bisect.calculateMT2w(ljetVectorResUp, bjetVectorResUp, leptonTLorentz, metTVector2ResUp, "MT2w")
            metTVector2ResDown = ROOT.TVector2(METcorrected_ptResDown * math.cos(METcorrected_phiResDown), METcorrected_ptResDown * math.sin(METcorrected_phiResDown))
            M_T2WResDown = Mt2Com_bisect.calculateMT2w(ljetVectorResDown, bjetVectorResDown, leptonTLorentz, metTVector2ResDown, "MT2w")
            
        if nTightElectrons + nTightMuons == 2:
            if nTightElectrons == 2:
                VisibleA = tightElectrons[0].p4()
                VisibleB = tightElectrons[1].p4()
            elif nTightMuons == 2:
                VisibleA = tightMuons[0].p4()
                VisibleB = tightMuons[1].p4()
            else:
                VisibleA = tightElectrons[0].p4()
                VisibleB = tightMuons[0].p4()
            
            #Calculate M_T2^ll
            mVisA = abs(VisibleA.M()) #Mass of visible object on side A. Must be >= 0
            mVisB = abs(VisibleB.M()) #Mass of visible object on side B. Must be >= 0
            
            chiA = 0. #Hypothesized mass of invisible on side A. Must be >= 0
            chiB = 0. #Hypothesized mass of invisible on side B. Must be >= 0

            pxA = VisibleA.Px() #x momentum of visible object on side A
            pyA = VisibleA.Py() #y momentum of visible object on side A
            
            pxB = VisibleB.Px() #x momentum of visible object on side B
            pyB = VisibleB.Py() #y momentum of visible object on side B

            pxMiss = METcorrected_pt*math.cos(METcorrected_phi) #x component of missing transverse momentum
            pyMiss = METcorrected_pt*math.sin(METcorrected_phi) #y component of missing transverse momentum
            
            pxMiss_puppi = event.PuppiMET_pt*math.cos(event.PuppiMET_phi) #x component of Puppi missing transverse momentum
            pyMiss_puppi = event.PuppiMET_pt*math.sin(event.PuppiMET_phi) #y component of Puppi missing transverse momentum

            desiredPrecisionOnM_T2ll = 0 #Must be >= 0. If = 0 algorithm aims for machine precision. If > 0 MT2 computed to supplied absolute precision

            M_T2ll = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMiss,pyMiss,chiA,chiB,desiredPrecisionOnM_T2ll)
            M_T2ll_puppi = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMiss_puppi,pyMiss_puppi,chiA,chiB,desiredPrecisionOnM_T2ll)

            #Systematics - JES, JER
            pxMissScaleUp = METcorrected_ptScaleUp*math.cos(METcorrected_phiScaleUp)
            pyMissScaleUp = METcorrected_ptScaleUp*math.sin(METcorrected_phiScaleUp)
            pxMissScaleDown = METcorrected_ptScaleDown*math.cos(METcorrected_phiScaleDown)
            pyMissScaleDown = METcorrected_ptScaleDown*math.sin(METcorrected_phiScaleDown)
            pxMissResUp = METcorrected_ptResUp*math.cos(METcorrected_phiResUp)
            pyMissResUp = METcorrected_ptResUp*math.sin(METcorrected_phiResUp)
            pxMissResDown = METcorrected_ptResDown*math.cos(METcorrected_phiResDown)
            pyMissResDown = METcorrected_ptResDown*math.sin(METcorrected_phiResDown)

            M_T2llScaleUp = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMissScaleUp,pyMissScaleUp,chiA,chiB,desiredPrecisionOnM_T2ll)
            M_T2llScaleDown = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMissScaleDown,pyMissScaleDown,chiA,chiB,desiredPrecisionOnM_T2ll)
            M_T2llResUp = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMissResUp,pyMissResUp,chiA,chiB,desiredPrecisionOnM_T2ll)
            M_T2llResDown = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMissResDown,pyMissResDown,chiA,chiB,desiredPrecisionOnM_T2ll)
        
        #Tau candidates are counted
        tauCandidates = Collection(event, "Tau")
        if self.isSignal and self.year == 2016:
            skimmedTaus = filter(lambda tau : tau.pt > 20 and abs(tau.eta) < 2.3 and tau.idMVAoldDM >= 31 and cleanJet(tau), tauCandidates)
        else:
            skimmedTaus = filter(lambda tau : tau.pt > 20 and abs(tau.eta) < 2.3 and tau.idMVAoldDM2017v2 >= 31 and cleanJet(tau), tauCandidates)
        ntaus = len(skimmedTaus)

        #Determine if there exists two tight electrons/muons such that their invariant mass m_ll is between 60-120 GeV and the hadronic recoil >= 250 GeV
        m_llExists = m_llExists_puppi = False
        m_ll = 0
        recoilPtMiss = recoilPtMiss_puppi = 0
        lepton1_charge = lepton2_charge = 0
        #Systematics - JES, JER
        m_llExistsScaleUp = m_llExistsScaleDown = m_llExistsResUp = m_llExistsResDown = False
        recoilPtMissScaleUp = recoilPtMissScaleDown = recoilPtMissResUp = recoilPtMissResDown = 0

        #Only calculate m_ll and recoilPtMiss when two tight leptons exis (2e, 2m, or 1e1m)
        if (nTightElectrons >= 2 and nLooseMuons == 0) or (nVetoElectrons == 0 and nTightMuons >= 2):
            if nTightElectrons >= 2:
                tightLeptons = tightElectrons
            elif nTightMuons >= 2:
                tightLeptons = tightMuons
            lepton1 = tightLeptons[0]
            lepton2 = tightLeptons[1]
            eventSum = lepton1.p4() + lepton2.p4()
            m_ll = eventSum.M()

            recoilPtMiss = math.sqrt(pow(METcorrected_pt*math.cos(METcorrected_phi) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(METcorrected_pt*math.sin(METcorrected_phi) + lepton1.p4().Py() + lepton2.p4().Py(), 2))
            recoilPtMiss_puppi = math.sqrt(pow(event.PuppiMET_pt*math.cos(event.PuppiMET_phi) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(event.PuppiMET_pt*math.sin(event.PuppiMET_phi) + lepton1.p4().Py() + lepton2.p4().Py(), 2))

            lepton1_charge = lepton1.charge
            lepton2_charge = lepton2.charge

            if 60 <= m_ll <= 120 and recoilPtMiss >= 250 and lepton1.charge == -lepton2.charge:
                m_llExists = True  
            if 60 <= m_ll <= 120 and recoilPtMiss_puppi >= 250 and lepton1.charge == -lepton2.charge:
                m_llExists_puppi = True

            #Systematics - JES, JER
            recoilPtMissScaleUp = math.sqrt(pow(METcorrected_ptScaleUp*math.cos(METcorrected_phiScaleUp) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(METcorrected_ptScaleUp*math.sin(METcorrected_phiScaleUp) + lepton1.p4().Py() + lepton2.p4().Py(), 2))
            recoilPtMissScaleDown = math.sqrt(pow(METcorrected_ptScaleDown*math.cos(METcorrected_phiScaleDown) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(METcorrected_ptScaleDown*math.sin(METcorrected_phiScaleDown) + lepton1.p4().Py() + lepton2.p4().Py(), 2))
            recoilPtMissResUp = math.sqrt(pow(METcorrected_ptResUp*math.cos(METcorrected_phiResUp) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(METcorrected_ptResUp*math.sin(METcorrected_phiResUp) + lepton1.p4().Py() + lepton2.p4().Py(), 2))
            recoilPtMissResDown = math.sqrt(pow(METcorrected_ptResDown*math.cos(METcorrected_phiResDown) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(METcorrected_ptResDown*math.sin(METcorrected_phiResDown) + lepton1.p4().Py() + lepton2.p4().Py(), 2))

            if 60 <= m_ll <= 120 and recoilPtMissScaleUp >= 250 and lepton1.charge == -lepton2.charge:
                m_llExistsScaleUp = True
            if 60 <= m_ll <= 120 and recoilPtMissScaleDown >= 250 and lepton1.charge == -lepton2.charge:
                m_llExistsScaleDown = True 
            if 60 <= m_ll <= 120 and recoilPtMissResUp >= 250 and lepton1.charge == -lepton2.charge:
                m_llExistsResUp = True 
            if 60 <= m_ll <= 120 and recoilPtMissResDown >= 250 and lepton1.charge == -lepton2.charge:
                m_llExistsResDown = True 

        #Only calculate scale factors if sample is MC
        if self.isMC:

            #Calculate PDF up/down systematics 
            pdfWeights = [event.LHEPdfWeight[i] for i in range(event.nLHEPdfWeight)]
            pdfMean = sum(pdfWeights)/event.nLHEPdfWeight
            pdfSquareSum = sum(i*i for i in pdfWeights)
            pdfRMS = math.sqrt(pdfSquareSum/event.nLHEPdfWeight - pdfMean*pdfMean)
            pdfWeightUp = 1 + pdfRMS
            pdfWeightDown = 1 - pdfRMS

            #Get QCD renormalization and factorization scale weight systematics (see [1] for more info)
            #[1] https://hypernews.cern.ch/HyperNews/CMS/get/physTools/3663.html?inline=-1
            qcdRenWeightUp = event.LHEScaleWeight[7]
            qcdRenWeightDown = event.LHEScaleWeight[1]
            qcdFacWeightUp = event.LHEScaleWeight[5]
            qcdFacWeightDown = event.LHEScaleWeight[3]

            #Calculate lepton scale factor weight
            leptonWeight = leptonWeightUp = leptonWeightDown = 1
            for tightElectron in tightElectrons:
                leptonWeight *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, 0)
                leptonWeightUp *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, 1)
                leptonWeightDown *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, -1)
            for tightMuon in tightMuons:
                leptonWeight *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, 0)
                leptonWeightUp *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, 1)
                leptonWeightDown *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, -1)

            #Calculate b-jet scale factor weight
            bjetWeight = self.btagTool.getWeight(centralJets)
            bjetWeightUp = self.btagToolUp.getWeight(centralJets)
            bjetWeightDown = self.btagToolDown.getWeight(centralJets)

            #Calculate PU weight
            puWeight = self.puTool.getWeight(event.Pileup_nTrueInt)
            puWeightUp = self.puToolUp.getWeight(event.Pileup_nTrueInt)
            puWeightDown = self.puToolDown.getWeight(event.Pileup_nTrueInt)

            #Calculate EWK and QCD k factors if a Gen V particles exists (Z or W)
            ewkWWeight = ewkZWeight = qcdWWeight = qcdZTo2NuWeight = qcdZTo2LWeight = 1
            qcdWWeightRenUp = qcdWWeightRenDown = qcdWWeightFacUp = qcdWWeightFacDown = qcdZWeightRenUp = qcdZWeightRenDown = qcdZWeightFacUp = qcdZWeightFacDown = 1
            genParticles = Collection(event, "GenPart")
            GenV = filter(lambda gen : (gen.pdgId == 23 or abs(gen.pdgId) == 24) and gen.status == 22, genParticles)
            if len(GenV) > 0:
                GenV_pt = GenV[0].pt
                ewkWWeight *= self.kFactorTool.getEWKW(GenV_pt)
                ewkZWeight *= self.kFactorTool.getEWKZ(GenV_pt)
                qcdWWeight *= self.kFactorTool.getQCDW(GenV_pt)
                qcdZTo2NuWeight *= self.kFactorTool.getQCDZTo2Nu(GenV_pt)
                qcdZTo2LWeight *= self.kFactorTool.getQCDZTo2L(GenV_pt)
                qcdWWeightRenUp *= self.kFactorTool.getRenUpW(GenV_pt)
                qcdWWeightRenDown *= self.kFactorTool.getRenDownW(GenV_pt)
                qcdWWeightFacUp *= self.kFactorTool.getFacUpW(GenV_pt)
                qcdWWeightFacDown *= self.kFactorTool.getFacDownW(GenV_pt)
                qcdZWeightRenUp *= self.kFactorTool.getRenUpZ(GenV_pt)
                qcdZWeightRenDown *= self.kFactorTool.getRenDownZ(GenV_pt)
                qcdZWeightFacUp *= self.kFactorTool.getFacUpZ(GenV_pt)
                qcdZWeightFacDown *= self.kFactorTool.getFacDownZ(GenV_pt)

        #Define MET filters contained in miniAOD analysis (https://github.com/zucchett/SFrame/blob/master/DM/src/DMSearches.cxx#L1542)
        # passMETfilters = event.Flag_goodVertices and event.Flag_HBHENoiseFilter and event.Flag_HBHENoiseIsoFilter and event.Flag_EcalDeadCellTriggerPrimitiveFilter and event.Flag_eeBadScFilter and event.Flag_globalTightHalo2016Filter and event.Flag_BadPFMuonFilter and event.Flag_chargedHadronTrackResolutionFilter

        #Define SingleIsoEle, SingleEle, and SingleIsoMu filters contained in miniAOD analysis (https://github.com/zucchett/SFrame/blob/master/DM/src/DMSearches.cxx#L112)
        # singleIsoEle = event.HLT_Ele27_eta2p1_WPTight_Gsf or event.HLT_Ele27_WPLoose_Gsf or event.HLT_Ele27_WPTight_Gsf or event.HLT_Ele32_eta2p1_WPTight_Gsf #or event.HLT_Ele32_WPTight_Gsf 
        # singleEle = event.HLT_Ele105_CaloIdVT_GsfTrkIdT or event.HLT_Ele115_CaloIdVT_GsfTrkIdT
        # singleIsoMu = event.HLT_IsoMu27 or event.HLT_IsoTkMu27 or event.HLT_IsoMu24 or event.HLT_IsoTkMu24

        #Preselection cuts defined here
        # SL1e = nTightElectrons == 1 and nVetoElectrons == 1 and nLooseMuons == 0 and njets >= 2 and nbjets >= 1 and event.MET_pt >= 160 and passMETfilters and (singleIsoEle or singleEle)
        # SL1m = nTightMuons == 1 and nLooseMuons == 1 and nVetoElectrons == 0 and njets >= 2 and nbjets >= 1 and event.MET_pt >= 160 and passMETfilters and singleIsoMu
        # AH = (nVetoElectrons + nLooseMuons) == 0 and njets >= 3 and nbjets >= 1 and event.MET_pt >= 250  and ntaus == 0 and minDeltaPhi > 0.4 and jet1_jetId >= 3 and jet1_chHEF > 0.1 and passMETfilters

        # SL1e = nTightElectrons == 1 and nVetoElectrons == 1 and nLooseMuons == 0 and njets >= 2 and event.MET_pt >= 160 and passMETfilters and (singleIsoEle or singleEle)
        # SL1m = nTightMuons == 1 and nLooseMuons == 1 and nVetoElectrons == 0 and njets >= 2 and event.MET_pt >= 160 and passMETfilters and singleIsoMu
        # AH = (nVetoElectrons + nLooseMuons) == 0 and njets >= 3 and event.MET_pt >= 250 and ntaus == 0 and minDeltaPhi > 0.4 and centralJets[0].jetId >= 3 and centralJets[0].chHEF > 0.1 and passMETfilters
        # SL = SL1e and M_T >= 160 and nbjets >= 2

        # SL1e0fSR = SL1e and nbjets == 1 and nfjets == 0
        # SL1m0fSR = SL1m and nbjets == 1 and nfjets == 0
        # SL1e1fSR = SL1e and nbjets == 1 and nfjets >= 1 
        # SL1m1fSR = SL1m and nbjets == 1 and nfjets >= 1 
        # SL1e2bSR = SL1e and nbjets >= 2 
        # SL1m2bSR = SL1m and nbjets >= 2 
        # AH0l0fSR = AH and nbjets == 1 and nfjets == 0
        # AH0l1fSR = AH and nbjets == 1 and nfjets >= 1
        # AH0l2bSR = AH and nbjets >= 2

        #Define skimming cuts to be applied
        Skim = (nTightElectrons + nTightMuons) <= 1 and nbjets >= 1 and njets >= 2 and event.MET_pt > 100 

        #Signal region chosen here
        if self.signalRegion == "All":
            signalRegion = True
        elif self.signalRegion == "Skim":
            signalRegion = Skim
        # elif self.signalRegion == "SL1e0fSR":
        #     signalRegion = SL1e0fSR
        # elif self.signalRegion == "SL1m0fSR":
        #     signalRegion = SL1m0fSR
        # elif self.signalRegion == "SL1e1fSR":
        #     signalRegion = SL1e1fSR
        # elif self.signalRegion == "SL1m1fSR":
        #     signalRegion = SL1m1fSR
        # elif self.signalRegion == "SL1e2bSR":
        #     signalRegion = SL1e2bSR
        # elif self.signalRegion == "SL1m2bSR":
        #     signalRegion = SL1m2bSR
        # elif self.signalRegion == "AH0l0fSR":
        #     signalRegion = AH0l0fSR
        # elif self.signalRegion == "AH0l1fSR":
        #     signalRegion = AH0l1fSR
        # elif self.signalRegion == "AH0l2bSR":
        #     signalRegion = AH0l2bSR
        # elif self.signalRegion == "SL1e":
        #     signalRegion = SL1e
        # elif self.signalRegion == "SL1m":
        #     signalRegion = SL1m
        # elif self.signalRegion == "AH":
        #     signalRegion = AH
        # elif self.signalRegion == "SL":
        #     signalRegion = SL
        else:
            signalRegion = False

        if signalRegion: #True if event satisfies all selection cuts for specified signal region
            #fill output branches
            self.out.fillBranch("nTightElectrons", nTightElectrons)
            self.out.fillBranch("nVetoElectrons", nVetoElectrons)
            self.out.fillBranch("nTightMuons", nTightMuons)
            self.out.fillBranch("nLooseMuons", nLooseMuons)
            self.out.fillBranch("tightElectron1_charge", tightElectron1_charge)
            self.out.fillBranch("tightMuon1_charge", tightMuon1_charge)

            self.out.fillBranch("njets", njets)
            self.out.fillBranch("nfjets", nfjets)
            self.out.fillBranch("nbjets", nbjets)

            self.out.fillBranch("METcorrected_pt", METcorrected_pt)
            self.out.fillBranch("METcorrected_phi", METcorrected_phi)

            self.out.fillBranch("minDeltaPhi", minDeltaPhi)
            self.out.fillBranch("minDeltaPhi12", minDeltaPhi12)
            self.out.fillBranch("M_Tb", M_Tb)
            self.out.fillBranch("M_T", M_T)
            self.out.fillBranch("M_T2W", M_T2W)
            self.out.fillBranch("M_T2ll", M_T2ll)
            self.out.fillBranch("jet1p_TH_T", jet1p_TH_T)
            self.out.fillBranch("jet1_jetId", jet1_jetId)
            self.out.fillBranch("jet1_chHEF", jet1_chHEF)
            self.out.fillBranch("ntaus", ntaus)
            self.out.fillBranch("m_llExists", m_llExists)
            self.out.fillBranch("m_ll", m_ll)
            self.out.fillBranch("recoilPtMiss", recoilPtMiss)

            self.out.fillBranch("minDeltaPhi_puppi", minDeltaPhi_puppi)
            self.out.fillBranch("minDeltaPhi12_puppi", minDeltaPhi12_puppi)
            self.out.fillBranch("M_Tb_puppi", M_Tb_puppi)
            self.out.fillBranch("M_T_puppi", M_T_puppi)
            self.out.fillBranch("M_T2W_puppi", M_T2W_puppi)
            self.out.fillBranch("M_T2ll_puppi", M_T2ll_puppi)
            self.out.fillBranch("m_llExists_puppi", m_llExists_puppi)
            self.out.fillBranch("recoilPtMiss_puppi", recoilPtMiss_puppi)

            self.out.fillBranch("lepton1_charge", lepton1_charge)
            self.out.fillBranch("lepton2_charge", lepton2_charge)

            self.out.fillBranch("index_vetoElectrons", index_vetoElectrons)
            self.out.fillBranch("index_tightElectrons", index_tightElectrons)
            self.out.fillBranch("index_looseMuons", index_looseMuons)
            self.out.fillBranch("index_tightMuons", index_tightMuons)
            self.out.fillBranch("index_centralJets", index_centralJets)
            self.out.fillBranch("index_forwardJets", index_forwardJets)
            self.out.fillBranch("index_bJets", index_bJets)

            #Systematics - JES, JER
            self.out.fillBranch("njetsScaleUp", njetsScaleUp)
            self.out.fillBranch("njetsScaleDown", njetsScaleDown)
            self.out.fillBranch("njetsResUp", njetsResUp)
            self.out.fillBranch("njetsResDown", njetsResDown)
            
            self.out.fillBranch("nfjetsScaleUp", nfjetsScaleUp)
            self.out.fillBranch("nfjetsScaleDown", nfjetsScaleDown)
            self.out.fillBranch("nfjetsResUp", nfjetsResUp)
            self.out.fillBranch("nfjetsResDown", nfjetsResDown)

            self.out.fillBranch("nbjetsScaleUp", nbjetsScaleUp)
            self.out.fillBranch("nbjetsScaleDown", nbjetsScaleDown)
            self.out.fillBranch("nbjetsResUp", nbjetsResUp)
            self.out.fillBranch("nbjetsResDown", nbjetsResDown)

            self.out.fillBranch("METcorrected_ptScaleUp", METcorrected_ptScaleUp)
            self.out.fillBranch("METcorrected_ptScaleDown", METcorrected_ptScaleDown)
            self.out.fillBranch("METcorrected_ptResUp", METcorrected_ptResUp)
            self.out.fillBranch("METcorrected_ptResDown", METcorrected_ptResDown)
            self.out.fillBranch("METcorrected_phiScaleUp", METcorrected_phiScaleUp)
            self.out.fillBranch("METcorrected_phiScaleDown", METcorrected_phiScaleDown)
            self.out.fillBranch("METcorrected_phiResUp", METcorrected_phiResUp)
            self.out.fillBranch("METcorrected_phiResDown", METcorrected_phiResDown)
            
            self.out.fillBranch("minDeltaPhiScaleUp", minDeltaPhiScaleUp)
            self.out.fillBranch("minDeltaPhiScaleDown", minDeltaPhiScaleDown)
            self.out.fillBranch("minDeltaPhiResUp", minDeltaPhiResUp)
            self.out.fillBranch("minDeltaPhiResDown", minDeltaPhiResDown)
            
            self.out.fillBranch("minDeltaPhi12ScaleUp", minDeltaPhi12ScaleUp)
            self.out.fillBranch("minDeltaPhi12ScaleDown", minDeltaPhi12ScaleDown)
            self.out.fillBranch("minDeltaPhi12ResUp", minDeltaPhiResUp)
            self.out.fillBranch("minDeltaPhi12ResDown", minDeltaPhiResDown)
            
            self.out.fillBranch("M_TbScaleUp", M_TbScaleUp)
            self.out.fillBranch("M_TbScaleDown", M_TbScaleDown)
            self.out.fillBranch("M_TbResUp", M_TbResUp)
            self.out.fillBranch("M_TbResDown", M_TbResDown)
            
            self.out.fillBranch("M_TScaleUp", M_TScaleUp)
            self.out.fillBranch("M_TScaleDown", M_TScaleDown)
            self.out.fillBranch("M_TResUp", M_TResUp)
            self.out.fillBranch("M_TResDown", M_TResDown)
            
            self.out.fillBranch("M_T2WScaleUp", M_T2WScaleUp)
            self.out.fillBranch("M_T2WScaleDown", M_T2WScaleDown)
            self.out.fillBranch("M_T2WResUp", M_T2WResUp)
            self.out.fillBranch("M_T2WResDown", M_T2WResDown)
            
            self.out.fillBranch("M_T2llScaleUp", M_T2llScaleUp)
            self.out.fillBranch("M_T2llScaleDown", M_T2llScaleDown)
            self.out.fillBranch("M_T2llResUp", M_T2llResUp)
            self.out.fillBranch("M_T2llResDown", M_T2llResDown)
            
            self.out.fillBranch("jet1p_TH_TScaleUp", jet1p_TH_TScaleUp)
            self.out.fillBranch("jet1p_TH_TScaleDown", jet1p_TH_TScaleDown)
            self.out.fillBranch("jet1p_TH_TResUp", jet1p_TH_TResUp)
            self.out.fillBranch("jet1p_TH_TResDown", jet1p_TH_TResDown)

            self.out.fillBranch("jet1_chHEFScaleUp", jet1_chHEFScaleUp)
            self.out.fillBranch("jet1_chHEFScaleDown", jet1_chHEFScaleDown)
            self.out.fillBranch("jet1_chHEFResUp", jet1_chHEFResUp)
            self.out.fillBranch("jet1_chHEFResDown", jet1_chHEFResDown)
            
            self.out.fillBranch("m_llExistsScaleUp", m_llExistsScaleUp)
            self.out.fillBranch("m_llExistsScaleDown", m_llExistsScaleDown)
            self.out.fillBranch("m_llExistsResUp", m_llExistsResUp)
            self.out.fillBranch("m_llExistsResDown", m_llExistsResDown)
            
            self.out.fillBranch("recoilPtMissScaleUp", recoilPtMissScaleUp)
            self.out.fillBranch("recoilPtMissScaleDown", recoilPtMissScaleDown)
            self.out.fillBranch("recoilPtMissResUp", recoilPtMissResUp)
            self.out.fillBranch("recoilPtMissResDown", recoilPtMissResDown)
            
            if self.isMC:
                #Systematics - PDF
                self.out.fillBranch("pdfWeightUp", pdfWeightUp)
                self.out.fillBranch("pdfWeightDown", pdfWeightDown)

                #Systematics - QCD Renormalization and Factorization scales
                self.out.fillBranch("qcdRenWeightUp", qcdRenWeightUp)
                self.out.fillBranch("qcdRenWeightDown", qcdRenWeightDown)
                self.out.fillBranch("qcdFacWeightUp", qcdFacWeightUp)
                self.out.fillBranch("qcdFacWeightDown", qcdFacWeightDown)

                self.out.fillBranch("leptonWeight", leptonWeight)
                #Systematics - lepton weights
                self.out.fillBranch("leptonWeightUp", leptonWeightUp)
                self.out.fillBranch("leptonWeightDown", leptonWeightDown)

                self.out.fillBranch("bjetWeight", bjetWeight)
                #Systematics - b-tag weights
                self.out.fillBranch("bjetWeightUp",bjetWeightUp)
                self.out.fillBranch("bjetWeightDown",bjetWeightDown)

                self.out.fillBranch("puWeight", puWeight)
                #Systematics - Pile-up
                self.out.fillBranch("puWeightUp", puWeightUp)
                self.out.fillBranch("puWeightDown", puWeightDown)

                self.out.fillBranch("ewkWWeight", ewkWWeight)
                self.out.fillBranch("ewkZWeight", ewkZWeight)
                self.out.fillBranch("qcdWWeight", qcdWWeight)
                self.out.fillBranch("qcdZTo2NuWeight", qcdZTo2NuWeight)
                self.out.fillBranch("qcdZTo2LWeight", qcdZTo2LWeight)
                #Systematics - QCD Scale Factors
                self.out.fillBranch("qcdWWeightRenUp", qcdWWeightRenUp)
                self.out.fillBranch("qcdWWeightRenDown", qcdWWeightRenDown)
                self.out.fillBranch("qcdWWeightFacUp", qcdWWeightFacUp)
                self.out.fillBranch("qcdWWeightFacDown", qcdWWeightFacDown)
                self.out.fillBranch("qcdZWeightRenUp", qcdZWeightRenUp)
                self.out.fillBranch("qcdZWeightRenDown", qcdZWeightRenDown)
                self.out.fillBranch("qcdZWeightFacUp", qcdZWeightFacUp)
                self.out.fillBranch("qcdZWeightFacDown", qcdZWeightFacDown)
            return True
        else:
            return False

        #return True

#Define CommonAnalysis cmodules for all years (Data and MC)
analyze2016MC = lambda : CommonAnalysis("All",year=2016,isData=False,isSignal=False,btag='DeepCSV')
analyze2016SignalMC = lambda : CommonAnalysis("All",year=2016,isData=False,isSignal=True,btag='DeepCSV')
analyze2016Data = lambda : CommonAnalysis("All",year=2016,isData=True,isSignal=False,btag='DeepCSV')

analyze2016MC_Skim = lambda : CommonAnalysis("Skim",year=2016,isData=False,isSignal=False,btag='DeepCSV')
analyze2016SignalMC_Skim = lambda : CommonAnalysis("Skim",year=2016,isData=False,isSignal=True,btag='DeepCSV')
analyze2016Data_Skim = lambda : CommonAnalysis("Skim",year=2016,isData=True,isSignal=False,btag='DeepCSV')

analyze2017MC = lambda : CommonAnalysis("All",year=2017,isData=False,isSignal=False,btag='DeepCSV')
analyze2017SignalMC = lambda : CommonAnalysis("All",year=2017,isData=False,isSignal=True,btag='DeepCSV')
analyze2017Data = lambda : CommonAnalysis("All",year=2017,isData=True,isSignal=False,btag='DeepCSV')

analyze2018MC = lambda : CommonAnalysis("All",year=2018,isData=False,isSignal=False,btag='DeepCSV')
analyze2018SignalMC = lambda : CommonAnalysis("All",year=2018,isData=False,isSignal=True,btag='DeepCSV')
analyze2018Data = lambda : CommonAnalysis("All",year=2018,isData=True,isSignal=False,btag='DeepCSV')

#Define jetmetHelperRun2 modules for all years to calculate systematic uncertanties
jetmetCorrector2016MC = createJMECorrector(isMC=True, dataYear=2016, jesUncert="Total")
jetmetCorrector2016Data = createJMECorrector(isMC=False, dataYear=2016, jesUncert="Total")

jetmetCorrector2017MC = createJMECorrector(isMC=True, dataYear=2017, jesUncert="Total", metBranchName="METFixEE2017")
jetmetCorrector2017Data = createJMECorrector(isMC=False, dataYear=2017, jesUncert="Total", metBranchName="METFixEE2017")

jetmetCorrector2018MC = createJMECorrector(isMC=True, dataYear=2018, jesUncert="Total", applyHEMfix=True)
jetmetCorrector2018Data = createJMECorrector(isMC=False, dataYear=2018, jesUncert="Total", applyHEMfix=True)

#########################################################################################################################################

if runLocal:
    #Select PostProcessor options here
    selection=None
    #outputDir = "outDir2016AnalysisSR/ttbarDM/"
    #outputDir = "testSamples/"
    outputDir = "."
    #inputbranches="python/postprocessing/analysis/keep_and_dropSR_in.txt"
    outputbranches="python/postprocessing/analysis/keep_and_dropSR_out.txt"
    #inputFiles=["samples/ttbarDM_Mchi1Mphi100_scalar_full1.root"]#,"samples/ttbarDM_Mchi1Mphi100_scalar_full2.root","samples/tDM_tChan_Mchi1Mphi100_scalar_full.root","samples/tDM_tWChan_Mchi1Mphi100_scalar_full.root"]
    #inputFiles=["testSamples/SingleElectron_2016H.root"]#,"SingleMuon_2016B_ver1.root","SingleMuon_2016B_ver2.root","SingleMuon_2016E.root"]
    inputFiles=["testSamples/ttbarPlusJets_Run2016.root"]
    #inputFiles=["testSamples/SingleElectron_2017B.root"]
    #inputFiles = ["testSamples/SingleElectron_2018A.root"]
    #inputFiles = ["testSamples/SingleElectron_2016H.root"]
    #jsonFile = "python/postprocessing/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
    #jsonFile = "python/postprocessing/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"
    #jsonFile = "python/postprocessing/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"

    #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[analyze2016SignalMC()],postfix="_ModuleCommon_2016MC",noOut=False,outputbranchsel=outputbranches)#,jsonInput=jsonFile)
    #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[analyze2016Data()],postfix="_ModuleCommon_2016Data",noOut=False,outputbranchsel=outputbranches,jsonInput=jsonFile)
    p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[jetmetCorrector2016MC(),analyze2016MC()],postfix="_ModuleCommon_2016MC_allSys",noOut=False,outputbranchsel=outputbranches)
    p.run()
