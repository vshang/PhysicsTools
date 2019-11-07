import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
#from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class exampleSR(Module):
    def __init__(self, jetSelection):
        self.jetSel = jetSelection
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("EventMass",  "F");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        eventSum = ROOT.TLorentzVector()
        for lep in muons :
            eventSum += lep.p4()
        for lep in electrons :
            eventSum += lep.p4()
        for j in filter(self.jetSel,jets):
            eventSum += j.p4()
        self.out.fillBranch("EventMass",eventSum.M())
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

exampleModuleConstr = lambda : exampleSR(jetSelection= lambda j : j.pt > 30) 

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
        self.out.branch("minDeltaPhi", "F")
        self.out.branch("nbjetsHF", "I")
        self.out.branch("ntaus", "I")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go 
to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")

        #Tight/Veto electrons are defined and counted
        vetoElectrons = filter(lambda lep : lep.pt > 10 and lep.cutBased_Sum16 != 0 and (abs(lep.eta) < 1.4442 or 1.566 < abs(lep.eta) < 2.5), electrons)
        tightElectrons = filter(lambda lep : lep.pt > 30 and abs(lep.eta) < 2.1 and lep.cutBased_Sum16 == 4, vetoElectrons)

        nVetoElectrons = len(vetoElectrons)
        nTightElectrons = len(tightElectrons)
        
        #Tight/Loose muons are defined and counted
        looseMuons = filter(lambda lep : lep.pt > 10 and lep.looseId and lep.pfRelIso04_all < 0.25 and abs(lep.eta) < 2.4, muons)
        tightMuons = filter(lambda lep : lep.pt > 30 and lep.tightId and lep.pfRelIso04_all < 0.15, looseMuons)

        nLooseMuons = len(looseMuons)
        nTightMuons = len(tightMuons)

        #Jets (including tau jets) are not considered if they are within Delta R < 0.4 of a loose/veto lepton
        def cleanJet(jet):
            for vetoElectron in vetoElectrons:
                if vetoElectron.p4().DeltaR(jet.p4()) < 0.4:
                    return False
            for looseMuon in looseMuons:
                if looseMuon.p4().DeltaR(jet.p4()) < 0.4:
                    return False
            return True

        #Manually implement loose Jet ID requirements (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID13TeVRun2016)
        def looseJet(jet):
            if abs(jet.eta) < 2.7:
                if jet.neHEF > 0.99 or jet.neEmEF > 0.99 or jet.nConstituents < 2:
                    return False
                if abs(jet.eta) < 2.4:
                    if jet.chHEF == 0 or jet.chEmEF > 0.99:
                        return False
            elif 2.7 < abs(jet.eta) < 3.0:
                if jet.neHEF < 0.01 or jet.neHEF > 0.98:
                    return False
            elif abs(jet.eta) > 3:
                if jet.neEmEF > 0.9:
                    return False
            return True

        #Jet categories are defined and counted 
        centralJets = filter(lambda j : j.pt > 30 and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId > 0, jets) #Define central jets 
        #centralJets = filter(lambda j : j.pt > 30 and abs(j.eta) < 2.4 and cleanJet(j) and looseJet(j), jets)
        bJets = filter(lambda j : j.btagCSVV2 > 0.8484, centralJets) #Define b-jets
        bJetsHF = filter(lambda j : j.hadronFlavour == 5, centralJets) #Define b-jets by hadron flavour
        forwardJets = filter(lambda j : j.pt > 30 and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId > 0, jets) #Define forward jets
        #forwardJets = filter(lambda j : j.pt > 30 and 2.4 < abs(j.eta) < 4 and cleanJet(j) and looseJet(j) > 0, jets)

        njets = len(centralJets)
        nbjets = len(bJets)
        nbjetsHF = len(bJetsHF)
        nfjets = len(forwardJets)

        #Calculate minDeltaPhi preselection variable of all central jets
        minDeltaPhi = 0
        if self.signalRegion == "AH0l0fSR" or self.signalRegion == "AH0l1fSR" or self.signalRegion == "AH0l2bSR" or self.signalRegion == "AH":
            if len(centralJets) > 1: #Should always be true for both SL and AH signal regions
                jet1 = centralJets[0]
                minDeltaPhi = min(abs(jet1.phi - event.MET_phi), 2 * math.pi - abs(jet1.phi - event.MET_phi)) #phi angle between jet1 and missing pt
                for i in range(1, len(centralJets)):
                    jet2 = centralJets[i]
                    minDeltaPhi2 = min(abs(jet2.phi - event.MET_phi), 2 * math.pi - abs(jet2.phi - event.MET_phi)) #phi angle between jet2 and missing pt
                    if minDeltaPhi2 < minDeltaPhi: #Choose lowest minDeltaPhi out of all central jets
                        minDeltaPhi = minDeltaPhi2

        #Tau candidates are counted
        tauCandidates = Collection(event, "Tau")
        skimmedTaus = filter(lambda tau : tau.pt > 18 and abs(tau.eta) < 2.3 and tau.idMVAnewDM >= 31 and cleanJet(tau), tauCandidates)
        ntaus = len(skimmedTaus)

        #Define MET filters contained in miniAOD analysis (https://github.com/zucchett/SFrame/blob/master/DM/src/DMSearches.cxx#L1542)
        passMETfilters = event.Flag_goodVertices and event.Flag_HBHENoiseFilter and event.Flag_HBHENoiseIsoFilter and event.Flag_EcalDeadCellTriggerPrimitiveFilter and event.Flag_eeBadScFilter and event.Flag_globalTightHalo2016Filter and event.Flag_BadPFMuonFilter and event.Flag_chargedHadronTrackResolutionFilter

        #Define SingleIsoEle, SingleEle, and SingleIsoMu filters contained in miniAOD analysis (https://github.com/zucchett/SFrame/blob/master/DM/src/DMSearches.cxx#L112)
        singleIsoEle = event.HLT_Ele27_eta2p1_WPTight_Gsf or event.HLT_Ele32_WPTight_Gsf or event.HLT_Ele32_eta2p1_WPTight_Gsf or event.HLT_Ele27_WPLoose_Gsf or event.HLT_Ele27_WPTight_Gsf
        singleEle = event.HLT_Ele105_CaloIdVT_GsfTrkIdT or event.HLT_Ele115_CaloIdVT_GsfTrkIdT
        singleIsoMu = event.HLT_IsoMu27 or event.HLT_IsoTkMu27 or event.HLT_IsoMu24 or event.HLT_IsoTkMu24

        #Preselection cuts defined here
        # SL1e = nTightElectrons == 1 and nVetoElectrons == 1 and nLooseMuons == 0 and njets >= 2 and nbjets >= 1 and event.MET_pt >= 160 and passMETfilters and (singleIsoEle or singleEle)
        # SL1m = nTightMuons == 1 and nLooseMuons == 1 and nVetoElectrons == 0 and njets >= 2 and nbjets >= 1 and event.MET_pt >= 160 and passMETfilters and singleIsoMu
        AH = (nVetoElectrons + nLooseMuons) == 0 and njets >= 3 and nbjets >= 1 and event.MET_pt >= 250  and ntaus == 0 and minDeltaPhi > 0.4 and centralJets[0].jetId >= 3 and centralJets[0].chHEF > 0.1 and passMETfilters

        SL1e = nTightElectrons == 1 and nVetoElectrons == 1 and nLooseMuons == 0 and njets >= 2 and event.MET_pt >= 160 and passMETfilters and (singleIsoEle or singleEle)
        SL1m = nTightMuons == 1 and nLooseMuons == 1 and nVetoElectrons == 0 and njets >= 2 and event.MET_pt >= 160 and passMETfilters and singleIsoMu
        # AH = (nVetoElectrons + nLooseMuons) == 0 and njets >= 3 and event.MET_pt >= 250 and ntaus == 0 and minDeltaPhi > 0.4 and centralJets[0].jetId >= 3 and centralJets[0].chHEF > 0.1 and passMETfilters
        SL = SL1e or SL1m

        # SL1e0fSR = SL1e and nbjets == 1 and nfjets == 0
        # SL1m0fSR = SL1m and nbjets == 1 and nfjets == 0
        # SL1e1fSR = SL1e and nbjets == 1 and nfjets >= 1 
        # SL1m1fSR = SL1m and nbjets == 1 and nfjets >= 1 
        # SL1e2bSR = SL1e and nbjets >= 2 
        # SL1m2bSR = SL1m and nbjets >= 2 
        # AH0l0fSR = AH and nbjets == 1 and nfjets == 0
        # AH0l1fSR = AH and nbjets == 1 and nfjets >= 1
        # AH0l2bSR = AH and nbjets >= 2

        #Signal region chosen here
        if self.signalRegion == "SL1e0fSR":
            signalRegionPreselect = SL1e0fSR
        elif self.signalRegion == "SL1m0fSR":
            signalRegionPreselect = SL1m0fSR
        elif self.signalRegion == "SL1e1fSR":
            signalRegionPreselect = SL1e1fSR
        elif self.signalRegion == "SL1m1fSR":
            signalRegionPreselect = SL1m1fSR
        elif self.signalRegion == "SL1e2bSR":
            signalRegionPreselect = SL1e2bSR
        elif self.signalRegion == "SL1m2bSR":
            signalRegionPreselect = SL1m2bSR
        elif self.signalRegion == "AH0l0fSR":
            signalRegionPreselect = AH0l0fSR
        elif self.signalRegion == "AH0l1fSR":
            signalRegionPreselect = AH0l1fSR
        elif self.signalRegion == "AH0l2bSR":
            signalRegionPreselect = AH0l2bSR
        elif self.signalRegion == "SL1e":
            signalRegionPreselect = SL1e
        elif self.signalRegion == "SL1m":
            signalRegionPreselect = SL1m
        elif self.signalRegion == "AH":
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
            self.out.fillBranch("minDeltaPhi", minDeltaPhi)
            self.out.fillBranch("nbjetsHF", nbjetsHF)
            self.out.fillBranch("ntaus", ntaus)
            return True
        else:
            return False

preselectAH = lambda : preselectAnalysis("AH")

#########################################################################################################################################

#Select PostProcessor options here
# preselection=None
# #outputDir = "outDir2016AnalysisSR/ttbarDM"
# outputDir = "."
# inputbranches="python/postprocessing/analysis/keep_and_dropSR_in.txt"
# outputbranches="python/postprocessing/analysis/keep_and_dropSR_out.txt"
# inputFiles=["samples/ttbarDM_Mchi1Mphi100_scalar_full1.root", "samples/ttbarDM_Mchi1Mphi100_scalar_full2.root"]#, "samples/tDM_tChan_Mchi1Mphi100_scalar_full.root", "samples/tDM_tWChan_Mchi1Mphi100_scalar_full.root"]

#Applies pre-selection cuts for each signal region (SL vs AH, nb = 1 vs nb >=2, nf = 0 vs nf >= 1), one file for each SR (9 total files)
# p1=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL1e0fSR")],postfix="_SL1e0fSR",noOut=False,outputbranchsel=outputbranches)
# p2=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL1m0fSR")],postfix="_SL1m0fSR",noOut=False,outputbranchsel=outputbranches)
# p3=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL1e1fSR")],postfix="_SL1e1fSR",noOut=False,outputbranchsel=outputbranches)
# p4=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL1m1fSR")],postfix="_SL1m1fSR",noOut=False,outputbranchsel=outputbranches)
# p5=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL1e2bSR")],postfix="_SL1e2bSR",noOut=False,outputbranchsel=outputbranches)
# p6=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL1m2bSR")],postfix="_SL1m2bSR",noOut=False,outputbranchsel=outputbranches)
# p7=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("AH0l0fSR")],postfix="_AH0l0fSR_looseJetId",noOut=False,outputbranchsel=outputbranches)
# p8=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("AH0l1fSR")],postfix="_AH0l1fSR_looseJetId",noOut=False,outputbranchsel=outputbranches)
# p9=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("AH0l2bSR")],postfix="_AH0l2bSR_looseJetId",noOut=False,outputbranchsel=outputbranches)
# p1=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("AH")],postfix="_AH",noOut=False,outputbranchsel=outputbranches)
# p2=PostProcessor(outputDir,inputFiles,cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL")],postfix="_SL",noOut=False,outputbranchsel=outputbranches)
# p1.run()
# p2.run()
# p3.run()
# p4.run()
# p5.run()
# p6.run()
# p7.run()
# p8.run()
# p9.run()
