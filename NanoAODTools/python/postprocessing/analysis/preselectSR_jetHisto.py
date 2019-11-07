import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class preselectAnalysis(Module):
    def __init__(self, signalRegion):
        self.signalRegion = signalRegion
        self.nEvent = 0
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        #Define output branches to check if preselection is working
        self.out = wrappedOutputTree
        self.out.branch("nTightElectrons",  "I");
        self.out.branch("nVetoElectrons", "I");
        self.out.branch("nTightMuons", "I");
        self.out.branch("nLooseMuons", "I");
        self.out.branch("njets", "I")
        self.out.branch("nbjets", "I")
        self.out.branch("nfjets", "I")
        self.out.branch("missing_pt", "F")
        # self.out.branch("minDeltaPhi", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go 
to next event)"""
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
        #looseMuons = muons
        #tightMuons = muons

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
        #centralJets = filter(lambda j : j.pt > 30 and abs(j.eta) < 2.4 and j.jetId > 0, jets)
        bJets = filter(lambda j : j.btagCSVV2 > 0.8484, centralJets) #Define b-jets
        #bJets = filter(lambda j : j.btagCSVV2 > 0.8000, centralJets)
        forwardJets = filter(lambda j : j.pt > 30 and 2.4 < abs(j.eta) < 5 and cleanJet(j) and j.jetId > 0, jets) #Define forward jets

        njets = len(centralJets)
        nbjets = len(bJets)
        nfjets = len(forwardJets)

        #Calculate minDeltaPhi(j_(1,2), missing pt) preselection variable
        # minDeltaPhi = 0
        # if self.signalRegion == "AH0l0fSR" or self.signalRegion == "AH0l1fSR" or self.signalRegion == "AH0l2bSR":
        #     if len(centralJets) > 1: #jet1 (jet2) is the jet with the largest (second-largest) pt
        #         jet1 = centralJets[0]
        #         jet2 = centralJets[1]
        #         deltaPhi1 = min(abs(jet1.phi - event.MET_phi), 2 * math.pi - abs(jet1.phi - event.MET_phi)) #phi angle between jet1 and missing pt
        #         deltaPhi2 = min(abs(jet2.phi - event.MET_phi), 2 * math.pi - abs(jet2.phi - event.MET_phi)) #phi angle between jet2 and missing pt
        #         minDeltaPhi = min(deltaPhi1, deltaPhi2)

        #Preselection cuts defined here
        AH = (nVetoElectrons + nLooseMuons) == 0 and njets >= 3 and event.MET_pt >= 250
        SL = (nTightElectrons + nTightMuons) == 1 and nTightElectrons == nVetoElectrons and nTightMuons == nLooseMuons and njets >= 2 and event.MET_pt >= 160

        #Signal region chosen here
        if self.signalRegion == "AH":
            signalRegionPreselect = AH
        elif self.signalRegion == "SL":
            signalRegionPreselect = SL
        else:
            signalRegionPreselect = True

        if signalRegionPreselect: #True if event satisfies all pre-selection cuts for specified signal region
            #fill output branches
            self.out.fillBranch("nTightElectrons", nTightElectrons)
            self.out.fillBranch("nVetoElectrons", nVetoElectrons)
            self.out.fillBranch("nTightMuons", nTightMuons)
            self.out.fillBranch("nLooseMuons", nLooseMuons)
            self.out.fillBranch("njets", njets)
            self.out.fillBranch("nbjets", nbjets)
            self.out.fillBranch("nfjets", nfjets)
            self.out.fillBranch("missing_pt", event.MET_pt)
            # self.out.fillBranch("minDeltaPhi", minDeltaPhi)
            return True
        else:
            return False

#Select PostProcessor options here
preselection=None
outputDir = "outDir2016AnalysisSR_histo"
#outputDir = "outDirDump"
inputbranches="python/postprocessing/2016Analysis/keep_and_dropSR_in.txt"
outputbranches="python/postprocessing/2016Analysis/keep_and_dropSR_out.txt"
inputFiles_ttbar=["samples/ttbarDM_Mchi1Mphi100_scalar.root"]
inputFiles_tChan=["samples/tDM_tChan_Mchi1Mphi100_scalar.root"]
inputFiles_tWChan=["samples/tDM_tWChan_Mchi1Mphi100_scalar.root"]

#Applies selection cuts 
p1=PostProcessor(outputDir,inputFiles_ttbar,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("AH")],postfix="_AH_noCleanJet",noOut=False,outputbranchsel=outputbranches)
p2=PostProcessor(outputDir,inputFiles_ttbar,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL")],postfix="_SL_noCleanJet",noOut=False,outputbranchsel=outputbranches)
p3=PostProcessor(outputDir,inputFiles_tChan,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("AH")],postfix="_AH_noCleanJet",noOut=False,outputbranchsel=outputbranches)
p4=PostProcessor(outputDir,inputFiles_tChan,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL")],postfix="_SL_noCleanJet",noOut=False,outputbranchsel=outputbranches)
p5=PostProcessor(outputDir,inputFiles_tWChan,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("AH")],postfix="_AH_noCleanJet",noOut=False,outputbranchsel=outputbranches)
p6=PostProcessor(outputDir,inputFiles_tWChan,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL")],postfix="_SL_noCleanJet",noOut=False,outputbranchsel=outputbranches)

p1.run()
p2.run()
p3.run()
p4.run()
p5.run()
p6.run()
