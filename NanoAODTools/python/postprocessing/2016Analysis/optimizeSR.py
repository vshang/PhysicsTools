import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

#Load Mt2Com_bisect.o object file that contains C++ code to calculate MT2W for SL region 
ROOT.gSystem.Load("/afs/cern.ch/user/v/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/2016Analysis/mt2w_bisect_cc")
ROOT.gSystem.Load("/afs/cern.ch/user/v/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/2016Analysis/MT2Utility_cc")
ROOT.gSystem.Load("/afs/cern.ch/user/v/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/2016Analysis/mt2bl_bisect_cc")
ROOT.gSystem.Load("/afs/cern.ch/user/v/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/2016Analysis/Mt2Com_bisect_cc")
Mt2Com_bisect = ROOT.Mt2Com_bisect()

class optimizeAnalysis(Module):
    def __init__(self, signalRegion):
        self.signalRegion = signalRegion
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        #Define output branches to check if selection cuts are working
        self.out = wrappedOutputTree
        self.out.branch("minDeltaPhi", "F")
        self.out.branch("M_Tb", "F")
        self.out.branch("njets", "I")
        self.out.branch("bjets", "I")
        if self.signalRegion == "SLe" or self.signalRegion == "SLm":
            self.out.branch("M_T", "F")
            self.out.branch("M_T2W", "F")
        if self.signalRegion == "AH2b":
            self.out.branch("jet1p_TH_T", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):  #Discriminating variables defined and checked here
        """process event, return True (go to next module) or False (fail, go to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")

        #Jet TLorentzVectors are constructed
        ljetVector = ROOT.vector("TLorentzVector")()
        bjetVector = ROOT.vector("TLorentzVector")()

        #Tight/veto leptons are defined
        vetoElectrons = filter(lambda lep : lep.pt > 10 and lep.cutBased_Sum16 != 0 and ((lep.eta) < 1.4442 or 1.566 < abs(lep.eta) < 2.5), electrons)
        tightElectrons = filter(lambda lep : lep.pt > 30 and lep.cutBased_Sum16 == 4, vetoElectrons)

        looseMuons = filter(lambda lep : lep.pt > 10 and lep.looseId and lep.pfRelIso04_all < 0.25 and abs(lep.eta) < 2.4, muons)
        tightMuons = filter(lambda lep : lep.pt > 30 and lep.tightId and lep.pfRelIso04_all < 0.15, looseMuons)
        
        #Jets (and tau jets) are not considered if they are within Delta R < 0.4 of a loose/veto lepton
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

        #Calculate minDeltaPhi(j_(1,2), missing pt) preselection variable
        minDeltaPhi = 0
        if len(centralJets) > 1: #jet1 (jet2) is the jet with the largest (second-largest) pt
            jet1 = centralJets[0]
            jet2 = centralJets[1]
            deltaPhi1 = min(abs(jet1.phi - event.MET_phi), 2 * math.pi - abs(jet1.phi - event.MET_phi)) #phi angle between jet1 and missing pt
            deltaPhi2 = min(abs(jet2.phi - event.MET_phi), 2 * math.pi - abs(jet2.phi - event.MET_phi)) #phi angle between jet2 and missing pt
            minDeltaPhi = min(deltaPhi1, deltaPhi2)

        #Calculate jet1p_T/H_T
        H_T = 0
        jet1pTHT = 0

        for jet in centralJets:
            H_T += jet.pt
            if jet.btagCSVV2 < 0.8484:
                ljetVector.push_back(jet.p4())

        if H_T > 0: 
            jet1pTHT = jet1.pt/H_T

        #Calculate M_T^b
        MTb = 0
        if nbjets > 0:
            bjet1 = bJets[0]

            for bjet in bJets:
                bjetVector.push_back(bjet.p4())
            if bjet.btagCSVV2 > bjet1.btagCSVV2:
                bjet1 = bjet

            deltaPhiMTb = bjet1.phi - event.MET_phi
            MTb = math.sqrt(2 * event.MET_pt * bjet1.pt * (1 - math.cos(deltaPhiMTb)))

        #Calculate M_T and M_T2^W for SL case
        M_T = 0
        MT2W = 0 
        if self.signalRegion == "SLe" or self.signalRegion == "SLm":
            if self.signalRegion == "SLe": #Select tight electron in single electron SR
                lepton = tightElectrons[0]
            else: #Select tight muon in single muon SR
                lepton = tightMuons[0]

            #Calculate M_T
            deltaPhiMT = lepton.phi - event.MET_phi
            M_T = math.sqrt(2 * event.MET_pt * lepton.pt * (1 - math.cos(deltaPhiMT)))

            #Calculate M_T2^W 
            leptonTLorentz = lepton.p4()
            metTVector2 = ROOT.TVector2(event.MET_pt * math.cos(event.MET_phi), event.MET_pt * math.sin(event.MET_phi))
            MT2W = Mt2Com_bisect.calculateMT2w(ljetVector, bjetVector, leptonTLorentz, metTVector2, "MT2w")
        
             
        #Optimization cuts defined here
        singleLeptonAccept = M_T >= 160 and MT2W >= 200 and minDeltaPhi >= 1.2 and MTb >= 180 
        allHadronicAccept = minDeltaPhi >= 1 and MTb >= 180
        allHadronicAccept2b = minDeltaPhi >= 1 and MTb >= 180 and jet1pTHT <= 0.5

        #Signal region chosen here
        signalRegionOptimize = True
        if self.signalRegion == "SLe" or self.signalRegion == "SLm":
            signalRegionOptimize = singleLeptonAccept
        elif self.signalRegion == "AH":
            signalRegionOptimize = allHadronicAccept
        elif self.signalRegion == "AH2b":
            signalRegionOptimize = allHadronicAccept2b

        if signalRegionOptimize: #True if event satisfies all optimization selections for specified signal region
            #fill output branches
            self.out.fillBranch("minDeltaPhi", minDeltaPhi)
            self.out.fillBranch("M_Tb", MTb)
            self.out.fillBranch("njets", njets)
            self.out.fillBranch("bjets", nbjets)
            if self.signalRegion == "SLe" or self.signalRegion == "SLm":
                self.out.fillBranch("M_T", M_T)
                self.out.fillBranch("M_T2W", MT2W)
            if self.signalRegion == "AH2b":
                self.out.fillBranch("jet1p_TH_T", jet1pTHT)
            return True
        else:
            return False

#Select PostProcessor options here
preselection=None
outputDir = "outDir2016AnalysisSR"
inputbranches="python/postprocessing/2016Analysis/keep_and_dropSR_in.txt"
outputbranches="python/postprocessing/2016Analysis/keep_and_dropSR_out.txt"
#Change input files to output of preselectSR.py for each signal region
inputFiles1=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_SL1e0fSR.root"]
inputFiles2=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_SL1m0fSR.root"]
inputFiles3=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_SL1e1fSR.root"]
inputFiles4=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_SL1m1fSR.root"]
inputFiles5=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_SL1e2bSR.root"]
inputFiles6=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_SL1m2bSR.root"]
inputFiles7=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_AH0l0fSR.root"]
inputFiles8=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_AH0l1fSR.root"]
inputFiles9=["outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_AH0l2bSR.root"]
#Applies optimization selection cuts for each signal region (SL vs AH, nb = 1 vs nb >=2, nf = 0 vs nf >= 1), one file for each SR (9 total files)
p1=PostProcessor(outputDir,inputFiles1,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("SLe")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p2=PostProcessor(outputDir,inputFiles2,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("SLm")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p3=PostProcessor(outputDir,inputFiles3,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("SLe")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p4=PostProcessor(outputDir,inputFiles4,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("SLm")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p5=PostProcessor(outputDir,inputFiles5,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("SLe")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p6=PostProcessor(outputDir,inputFiles6,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("SLm")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p7=PostProcessor(outputDir,inputFiles7,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("AH")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p8=PostProcessor(outputDir,inputFiles8,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("AH")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p9=PostProcessor(outputDir,inputFiles9,cut=preselection,branchsel=inputbranches,modules=[optimizeAnalysis("AH2b")],postfix="_optimized",noOut=False,outputbranchsel=outputbranches)
p1.run()
p2.run()
p3.run()
p4.run()
p5.run()
p6.run()
p7.run()
p8.run()
p9.run()
