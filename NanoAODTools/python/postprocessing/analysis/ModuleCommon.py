import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.corrections.leptonSFs import *
from PhysicsTools.NanoAODTools.postprocessing.corrections.METSFs import *
from PhysicsTools.NanoAODTools.postprocessing.corrections.BTaggingTool import *
from PhysicsTools.NanoAODTools.postprocessing.corrections.kFactorTool import *
from PhysicsTools.NanoAODTools.postprocessing.corrections.PileupWeightTool import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *

print 'Python version = ', sys.version

#Set runLocal to false if running jobs through CRAB
runLocal = False
#runLocal = True

#Set jesSys to "All" for split JES systematics and "Total" for combined JES systematics
jesSys = "All"
#jesSys = "Total"

#Load shared object files that contains C++ code to calculate discriminating variables 
if runLocal:
    print 'gSystem Load mt2w_bisect = ', ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2w_bisect_cc.so")
    print 'gSystem Load MT2Utility = ', ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/MT2Utility_cc.so")
    print 'gSystem Load mt2bl_bisect = ', ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2bl_bisect_cc.so")
    print 'gSystem Load Mt2Com_bisect = ',ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/Mt2Com_bisect_cc.so")
    print 'gSystem Load JetUtil = ', ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/JetUtil_cc.so")
    print 'gSystem Load topness = ', ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/topness_cc.so")
    print 'gRoot ProcessLine lester_mt2_bisect = ', ROOT.gROOT.ProcessLine(".L /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/lester_mt2_bisect.h")
    print 'gRoot ProcessLine XYMETCorrection = ', ROOT.gROOT.ProcessLine(".L /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/XYMETCorrection.h")
else:
    print 'gSystem Load mt2w_bisect = ', ROOT.gSystem.Load("mt2w_bisect_cc.so")
    print 'gSystem Load MT2Utility = ', ROOT.gSystem.Load("MT2Utility_cc.so")
    print 'gSystem Load mt2bl_bisect = ', ROOT.gSystem.Load("mt2bl_bisect_cc.so")
    print 'gSystem Load Mt2Com_bisect = ', ROOT.gSystem.Load("Mt2Com_bisect_cc.so")
    print 'gSystem Load JetUtil = ', ROOT.gSystem.Load("JetUtil_cc.so")
    print 'gSystem Load topness = ', ROOT.gSystem.Load("topness_cc.so")
    print 'gRoot ProcessLine lester_mt2_bisect = ', ROOT.gROOT.ProcessLine(".L lester_mt2_bisect.h")
    print 'gRoot ProcessLine XYMETCorrection = ', ROOT.gROOT.ProcessLine(".L XYMETCorrection.h")

try:
    ROOT.asymm_mt2_lester_bisect.disableCopyrightMessage()
except:
    pass

Mt2Com_bisect = ROOT.Mt2Com_bisect()
asymm_mt2_lester_bisect = ROOT.asymm_mt2_lester_bisect()

#List of all JES systematic uncertainties
if jesSys == "All":
    jesUnc = ["","AbsoluteMPFBias", "AbsoluteScale", "AbsoluteStat", "FlavorQCD", "Fragmentation", "PileUpDataMC", "PileUpPtBB", "PileUpPtEC1", "PileUpPtEC2", "PileUpPtHF", "PileUpPtRef", "RelativeFSR", "RelativeJEREC1", "RelativeJEREC2", "RelativeJERHF", "RelativePtBB", "RelativePtEC1", "RelativePtEC2", "RelativePtHF", "RelativeBal", "RelativeSample", "RelativeStatEC", "RelativeStatFSR", "RelativeStatHF", "SinglePionECAL", "SinglePionHCAL", "TimePtEta"]
else:
    jesUnc = [""]

class CommonAnalysis(Module):
    def __init__(self, signalRegion, year=2016, isData=False, isSignal=False, btag='DeepCSV', UL=False):
        self.signalRegion = signalRegion
        self.year = year
        self.isData = isData
        self.isMC = not self.isData
        self.isSignal = isSignal
        self.btag = btag
        self.nEvent = 0
        self.UL = UL
        if self.isMC:
            self.eleSFs = ElectronSFs(self.year)
            self.muSFs = MuonSFs(self.year)
            self.METSFs = METSFs(self.year)
            self.btagTool = BTagWeightTool(tagger=self.btag,wp='medium',channel='ttbar',year=self.year)
            self.btagToolbcUpCorrelated = BTagWeightTool(tagger=self.btag,wp='medium',sigmabc='up_correlated',channel='ttbar',year=self.year)
            self.btagToolbcDownCorrelated = BTagWeightTool(tagger=self.btag,wp='medium',sigmabc='down_correlated',channel='ttbar',year=self.year)
            self.btagToolbcUpUncorrelated = BTagWeightTool(tagger=self.btag,wp='medium',sigmabc='up_uncorrelated',channel='ttbar',year=self.year)
            self.btagToolbcDownUncorrelated = BTagWeightTool(tagger=self.btag,wp='medium',sigmabc='down_uncorrelated',channel='ttbar',year=self.year)
            self.btagToollightUpCorrelated = BTagWeightTool(tagger=self.btag,wp='medium',sigmalight='up_correlated',channel='ttbar',year=self.year)
            self.btagToollightDownCorrelated = BTagWeightTool(tagger=self.btag,wp='medium',sigmalight='down_correlated',channel='ttbar',year=self.year)
            self.btagToollightUpUncorrelated = BTagWeightTool(tagger=self.btag,wp='medium',sigmalight='up_uncorrelated',channel='ttbar',year=self.year)
            self.btagToollightDownUncorrelated = BTagWeightTool(tagger=self.btag,wp='medium',sigmalight='down_uncorrelated',channel='ttbar',year=self.year)
            self.puTool = PileupWeightTool(year=self.year, UL=self.UL)
            self.puToolUp = PileupWeightTool(year=self.year,sigma='up', UL=self.UL)
            self.puToolDown = PileupWeightTool(year=self.year,sigma='down', UL=self.UL)
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
        self.out.branch("deltaPhij1", "F")
        self.out.branch("deltaPhij2", "F")
        self.out.branch("deltaPhij3", "F")
        self.out.branch("deltaPhib1", "F")
        self.out.branch("deltaPhib2", "F")
        self.out.branch("M_Tb", "F")
        self.out.branch("M_T", "F")
        self.out.branch("M_T2W", "F")
        self.out.branch("M_T2ll", "F")
        self.out.branch("jet1p_TH_T", "F")
        self.out.branch("ntaus", "I")
        self.out.branch("m_ll","F")
        self.out.branch("recoilPtMiss","F")

        self.out.branch("lepton1_charge","I")
        self.out.branch("lepton2_charge","I")

        self.out.branch("index_vetoElectrons","I",lenVar="nVetoElectrons")
        self.out.branch("index_tightElectrons","I",lenVar="nTightElectrons")
        self.out.branch("index_looseMuons","I",lenVar="nLooseMuons")
        self.out.branch("index_tightMuons","I",lenVar="nTightMuons")
        self.out.branch("index_centralJets","I",lenVar="njets")
        self.out.branch("index_forwardJets","I",lenVar="nfjets")
        self.out.branch("index_bJets","I",lenVar="nbjets")

        self.out.branch("passEle32WPTightGsf2017", "I")
        self.out.branch("EE_L1_prefire", "I") 
        self.out.branch("modified_topness", "F")
        self.out.branch("full_topness", "F")
        self.out.branch("noB2Bleadingfjet", "I")

        if self.isMC:
            #Systematics - JES, JER
            for sys in jesUnc:
                self.out.branch("njetsScale"+sys+"Up", "I")
                self.out.branch("njetsScale"+sys+"Down", "I")

                self.out.branch("nfjetsScale"+sys+"Up", "I")
                self.out.branch("nfjetsScale"+sys+"Down", "I")

                self.out.branch("nbjetsScale"+sys+"Up", "I")
                self.out.branch("nbjetsScale"+sys+"Down", "I")

                self.out.branch("minDeltaPhiScale"+sys+"Up", "F")
                self.out.branch("minDeltaPhiScale"+sys+"Down", "F")

                self.out.branch("minDeltaPhi12Scale"+sys+"Up", "F")
                self.out.branch("minDeltaPhi12Scale"+sys+"Down", "F")

                self.out.branch("M_TbScale"+sys+"Up", "F")
                self.out.branch("M_TbScale"+sys+"Down", "F")

                self.out.branch("M_TScale"+sys+"Up", "F")
                self.out.branch("M_TScale"+sys+"Down", "F")
                
                self.out.branch("M_T2WScale"+sys+"Up", "F")
                self.out.branch("M_T2WScale"+sys+"Down", "F")
                
                self.out.branch("M_T2llScale"+sys+"Up", "F")
                self.out.branch("M_T2llScale"+sys+"Down", "F")
                
                self.out.branch("jet1p_TH_TScale"+sys+"Up", "F")
                self.out.branch("jet1p_TH_TScale"+sys+"Down", "F")
                
                self.out.branch("recoilPtMissScale"+sys+"Up", "F")
                self.out.branch("recoilPtMissScale"+sys+"Down", "F")
                
                self.out.branch("modified_topnessScale"+sys+"Up", "F")
                self.out.branch("modified_topnessScale"+sys+"Down", "F")
                
                self.out.branch("full_topnessScale"+sys+"Up", "F")
                self.out.branch("full_topnessScale"+sys+"Down", "F")

                self.out.branch("METcorrected_ptScale"+sys+"Up", "F")
                self.out.branch("METcorrected_ptScale"+sys+"Down", "F")
                self.out.branch("METcorrected_phiScale"+sys+"Up", "F")
                self.out.branch("METcorrected_phiScale"+sys+"Down", "F")

            self.out.branch("njetsResUp", "I")
            self.out.branch("njetsResDown", "I")

            
            self.out.branch("nfjetsResUp", "I")
            self.out.branch("nfjetsResDown", "I")
            
            self.out.branch("nbjetsResUp", "I")
            self.out.branch("nbjetsResDown", "I")

            self.out.branch("METcorrected_ptResUp", "F")
            self.out.branch("METcorrected_ptResDown", "F")
            self.out.branch("METcorrected_phiResUp", "F")
            self.out.branch("METcorrected_phiResDown", "F")
            
            self.out.branch("minDeltaPhiResUp", "F")
            self.out.branch("minDeltaPhiResDown", "F")
            
            self.out.branch("minDeltaPhi12ResUp", "F")
            self.out.branch("minDeltaPhi12ResDown", "F")
            
            self.out.branch("M_TbResUp", "F")
            self.out.branch("M_TbResDown", "F")
            
            self.out.branch("M_TResUp", "F")
            self.out.branch("M_TResDown", "F")
            
            self.out.branch("M_T2WResUp", "F")
            self.out.branch("M_T2WResDown", "F")
            
            self.out.branch("M_T2llResUp", "F")
            self.out.branch("M_T2llResDown", "F")
            
            self.out.branch("jet1p_TH_TResUp", "F")
            self.out.branch("jet1p_TH_TResDown", "F")
            
            self.out.branch("recoilPtMissResUp", "F")
            self.out.branch("recoilPtMissResDown", "F")
            
            self.out.branch("modified_topnessResUp", "F")
            self.out.branch("modified_topnessResDown", "F")

            self.out.branch("full_topnessResUp", "F")
            self.out.branch("full_topnessResDown", "F")

            if not self.isSignal:
                #Systematics - PDF
                self.out.branch("pdfWeightUp", "F")
                self.out.branch("pdfWeightDown", "F")

                #Systematics - QCD Renormalization and Factorization scales
                self.out.branch("qcdRenWeightUp", "F")
                self.out.branch("qcdRenWeightDown", "F")
                self.out.branch("qcdFacWeightUp", "F")
                self.out.branch("qcdFacWeightDown", "F")

            self.out.branch("leptonWeight", "F")
            self.out.branch("electronWeight", "F")
            self.out.branch("muonWeight", "F")
            #Systematics - lepton weights
            self.out.branch("leptonWeightUp", "F")
            self.out.branch("leptonWeightDown", "F")
            self.out.branch("electronWeightUp", "F")
            self.out.branch("electronWeightDown", "F")
            self.out.branch("muonWeightUp", "F")
            self.out.branch("muonWeightDown", "F")

            self.out.branch("electronTriggerWeight", "F")
            #Systematics - electron trigger weights
            self.out.branch("electronTriggerWeightUp", "F")
            self.out.branch("electronTriggerWeightDown", "F")

            self.out.branch("muonTriggerWeight", "F")
            #Systematics - muon trigger weights
            self.out.branch("muonTriggerWeightUp", "F")
            self.out.branch("muonTriggerWeightDown", "F")

            self.out.branch("METTriggerWeight", "F")

            self.out.branch("EE_L1_prefire_Weight", "F")
            #Systematics - EE L1 prefiring weights
            self.out.branch("EE_L1_prefire_WeightUp", "F")
            self.out.branch("EE_L1_prefire_WeightDown", "F")

            self.out.branch("bjetWeight", "F")
            #Systematics - b-tagging weights
            self.out.branch("bjetWeightbcUpCorrelated","F")
            self.out.branch("bjetWeightbcDownCorrelated","F")
            self.out.branch("bjetWeightbcUpUncorrelated","F")
            self.out.branch("bjetWeightbcDownUncorrelated","F")
            self.out.branch("bjetWeightlightUpCorrelated","F")
            self.out.branch("bjetWeightlightDownCorrelated","F")
            self.out.branch("bjetWeightlightUpUncorrelated","F")
            self.out.branch("bjetWeightlightDownUncorrelated","F")

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
            self.out.branch("qcdZTo2NuWeightRenUp", "F")
            self.out.branch("qcdZTo2NuWeightRenDown", "F")
            self.out.branch("qcdZTo2NuWeightFacUp", "F")
            self.out.branch("qcdZTo2NuWeightFacDown", "F")
            self.out.branch("qcdZTo2LWeightRenUp", "F")
            self.out.branch("qcdZTo2LWeightRenDown", "F")
            self.out.branch("qcdZTo2LWeightFacUp", "F")
            self.out.branch("qcdZTo2LWeightFacDown", "F")

            #Systematics - parton shower weights
            self.out.branch("PSWeightISRUp", "F")
            self.out.branch("PSWeightISRDown", "F")
            self.out.branch("PSWeightFSRUp", "F")
            self.out.branch("PSWeightFSRDown", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go 
to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        jesBranches = {}

        #Tight/Veto electrons are defined and counted
        if self.year == 2016:
            vetoElectronsEnumerate = filter(lambda lep : lep[1].pt > 10 and lep[1].cutBased_Sum16 != 0 and (abs(lep[1].eta) < 1.4442 or 1.566 < abs(lep[1].eta) < 2.5), enumerate(electrons))
            tightElectronsEnumerate = filter(lambda lep : lep[1].pt > 35 and abs(lep[1].eta) < 2.1 and lep[1].cutBased_Sum16 == 4, vetoElectronsEnumerate)

        else:
            vetoElectronsEnumerate = filter(lambda lep : lep[1].pt > 10 and lep[1].cutBased != 0 and (abs(lep[1].eta) < 1.4442 or 1.566 < abs(lep[1].eta) < 2.5), enumerate(electrons))
            tightElectronsEnumerate = filter(lambda lep : lep[1].pt > 35 and abs(lep[1].eta) < 2.1 and lep[1].cutBased == 4, vetoElectronsEnumerate)
        
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
            dirtyElectrons = filter(lambda e : e.p4().DeltaR(jet.p4()) < 0.4, vetoElectrons)
            dirtyMuons = filter(lambda m : m.p4().DeltaR(jet.p4()) < 0.4, looseMuons)
            if len(dirtyElectrons) + len(dirtyMuons) > 0:
                return False
            else:
                return True

        #Helper function to return correct jet pt for corresponding JES systematic uncertainty
        def getJESjetpt(jet, sys):
            if sys == "Up":
                return jet.pt_jesTotalUp
            elif sys == "Down":
                return jet.pt_jesTotalDown
            elif sys == "AbsoluteMPFBiasUp":
                return jet.pt_jesAbsoluteMPFBiasUp
            elif sys == "AbsoluteMPFBiasDown":
                return jet.pt_jesAbsoluteMPFBiasDown
            elif sys == "AbsoluteScaleUp":
                return jet.pt_jesAbsoluteScaleUp
            elif sys == "AbsoluteScaleDown":
                return jet.pt_jesAbsoluteScaleDown
            elif sys == "AbsoluteStatUp":
                return jet.pt_jesAbsoluteStatUp
            elif sys == "AbsoluteStatDown":
                return jet.pt_jesAbsoluteStatDown
            elif sys == "FlavorQCDUp":
                return jet.pt_jesFlavorQCDUp
            elif sys == "FlavorQCDDown":
                return jet.pt_jesFlavorQCDDown
            elif sys == "FragmentationUp":
                return jet.pt_jesFragmentationUp
            elif sys == "FragmentationDown":
                return jet.pt_jesFragmentationDown
            elif sys == "PileUpDataMCUp":
                return jet.pt_jesPileUpDataMCUp
            elif sys == "PileUpDataMCDown":
                return jet.pt_jesPileUpDataMCDown
            elif sys == "PileUpPtBBUp":
                return jet.pt_jesPileUpPtBBUp
            elif sys == "PileUpPtBBDown":
                return jet.pt_jesPileUpPtBBDown
            elif sys == "PileUpPtEC1Up":
                return jet.pt_jesPileUpPtEC1Up
            elif sys == "PileUpPtEC1Down":
                return jet.pt_jesPileUpPtEC1Down
            elif sys == "PileUpPtEC2Up":
                return jet.pt_jesPileUpPtEC2Up
            elif sys == "PileUpPtEC2Down":
                return jet.pt_jesPileUpPtEC2Down
            elif sys == "PileUpPtHFUp":
                return jet.pt_jesPileUpPtHFUp
            elif sys == "PileUpPtHFDown":
                return jet.pt_jesPileUpPtHFDown
            elif sys == "PileUpPtRefUp":
                return jet.pt_jesPileUpPtRefUp
            elif sys == "PileUpPtRefDown":
                return jet.pt_jesPileUpPtRefDown
            elif sys == "RelativeFSRUp":
                return jet.pt_jesRelativeFSRUp
            elif sys == "RelativeFSRDown":
                return jet.pt_jesRelativeFSRDown
            elif sys == "RelativeJEREC1Up":
                return jet.pt_jesRelativeJEREC1Up
            elif sys == "RelativeJEREC1Down":
                return jet.pt_jesRelativeJEREC1Down
            elif sys == "RelativeJEREC2Up":
                return jet.pt_jesRelativeJEREC2Up
            elif sys == "RelativeJEREC2Down":
                return jet.pt_jesRelativeJEREC2Down
            elif sys == "RelativeJERHFUp":
                return jet.pt_jesRelativeJERHFUp
            elif sys == "RelativeJERHFDown":
                return jet.pt_jesRelativeJERHFDown
            elif sys == "RelativePtBBUp":
                return jet.pt_jesRelativePtBBUp
            elif sys == "RelativePtBBDown":
                return jet.pt_jesRelativePtBBDown
            elif sys == "RelativePtEC1Up":
                return jet.pt_jesRelativePtEC1Up
            elif sys == "RelativePtEC1Down":
                return jet.pt_jesRelativePtEC1Down
            elif sys == "RelativePtEC2Up":
                return jet.pt_jesRelativePtEC2Up
            elif sys == "RelativePtEC2Down":
                return jet.pt_jesRelativePtEC2Down
            elif sys == "RelativePtHFUp":
                return jet.pt_jesRelativePtHFUp
            elif sys == "RelativePtHFDown":
                return jet.pt_jesRelativePtHFDown
            elif sys == "RelativeBalUp":
                return jet.pt_jesRelativeBalUp
            elif sys == "RelativeBalDown":
                return jet.pt_jesRelativeBalDown
            elif sys == "RelativeSampleUp":
                return jet.pt_jesRelativeSampleUp
            elif sys == "RelativeSampleDown":
                return jet.pt_jesRelativeSampleDown
            elif sys == "RelativeStatECUp":
                return jet.pt_jesRelativeStatECUp
            elif sys == "RelativeStatECDown":
                return jet.pt_jesRelativeStatECDown
            elif sys == "RelativeStatFSRUp":
                return jet.pt_jesRelativeStatFSRUp
            elif sys == "RelativeStatFSRDown":
                return jet.pt_jesRelativeStatFSRDown
            elif sys == "RelativeStatHFUp":
                return jet.pt_jesRelativeStatHFUp
            elif sys == "RelativeStatHFDown":
                return jet.pt_jesRelativeStatHFDown
            elif sys == "SinglePionECALUp":
                return jet.pt_jesSinglePionECALUp
            elif sys == "SinglePionECALDown":
                return jet.pt_jesSinglePionECALDown
            elif sys == "SinglePionHCALUp":
                return jet.pt_jesSinglePionHCALUp
            elif sys == "SinglePionHCALDown":
                return jet.pt_jesSinglePionHCALDown
            elif sys == "TimePtEtaUp":
                return jet.pt_jesTimePtEtaUp
            elif sys == "TimePtEtaDown":
                return jet.pt_jesTimePtEtaDown

        #Helper function to return correct MET pt for corresponding JES systematic uncertainty
        def getJESMETpt(sys):
            if self.year == 2017 and not self.UL:
                if sys == "Up":
                    return event.METFixEE2017_T1Smear_pt_jesTotalUp 
                elif sys == "Down":
                    return event.METFixEE2017_T1Smear_pt_jesTotalDown
                elif sys == "AbsoluteMPFBiasUp":
                    return event.METFixEE2017_T1Smear_pt_jesAbsoluteMPFBiasUp
                elif sys == "AbsoluteMPFBiasDown":
                    return event.METFixEE2017_T1Smear_pt_jesAbsoluteMPFBiasDown
                elif sys == "AbsoluteScaleUp":
                    return event.METFixEE2017_T1Smear_pt_jesAbsoluteScaleUp
                elif sys == "AbsoluteScaleDown":
                    return event.METFixEE2017_T1Smear_pt_jesAbsoluteScaleDown
                elif sys == "AbsoluteStatUp":
                    return event.METFixEE2017_T1Smear_pt_jesAbsoluteStatUp
                elif sys == "AbsoluteStatDown":
                    return event.METFixEE2017_T1Smear_pt_jesAbsoluteStatDown
                elif sys == "FlavorQCDUp":
                    return event.METFixEE2017_T1Smear_pt_jesFlavorQCDUp
                elif sys == "FlavorQCDDown":
                    return event.METFixEE2017_T1Smear_pt_jesFlavorQCDDown
                elif sys == "FragmentationUp":
                    return event.METFixEE2017_T1Smear_pt_jesFragmentationUp
                elif sys == "FragmentationDown":
                    return event.METFixEE2017_T1Smear_pt_jesFragmentationDown
                elif sys == "PileUpDataMCUp":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpDataMCUp
                elif sys == "PileUpDataMCDown":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpDataMCDown
                elif sys == "PileUpPtBBUp":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtBBUp
                elif sys == "PileUpPtBBDown":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtBBDown
                elif sys == "PileUpPtEC1Up":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtEC1Up
                elif sys == "PileUpPtEC1Down":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtEC1Down
                elif sys == "PileUpPtEC2Up":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtEC2Up
                elif sys == "PileUpPtEC2Down":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtEC2Down
                elif sys == "PileUpPtHFUp":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtHFUp
                elif sys == "PileUpPtHFDown":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtHFDown
                elif sys == "PileUpPtRefUp":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtRefUp
                elif sys == "PileUpPtRefDown":
                    return event.METFixEE2017_T1Smear_pt_jesPileUpPtRefDown
                elif sys == "RelativeFSRUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeFSRUp
                elif sys == "RelativeFSRDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeFSRDown
                elif sys == "RelativeJEREC1Up":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeJEREC1Up
                elif sys == "RelativeJEREC1Down":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeJEREC1Down
                elif sys == "RelativeJEREC2Up":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeJEREC2Up
                elif sys == "RelativeJEREC2Down":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeJEREC2Down
                elif sys == "RelativeJERHFUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeJERHFUp
                elif sys == "RelativeJERHFDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeJERHFDown
                elif sys == "RelativePtBBUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativePtBBUp
                elif sys == "RelativePtBBDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativePtBBDown
                elif sys == "RelativePtEC1Up":
                    return event.METFixEE2017_T1Smear_pt_jesRelativePtEC1Up
                elif sys == "RelativePtEC1Down":
                    return event.METFixEE2017_T1Smear_pt_jesRelativePtEC1Down
                elif sys == "RelativePtEC2Up":
                    return event.METFixEE2017_T1Smear_pt_jesRelativePtEC2Up
                elif sys == "RelativePtEC2Down":
                    return event.METFixEE2017_T1Smear_pt_jesRelativePtEC2Down
                elif sys == "RelativePtHFUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativePtHFUp
                elif sys == "RelativePtHFDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativePtHFDown
                elif sys == "RelativeBalUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeBalUp
                elif sys == "RelativeBalDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeBalDown
                elif sys == "RelativeSampleUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeSampleUp
                elif sys == "RelativeSampleDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeSampleDown
                elif sys == "RelativeStatECUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeStatECUp
                elif sys == "RelativeStatECDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeStatECDown
                elif sys == "RelativeStatFSRUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeStatFSRUp
                elif sys == "RelativeStatFSRDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeStatFSRDown
                elif sys == "RelativeStatHFUp":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeStatHFUp
                elif sys == "RelativeStatHFDown":
                    return event.METFixEE2017_T1Smear_pt_jesRelativeStatHFDown
                elif sys == "SinglePionECALUp":
                    return event.METFixEE2017_T1Smear_pt_jesSinglePionECALUp
                elif sys == "SinglePionECALDown":
                    return event.METFixEE2017_T1Smear_pt_jesSinglePionECALDown
                elif sys == "SinglePionHCALUp":
                    return event.METFixEE2017_T1Smear_pt_jesSinglePionHCALUp
                elif sys == "SinglePionHCALDown":
                    return event.METFixEE2017_T1Smear_pt_jesSinglePionHCALDown
                elif sys == "TimePtEtaUp":
                    return event.METFixEE2017_T1Smear_pt_jesTimePtEtaUp
                elif sys == "TimePtEtaDown":
                    return event.METFixEE2017_T1Smear_pt_jesTimePtEtaDown
            else:
                if sys == "Up":
                    return event.MET_T1Smear_pt_jesTotalUp 
                elif sys == "Down":
                    return event.MET_T1Smear_pt_jesTotalDown
                elif sys == "AbsoluteMPFBiasUp":
                    return event.MET_T1Smear_pt_jesAbsoluteMPFBiasUp
                elif sys == "AbsoluteMPFBiasDown":
                    return event.MET_T1Smear_pt_jesAbsoluteMPFBiasDown
                elif sys == "AbsoluteScaleUp":
                    return event.MET_T1Smear_pt_jesAbsoluteScaleUp
                elif sys == "AbsoluteScaleDown":
                    return event.MET_T1Smear_pt_jesAbsoluteScaleDown
                elif sys == "AbsoluteStatUp":
                    return event.MET_T1Smear_pt_jesAbsoluteStatUp
                elif sys == "AbsoluteStatDown":
                    return event.MET_T1Smear_pt_jesAbsoluteStatDown
                elif sys == "FlavorQCDUp":
                    return event.MET_T1Smear_pt_jesFlavorQCDUp
                elif sys == "FlavorQCDDown":
                    return event.MET_T1Smear_pt_jesFlavorQCDDown
                elif sys == "FragmentationUp":
                    return event.MET_T1Smear_pt_jesFragmentationUp
                elif sys == "FragmentationDown":
                    return event.MET_T1Smear_pt_jesFragmentationDown
                elif sys == "PileUpDataMCUp":
                    return event.MET_T1Smear_pt_jesPileUpDataMCUp
                elif sys == "PileUpDataMCDown":
                    return event.MET_T1Smear_pt_jesPileUpDataMCDown
                elif sys == "PileUpPtBBUp":
                    return event.MET_T1Smear_pt_jesPileUpPtBBUp
                elif sys == "PileUpPtBBDown":
                    return event.MET_T1Smear_pt_jesPileUpPtBBDown
                elif sys == "PileUpPtEC1Up":
                    return event.MET_T1Smear_pt_jesPileUpPtEC1Up
                elif sys == "PileUpPtEC1Down":
                    return event.MET_T1Smear_pt_jesPileUpPtEC1Down
                elif sys == "PileUpPtEC2Up":
                    return event.MET_T1Smear_pt_jesPileUpPtEC2Up
                elif sys == "PileUpPtEC2Down":
                    return event.MET_T1Smear_pt_jesPileUpPtEC2Down
                elif sys == "PileUpPtHFUp":
                    return event.MET_T1Smear_pt_jesPileUpPtHFUp
                elif sys == "PileUpPtHFDown":
                    return event.MET_T1Smear_pt_jesPileUpPtHFDown
                elif sys == "PileUpPtRefUp":
                    return event.MET_T1Smear_pt_jesPileUpPtRefUp
                elif sys == "PileUpPtRefDown":
                    return event.MET_T1Smear_pt_jesPileUpPtRefDown
                elif sys == "RelativeFSRUp":
                    return event.MET_T1Smear_pt_jesRelativeFSRUp
                elif sys == "RelativeFSRDown":
                    return event.MET_T1Smear_pt_jesRelativeFSRDown
                elif sys == "RelativeJEREC1Up":
                    return event.MET_T1Smear_pt_jesRelativeJEREC1Up
                elif sys == "RelativeJEREC1Down":
                    return event.MET_T1Smear_pt_jesRelativeJEREC1Down
                elif sys == "RelativeJEREC2Up":
                    return event.MET_T1Smear_pt_jesRelativeJEREC2Up
                elif sys == "RelativeJEREC2Down":
                    return event.MET_T1Smear_pt_jesRelativeJEREC2Down
                elif sys == "RelativeJERHFUp":
                    return event.MET_T1Smear_pt_jesRelativeJERHFUp
                elif sys == "RelativeJERHFDown":
                    return event.MET_T1Smear_pt_jesRelativeJERHFDown
                elif sys == "RelativePtBBUp":
                    return event.MET_T1Smear_pt_jesRelativePtBBUp
                elif sys == "RelativePtBBDown":
                    return event.MET_T1Smear_pt_jesRelativePtBBDown
                elif sys == "RelativePtEC1Up":
                    return event.MET_T1Smear_pt_jesRelativePtEC1Up
                elif sys == "RelativePtEC1Down":
                    return event.MET_T1Smear_pt_jesRelativePtEC1Down
                elif sys == "RelativePtEC2Up":
                    return event.MET_T1Smear_pt_jesRelativePtEC2Up
                elif sys == "RelativePtEC2Down":
                    return event.MET_T1Smear_pt_jesRelativePtEC2Down
                elif sys == "RelativePtHFUp":
                    return event.MET_T1Smear_pt_jesRelativePtHFUp
                elif sys == "RelativePtHFDown":
                    return event.MET_T1Smear_pt_jesRelativePtHFDown
                elif sys == "RelativeBalUp":
                    return event.MET_T1Smear_pt_jesRelativeBalUp
                elif sys == "RelativeBalDown":
                    return event.MET_T1Smear_pt_jesRelativeBalDown
                elif sys == "RelativeSampleUp":
                    return event.MET_T1Smear_pt_jesRelativeSampleUp
                elif sys == "RelativeSampleDown":
                    return event.MET_T1Smear_pt_jesRelativeSampleDown
                elif sys == "RelativeStatECUp":
                    return event.MET_T1Smear_pt_jesRelativeStatECUp
                elif sys == "RelativeStatECDown":
                    return event.MET_T1Smear_pt_jesRelativeStatECDown
                elif sys == "RelativeStatFSRUp":
                    return event.MET_T1Smear_pt_jesRelativeStatFSRUp
                elif sys == "RelativeStatFSRDown":
                    return event.MET_T1Smear_pt_jesRelativeStatFSRDown
                elif sys == "RelativeStatHFUp":
                    return event.MET_T1Smear_pt_jesRelativeStatHFUp
                elif sys == "RelativeStatHFDown":
                    return event.MET_T1Smear_pt_jesRelativeStatHFDown
                elif sys == "SinglePionECALUp":
                    return event.MET_T1Smear_pt_jesSinglePionECALUp
                elif sys == "SinglePionECALDown":
                    return event.MET_T1Smear_pt_jesSinglePionECALDown
                elif sys == "SinglePionHCALUp":
                    return event.MET_T1Smear_pt_jesSinglePionHCALUp
                elif sys == "SinglePionHCALDown":
                    return event.MET_T1Smear_pt_jesSinglePionHCALDown
                elif sys == "TimePtEtaUp":
                    return event.MET_T1Smear_pt_jesTimePtEtaUp
                elif sys == "TimePtEtaDown":
                    return event.MET_T1Smear_pt_jesTimePtEtaDown

        #Helper function to return correct MET phi for corresponding JES systematic uncertainty
        def getJESMETphi(sys):
            if self.year == 2017 and not self.UL:
                if sys == "Up":
                    return event.METFixEE2017_T1Smear_phi_jesTotalUp 
                elif sys == "Down":
                    return event.METFixEE2017_T1Smear_phi_jesTotalDown
                elif sys == "AbsoluteMPFBiasUp":
                    return event.METFixEE2017_T1Smear_phi_jesAbsoluteMPFBiasUp
                elif sys == "AbsoluteMPFBiasDown":
                    return event.METFixEE2017_T1Smear_phi_jesAbsoluteMPFBiasDown
                elif sys == "AbsoluteScaleUp":
                    return event.METFixEE2017_T1Smear_phi_jesAbsoluteScaleUp
                elif sys == "AbsoluteScaleDown":
                    return event.METFixEE2017_T1Smear_phi_jesAbsoluteScaleDown
                elif sys == "AbsoluteStatUp":
                    return event.METFixEE2017_T1Smear_phi_jesAbsoluteStatUp
                elif sys == "AbsoluteStatDown":
                    return event.METFixEE2017_T1Smear_phi_jesAbsoluteStatDown
                elif sys == "FlavorQCDUp":
                    return event.METFixEE2017_T1Smear_phi_jesFlavorQCDUp
                elif sys == "FlavorQCDDown":
                    return event.METFixEE2017_T1Smear_phi_jesFlavorQCDDown
                elif sys == "FragmentationUp":
                    return event.METFixEE2017_T1Smear_phi_jesFragmentationUp
                elif sys == "FragmentationDown":
                    return event.METFixEE2017_T1Smear_phi_jesFragmentationDown
                elif sys == "PileUpDataMCUp":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpDataMCUp
                elif sys == "PileUpDataMCDown":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpDataMCDown
                elif sys == "PileUpPtBBUp":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtBBUp
                elif sys == "PileUpPtBBDown":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtBBDown
                elif sys == "PileUpPtEC1Up":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtEC1Up
                elif sys == "PileUpPtEC1Down":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtEC1Down
                elif sys == "PileUpPtEC2Up":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtEC2Up
                elif sys == "PileUpPtEC2Down":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtEC2Down
                elif sys == "PileUpPtHFUp":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtHFUp
                elif sys == "PileUpPtHFDown":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtHFDown
                elif sys == "PileUpPtRefUp":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtRefUp
                elif sys == "PileUpPtRefDown":
                    return event.METFixEE2017_T1Smear_phi_jesPileUpPtRefDown
                elif sys == "RelativeFSRUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeFSRUp
                elif sys == "RelativeFSRDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeFSRDown
                elif sys == "RelativeJEREC1Up":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeJEREC1Up
                elif sys == "RelativeJEREC1Down":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeJEREC1Down
                elif sys == "RelativeJEREC2Up":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeJEREC2Up
                elif sys == "RelativeJEREC2Down":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeJEREC2Down
                elif sys == "RelativeJERHFUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeJERHFUp
                elif sys == "RelativeJERHFDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeJERHFDown
                elif sys == "RelativePtBBUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativePtBBUp
                elif sys == "RelativePtBBDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativePtBBDown
                elif sys == "RelativePtEC1Up":
                    return event.METFixEE2017_T1Smear_phi_jesRelativePtEC1Up
                elif sys == "RelativePtEC1Down":
                    return event.METFixEE2017_T1Smear_phi_jesRelativePtEC1Down
                elif sys == "RelativePtEC2Up":
                    return event.METFixEE2017_T1Smear_phi_jesRelativePtEC2Up
                elif sys == "RelativePtEC2Down":
                    return event.METFixEE2017_T1Smear_phi_jesRelativePtEC2Down
                elif sys == "RelativePtHFUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativePtHFUp
                elif sys == "RelativePtHFDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativePtHFDown
                elif sys == "RelativeBalUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeBalUp
                elif sys == "RelativeBalDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeBalDown
                elif sys == "RelativeSampleUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeSampleUp
                elif sys == "RelativeSampleDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeSampleDown
                elif sys == "RelativeStatECUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeStatECUp
                elif sys == "RelativeStatECDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeStatECDown
                elif sys == "RelativeStatFSRUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeStatFSRUp
                elif sys == "RelativeStatFSRDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeStatFSRDown
                elif sys == "RelativeStatHFUp":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeStatHFUp
                elif sys == "RelativeStatHFDown":
                    return event.METFixEE2017_T1Smear_phi_jesRelativeStatHFDown
                elif sys == "SinglePionECALUp":
                    return event.METFixEE2017_T1Smear_phi_jesSinglePionECALUp
                elif sys == "SinglePionECALDown":
                    return event.METFixEE2017_T1Smear_phi_jesSinglePionECALDown
                elif sys == "SinglePionHCALUp":
                    return event.METFixEE2017_T1Smear_phi_jesSinglePionHCALUp
                elif sys == "SinglePionHCALDown":
                    return event.METFixEE2017_T1Smear_phi_jesSinglePionHCALDown
                elif sys == "TimePtEtaUp":
                    return event.METFixEE2017_T1Smear_phi_jesTimePtEtaUp
                elif sys == "TimePtEtaDown":
                    return event.METFixEE2017_T1Smear_phi_jesTimePtEtaDown
            else:
                if sys == "Up":
                    return event.MET_T1Smear_phi_jesTotalUp 
                elif sys == "Down":
                    return event.MET_T1Smear_phi_jesTotalDown
                elif sys == "AbsoluteMPFBiasUp":
                    return event.MET_T1Smear_phi_jesAbsoluteMPFBiasUp
                elif sys == "AbsoluteMPFBiasDown":
                    return event.MET_T1Smear_phi_jesAbsoluteMPFBiasDown
                elif sys == "AbsoluteScaleUp":
                    return event.MET_T1Smear_phi_jesAbsoluteScaleUp
                elif sys == "AbsoluteScaleDown":
                    return event.MET_T1Smear_phi_jesAbsoluteScaleDown
                elif sys == "AbsoluteStatUp":
                    return event.MET_T1Smear_phi_jesAbsoluteStatUp
                elif sys == "AbsoluteStatDown":
                    return event.MET_T1Smear_phi_jesAbsoluteStatDown
                elif sys == "FlavorQCDUp":
                    return event.MET_T1Smear_phi_jesFlavorQCDUp
                elif sys == "FlavorQCDDown":
                    return event.MET_T1Smear_phi_jesFlavorQCDDown
                elif sys == "FragmentationUp":
                    return event.MET_T1Smear_phi_jesFragmentationUp
                elif sys == "FragmentationDown":
                    return event.MET_T1Smear_phi_jesFragmentationDown
                elif sys == "PileUpDataMCUp":
                    return event.MET_T1Smear_phi_jesPileUpDataMCUp
                elif sys == "PileUpDataMCDown":
                    return event.MET_T1Smear_phi_jesPileUpDataMCDown
                elif sys == "PileUpPtBBUp":
                    return event.MET_T1Smear_phi_jesPileUpPtBBUp
                elif sys == "PileUpPtBBDown":
                    return event.MET_T1Smear_phi_jesPileUpPtBBDown
                elif sys == "PileUpPtEC1Up":
                    return event.MET_T1Smear_phi_jesPileUpPtEC1Up
                elif sys == "PileUpPtEC1Down":
                    return event.MET_T1Smear_phi_jesPileUpPtEC1Down
                elif sys == "PileUpPtEC2Up":
                    return event.MET_T1Smear_phi_jesPileUpPtEC2Up
                elif sys == "PileUpPtEC2Down":
                    return event.MET_T1Smear_phi_jesPileUpPtEC2Down
                elif sys == "PileUpPtHFUp":
                    return event.MET_T1Smear_phi_jesPileUpPtHFUp
                elif sys == "PileUpPtHFDown":
                    return event.MET_T1Smear_phi_jesPileUpPtHFDown
                elif sys == "PileUpPtRefUp":
                    return event.MET_T1Smear_phi_jesPileUpPtRefUp
                elif sys == "PileUpPtRefDown":
                    return event.MET_T1Smear_phi_jesPileUpPtRefDown
                elif sys == "RelativeFSRUp":
                    return event.MET_T1Smear_phi_jesRelativeFSRUp
                elif sys == "RelativeFSRDown":
                    return event.MET_T1Smear_phi_jesRelativeFSRDown
                elif sys == "RelativeJEREC1Up":
                    return event.MET_T1Smear_phi_jesRelativeJEREC1Up
                elif sys == "RelativeJEREC1Down":
                    return event.MET_T1Smear_phi_jesRelativeJEREC1Down
                elif sys == "RelativeJEREC2Up":
                    return event.MET_T1Smear_phi_jesRelativeJEREC2Up
                elif sys == "RelativeJEREC2Down":
                    return event.MET_T1Smear_phi_jesRelativeJEREC2Down
                elif sys == "RelativeJERHFUp":
                    return event.MET_T1Smear_phi_jesRelativeJERHFUp
                elif sys == "RelativeJERHFDown":
                    return event.MET_T1Smear_phi_jesRelativeJERHFDown
                elif sys == "RelativePtBBUp":
                    return event.MET_T1Smear_phi_jesRelativePtBBUp
                elif sys == "RelativePtBBDown":
                    return event.MET_T1Smear_phi_jesRelativePtBBDown
                elif sys == "RelativePtEC1Up":
                    return event.MET_T1Smear_phi_jesRelativePtEC1Up
                elif sys == "RelativePtEC1Down":
                    return event.MET_T1Smear_phi_jesRelativePtEC1Down
                elif sys == "RelativePtEC2Up":
                    return event.MET_T1Smear_phi_jesRelativePtEC2Up
                elif sys == "RelativePtEC2Down":
                    return event.MET_T1Smear_phi_jesRelativePtEC2Down
                elif sys == "RelativePtHFUp":
                    return event.MET_T1Smear_phi_jesRelativePtHFUp
                elif sys == "RelativePtHFDown":
                    return event.MET_T1Smear_phi_jesRelativePtHFDown
                elif sys == "RelativeBalUp":
                    return event.MET_T1Smear_phi_jesRelativeBalUp
                elif sys == "RelativeBalDown":
                    return event.MET_T1Smear_phi_jesRelativeBalDown
                elif sys == "RelativeSampleUp":
                    return event.MET_T1Smear_phi_jesRelativeSampleUp
                elif sys == "RelativeSampleDown":
                    return event.MET_T1Smear_phi_jesRelativeSampleDown
                elif sys == "RelativeStatECUp":
                    return event.MET_T1Smear_phi_jesRelativeStatECUp
                elif sys == "RelativeStatECDown":
                    return event.MET_T1Smear_phi_jesRelativeStatECDown
                elif sys == "RelativeStatFSRUp":
                    return event.MET_T1Smear_phi_jesRelativeStatFSRUp
                elif sys == "RelativeStatFSRDown":
                    return event.MET_T1Smear_phi_jesRelativeStatFSRDown
                elif sys == "RelativeStatHFUp":
                    return event.MET_T1Smear_phi_jesRelativeStatHFUp
                elif sys == "RelativeStatHFDown":
                    return event.MET_T1Smear_phi_jesRelativeStatHFDown
                elif sys == "SinglePionECALUp":
                    return event.MET_T1Smear_phi_jesSinglePionECALUp
                elif sys == "SinglePionECALDown":
                    return event.MET_T1Smear_phi_jesSinglePionECALDown
                elif sys == "SinglePionHCALUp":
                    return event.MET_T1Smear_phi_jesSinglePionHCALUp
                elif sys == "SinglePionHCALDown":
                    return event.MET_T1Smear_phi_jesSinglePionHCALDown
                elif sys == "TimePtEtaUp":
                    return event.MET_T1Smear_phi_jesTimePtEtaUp
                elif sys == "TimePtEtaDown":
                    return event.MET_T1Smear_phi_jesTimePtEtaDown

        #Jet categories are defined and counted 
        if self.year == 2016:
            #Central jets  (2016)
            centralJetsEnumerate = filter(lambda j : ((30 < j[1].pt_nom < 50 and j[1].puId == 7) or j[1].pt_nom > 50) and abs(j[1].eta) < 2.4 and cleanJet(j[1]) and j[1].jetId == 7, enumerate(jets)) #Use tightLepVeto jet ID WP for 2016 with tight puId for jet_pt < 50

            #Forward jets (2016)
            forwardJetsEnumerate = filter(lambda j : ((30 < j[1].pt_nom < 50 and j[1].puId == 7) or j[1].pt_nom > 50) and 2.4 < abs(j[1].eta) < 4 and cleanJet(j[1]) and j[1].jetId == 7, enumerate(jets))

        else:
            #Central jets (2017, 2018)
            centralJetsEnumerate = filter(lambda j : ((30 < j[1].pt_nom < 50 and j[1].puId == 7) or j[1].pt_nom > 50) and abs(j[1].eta) < 2.4 and cleanJet(j[1]) and j[1].jetId == 6, enumerate(jets)) #Use tightLepVeto jet ID WP for 2017 and 2018 with tight puId for jet_pt < 50

            #Forward jets (2017, 2018)
            forwardJetsEnumerate = filter(lambda j : ((30 < j[1].pt_nom < 50 and j[1].puId == 7) or j[1].pt_nom > 50) and 2.4 < abs(j[1].eta) < 4 and cleanJet(j[1]) and j[1].jetId == 6, enumerate(jets))

        #B-jets
        btag_WP = getattr(BTagWPs(self.btag,self.year),'medium')
        if self.btag == 'CSVv2':
            bJetsEnumerate = filter(lambda j : j[1].btagCSVV2 > btag_WP, centralJetsEnumerate)

        elif self.btag == 'DeepCSV':
            bJetsEnumerate = filter(lambda j : j[1].btagDeepB > btag_WP, centralJetsEnumerate)

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

        #Check EE L1 prefiring issue (https://twiki.cern.ch/twiki/bin/viewauth/CMS/ExoPreapprovalChecklist). True if there is a jet with pT > 100 GeV and 2.25 < |eta| < 3.0, False otherwise.
        EE_L1_prefire = False
        prefireCentralJets = filter(lambda j : j.pt > 100 and 2.25 < abs(j.eta) < 3.0, centralJets)
        prefireForwardJets = filter(lambda j : j.pt > 100 and 2.25 < abs(j.eta) < 3.0, forwardJets)
        nPrefireJets = len(prefireCentralJets) + len(prefireForwardJets)
        if nPrefireJets > 0:
            EE_L1_prefire = True


        #Apply MET corrections (JEC, JER, METFixEE2017, xy-Shift)
        if self.year == 2017 and not self.UL:
            #Apply EE noise fix for 2017 (https://twiki.cern.ch/twiki/bin/viewauth/CMS/ExoPreapprovalChecklist)
            if self.isData:
                METcorrected_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_T1_pt, event.METFixEE2017_T1_phi, event.run, self.year, self.isMC, event.PV_npvs)
            else:
                METcorrected_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_T1Smear_pt, event.METFixEE2017_T1Smear_phi, event.run, self.year, self.isMC, event.PV_npvs)

        else:
            if self.isData:
                METcorrected_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.MET_T1_pt, event.MET_T1_phi, event.run, self.year, self.isMC, event.PV_npvs)
            else:
                METcorrected_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.MET_T1Smear_pt, event.MET_T1Smear_phi, event.run, self.year, self.isMC, event.PV_npvs)

        METcorrected_pt = METcorrected_pt_phi[0]
        METcorrected_phi = METcorrected_pt_phi[1]

        #Determine if there exists two tight electrons/muons such that their invariant mass m_ll is between 60-120 GeV and the hadronic recoil >= 250 GeV
        m_ll = recoilPtMiss = lepton1_charge = lepton2_charge = 0

        #Only calculate m_ll and recoilPtMiss when two tight leptons exist (2e, 2m, or 1e1m)
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

            lepton1_charge = lepton1.charge
            lepton2_charge = lepton2.charge

        #Define skimming cuts to be applied
        #Skim = ((nTightElectrons + nTightMuons) <= 1 and njets >= 2 and event.MET_pt > 140) or ((nTightElectrons + nTightMuons) == 2 and njets >= 2)
        Skim = ((nTightElectrons + nTightMuons) <= 1 and njets >= 2 and METcorrected_pt > 230) or ((nTightElectrons + nTightMuons) == 2 and njets >= 2 and (METcorrected_pt > 230 or recoilPtMiss > 230) )

        #Signal region chosen here
        if self.signalRegion == "All":
            signalRegion = True
        elif self.signalRegion == "Skim":
            signalRegion = Skim
        else:
            signalRegion = False

        #Immediately return false if event doesn't pass skimming cut to skip calculating the rest of the branches and speed up runtime
        if not signalRegion:
            return False

        #Leading forward jet veto: veto any events where leading pT jet is in the forward region and is back-to-back with MET
        noB2Bleadingfjet = True
        if njets > 0 and nfjets > 0:
            fjetMinDeltaPhi = min(abs(forwardJets[0].phi-METcorrected_phi),2*math.pi-abs(forwardJets[0].phi-METcorrected_phi))
            if (forwardJets[0].pt_nom > centralJets[0].pt_nom) and (fjetMinDeltaPhi > 2.8):
                noB2Bleadingfjet = False

        #Systematics - JES, JER (jets)
        if self.isMC:
            if self.year == 2016:
                #Central jets  (2016)
                for sys in jesUnc:
                    jesBranches["centralJetsScale"+sys+"Up"] = filter(lambda j : ((30 < getJESjetpt(j, sys+"Up") < 50 and j.puId == 7) or getJESjetpt(j, sys+"Up") > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 7, jets)
                    jesBranches["centralJetsScale"+sys+"Down"] = filter(lambda j : ((30 < getJESjetpt(j, sys+"Down") < 50 and j.puId == 7) or getJESjetpt(j, sys+"Down") > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 7, jets)
                centralJetsResUp = filter(lambda j : ((30 < j.pt_jerUp < 50 and j.puId == 7) or j.pt_jerUp > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 7, jets)
                centralJetsResDown = filter(lambda j : ((30 < j.pt_jerDown < 50 and j.puId == 7) or j.pt_jerDown > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 7, jets)
                #Forward jets (2016)
                for sys in jesUnc:
                    jesBranches["forwardJetsScale"+sys+"Up"] = filter(lambda j : ((30 < getJESjetpt(j, sys+"Up") < 50 and j.puId == 7) or getJESjetpt(j, sys+"Up") > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 7, jets)
                    jesBranches["forwardJetsScale"+sys+"Down"] = filter(lambda j : ((30 < getJESjetpt(j, sys+"Down") < 50 and j.puId == 7) or getJESjetpt(j, sys+"Down") > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 7, jets)
                forwardJetsResUp = filter(lambda j : ((30 < j.pt_jerUp < 50 and j.puId == 7) or j.pt_jerUp > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 7, jets)
                forwardJetsResDown = filter(lambda j : ((30 < j.pt_jerDown < 50 and j.puId == 7) or j.pt_jerDown > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 7, jets)

            else:
                #Central jets (2017, 2018)
                for sys in jesUnc:
                    jesBranches["centralJetsScale"+sys+"Up"] = filter(lambda j : ((30 < getJESjetpt(j, sys+"Up") < 50 and j.puId == 7) or getJESjetpt(j, sys+"Up") > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 6, jets)
                    jesBranches["centralJetsScale"+sys+"Down"] = filter(lambda j : ((30 < getJESjetpt(j, sys+"Down") < 50 and j.puId == 7) or getJESjetpt(j, sys+"Down") > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 6, jets)
                centralJetsResUp = filter(lambda j : ((30 < j.pt_jerUp < 50 and j.puId == 7) or j.pt_jerUp > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 6, jets)
                centralJetsResDown = filter(lambda j : ((30 < j.pt_jerDown < 50 and j.puId == 7) or j.pt_jerDown > 50) and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId == 6, jets)
                #Forward jets (2017, 2018)
                for sys in jesUnc:
                    jesBranches["forwardJetsScale"+sys+"Up"] = filter(lambda j : ((30 < getJESjetpt(j, sys+"Up") < 50 and j.puId == 7) or getJESjetpt(j, sys+"Up") > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 6, jets)
                    jesBranches["forwardJetsScale"+sys+"Down"] = filter(lambda j : ((30 < getJESjetpt(j, sys+"Down") < 50 and j.puId == 7) or getJESjetpt(j, sys+"Down") > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 6, jets)
                forwardJetsResUp = filter(lambda j : ((30 < j.pt_jerUp < 50 and j.puId == 7) or j.pt_jerUp > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 6, jets)
                forwardJetsResDown = filter(lambda j : ((30 < j.pt_jerDown < 50 and j.puId == 7) or j.pt_jerDown > 50) and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId == 6, jets)

            #B-jets
            if self.btag == 'CSVv2':
                for sys in jesUnc:
                    jesBranches["bJetsScale"+sys+"Up"] = filter(lambda j : j.btagCSVV2 > btag_WP, jesBranches["centralJetsScale"+sys+"Up"])
                    jesBranches["bJetsScale"+sys+"Down"] = filter(lambda j : j.btagCSVV2 > btag_WP, jesBranches["centralJetsScale"+sys+"Down"])
                bJetsResUp = filter(lambda j : j.btagCSVV2 > btag_WP, centralJetsResUp)
                bJetsResDown = filter(lambda j : j.btagCSVV2 > btag_WP, centralJetsResDown)

            elif self.btag == 'DeepCSV':
                for sys in jesUnc:
                    jesBranches["bJetsScale"+sys+"Up"] = filter(lambda j : j.btagDeepB > btag_WP, jesBranches["centralJetsScale"+sys+"Up"])
                    jesBranches["bJetsScale"+sys+"Down"] = filter(lambda j : j.btagDeepB > btag_WP, jesBranches["centralJetsScale"+sys+"Down"])
                bJetsResUp = filter(lambda j : j.btagDeepB > btag_WP, centralJetsResUp)
                bJetsResDown = filter(lambda j : j.btagDeepB > btag_WP, centralJetsResDown)

            #Count central, forward, and b-tagged jets
            for sys in jesUnc:
                jesBranches["njetsScale"+sys+"Up"] = len(jesBranches["centralJetsScale"+sys+"Up"])
                jesBranches["njetsScale"+sys+"Down"] = len(jesBranches["centralJetsScale"+sys+"Down"])


                jesBranches["nfjetsScale"+sys+"Up"] = len(jesBranches["forwardJetsScale"+sys+"Up"])
                jesBranches["nfjetsScale"+sys+"Down"] = len(jesBranches["forwardJetsScale"+sys+"Down"])

                jesBranches["nbjetsScale"+sys+"Up"] = len(jesBranches["bJetsScale"+sys+"Up"])
                jesBranches["nbjetsScale"+sys+"Down"] = len(jesBranches["bJetsScale"+sys+"Down"])

            njetsResUp = len(centralJetsResUp)
            njetsResDown = len(centralJetsResDown)
 
            nfjetsResUp = len(forwardJetsResUp)
            nfjetsResDown = len(forwardJetsResDown)
  
            nbjetsResUp = len(bJetsResUp)
            nbjetsResDown = len(bJetsResDown)


        #Systematics - JES, JER (MET)
        if self.isMC:
            #Apply MET corrections (JEC, JER, METFixEE2017, xy-Shift)
            if self.year == 2017 and not self.UL:
                #Apply EE noise fix for 2017 (https://twiki.cern.ch/twiki/bin/viewauth/CMS/ExoPreapprovalChecklist)
                for sys in jesUnc:
                    jesBranches["METcorrected_pt_phiScale"+sys+"Up"] = ROOT.METXYCorr_Met_MetPhi(getJESMETpt(sys+"Up"), getJESMETphi(sys+"Up"), event.run, self.year, self.isMC, event.PV_npvs)
                    jesBranches["METcorrected_pt_phiScale"+sys+"Down"] = ROOT.METXYCorr_Met_MetPhi(getJESMETpt(sys+"Down"), getJESMETphi(sys+"Down"), event.run, self.year, self.isMC, event.PV_npvs)
                METcorrected_pt_phiResUp = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_T1Smear_pt_jerUp, event.METFixEE2017_T1Smear_phi_jerUp, event.run, self.year, self.isMC, event.PV_npvs)
                METcorrected_pt_phiResDown = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_T1Smear_pt_jerDown, event.METFixEE2017_T1Smear_phi_jerDown, event.run, self.year, self.isMC, event.PV_npvs)

            else:
                for sys in jesUnc:
                    jesBranches["METcorrected_pt_phiScale"+sys+"Up"] = ROOT.METXYCorr_Met_MetPhi(getJESMETpt(sys+"Up"), getJESMETphi(sys+"Up"), event.run, self.year, self.isMC, event.PV_npvs)
                    jesBranches["METcorrected_pt_phiScale"+sys+"Down"] = ROOT.METXYCorr_Met_MetPhi(getJESMETpt(sys+"Down"), getJESMETphi(sys+"Down"), event.run, self.year, self.isMC, event.PV_npvs)
                METcorrected_pt_phiResUp = ROOT.METXYCorr_Met_MetPhi(event.MET_T1Smear_pt_jerUp, event.MET_T1Smear_phi_jerUp, event.run, self.year, self.isMC, event.PV_npvs)
                METcorrected_pt_phiResDown = ROOT.METXYCorr_Met_MetPhi(event.MET_T1Smear_pt_jerDown, event.MET_T1Smear_phi_jerDown, event.run, self.year, self.isMC, event.PV_npvs)

            for sys in jesUnc:
                jesBranches["METcorrected_ptScale"+sys+"Up"] = jesBranches["METcorrected_pt_phiScale"+sys+"Up"][0]
                jesBranches["METcorrected_phiScale"+sys+"Up"] = jesBranches["METcorrected_pt_phiScale"+sys+"Up"][1]
                jesBranches["METcorrected_ptScale"+sys+"Down"] = jesBranches["METcorrected_pt_phiScale"+sys+"Down"][0]
                jesBranches["METcorrected_phiScale"+sys+"Down"] = jesBranches["METcorrected_pt_phiScale"+sys+"Down"][1]

            METcorrected_ptResUp = METcorrected_pt_phiResUp[0]
            METcorrected_phiResUp = METcorrected_pt_phiResUp[1]
            METcorrected_ptResDown = METcorrected_pt_phiResDown[0]
            METcorrected_phiResDown = METcorrected_pt_phiResDown[1]


        #Systematics - JES, JER (recoilPtMiss)
        if self.isMC:
            for sys in jesUnc:
                jesBranches["recoilPtMissScale"+sys+"Up"] = jesBranches["recoilPtMissScale"+sys+"Down"] = 0
            recoilPtMissResUp = recoilPtMissResDown = 0
            #Only calculate recoilPtMiss when two tight leptons exist (2e, 2m, or 1e1m)
            if (nTightElectrons >= 2 and nLooseMuons == 0) or (nVetoElectrons == 0 and nTightMuons >= 2):
                for sys in jesUnc:
                    jesBranches["recoilPtMissScale"+sys+"Up"] = math.sqrt(pow(jesBranches["METcorrected_ptScale"+sys+"Up"]*math.cos(jesBranches["METcorrected_phiScale"+sys+"Up"]) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(jesBranches["METcorrected_ptScale"+sys+"Up"]*math.sin(jesBranches["METcorrected_phiScale"+sys+"Up"]) + lepton1.p4().Py() + lepton2.p4().Py(), 2))
                    jesBranches["recoilPtMissScale"+sys+"Down"] = math.sqrt(pow(jesBranches["METcorrected_ptScale"+sys+"Down"]*math.cos(jesBranches["METcorrected_phiScale"+sys+"Down"]) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(jesBranches["METcorrected_ptScale"+sys+"Down"]*math.sin(jesBranches["METcorrected_phiScale"+sys+"Down"]) + lepton1.p4().Py() + lepton2.p4().Py(), 2))
                recoilPtMissResUp = math.sqrt(pow(METcorrected_ptResUp*math.cos(METcorrected_phiResUp) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(METcorrected_ptResUp*math.sin(METcorrected_phiResUp) + lepton1.p4().Py() + lepton2.p4().Py(), 2))
                recoilPtMissResDown = math.sqrt(pow(METcorrected_ptResDown*math.cos(METcorrected_phiResDown) + lepton1.p4().Px() + lepton2.p4().Px(), 2) + pow(METcorrected_ptResDown*math.sin(METcorrected_phiResDown) + lepton1.p4().Py() + lepton2.p4().Py(), 2))



        #Calculate minDeltaPhi and minDeltaPhi(j_(1,2), missing pt) preselection variable of all central jets 
        minDeltaPhi = minDeltaPhi12 = -9 #If there is less than 2 jets, set value to -9 to indicate  minDeltaPhi cannot be calculated
        deltaPhij1 = deltaPhij2 = deltaPhij3 = deltaPhib1 = deltaPhib2 = -9

        #Systematics - JES, JER
        if self.isMC:
            for sys in jesUnc:
                jesBranches["minDeltaPhiScale"+sys+"Up"] = jesBranches["minDeltaPhiScale"+sys+"Down"] = -9
                jesBranches["minDeltaPhi12Scale"+sys+"Up"] = jesBranches["minDeltaPhi12Scale"+sys+"Down"] = -9
            minDeltaPhiResUp = minDeltaPhiResDown = -9 
            minDeltaPhi12ResUp = minDeltaPhi12ResDown = -9

        if nbjets > 0:
            bjet1 = bJets[0]
            deltaPhib1 = min(abs(bjet1.phi - METcorrected_phi), 2 * math.pi - abs(bjet1.phi - METcorrected_phi))
            if nbjets > 1:
                bjet2 = bJets[1]
                deltaPhib2 = min(abs(bjet2.phi - METcorrected_phi), 2 * math.pi - abs(bjet2.phi - METcorrected_phi))

        if njets > 0:
            jet1 = centralJets[0] #jet1 is the jet with the largest pt
            minDeltaPhi = minDeltaPhi12 = deltaPhi1 = deltaPhij1 = min(abs(jet1.phi - METcorrected_phi), 2 * math.pi - abs(jet1.phi - METcorrected_phi)) #phi angle between jet1 and missing pt
            if njets > 1: #Should always be true for both SL and AH signal regions
                jet2 = centralJets[1] #jet2 is the jet with the second-largest pt
                deltaPhi2 = deltaPhij2 = min(abs(jet2.phi - METcorrected_phi), 2 * math.pi - abs(jet2.phi - METcorrected_phi)) #phi angle between jet2 and missing pt
                minDeltaPhi = minDeltaPhi12 = min(deltaPhi1, deltaPhi2) #First calculate minDeltaPhi12
                if njets > 2:
                    jet3 = centralJets[2]
                    deltaPhij3 = min(abs(jet3.phi - METcorrected_phi), 2 * math.pi - abs(jet3.phi - METcorrected_phi))
                #Now calculate minDeltaPhi 
                for i in range(2, njets):
                    jeti = centralJets[i]
                    minDeltaPhi_i = min(abs(jeti.phi - METcorrected_phi), 2 * math.pi - abs(jeti.phi - METcorrected_phi)) #phi angle between jeti and missing pt
                    if minDeltaPhi_i < minDeltaPhi: #Choose lowest minDeltaPhi out of all central jets
                        minDeltaPhi = minDeltaPhi_i

        #Systematics - JES, JER
        if self.isMC:
            #JES (including split uncertainties)
            for sys in jesUnc:
                #First do JES up variation
                if jesBranches["njetsScale"+sys+"Up"] > 0:
                    jesBranches["jet1Scale"+sys+"Up"] = jesBranches["centralJetsScale"+sys+"Up"][0] #jet1 is the jet with the largest pt
                    jesBranches["minDeltaPhiScale"+sys+"Up"] = jesBranches["minDeltaPhi12Scale"+sys+"Up"] = jesBranches["deltaPhi1Scale"+sys+"Up"] = min(abs(jesBranches["jet1Scale"+sys+"Up"].phi - jesBranches["METcorrected_phiScale"+sys+"Up"]), 2 * math.pi - abs(jesBranches["jet1Scale"+sys+"Up"].phi - jesBranches["METcorrected_phiScale"+sys+"Up"]))
                    if jesBranches["njetsScale"+sys+"Up"] > 1: #Should always be true for both SL and AH signal regions
                        jesBranches["jet2Scale"+sys+"Up"] = jesBranches["centralJetsScale"+sys+"Up"][1] #jet2 is the jet with the second-largest pt
                        jesBranches["deltaPhi2Scale"+sys+"Up"] = min(abs(jesBranches["jet2Scale"+sys+"Up"].phi - jesBranches["METcorrected_phiScale"+sys+"Up"]), 2 * math.pi - abs(jesBranches["jet2Scale"+sys+"Up"].phi - jesBranches["METcorrected_phiScale"+sys+"Up"]))
                        jesBranches["minDeltaPhiScale"+sys+"Up"] = jesBranches["minDeltaPhi12Scale"+sys+"Up"] = min(jesBranches["deltaPhi1Scale"+sys+"Up"], jesBranches["deltaPhi2Scale"+sys+"Up"])
                        for i in range(2, jesBranches["njetsScale"+sys+"Up"]):
                            jesBranches["jetiScale"+sys+"Up"] = jesBranches["centralJetsScale"+sys+"Up"][i]
                            jesBranches["minDeltaPhiScale"+sys+"Up_i"] = min(abs(jesBranches["jetiScale"+sys+"Up"].phi - jesBranches["METcorrected_phiScale"+sys+"Up"]), 2 * math.pi - abs(jesBranches["jetiScale"+sys+"Up"].phi - jesBranches["METcorrected_phiScale"+sys+"Up"])) #phi angle between jeti and missing pt
                            if jesBranches["minDeltaPhiScale"+sys+"Up_i"] < jesBranches["minDeltaPhiScale"+sys+"Up"]: #Choose lowest minDeltaPhi out of all central jets
                                jesBranches["minDeltaPhiScale"+sys+"Up"] = jesBranches["minDeltaPhiScale"+sys+"Up_i"]
                #Then do JES down variation
                if jesBranches["njetsScale"+sys+"Down"] > 0:
                    jesBranches["jet1Scale"+sys+"Down"] = jesBranches["centralJetsScale"+sys+"Down"][0] #jet1 is the jet with the largest pt
                    jesBranches["minDeltaPhiScale"+sys+"Down"] = jesBranches["minDeltaPhi12Scale"+sys+"Down"] = jesBranches["deltaPhi1Scale"+sys+"Down"] = min(abs(jesBranches["jet1Scale"+sys+"Down"].phi - jesBranches["METcorrected_phiScale"+sys+"Down"]), 2 * math.pi - abs(jesBranches["jet1Scale"+sys+"Down"].phi - jesBranches["METcorrected_phiScale"+sys+"Down"]))
                    if jesBranches["njetsScale"+sys+"Down"] > 1: #Should always be true for both SL and AH signal regions
                        jesBranches["jet2Scale"+sys+"Down"] = jesBranches["centralJetsScale"+sys+"Down"][1] #jet2 is the jet with the second-largest pt
                        jesBranches["deltaPhi2Scale"+sys+"Down"] = min(abs(jesBranches["jet2Scale"+sys+"Down"].phi - jesBranches["METcorrected_phiScale"+sys+"Down"]), 2 * math.pi - abs(jesBranches["jet2Scale"+sys+"Down"].phi - jesBranches["METcorrected_phiScale"+sys+"Down"]))
                        jesBranches["minDeltaPhiScale"+sys+"Down"] = jesBranches["minDeltaPhi12Scale"+sys+"Down"] = min(jesBranches["deltaPhi1Scale"+sys+"Down"], jesBranches["deltaPhi2Scale"+sys+"Down"])
                        for i in range(2, jesBranches["njetsScale"+sys+"Down"]):
                            jesBranches["jetiScale"+sys+"Down"] = jesBranches["centralJetsScale"+sys+"Down"][i]
                            jesBranches["minDeltaPhiScale"+sys+"Down_i"] = min(abs(jesBranches["jetiScale"+sys+"Down"].phi - jesBranches["METcorrected_phiScale"+sys+"Down"]), 2 * math.pi - abs(jesBranches["jetiScale"+sys+"Down"].phi - jesBranches["METcorrected_phiScale"+sys+"Down"])) #phi angle between jeti and missing pt
                            if jesBranches["minDeltaPhiScale"+sys+"Down_i"] < jesBranches["minDeltaPhiScale"+sys+"Down"]: #Choose lowest minDeltaPhi out of all central jets
                                jesBranches["minDeltaPhiScale"+sys+"Down"] = jesBranches["minDeltaPhiScale"+sys+"Down_i"]
            #JER up variation
            if njetsResUp > 0:
                jet1ResUp = centralJetsResUp[0] #jet1 is the jet with the largest pt
                minDeltaPhiResUp = minDeltaPhi12ResUp = deltaPhi1ResUp = min(abs(jet1ResUp.phi - METcorrected_phiResUp), 2 * math.pi - abs(jet1ResUp.phi - METcorrected_phiResUp)) #phi angle between jet1 and missing pt
                if njetsResUp > 1: #Should always be true for both SL and AH signal regions
                    jet2ResUp = centralJetsResUp[1] #jet2 is the jet with the second-largest pt
                    deltaPhi2ResUp = min(abs(jet2ResUp.phi - METcorrected_phiResUp), 2 * math.pi - abs(jet2ResUp.phi - METcorrected_phiResUp)) #phi angle between jet2 and missing pt
                    minDeltaPhiResUp = minDeltaPhi12ResUp = min(deltaPhi1ResUp, deltaPhi2ResUp) #First calculate minDeltaPhi12
                    #Now calculate minDeltaPhi 
                    for i in range(2, njetsResUp):
                        jetiResUp = centralJetsResUp[i]
                        minDeltaPhiResUp_i = min(abs(jetiResUp.phi - METcorrected_phiResUp), 2 * math.pi - abs(jetiResUp.phi - METcorrected_phiResUp)) #phi angle between jeti and missing pt
                        if minDeltaPhiResUp_i < minDeltaPhiResUp: #Choose lowest minDeltaPhi out of all central jets
                            minDeltaPhiResUp = minDeltaPhiResUp_i
            #JER down variation
            if njetsResDown > 0:
                jet1ResDown = centralJetsResDown[0] #jet1 is the jet with the largest pt
                minDeltaPhiResDown = minDeltaPhi12ResDown = deltaPhi1ResDown = min(abs(jet1ResDown.phi - METcorrected_phiResDown), 2 * math.pi - abs(jet1ResDown.phi - METcorrected_phiResDown)) #phi angle between jet1 and missing pt
                if njetsResDown > 1: #Should always be true for both SL and AH signal regions
                    jet2ResDown = centralJetsResDown[1] #jet2 is the jet with the second-largest pt
                    deltaPhi2ResDown = min(abs(jet2ResDown.phi - METcorrected_phiResDown), 2 * math.pi - abs(jet2ResDown.phi - METcorrected_phiResDown)) #phi angle between jet2 and missing pt
                    minDeltaPhiResDown = minDeltaPhi12ResDown = min(deltaPhi1ResDown, deltaPhi2ResDown) #First calculate minDeltaPhi12
                    #Now calculate minDeltaPhi 
                    for i in range(2, njetsResDown):
                        jetiResDown = centralJetsResDown[i]
                        minDeltaPhiResDown_i = min(abs(jetiResDown.phi - METcorrected_phiResDown), 2 * math.pi - abs(jetiResDown.phi - METcorrected_phiResDown)) #phi angle between jeti and missing pt
                        if minDeltaPhiResDown_i < minDeltaPhiResDown: #Choose lowest minDeltaPhi out of all central jets
                            minDeltaPhiResDown = minDeltaPhiResDown_i

        #Jet TLorentzVectors are constructed to calculate M_T2^W and topness variables
        ljetVector = ROOT.vector("TLorentzVector")()
        bjetVector = ROOT.vector("TLorentzVector")()
        #Systematics - JES, JER
        if self.isMC:
            for sys in jesUnc:
                jesBranches["ljetVectorScale"+sys+"Up"] = ROOT.vector("TLorentzVector")()
                jesBranches["bjetVectorScale"+sys+"Up"] = ROOT.vector("TLorentzVector")()
                jesBranches["ljetVectorScale"+sys+"Down"] = ROOT.vector("TLorentzVector")()
                jesBranches["bjetVectorScale"+sys+"Down"] = ROOT.vector("TLorentzVector")()
            ljetVectorResUp = ROOT.vector("TLorentzVector")()
            bjetVectorResUp = ROOT.vector("TLorentzVector")()
            ljetVectorResDown = ROOT.vector("TLorentzVector")()
            bjetVectorResDown = ROOT.vector("TLorentzVector")()

        #Calculate jet1p_T/H_T
        H_T = 0
        jet1p_TH_T = 9 #If there are no jets, set value to +9 to indicate jet1p_T/H_T cannnot be calculated
        #Systematics - JES, JER
        if self.isMC:
            for sys in jesUnc:
                jesBranches["H_TScale"+sys+"Up"] = jesBranches["H_TScale"+sys+"Down"] = 0
                jesBranches["jet1p_TH_TScale"+sys+"Up"] = jesBranches["jet1p_TH_TScale"+sys+"Down"] = -9
            H_TResUp = H_TResDown = 0
            jet1p_TH_TResUp = jet1p_TH_TResDown = -9
        
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
        if self.isMC:
            for sys in jesUnc:
                if jesBranches["njetsScale"+sys+"Up"] > 0:
                    for jetScaleUp in jesBranches["centralJetsScale"+sys+"Up"]:
                        jesBranches["H_TScale"+sys+"Up"] += getJESjetpt(jetScaleUp, sys+"Up")
                        if self.btag == 'CSVv2':
                            jetScaleUp_btag = jetScaleUp.btagCSVV2
                        elif self.btag == 'DeepCSV':
                            jetScaleUp_btag = jetScaleUp.btagDeepB
                        if jetScaleUp_btag < btag_WP:
                            jesBranches["ljetVectorScale"+sys+"Up"].push_back(jetScaleUp.p4()*(getJESjetpt(jetScaleUp, sys+"Up")/jetScaleUp.pt_nom))
                    jesBranches["jet1p_TH_TScale"+sys+"Up"] = getJESjetpt(jesBranches["centralJetsScale"+sys+"Up"][0], sys+"Up")/jesBranches["H_TScale"+sys+"Up"]

                if jesBranches["njetsScale"+sys+"Down"] > 0:
                    for jetScaleDown in jesBranches["centralJetsScale"+sys+"Down"]:
                        jesBranches["H_TScale"+sys+"Down"] += getJESjetpt(jetScaleDown, sys+"Down")
                        if self.btag == 'CSVv2':
                            jetScaleDown_btag = jetScaleDown.btagCSVV2
                        elif self.btag == 'DeepCSV':
                            jetScaleDown_btag = jetScaleDown.btagDeepB
                        if jetScaleDown_btag < btag_WP:
                            jesBranches["ljetVectorScale"+sys+"Down"].push_back(jetScaleDown.p4()*(getJESjetpt(jetScaleDown, sys+"Down")/jetScaleDown.pt_nom))
                    jesBranches["jet1p_TH_TScale"+sys+"Down"] = getJESjetpt(jesBranches["centralJetsScale"+sys+"Down"][0], sys+"Down")/jesBranches["H_TScale"+sys+"Down"]

            if njetsResUp > 0:
                for jetResUp in centralJetsResUp:
                    H_TResUp += jetResUp.pt_jerUp
                    if self.btag == 'CSVv2':
                        jetResUp_btag = jetResUp.btagCSVV2
                    elif self.btag == 'DeepCSV':
                        jetResUp_btag = jetResUp.btagDeepB
                    if jetResUp_btag < btag_WP:
                        ljetVectorResUp.push_back(jetResUp.p4()*(jetResUp.pt_jerUp/jetResUp.pt_nom))
                jet1p_TH_TResUp = centralJetsResUp[0].pt_jerUp/H_TResUp

            if njetsResDown > 0:
                for jetResDown in centralJetsResDown:
                    H_TResDown += jetResDown.pt_jerDown
                    if self.btag == 'CSVv2':
                        jetResDown_btag = jetResDown.btagCSVV2
                    elif self.btag == 'DeepCSV':
                        jetResDown_btag = jetResDown.btagDeepB
                    if jetResDown_btag < btag_WP:
                        ljetVectorResDown.push_back(jetResDown.p4()*(jetResDown.pt_jerDown/jetResDown.pt_nom))
                jet1p_TH_TResDown = centralJetsResDown[0].pt_jerDown/H_TResDown

        #Calculate M_T^b
        M_Tb = -9 #If there are no bjets, set value to -9 to indicate M_Tb cannot be calculated
        #Systematics - JES, JER
        if self.isMC:
            for sys in jesUnc:
                jesBranches["M_TbScale"+sys+"Up"] = jesBranches["M_TbScale"+sys+"Down"] = -9
            M_TbResUp = M_TbResDown = -9
        
        if nbjets > 0:
            bjet1 = bJets[0]
            for bjet in bJets:
                bjetVector.push_back(bjet.p4())
                if self.btag == 'CSVv2':
                    bjet_btag = bjet.btagCSVV2
                    bjet1_btag = bjet1.btagCSVV2
                elif self.btag == 'DeepCSV':
                    bjet_btag = bjet.btagDeepB
                    bjet1_btag = bjet1.btagDeepB
                if bjet_btag > bjet1_btag:
                    bjet1 = bjet

            deltaPhiMTb = bjet1.phi - METcorrected_phi
            M_Tb = math.sqrt(2 * METcorrected_pt * bjet1.pt_nom * (1 - math.cos(deltaPhiMTb)))

        #Systematics - JES, JER
        if self.isMC:
            for sys in jesUnc:
                if jesBranches["nbjetsScale"+sys+"Up"] > 0:
                    bjetScaleUp1 = jesBranches["bJetsScale"+sys+"Up"][0]
                    for bjetScaleUp in jesBranches["bJetsScale"+sys+"Up"]:
                        jesBranches["bjetVectorScale"+sys+"Up"].push_back(bjetScaleUp.p4()*(getJESjetpt(bjetScaleUp, sys+"Up")/bjetScaleUp.pt_nom))
                        if self.btag == 'CSVv2':
                            bjetScaleUp_btag = bjetScaleUp.btagCSVV2
                            bjetScaleUp1_btag = bjetScaleUp1.btagCSVV2
                        elif self.btag == 'DeepCSV':
                            bjetScaleUp_btag = bjetScaleUp.btagDeepB
                            bjetScaleUp1_btag = bjetScaleUp1.btagDeepB
                        if bjetScaleUp_btag > bjetScaleUp1_btag:
                            bjetScaleUp1 = bjetScaleUp

                    jesBranches["deltaPhiMTbScale"+sys+"Up"] = bjetScaleUp1.phi - jesBranches["METcorrected_phiScale"+sys+"Up"]
                    jesBranches["M_TbScale"+sys+"Up"] = math.sqrt(2 * jesBranches["METcorrected_ptScale"+sys+"Up"] * getJESjetpt(bjetScaleUp1, sys+"Up") * (1 - math.cos(jesBranches["deltaPhiMTbScale"+sys+"Up"])))

                if jesBranches["nbjetsScale"+sys+"Down"] > 0:
                    bjetScaleDown1 = jesBranches["bJetsScale"+sys+"Down"][0]
                    for bjetScaleDown in jesBranches["bJetsScale"+sys+"Down"]:
                        jesBranches["bjetVectorScale"+sys+"Down"].push_back(bjetScaleDown.p4()*(getJESjetpt(bjetScaleDown, sys+"Down")/bjetScaleDown.pt_nom))
                        if self.btag == 'CSVv2':
                            bjetScaleDown_btag = bjetScaleDown.btagCSVV2
                            bjetScaleDown1_btag = bjetScaleDown1.btagCSVV2
                        elif self.btag == 'DeepCSV':
                            bjetScaleDown_btag = bjetScaleDown.btagDeepB
                            bjetScaleDown1_btag = bjetScaleDown1.btagDeepB
                        if bjetScaleDown_btag > bjetScaleDown1_btag:
                            bjetScaleDown1 = bjetScaleDown

                    jesBranches["deltaPhiMTbScale"+sys+"Down"] = bjetScaleDown1.phi - jesBranches["METcorrected_phiScale"+sys+"Down"]
                    jesBranches["M_TbScale"+sys+"Down"] = math.sqrt(2 * jesBranches["METcorrected_ptScale"+sys+"Down"] * getJESjetpt(bjetScaleDown1, sys+"Down") * (1 - math.cos(jesBranches["deltaPhiMTbScale"+sys+"Down"])))

            if nbjetsResUp > 0:
                bjetResUp1 = bJetsResUp[0]
                for bjetResUp in bJetsResUp:
                    bjetVectorResUp.push_back(bjetResUp.p4()*(bjetResUp.pt_jerUp/bjetResUp.pt_nom))
                    if self.btag == 'CSVv2':
                        bjetResUp_btag = bjetResUp.btagCSVV2
                        bjetResUp1_btag = bjetResUp1.btagCSVV2
                    elif self.btag == 'DeepCSV':
                        bjetResUp_btag = bjetResUp.btagDeepB
                        bjetResUp1_btag = bjetResUp1.btagDeepB
                    if bjetResUp_btag > bjetResUp1_btag:
                        bjetResUp1 = bjetResUp

                deltaPhiMTbResUp = bjetResUp1.phi - METcorrected_phiResUp
                M_TbResUp = math.sqrt(2 * METcorrected_ptResUp * bjetResUp1.pt_jerUp * (1 - math.cos(deltaPhiMTbResUp)))

            if nbjetsResDown > 0:
                bjetResDown1 = bJetsResDown[0]
                for bjetResDown in bJetsResDown:
                    bjetVectorResDown.push_back(bjetResDown.p4()*(bjetResDown.pt_jerDown/bjetResDown.pt_nom))
                    if self.btag == 'CSVv2':
                        bjetResDown_btag = bjetResDown.btagCSVV2
                        bjetResDown1_btag = bjetResDown1.btagCSVV2
                    elif self.btag == 'DeepCSV':
                        bjetResDown_btag = bjetResDown.btagDeepB
                        bjetResDown1_btag = bjetResDown1.btagDeepB
                    if bjetResDown_btag > bjetResDown1_btag:
                        bjetResDown1 = bjetResDown
            
                deltaPhiMTbResDown = bjetResDown1.phi - METcorrected_phiResDown
                M_TbResDown = math.sqrt(2 * METcorrected_ptResDown * bjetResDown1.pt_jerDown * (1 - math.cos(deltaPhiMTbResDown)))

        #Calculate M_T, M_T2^W, M_T2^ll, and topness variables using PFMET
        M_T = M_T2W = M_T2ll  = -9 #If there are not enough tight leptons, set value to -9 to indicate variable cannot be calculated
        modified_topness = full_topness = -999
        full_topness = -999
        #Systematics - JES, JER
        if self.isMC:
            for sys in jesUnc:
                jesBranches["M_TScale"+sys+"Up"] = jesBranches["M_TScale"+sys+"Down"] = -9
                jesBranches["M_T2WScale"+sys+"Up"] = jesBranches["M_T2WScale"+sys+"Down"] = -9
                jesBranches["M_T2llScale"+sys+"Up"] = jesBranches["M_T2llScale"+sys+"Down"] = -9
                jesBranches["modified_topnessScale"+sys+"Up"] = jesBranches["modified_topnessScale"+sys+"Down"] = -999
                jesBranches["full_topnessScale"+sys+"Up"] = jesBranches["full_topnessScale"+sys+"Down"] = -999
            M_TResUp = M_TResDown = -9
            M_T2WResUp = M_T2WResDown = -9
            M_T2llResUp = M_T2llResDown = -9
            modified_topnessResUp = modified_topnessResDown = -999
            full_topnessResUp = full_topnessResDown = -999

        if nTightElectrons > 0 or nTightMuons > 0: #Default to using electron if both tight electron and muon exist
            if nTightElectrons > 0:
                lepton = tightElectrons[0] #Default to using tight electron with greatest pT
            elif nTightMuons > 0:
                lepton = tightMuons[0] #Default to using tight muon with greatest pT

            #Calculate M_T
            deltaPhiMT = lepton.phi - METcorrected_phi
            M_T = math.sqrt(2 * METcorrected_pt * lepton.pt * (1 - math.cos(deltaPhiMT)))
            #Systematics - JES, JER
            if self.isMC:
                for sys in jesUnc:
                    jesBranches["deltaPhiMTScale"+sys+"Up"] = lepton.phi - jesBranches["METcorrected_phiScale"+sys+"Up"]
                    jesBranches["M_TScale"+sys+"Up"] = math.sqrt(2 * jesBranches["METcorrected_ptScale"+sys+"Up"] * lepton.pt * (1 - math.cos(jesBranches["deltaPhiMTScale"+sys+"Up"])))
                    jesBranches["deltaPhiMTScale"+sys+"Down"] = lepton.phi - jesBranches["METcorrected_phiScale"+sys+"Down"]
                    jesBranches["M_TScale"+sys+"Down"] = math.sqrt(2 * jesBranches["METcorrected_ptScale"+sys+"Down"] * lepton.pt * (1 - math.cos(jesBranches["deltaPhiMTScale"+sys+"Down"])))
                deltaPhiMTResUp = lepton.phi - METcorrected_phiResUp
                M_TResUp = math.sqrt(2 * METcorrected_ptResUp * lepton.pt * (1 - math.cos(deltaPhiMTResUp)))
                deltaPhiMTResDown = lepton.phi - METcorrected_phiResDown
                M_TResDown = math.sqrt(2 * METcorrected_ptResDown * lepton.pt * (1 - math.cos(deltaPhiMTResDown)))

            #Calculate M_T2^W 
            leptonTLorentz = lepton.p4()
            metTVector2 = ROOT.TVector2(METcorrected_pt * math.cos(METcorrected_phi), METcorrected_pt * math.sin(METcorrected_phi))
            M_T2W = Mt2Com_bisect.calculateMT2w(ljetVector, bjetVector, leptonTLorentz, metTVector2, "MT2w")
            #Systematics - JES, JER
            if self.isMC:
                for sys in jesUnc:
                    jesBranches["metTVector2Scale"+sys+"Up"] = ROOT.TVector2(jesBranches["METcorrected_ptScale"+sys+"Up"] * math.cos(jesBranches["METcorrected_phiScale"+sys+"Up"]), jesBranches["METcorrected_ptScale"+sys+"Up"] * math.sin(jesBranches["METcorrected_phiScale"+sys+"Up"]))
                    jesBranches["M_T2WScale"+sys+"Up"] = Mt2Com_bisect.calculateMT2w(jesBranches["ljetVectorScale"+sys+"Up"], jesBranches["bjetVectorScale"+sys+"Up"], leptonTLorentz, jesBranches["metTVector2Scale"+sys+"Up"], "MT2w")
                    jesBranches["metTVector2Scale"+sys+"Down"] = ROOT.TVector2(jesBranches["METcorrected_ptScale"+sys+"Down"] * math.cos(jesBranches["METcorrected_phiScale"+sys+"Down"]), jesBranches["METcorrected_ptScale"+sys+"Down"] * math.sin(jesBranches["METcorrected_phiScale"+sys+"Down"]))
                    jesBranches["M_T2WScale"+sys+"Down"] = Mt2Com_bisect.calculateMT2w(jesBranches["ljetVectorScale"+sys+"Down"], jesBranches["bjetVectorScale"+sys+"Down"], leptonTLorentz, jesBranches["metTVector2Scale"+sys+"Down"], "MT2w")
                metTVector2ResUp = ROOT.TVector2(METcorrected_ptResUp * math.cos(METcorrected_phiResUp), METcorrected_ptResUp * math.sin(METcorrected_phiResUp))
                M_T2WResUp = Mt2Com_bisect.calculateMT2w(ljetVectorResUp, bjetVectorResUp, leptonTLorentz, metTVector2ResUp, "MT2w")
                metTVector2ResDown = ROOT.TVector2(METcorrected_ptResDown * math.cos(METcorrected_phiResDown), METcorrected_ptResDown * math.sin(METcorrected_phiResDown))
                M_T2WResDown = Mt2Com_bisect.calculateMT2w(ljetVectorResDown, bjetVectorResDown, leptonTLorentz, metTVector2ResDown, "MT2w")

            #Only calculate topness variables when a single tight lepton exists (1e or 1m)
            if (nTightElectrons + nTightMuons) == 1:
                modified_topness = ROOT.CalcTopness_(1, METcorrected_pt, METcorrected_phi, leptonTLorentz, bjetVector, ljetVector)
                full_topness = ROOT.CalcTopness_(2, METcorrected_pt, METcorrected_phi, leptonTLorentz, bjetVector, ljetVector)
                #Systematics - JES, JER
                if self.isMC:
                    for sys in jesUnc:
                        jesBranches["modified_topnessScale"+sys+"Up"] = ROOT.CalcTopness_(1, jesBranches["METcorrected_ptScale"+sys+"Up"], jesBranches["METcorrected_phiScale"+sys+"Up"], leptonTLorentz, jesBranches["bjetVectorScale"+sys+"Up"], jesBranches["ljetVectorScale"+sys+"Up"])
                        jesBranches["full_topnessScale"+sys+"Up"] = ROOT.CalcTopness_(2, jesBranches["METcorrected_ptScale"+sys+"Up"], jesBranches["METcorrected_phiScale"+sys+"Up"], leptonTLorentz, jesBranches["bjetVectorScale"+sys+"Up"], jesBranches["ljetVectorScale"+sys+"Up"])
                        jesBranches["modified_topnessScale"+sys+"Down"] = ROOT.CalcTopness_(1, jesBranches["METcorrected_ptScale"+sys+"Down"], jesBranches["METcorrected_phiScale"+sys+"Down"], leptonTLorentz, jesBranches["bjetVectorScale"+sys+"Down"], jesBranches["ljetVectorScale"+sys+"Down"])
                        jesBranches["full_topnessScale"+sys+"Down"] = ROOT.CalcTopness_(2, jesBranches["METcorrected_ptScale"+sys+"Down"], jesBranches["METcorrected_phiScale"+sys+"Down"], leptonTLorentz, jesBranches["bjetVectorScale"+sys+"Down"], jesBranches["ljetVectorScale"+sys+"Down"])
                    modified_topnessResUp = ROOT.CalcTopness_(1, METcorrected_ptResUp, METcorrected_phiResUp, leptonTLorentz, bjetVectorResUp, ljetVectorResUp)
                    full_topnessResUp = ROOT.CalcTopness_(2, METcorrected_ptResUp, METcorrected_phiResUp, leptonTLorentz, bjetVectorResUp, ljetVectorResUp)
                    modified_topnessResDown = ROOT.CalcTopness_(1, METcorrected_ptResDown, METcorrected_phiResDown, leptonTLorentz, bjetVectorResDown, ljetVectorResDown)
                    full_topnessResDown = ROOT.CalcTopness_(2, METcorrected_ptResDown, METcorrected_phiResDown, leptonTLorentz, bjetVectorResDown, ljetVectorResDown)
                
            
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

            desiredPrecisionOnM_T2ll = 0 #Must be >= 0. If = 0 algorithm aims for machine precision. If > 0 MT2 computed to supplied absolute precision

            M_T2ll = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMiss,pyMiss,chiA,chiB,desiredPrecisionOnM_T2ll)

            #Systematics - JES, JER
            if self.isMC:
                for sys in jesUnc:
                    jesBranches["pxMissScale"+sys+"Up"] = jesBranches["METcorrected_ptScale"+sys+"Up"]*math.cos(jesBranches["METcorrected_phiScale"+sys+"Up"])
                    jesBranches["pyMissScale"+sys+"Up"] = jesBranches["METcorrected_ptScale"+sys+"Up"]*math.sin(jesBranches["METcorrected_phiScale"+sys+"Up"])
                    jesBranches["pxMissScale"+sys+"Down"] = jesBranches["METcorrected_ptScale"+sys+"Down"]*math.cos(jesBranches["METcorrected_phiScale"+sys+"Down"])
                    jesBranches["pyMissScale"+sys+"Down"] = jesBranches["METcorrected_ptScale"+sys+"Down"]*math.sin(jesBranches["METcorrected_phiScale"+sys+"Down"])

                    jesBranches["M_T2llScale"+sys+"Up"] = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,jesBranches["pxMissScale"+sys+"Up"],jesBranches["pyMissScale"+sys+"Up"],chiA,chiB,desiredPrecisionOnM_T2ll)
                    jesBranches["M_T2llScale"+sys+"Down"] = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,jesBranches["pxMissScale"+sys+"Down"],jesBranches["pyMissScale"+sys+"Down"],chiA,chiB,desiredPrecisionOnM_T2ll)

                pxMissResUp = METcorrected_ptResUp*math.cos(METcorrected_phiResUp)
                pyMissResUp = METcorrected_ptResUp*math.sin(METcorrected_phiResUp)
                pxMissResDown = METcorrected_ptResDown*math.cos(METcorrected_phiResDown)
                pyMissResDown = METcorrected_ptResDown*math.sin(METcorrected_phiResDown)
                
                M_T2llResUp = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMissResUp,pyMissResUp,chiA,chiB,desiredPrecisionOnM_T2ll)
                M_T2llResDown = asymm_mt2_lester_bisect.get_mT2(mVisA,pxA,pyA,mVisB,pxB,pyB,pxMissResDown,pyMissResDown,chiA,chiB,desiredPrecisionOnM_T2ll)
        
        #Tau candidates are counted
        tauCandidates = Collection(event, "Tau")
        if self.isSignal and self.year == 2016:
            skimmedTaus = filter(lambda tau : tau.pt > 20 and abs(tau.eta) < 2.3 and tau.idMVAoldDM >= 31 and cleanJet(tau), tauCandidates)
        else:
            skimmedTaus = filter(lambda tau : tau.pt > 20 and abs(tau.eta) < 2.3 and tau.idMVAoldDM2017v2 >= 31 and cleanJet(tau), tauCandidates)
        ntaus = len(skimmedTaus)

        #Only calculate scale factors if sample is MC
        if self.isMC:

            if not self.isSignal:
                #Calculate PDF up/down systematics
                if event.nLHEPdfWeight > 0:
                    pdfWeights = [event.LHEPdfWeight[i] for i in range(event.nLHEPdfWeight)]
                    pdfMean = sum(pdfWeights)/event.nLHEPdfWeight
                    pdfSquareSum = sum(i*i for i in pdfWeights)
                    pdfRMS = math.sqrt(pdfSquareSum/event.nLHEPdfWeight - pdfMean*pdfMean)
                    pdfWeightUp = 1 + pdfRMS
                    pdfWeightDown = 1 - pdfRMS
                else:
                    pdfWeightUp = pdfWeightDown = 1

                #Get QCD renormalization and factorization scale weight systematics (see [1] for more info)
                #[1] https://hypernews.cern.ch/HyperNews/CMS/get/physTools/3663.html?inline=-1
                if event.nLHEScaleWeight > 0:
                    qcdRenWeightUp = event.LHEScaleWeight[7]
                    qcdRenWeightDown = event.LHEScaleWeight[1]
                    qcdFacWeightUp = event.LHEScaleWeight[5]
                    qcdFacWeightDown = event.LHEScaleWeight[3]
                else:
                    qcdRenWeightUp = qcdRenWeightDown = qcdFacWeightUp = qcdFacWeightDown = 1

            #Calculate lepton scale factor and trigger weights
            leptonWeight = leptonWeightUp = leptonWeightDown = 1
            electronWeight = electronWeightUp = electronWeightDown = 1
            muonWeight = muonWeightUp = muonWeightDown = 1
            electronTriggerWeight = electronTriggerWeightUp = electronTriggerWeightDown = 1
            muonTriggerWeight = muonTriggerWeightUp = muonTriggerWeightDown = 1

            for tightElectron in tightElectrons:
                leptonWeight *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, 0)
                leptonWeightUp *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, 1)
                leptonWeightDown *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, -1)

                electronWeight *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, 0)
                electronWeightUp *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, 1)
                electronWeightDown *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta, -1)

                electronTriggerWeight *= self.eleSFs.getWeight(tightElectron.pt, tightElectron.eta, 0)
                electronTriggerWeightUp *= self.eleSFs.getWeight(tightElectron.pt, tightElectron.eta, 1)
                electronTriggerWeightDown *= self.eleSFs.getWeight(tightElectron.pt, tightElectron.eta, -1)

            for tightMuon in tightMuons:
                leptonWeight *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, 0)
                leptonWeightUp *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, 1)
                leptonWeightDown *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, -1)

                muonWeight *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, 0)
                muonWeightUp *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, 1)
                muonWeightDown *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta, -1)

                muonTriggerWeight *= self.muSFs.getWeight(tightMuon.pt, tightMuon.eta, event.run, 0)
                muonTriggerWeightUp *= self.muSFs.getWeight(tightMuon.pt, tightMuon.eta, event.run, 1)
                muonTriggerWeightDown *= self.muSFs.getWeight(tightMuon.pt, tightMuon.eta, event.run, -1)

            #Calculate MET trigger weight
            METTriggerWeight = self.METSFs.getSF(METcorrected_pt)

            #Calculate EE L1 prefiring weight
            EE_L1_prefire_Weight = EE_L1_prefire_WeightUp = EE_L1_prefire_WeightDown = 1

            if self.year == 2016 or self.year == 2017:
                EE_L1_prefire_Weight = event.L1PreFiringWeight_Nom
                EE_L1_prefire_WeightUp = event.L1PreFiringWeight_Up
                EE_L1_prefire_WeightDown = event.L1PreFiringWeight_Dn

            #Calculate b-jet scale factor weight
            bjetWeight = self.btagTool.getWeight(centralJets)
            bjetWeightbcUpCorrelated = self.btagToolbcUpCorrelated.getWeight(centralJets)
            bjetWeightbcDownCorrelated = self.btagToolbcDownCorrelated.getWeight(centralJets)
            bjetWeightbcUpUncorrelated = self.btagToolbcUpUncorrelated.getWeight(centralJets)
            bjetWeightbcDownUncorrelated = self.btagToolbcDownUncorrelated.getWeight(centralJets)
            bjetWeightlightUpCorrelated = self.btagToollightUpCorrelated.getWeight(centralJets)
            bjetWeightlightDownCorrelated = self.btagToollightDownCorrelated.getWeight(centralJets)
            bjetWeightlightUpUncorrelated = self.btagToollightUpUncorrelated.getWeight(centralJets)
            bjetWeightlightDownUncorrelated = self.btagToollightDownUncorrelated.getWeight(centralJets)

            #Calculate PU weight
            puWeight = self.puTool.getWeight(event.Pileup_nTrueInt)
            puWeightUp = self.puToolUp.getWeight(event.Pileup_nTrueInt)
            puWeightDown = self.puToolDown.getWeight(event.Pileup_nTrueInt)

            #Calculate EWK and QCD k factors if a Gen V particles exists (Z or W)
            ewkWWeight = ewkZWeight = qcdWWeight = qcdZTo2NuWeight = qcdZTo2LWeight = 1
            qcdWWeightRenUp = qcdWWeightRenDown = qcdWWeightFacUp = qcdWWeightFacDown = 1
            qcdZTo2NuWeightRenUp = qcdZTo2NuWeightRenDown = qcdZTo2NuWeightFacUp = qcdZTo2NuWeightFacDown = 1
            qcdZTo2LWeightRenUp = qcdZTo2LWeightRenDown = qcdZTo2LWeightFacUp = qcdZTo2LWeightFacDown = 1
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
                qcdZTo2NuWeightRenUp *= self.kFactorTool.getRenUpZTo2Nu(GenV_pt)
                qcdZTo2NuWeightRenDown *= self.kFactorTool.getRenDownZTo2Nu(GenV_pt)
                qcdZTo2NuWeightFacUp *= self.kFactorTool.getFacUpZTo2Nu(GenV_pt)
                qcdZTo2NuWeightFacDown *= self.kFactorTool.getFacDownZTo2Nu(GenV_pt)
                qcdZTo2LWeightRenUp *= self.kFactorTool.getRenUpZTo2L(GenV_pt)
                qcdZTo2LWeightRenDown *= self.kFactorTool.getRenDownZTo2L(GenV_pt)
                qcdZTo2LWeightFacUp *= self.kFactorTool.getFacUpZTo2L(GenV_pt)
                qcdZTo2LWeightFacDown *= self.kFactorTool.getFacDownZTo2L(GenV_pt)

            #Calculate parton shower weights
            PSWeightISRUp = PSWeightISRDown = PSWeightFSRUp = PSWeightFSRDown = 1
            if event.nPSWeight == 4:
                PSWeightISRUp = event.PSWeight[2]
                PSWeightISRDown = event.PSWeight[0]
                PSWeightFSRUp = event.PSWeight[3]
                PSWeightFSRDown = event.PSWeight[1]

        #Emulate HLT_Ele32_WPTight_Gsf trigger for 2017 Run B (https://twiki.cern.ch/twiki/bin/view/CMS/EgHLTRunIISummary#Emulation_of_HLT_Ele32_WPTight_G)
        passEle32WPTightGsf2017 = False
        trigObjects = Collection(event, "TrigObj")
        for electron in electrons:
            matchedTrigObjs = filter(lambda o : electron.DeltaR(o) < 0.1 and o.id == 11 and (o.filterBits & (1 << 10)), trigObjects)
            if len(matchedTrigObjs) > 0:
                passEle32WPTightGsf2017 = True
                break

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
            self.out.fillBranch("deltaPhij1", deltaPhij1)
            self.out.fillBranch("deltaPhij2", deltaPhij2)
            self.out.fillBranch("deltaPhij3", deltaPhij3)
            self.out.fillBranch("deltaPhib1", deltaPhib1)
            self.out.fillBranch("deltaPhib2", deltaPhib2)
            self.out.fillBranch("M_Tb", M_Tb)
            self.out.fillBranch("M_T", M_T)
            self.out.fillBranch("M_T2W", M_T2W)
            self.out.fillBranch("M_T2ll", M_T2ll)
            self.out.fillBranch("jet1p_TH_T", jet1p_TH_T)
            self.out.fillBranch("ntaus", ntaus)
            self.out.fillBranch("m_ll", m_ll)
            self.out.fillBranch("recoilPtMiss", recoilPtMiss)

            self.out.fillBranch("lepton1_charge", lepton1_charge)
            self.out.fillBranch("lepton2_charge", lepton2_charge)

            self.out.fillBranch("index_vetoElectrons", index_vetoElectrons)
            self.out.fillBranch("index_tightElectrons", index_tightElectrons)
            self.out.fillBranch("index_looseMuons", index_looseMuons)
            self.out.fillBranch("index_tightMuons", index_tightMuons)
            self.out.fillBranch("index_centralJets", index_centralJets)
            self.out.fillBranch("index_forwardJets", index_forwardJets)
            self.out.fillBranch("index_bJets", index_bJets)
            
            self.out.fillBranch("passEle32WPTightGsf2017", passEle32WPTightGsf2017)
            self.out.fillBranch("EE_L1_prefire", EE_L1_prefire)
            self.out.fillBranch("modified_topness", modified_topness)
            self.out.fillBranch("full_topness", full_topness)
            self.out.fillBranch("noB2Bleadingfjet", noB2Bleadingfjet)
            
            if self.isMC:
                #Systematics - JES, JER
                for sys in jesUnc:
                    self.out.fillBranch("njetsScale"+sys+"Up", jesBranches["njetsScale"+sys+"Up"])
                    self.out.fillBranch("njetsScale"+sys+"Down", jesBranches["njetsScale"+sys+"Down"])

                    self.out.fillBranch("nfjetsScale"+sys+"Up", jesBranches["nfjetsScale"+sys+"Up"])
                    self.out.fillBranch("nfjetsScale"+sys+"Down", jesBranches["nfjetsScale"+sys+"Down"])
                    
                    self.out.fillBranch("nbjetsScale"+sys+"Up", jesBranches["nbjetsScale"+sys+"Up"])
                    self.out.fillBranch("nbjetsScale"+sys+"Down", jesBranches["nbjetsScale"+sys+"Down"])
                    
                    self.out.fillBranch("minDeltaPhiScale"+sys+"Up", jesBranches["minDeltaPhiScale"+sys+"Up"])
                    self.out.fillBranch("minDeltaPhiScale"+sys+"Down", jesBranches["minDeltaPhiScale"+sys+"Down"])
                    
                    self.out.fillBranch("minDeltaPhi12Scale"+sys+"Up", jesBranches["minDeltaPhi12Scale"+sys+"Up"])
                    self.out.fillBranch("minDeltaPhi12Scale"+sys+"Down", jesBranches["minDeltaPhi12Scale"+sys+"Down"])
                    
                    self.out.fillBranch("M_TbScale"+sys+"Up", jesBranches["M_TbScale"+sys+"Up"])
                    self.out.fillBranch("M_TbScale"+sys+"Down", jesBranches["M_TbScale"+sys+"Down"])
                    
                    self.out.fillBranch("M_TScale"+sys+"Up", jesBranches["M_TScale"+sys+"Up"])
                    self.out.fillBranch("M_TScale"+sys+"Down", jesBranches["M_TScale"+sys+"Down"])
                    
                    self.out.fillBranch("M_T2WScale"+sys+"Up", jesBranches["M_T2WScale"+sys+"Up"])
                    self.out.fillBranch("M_T2WScale"+sys+"Down", jesBranches["M_T2WScale"+sys+"Down"])
                    
                    self.out.fillBranch("M_T2llScale"+sys+"Up", jesBranches["M_T2llScale"+sys+"Up"])
                    self.out.fillBranch("M_T2llScale"+sys+"Down", jesBranches["M_T2llScale"+sys+"Down"])
                    
                    self.out.fillBranch("jet1p_TH_TScale"+sys+"Up", jesBranches["jet1p_TH_TScale"+sys+"Up"])
                    self.out.fillBranch("jet1p_TH_TScale"+sys+"Down", jesBranches["jet1p_TH_TScale"+sys+"Down"])
                    
                    self.out.fillBranch("recoilPtMissScale"+sys+"Up", jesBranches["recoilPtMissScale"+sys+"Up"])
                    self.out.fillBranch("recoilPtMissScale"+sys+"Down", jesBranches["recoilPtMissScale"+sys+"Down"])
                    
                    self.out.fillBranch("modified_topnessScale"+sys+"Up", jesBranches["modified_topnessScale"+sys+"Up"])
                    self.out.fillBranch("modified_topnessScale"+sys+"Down", jesBranches["modified_topnessScale"+sys+"Down"])
                    
                    self.out.fillBranch("full_topnessScale"+sys+"Up", jesBranches["full_topnessScale"+sys+"Up"])
                    self.out.fillBranch("full_topnessScale"+sys+"Down", jesBranches["full_topnessScale"+sys+"Down"])

                    self.out.fillBranch("METcorrected_ptScale"+sys+"Up", jesBranches["METcorrected_ptScale"+sys+"Up"])
                    self.out.fillBranch("METcorrected_ptScale"+sys+"Down", jesBranches["METcorrected_ptScale"+sys+"Down"])
                    self.out.fillBranch("METcorrected_phiScale"+sys+"Up", jesBranches["METcorrected_phiScale"+sys+"Up"])
                    self.out.fillBranch("METcorrected_phiScale"+sys+"Down", jesBranches["METcorrected_phiScale"+sys+"Down"])

                self.out.fillBranch("njetsResUp", njetsResUp)
                self.out.fillBranch("njetsResDown", njetsResDown)
                
                self.out.fillBranch("nfjetsResUp", nfjetsResUp)
                self.out.fillBranch("nfjetsResDown", nfjetsResDown)
                
                self.out.fillBranch("nbjetsResUp", nbjetsResUp)
                self.out.fillBranch("nbjetsResDown", nbjetsResDown)
                
                self.out.fillBranch("METcorrected_ptResUp", METcorrected_ptResUp)
                self.out.fillBranch("METcorrected_ptResDown", METcorrected_ptResDown)
                self.out.fillBranch("METcorrected_phiResUp", METcorrected_phiResUp)
                self.out.fillBranch("METcorrected_phiResDown", METcorrected_phiResDown)
                
                self.out.fillBranch("minDeltaPhiResUp", minDeltaPhiResUp)
                self.out.fillBranch("minDeltaPhiResDown", minDeltaPhiResDown)
                
                self.out.fillBranch("minDeltaPhi12ResUp", minDeltaPhi12ResUp)
                self.out.fillBranch("minDeltaPhi12ResDown", minDeltaPhi12ResDown)
                
                self.out.fillBranch("M_TbResUp", M_TbResUp)
                self.out.fillBranch("M_TbResDown", M_TbResDown)
                
                self.out.fillBranch("M_TResUp", M_TResUp)
                self.out.fillBranch("M_TResDown", M_TResDown)
                
                self.out.fillBranch("M_T2WResUp", M_T2WResUp)
                self.out.fillBranch("M_T2WResDown", M_T2WResDown)
                
                self.out.fillBranch("M_T2llResUp", M_T2llResUp)
                self.out.fillBranch("M_T2llResDown", M_T2llResDown)
                
                self.out.fillBranch("jet1p_TH_TResUp", jet1p_TH_TResUp)
                self.out.fillBranch("jet1p_TH_TResDown", jet1p_TH_TResDown)
                
                self.out.fillBranch("recoilPtMissResUp", recoilPtMissResUp)
                self.out.fillBranch("recoilPtMissResDown", recoilPtMissResDown)

                self.out.fillBranch("modified_topnessResUp", modified_topnessResUp)
                self.out.fillBranch("modified_topnessResDown", modified_topnessResDown)
                
                self.out.fillBranch("full_topnessResUp", full_topnessResUp)
                self.out.fillBranch("full_topnessResDown", full_topnessResDown)

                if not self.isSignal:
                    #Systematics - PDF
                    self.out.fillBranch("pdfWeightUp", pdfWeightUp)
                    self.out.fillBranch("pdfWeightDown", pdfWeightDown)

                    #Systematics - QCD Renormalization and Factorization scales
                    self.out.fillBranch("qcdRenWeightUp", qcdRenWeightUp)
                    self.out.fillBranch("qcdRenWeightDown", qcdRenWeightDown)
                    self.out.fillBranch("qcdFacWeightUp", qcdFacWeightUp)
                    self.out.fillBranch("qcdFacWeightDown", qcdFacWeightDown)

                self.out.fillBranch("leptonWeight", leptonWeight)
                self.out.fillBranch("electronWeight", electronWeight)
                self.out.fillBranch("muonWeight", electronWeight)
                #Systematics - lepton weights
                self.out.fillBranch("leptonWeightUp", leptonWeightUp)
                self.out.fillBranch("leptonWeightDown", leptonWeightDown)
                self.out.fillBranch("electronWeightUp", electronWeightUp)
                self.out.fillBranch("electronWeightDown", electronWeightDown)
                self.out.fillBranch("muonWeightUp", muonWeightUp)
                self.out.fillBranch("muonWeightDown", muonWeightDown)

                self.out.fillBranch("electronTriggerWeight", electronTriggerWeight)
                #Systematics - electron trigger weights
                self.out.fillBranch("electronTriggerWeightUp", electronTriggerWeightUp)
                self.out.fillBranch("electronTriggerWeightDown", electronTriggerWeightDown)

                self.out.fillBranch("muonTriggerWeight", muonTriggerWeight)
                #Systematics - muon trigger weights
                self.out.fillBranch("muonTriggerWeightUp", muonTriggerWeightUp)
                self.out.fillBranch("muonTriggerWeightDown", muonTriggerWeightDown)

                self.out.fillBranch("METTriggerWeight", METTriggerWeight)

                self.out.fillBranch("EE_L1_prefire_Weight", EE_L1_prefire_Weight)
                #Systematics - EE L1 prefiring weights
                self.out.fillBranch("EE_L1_prefire_WeightUp", EE_L1_prefire_WeightUp)
                self.out.fillBranch("EE_L1_prefire_WeightDown", EE_L1_prefire_WeightDown)

                self.out.fillBranch("bjetWeight", bjetWeight)
                #Systematics - b-tagging weights
                self.out.fillBranch("bjetWeightbcUpCorrelated",bjetWeightbcUpCorrelated)
                self.out.fillBranch("bjetWeightbcDownCorrelated",bjetWeightbcDownCorrelated)
                self.out.fillBranch("bjetWeightbcUpUncorrelated",bjetWeightbcUpUncorrelated)
                self.out.fillBranch("bjetWeightbcDownUncorrelated",bjetWeightbcDownUncorrelated)
                self.out.fillBranch("bjetWeightlightUpCorrelated",bjetWeightlightUpCorrelated)
                self.out.fillBranch("bjetWeightlightDownCorrelated",bjetWeightlightDownCorrelated)
                self.out.fillBranch("bjetWeightlightUpUncorrelated",bjetWeightlightUpUncorrelated)
                self.out.fillBranch("bjetWeightlightDownUncorrelated",bjetWeightlightDownUncorrelated)

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
                self.out.fillBranch("qcdZTo2NuWeightRenUp", qcdZTo2NuWeightRenUp)
                self.out.fillBranch("qcdZTo2NuWeightRenDown", qcdZTo2NuWeightRenDown)
                self.out.fillBranch("qcdZTo2NuWeightFacUp", qcdZTo2NuWeightFacUp)
                self.out.fillBranch("qcdZTo2NuWeightFacDown", qcdZTo2NuWeightFacDown)
                self.out.fillBranch("qcdZTo2LWeightRenUp", qcdZTo2LWeightRenUp)
                self.out.fillBranch("qcdZTo2LWeightRenDown", qcdZTo2LWeightRenDown)
                self.out.fillBranch("qcdZTo2LWeightFacUp", qcdZTo2LWeightFacUp)
                self.out.fillBranch("qcdZTo2LWeightFacDown", qcdZTo2LWeightFacDown)

                #Systematics - parton shower weights
                self.out.fillBranch("PSWeightISRUp", PSWeightISRUp)
                self.out.fillBranch("PSWeightISRDown", PSWeightISRDown)
                self.out.fillBranch("PSWeightFSRUp", PSWeightFSRUp)
                self.out.fillBranch("PSWeightFSRDown", PSWeightFSRDown)
            return True
        else:
            return False

class CountEvents(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        return True

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

analyze2017MC_Skim = lambda : CommonAnalysis("Skim",year=2017,isData=False,isSignal=False,btag='DeepCSV')
analyze2017SignalMC_Skim = lambda : CommonAnalysis("Skim",year=2017,isData=False,isSignal=True,btag='DeepCSV')
analyze2017Data_Skim = lambda : CommonAnalysis("Skim",year=2017,isData=True,isSignal=False,btag='DeepCSV')

analyze2018MC = lambda : CommonAnalysis("All",year=2018,isData=False,isSignal=False,btag='DeepCSV')
analyze2018SignalMC = lambda : CommonAnalysis("All",year=2018,isData=False,isSignal=True,btag='DeepCSV')
analyze2018Data = lambda : CommonAnalysis("All",year=2018,isData=True,isSignal=False,btag='DeepCSV')

analyze2018MC_Skim = lambda : CommonAnalysis("Skim",year=2018,isData=False,isSignal=False,btag='DeepCSV')
analyze2018SignalMC_Skim = lambda : CommonAnalysis("Skim",year=2018,isData=False,isSignal=True,btag='DeepCSV')
analyze2018Data_Skim = lambda : CommonAnalysis("Skim",year=2018,isData=True,isSignal=False,btag='DeepCSV')

#UL
analyzeUL2017MC = lambda : CommonAnalysis("All",year=2017,isData=False,isSignal=False,btag='DeepCSV',UL=True)
analyzeUL2017SignalMC = lambda : CommonAnalysis("All",year=2017,isData=False,isSignal=True,btag='DeepCSV',UL=True)
analyzeUL2017Data = lambda : CommonAnalysis("All",year=2017,isData=True,isSignal=False,btag='DeepCSV',UL=True)

analyzeUL2017MC_Skim = lambda : CommonAnalysis("Skim",year=2017,isData=False,isSignal=False,btag='DeepCSV',UL=True)
analyzeUL2017SignalMC_Skim = lambda : CommonAnalysis("Skim",year=2017,isData=False,isSignal=True,btag='DeepCSV',UL=True)
analyzeUL2017Data_Skim = lambda : CommonAnalysis("Skim",year=2017,isData=True,isSignal=False,btag='DeepCSV',UL=True)

analyzeUL2018MC = lambda : CommonAnalysis("All",year=2018,isData=False,isSignal=False,btag='DeepCSV',UL=True)
analyzeUL2018SignalMC = lambda : CommonAnalysis("All",year=2018,isData=False,isSignal=True,btag='DeepCSV',UL=True)
analyzeUL2018Data = lambda : CommonAnalysis("All",year=2018,isData=True,isSignal=False,btag='DeepCSV',UL=True)

analyzeUL2018MC_Skim = lambda : CommonAnalysis("Skim",year=2018,isData=False,isSignal=False,btag='DeepCSV',UL=True)
analyzeUL2018SignalMC_Skim = lambda : CommonAnalysis("Skim",year=2018,isData=False,isSignal=True,btag='DeepCSV',UL=True)
analyzeUL2018Data_Skim = lambda : CommonAnalysis("Skim",year=2018,isData=True,isSignal=False,btag='DeepCSV',UL=True)

#Define jetmetHelperRun2 modules for all years to calculate systematic uncertanties
jetmetCorrector2016MC = createJMECorrector(isMC=True, dataYear=2016, jesUncert=jesSys)
jetmetCorrector2016DataB = createJMECorrector(isMC=False, dataYear=2016, runPeriod="B", jesUncert=jesSys)
jetmetCorrector2016DataC = createJMECorrector(isMC=False, dataYear=2016, runPeriod="C", jesUncert=jesSys)
jetmetCorrector2016DataD = createJMECorrector(isMC=False, dataYear=2016, runPeriod="D", jesUncert=jesSys)
jetmetCorrector2016DataE = createJMECorrector(isMC=False, dataYear=2016, runPeriod="E", jesUncert=jesSys)
jetmetCorrector2016DataF = createJMECorrector(isMC=False, dataYear=2016, runPeriod="F", jesUncert=jesSys)
jetmetCorrector2016DataG = createJMECorrector(isMC=False, dataYear=2016, runPeriod="G", jesUncert=jesSys)
jetmetCorrector2016DataH = createJMECorrector(isMC=False, dataYear=2016, runPeriod="H", jesUncert=jesSys)

jetmetCorrector2017MC = createJMECorrector(isMC=True, dataYear='2017', jesUncert=jesSys, metBranchName="METFixEE2017")
jetmetCorrector2017DataB = createJMECorrector(isMC=False, dataYear='2017', runPeriod="B", jesUncert=jesSys, metBranchName="METFixEE2017")
jetmetCorrector2017DataC = createJMECorrector(isMC=False, dataYear='2017', runPeriod="C", jesUncert=jesSys, metBranchName="METFixEE2017")
jetmetCorrector2017DataD = createJMECorrector(isMC=False, dataYear='2017', runPeriod="D", jesUncert=jesSys, metBranchName="METFixEE2017")
jetmetCorrector2017DataE = createJMECorrector(isMC=False, dataYear='2017', runPeriod="E", jesUncert=jesSys, metBranchName="METFixEE2017")
jetmetCorrector2017DataF = createJMECorrector(isMC=False, dataYear='2017', runPeriod="F", jesUncert=jesSys, metBranchName="METFixEE2017")

jetmetCorrector2018MC = createJMECorrector(isMC=True, dataYear=2018, jesUncert="All", applyHEMfix=True)
jetmetCorrector2018DataA = createJMECorrector(isMC=False, dataYear=2018, runPeriod="A", jesUncert=jesSys, applyHEMfix=True)
jetmetCorrector2018DataB = createJMECorrector(isMC=False, dataYear=2018, runPeriod="B", jesUncert=jesSys, applyHEMfix=True)
jetmetCorrector2018DataC = createJMECorrector(isMC=False, dataYear=2018, runPeriod="C", jesUncert=jesSys, applyHEMfix=True)
jetmetCorrector2018DataD = createJMECorrector(isMC=False, dataYear=2018, runPeriod="D", jesUncert=jesSys, applyHEMfix=True)

#UL
jetmetCorrectorUL2017MC = createJMECorrector(isMC=True, dataYear='UL2017', jesUncert=jesSys)
jetmetCorrectorUL2017DataB = createJMECorrector(isMC=False, dataYear='UL2017', runPeriod="B")
jetmetCorrectorUL2017DataC = createJMECorrector(isMC=False, dataYear='UL2017', runPeriod="C")
jetmetCorrectorUL2017DataD = createJMECorrector(isMC=False, dataYear='UL2017', runPeriod="D")
jetmetCorrectorUL2017DataE = createJMECorrector(isMC=False, dataYear='UL2017', runPeriod="E")
jetmetCorrectorUL2017DataF = createJMECorrector(isMC=False, dataYear='UL2017', runPeriod="F")

jetmetCorrectorUL2018MC = createJMECorrector(isMC=True, dataYear='UL2018', jesUncert=jesSys)
jetmetCorrectorUL2018DataA = createJMECorrector(isMC=False, dataYear='UL2018', runPeriod="A")
jetmetCorrectorUL2018DataB = createJMECorrector(isMC=False, dataYear='UL2018', runPeriod="B")
jetmetCorrectorUL2018DataC = createJMECorrector(isMC=False, dataYear='UL2018', runPeriod="C")
jetmetCorrectorUL2018DataD = createJMECorrector(isMC=False, dataYear='UL2018', runPeriod="D")

#Define module to count number of events in root file
countEvents = lambda : CountEvents()

# #########################################################################################################################################

# if runLocal:
#     #Select PostProcessor options here
#     selection=None
#     #outputDir = "outDir2016AnalysisSR/ttbarDM/"
#     #outputDir = "testSamples/"
#     outputDir = "."
#     #inputbranches="python/postprocessing/analysis/keep_and_dropSR_in.txt"
#     outputbranches="python/postprocessing/analysis/keep_and_dropSR_out.txt"
#     #outputbranches="python/postprocessing/analysis/keep_and_dropCount_out.txt"
#     #inputFiles=["/hdfs/store/user/vshang/testSamples/privateSignalMC/2016/tDM_tChan_Mchi1Mphi100_scalar_full.root","/hdfs/store/user/vshang/testSamples/privateSignalMC/2016/tDM_tWChan_Mchi1Mphi100_scalar_full.root"]#,"/hdfs/store/user/vshang/testSamples/privateSignalMC/2016/ttbarDM_Mchi1Mphi100_scalar_full1.root","/hdfs/store/user/vshang/testSamples/privateSignalMC/2016/ttbarDM_Mchi1Mphi100_scalar_full2.root"]
#     #inputFiles=["/hdfs/store/user/vshang/testSamples/nanoAODv7/SingleElectron_2016H_v7.root"]#,"SingleMuon_2016B_ver1.root","SingleMuon_2016B_ver2.root","SingleMuon_2016E.root"]
#     inputFiles=["ttbarPlusJets_Run2016_v7.root"]
#     #jsonFile = "python/postprocessing/data/json/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt"
#     #jsonFile = "python/postprocessing/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
#     #jsonFile = "python/postprocessing/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"
#     #jsonFile = "python/postprocessing/data/json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt"
#     #jsonFile = "python/postprocessing/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"

#     #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[analyze2016SignalMC()],postfix="_ModuleCommon_2016MC_noJME",noOut=False,outputbranchsel=outputbranches)#,jsonInput=jsonFile)
#     #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[jetmetCorrector2018MC()],postfix="_ModuleCommon_2016MC_onlyJME_Allsys",noOut=False,outputbranchsel=outputbranches)#,jsonInput=jsonFile)
#     p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[jetmetCorrector2016MC(),analyze2016MC_Skim()],postfix="_ModuleCommon07252022",noOut=False,outputbranchsel=outputbranches)
#     #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[jetmetCorrector2018MC(),analyze2018SignalMC_Skim()],postfix="_pseudo2018_tChan_Mchi1_Mphi450",noOut=False,outputbranchsel=outputbranches)
#     #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[jetmetCorrector2016DataC(),analyze2016Data_Skim()],postfix="_ModuleCommon_2016Data_Skim",noOut=False,outputbranchsel=outputbranches)#,jsonInput=jsonFile)
#     #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=outputbranches,modules=[countEvents()],postfix="_2016MC_countEvents_03182021",noOut=False,outputbranchsel=outputbranches)
#     p.run()
