import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class controlRegionAnalysis(Module):
    def __init__(self, controlRegion):
        self.controlRegion = controlRegion
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        #Define output branches to check if selection cuts are working
        self.out = wrappedOutputTree
        self.out.branch("nTightElectrons",  "I");
        self.out.branch("nVetoElectrons", "I");
        self.out.branch("nTightMuons", "I");
        self.out.branch("nLooseMuons", "I");
        self.out.branch("njets", "I")
        self.out.branch("nbjets", "I")
        self.out.branch("missing_pt", "F")
        if self.controlRegion == "SL1eWR" or self.controlRegion == "SL1mWR" or self.controlRegion == "AH1eTR" or self.controlRegion == "AH1mTR" or self.controlRegion == "AH1eWR" or self.controlRegion == "AH1mWR":
            self.out.branch("M_T", "F")
        if self.controlRegion == "AH1eTR" or self.controlRegion == "AH1mTR":
            self.out.branch("minDeltaPhi", "F")
        if self.controlRegion == "AH2eZR" or self.controlRegion == "AH2mZR":
            self.out.branch("m_ll", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event): 
        """process event, return True (go to next module) or False (fail, go to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")

        #Tight/Veto electrons are defined and counted
        vetoElectrons = filter(lambda lep : lep.pt > 10 and lep.cutBased != 0 and ((lep.eta) < 1.4442 or 1.566 < abs(lep.eta) < 2.1), electrons)
        tightElectrons = filter(lambda lep : lep.pt > 30 and lep.cutBased == 4, vetoElectrons)

        nVetoElectrons = len(vetoElectrons)
        nTightElectrons = len(tightElectrons)
        
        #Tight/Loose muons are defined and counted
        looseMuons = filter(lambda lep : lep.pt > 10 and lep.looseId and lep.pfRelIso04_all < 0.25 and abs(lep.eta) < 2.4, muons) 
        tightMuons = filter(lambda lep : lep.pt > 30 and lep.tightId and lep.pfRelIso04_all < 0.15, looseMuons)

        nLooseMuons = len(looseMuons)
        nTightMuons = len(tightMuons)
        
        #Jets are not considered if they are within Delta R < 0.4 of a loose/veto lepton
        def cleanJet(jet):
            for vetoElectron in vetoElectrons:
                if vetoElectron.p4().DeltaR(jet.p4()) < 0.4:
                    return False
            for looseMuon in looseMuons:
                if looseMuon.p4().DeltaR(jet.p4()) < 0.4:
                    return False
            return True

        #Jet categories are defined and counted 
        centralJets = filter(lambda j : j.pt > 30 and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId > 0, jets) #Define central jets 
        bJets = filter(lambda j : j.btagCSVV2 > 0.8484, centralJets) #Define b-jets

        njets = len(centralJets)
        nbjets = len(bJets)

        #Choose single lepton
        lepton = 0
        if nTightElectrons == 1 and nLooseMuons == 0:
            lepton = tightElectrons[0]
        if nTightMuons == 1 and nVetoElectrons == 0:
            lepton = tightMuons[0]

        #Calculate M_T for CRW(lv), CR(1l)tt, and CRW(lv) control regions
        M_T = 0

        if self.controlRegion == "SL1eWR" or self.controlRegion == "AH1eTR" or self.controlRegion == "AH1eWR" or self.controlRegion == "SL1mWR" or self.controlRegion == "AH1mTR" or self.controlRegion == "AH1mWR":
            if lepton != 0:
                deltaPhiMT = min(abs(lepton.phi - event.MET_phi), 2 * math.pi - abs(lepton.phi - event.MET_phi))
                M_T = math.sqrt(2 * event.MET_pt * lepton.pt * (1 - math.cos(deltaPhiMT)))
        
        #Calculate minDeltaPhi(j_(1,2), missing pt) for CR(1l)tt control region 
        minDeltaPhi = 0
        if self.controlRegion == "AH1eTR" or self.controlRegion == "AH1mTR":
            if len(centralJets) > 1: #jet1 (jet2) is the jet with the largest (second-largest) pt
                jet1 = centralJets[0]
                jet2 = centralJets[1]
                deltaPhi1 = min(abs(jet1.phi - event.MET_phi), 2 * math.pi - abs(jet1.phi - event.MET_phi)) #phi angle between jet1 and missing pt
                deltaPhi2 = min(abs(jet2.phi - event.MET_phi), 2 * math.pi - abs(jet2.phi - event.MET_phi)) #phi angle between jet2 and missing pt
                minDeltaPhi = min(deltaPhi1, deltaPhi2)

        #Determine if there exists two tight electrons/muons such that their invariant mass m_ll is between 60-120 GeV and the hadronic recoil >= 250 GeV
        m_ll = 0
        m_llExists = False

        if self.controlRegion == "AH2eZR" or self.controlRegion == "AH2mZR":
            if self.controlRegion == "AH2eZR":
                tightLeptons = tightElectrons
            else:
                tightLeptons = tightMuons
            if len(tightLeptons) >= 2:
                for i in range(0, len(tightLeptons)):
                    for j in range(i+1, len(tightLeptons)):
                        lepton1 = tightLeptons[i]
                        lepton2 = tightLeptons[j]
                        eventSum = lepton1.p4() + lepton2.p4()
                        m_llTest = eventSum.M()
                        deltaPhiRecoil = eventSum.Phi() - event.MET_phi
                        recoilPtMiss = event.MET_pt + eventSum.Pt() * math.cos(deltaPhiRecoil)
                        if 60 <= m_llTest <= 120 and recoilPtMiss >= 250 and lepton1.charge == -lepton2.charge:
                            m_llExists = True
                            m_ll = m_llTest
             
        #Control region selection cuts defined here
        SL1e1mTR = njets >= 2 and nbjets >= 1 and (nTightElectrons + nTightMuons) == 2 and nTightElectrons == nVetoElectrons and nTightMuons == nLooseMuons and event.MET_pt >= 160 
        SL1eWR = njets >= 2 and nbjets == 0 and nTightElectrons == 1 and nVetoElectrons == 1 and nLooseMuons == 0 and event.MET_pt >= 160 and M_T >= 160 
        SL1mWR = njets >= 2 and nbjets == 0 and nVetoElectrons == 0 and nTightMuons == 1 and nLooseMuons == 1 and event.MET_pt >= 160 and M_T >= 160
        AH1eTR = njets >= 3 and nbjets >= 1 and nTightElectrons == 1 and nVetoElectrons == 1 and nLooseMuons == 0 and event.MET_pt >= 250 and M_T <= 160 and minDeltaPhi >= 1.0
        AH1mTR = njets >= 3 and nbjets >= 1 and nVetoElectrons == 0 and nTightMuons == 1 and nLooseMuons == 1 and event.MET_pt >= 250 and M_T <= 160 and minDeltaPhi >= 1.0
        AH1eWR = njets >= 3 and nbjets == 0 and nTightElectrons == 1 and nVetoElectrons == 1 and nLooseMuons == 0 and event.MET_pt >= 250 and M_T <= 160
        AH1mWR = njets >= 3 and nbjets == 0 and nVetoElectrons == 0 and nTightMuons == 1 and nLooseMuons == 1 and event.MET_pt >= 250 and M_T <= 160
        AH2eZR = njets >= 3 and nbjets == 0 and nTightElectrons >= 2 and m_llExists
        AH2mZR = njets >= 3 and nbjets == 0 and nTightMuons >= 2 and m_llExists

        #Control region chosen here
        if self.controlRegion == "SL1e1mTR":
            controlRegionSelect = SL1e1mTR
        elif self.controlRegion == "SL1eWR":
            controlRegionSelect = SL1eWR
        elif self.controlRegion == "SL1mWR":
            controlRegionSelect = SL1mWR
        elif self.controlRegion == "AH1eTR":
            controlRegionSelect =  AH1eTR
        elif self.controlRegion == "AH1mTR":
            controlRegionSelect = AH1mTR
        elif self.controlRegion == "AH1eWR":
            controlRegionSelect = AH1eWR
        elif self.controlRegion == "AH1mWR":
            controlRegionSelect = AH1mWR
        elif self.controlRegion == "AH2eZR":
            controlRegionSelect = AH2eZR
        elif self.controlRegion == "AH2mZR":
            controlRegionSelect = AH2mZR
        else:
            controlRegionSelect = True

        if controlRegionSelect: #True if event satisfies all selection cuts for specified control region
            #fill output branches
            self.out.fillBranch("nTightElectrons", nTightElectrons)
            self.out.fillBranch("nVetoElectrons", nVetoElectrons)
            self.out.fillBranch("nTightMuons", nTightMuons)
            self.out.fillBranch("nLooseMuons", nLooseMuons)
            self.out.fillBranch("njets", njets)
            self.out.fillBranch("nbjets", nbjets)
            self.out.fillBranch("missing_pt", event.MET_pt)
            if self.controlRegion == "SL1eWR" or self.controlRegion == "SL1mWR" or self.controlRegion == "AH1eTR" or self.controlRegion == "AH1mTR" or self.controlRegion == "AH1eWR" or self.controlRegion == "AH1mWR":
                self.out.fillBranch("M_T", M_T)
            if self.controlRegion == "AH1eTR" or self.controlRegion == "AH1mTR":
                self.out.fillBranch("minDeltaPhi", minDeltaPhi)
            if self.controlRegion == "AH2eZR" or self.controlRegion == "AH2mZR":
                self.out.fillBranch("m_ll", m_ll)
            return True
        else:
            return False

#Select PostProcessor options here
preselection=None
outputDir = "outDir2016AnalysisCR"
inputbranches="python/postprocessing/2016Analysis/keep_and_dropCR_in.txt"
outputbranches="python/postprocessing/2016Analysis/keep_and_dropCR_out.txt"
inputFiles=["samples/tDM_tWChan_Mchi1Mphi100_scalar.root"]
#Applies selection cuts for each control region, one file for each CR (9 total files)
p1=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("SL1e1mTR")],postfix="_SL1e1mTR_control",noOut=False,outputbranchsel=outputbranches)
p2=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("SL1eWR")],postfix="_SL1eWR_control",noOut=False,outputbranchsel=outputbranches)
p3=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("SL1mWR")],postfix="_SL1mWR_control",noOut=False,outputbranchsel=outputbranches)
p4=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("AH1eTR")],postfix="_AH1eTR_control",noOut=False,outputbranchsel=outputbranches)
p5=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("AH1mTR")],postfix="_AH1mTR_control",noOut=False,outputbranchsel=outputbranches)
p6=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("AH1eWR")],postfix="_AH1eWR_control",noOut=False,outputbranchsel=outputbranches)
p7=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("AH1mWR")],postfix="_AH1mWR_control",noOut=False,outputbranchsel=outputbranches)
p8=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("AH2eZR")],postfix="_AH2eZR_control",noOut=False,outputbranchsel=outputbranches)
p9=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[controlRegionAnalysis("AH2mZR")],postfix="_AH2mZR_control",noOut=False,outputbranchsel=outputbranches)
p1.run()
p2.run()
p3.run()
p4.run()
p5.run()
p6.run()
p7.run()
p8.run()
p9.run()
