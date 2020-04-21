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
from PhysicsTools.NanoAODTools.postprocessing.corrections.kfactors import *
from PhysicsTools.NanoAODTools.postprocessing.corrections.PileupWeightTool import *

#Load Mt2Com_bisect.o object file that contains C++ code to calculate M_T2W for SL region 
# ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2w_bisect_cc.so")
# ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/MT2Utility_cc.so")
# ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2bl_bisect_cc.so")
# ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/Mt2Com_bisect_cc.so")

ROOT.gSystem.Load("mt2w_bisect_cc.so")
ROOT.gSystem.Load("MT2Utility_cc.so")
ROOT.gSystem.Load("mt2bl_bisect_cc.so")
ROOT.gSystem.Load("Mt2Com_bisect_cc.so")

Mt2Com_bisect = ROOT.Mt2Com_bisect()

class CommonAnalysis(Module):
    def __init__(self, signalRegion, year=2016, isData=False):
        self.signalRegion = signalRegion
        self.year = year
        self.isData = isData
        self.isMC = not self.isData
        self.nEvent = 0
        if self.isMC:
            self.eleSFs = ElectronSFs(self.year)
            self.muSFs = MuonSFs(self.year)
            self.btagTool = BTagWeightTool('CSVv2','medium',channel='ttbar',year=self.year)
            self.puTool = PileupWeightTool(year=self.year)

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
        #self.out.branch("nbjetsHF", "I")
        self.out.branch("nfjets", "I")
        self.out.branch("minDeltaPhi", "F")
        self.out.branch("minDeltaPhi12", "F")
        self.out.branch("M_Tb", "F")
        self.out.branch("M_T", "F")
        self.out.branch("M_T2W", "F")
        self.out.branch("jet1p_TH_T", "F")
        self.out.branch("jet1_jetId", "I")
        self.out.branch("jet1_chHEF", "F")
        self.out.branch("ntaus", "I")
        if self.isMC:
            self.out.branch("leptonWeight", "F")
            self.out.branch("bjetWeight", "F")
            self.out.branch("puWeight", "F")
            self.out.branch("eventWeight", "F")
            self.out.branch("ewkWeight", "F")
            self.out.branch("qcdWeight", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go 
to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        if self.isMC:
            genParticles = Collection(event, "GenPart")

        #Tight/Veto electrons are defined and counted
        vetoElectrons = filter(lambda lep : lep.pt > 10 and lep.cutBased_Sum16 != 0 and (abs(lep.eta) < 1.4442 or 1.566 < abs(lep.eta) < 2.5), electrons)
        tightElectrons = filter(lambda lep : lep.pt > 30 and abs(lep.eta) < 2.1 and lep.cutBased_Sum16 == 4, vetoElectrons)
        #vetoElectrons = filter(lambda lep : lep.pt > 10 and lep.cutBased != 0 and (abs(lep.eta) < 1.4442 or 1.566 < abs(lep.eta) < 2.5), electrons)
        #tightElectrons = filter(lambda lep : lep.pt > 30 and abs(lep.eta) < 2.1 and lep.cutBased == 4, vetoElectrons)

        nVetoElectrons = len(vetoElectrons)
        nTightElectrons = len(tightElectrons)
        
        #Tight/Loose muons are defined and counted
        looseMuons = filter(lambda lep : lep.pt > 10 and lep.looseId and lep.pfRelIso04_all < 0.25 and abs(lep.eta) < 2.4, muons)
        #looseMuons = filter(lambda lep : lep.pt > 10 and lep.softId and lep.pfRelIso04_all < 0.25 and abs(lep.eta) < 2.4, muons)
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

        #Jet categories are defined and counted 
        centralJets = filter(lambda j : j.pt > 30 and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId > 0, jets) #Define central jets 
        #centralJets = filter(lambda j : j.pt > 30 and abs(j.eta) < 2.4 and cleanJet(j) and looseJet(j), jets)
        bJets = filter(lambda j : j.btagCSVV2 > 0.8484, centralJets) #Define b-jets
        #bJetsHF = filter(lambda j : j.hadronFlavour == 5, centralJets) #Define b-jets by hadron flavour
        forwardJets = filter(lambda j : j.pt > 30 and 2.4 < abs(j.eta) < 4 and cleanJet(j) and j.jetId > 0, jets) #Define forward jets
        #forwardJets = filter(lambda j : j.pt > 30 and 2.4 < abs(j.eta) < 4 and cleanJet(j) and looseJet(j) > 0, jets)

        njets = len(centralJets)
        nbjets = len(bJets)
        #nbjetsHF = len(bJetsHF)
        nfjets = len(forwardJets)

        #Calculate minDeltaPhi and minDeltaPhi(j_(1,2), missing pt) preselection variable of all central jets
        minDeltaPhi = -9 #If there is less than 2 jets, set value to -9 to indicate  minDeltaPhi cannot be calculated
        minDeltaPhi12 = -9 #If there is less than 2 jets, set value to -9 to indicate minDeltaPhi12 cannot be calculated
        if len(centralJets) > 1: #Should always be true for both SL and AH signal regions
            jet1 = centralJets[0] #jet1 (jet2) is the jet with the largest (second-largest) pt
            jet2 = centralJets[1]
            deltaPhi1 = min(abs(jet1.phi - event.MET_phi), 2 * math.pi - abs(jet1.phi - event.MET_phi)) #phi angle between jet1 and missing pt
            deltaPhi2 = min(abs(jet2.phi - event.MET_phi), 2 * math.pi - abs(jet2.phi - event.MET_phi)) #phi angle between jet2 and missing pt
            minDeltaPhi12 = min(deltaPhi1, deltaPhi2) #First calculate minDeltaPhi12
            #Now calculate minDeltaPhi
            minDeltaPhi = min(abs(jet1.phi - event.MET_phi), 2 * math.pi - abs(jet1.phi - event.MET_phi)) #phi angle between jet1 and missing pt
            for i in range(1, len(centralJets)):
                jeti = centralJets[i]
                minDeltaPhi_i = min(abs(jeti.phi - event.MET_phi), 2 * math.pi - abs(jeti.phi - event.MET_phi)) #phi angle between jeti and missing pt
                if minDeltaPhi_i < minDeltaPhi: #Choose lowest minDeltaPhi out of all central jets
                    minDeltaPhi = minDeltaPhi_i

        #Jet TLorentzVectors are constructed to calculate M_T2^W
        ljetVector = ROOT.vector("TLorentzVector")()
        bjetVector = ROOT.vector("TLorentzVector")()

        #Calculate jet1p_T/H_T
        H_T = 0
        jet1p_TH_T = 9 #If there are no jets, set value to +9 to indicate jet1p_T/H_T cannnot be calculated
        
        if len(centralJets) > 0:
            for jet in centralJets:
                H_T += jet.pt
                if jet.btagCSVV2 < 0.8484:
                    ljetVector.push_back(jet.p4())

            jet1p_TH_T = centralJets[0].pt/H_T

        #Calculate jet1_jetId and jet1_chHEF
        jet1_jetId  = -9
        jet1_chHEF = -9
        if len(centralJets) > 0:
            jet1_jetId = centralJets[0].jetId
            jet1_chHEF = centralJets[0].chHEF

        #Calculate M_T^b
        M_Tb = -9 #If there are no bjets, set value to -9 to indicate M_Tb cannot be calculated
        
        if len(bJets) > 0:
            bjet1 = bJets[0]

            for bjet in bJets:
                bjetVector.push_back(bjet.p4())
                if bjet.btagCSVV2 > bjet1.btagCSVV2:
                    bjet1 = bjet

            deltaPhiMTb = bjet1.phi - event.MET_phi
            M_Tb = math.sqrt(2 * event.MET_pt * bjet1.pt * (1 - math.cos(deltaPhiMTb)))

        #Calculate M_T and M_T2^W 
        M_T = -9 #If there are no tight leptons, set value to -9 to indicate M_T cannot be calculated
        M_T2W = -9 #If there are no tight leptons, set value to -9 to indicate M_T2W cannot be calculated
        if len(tightElectrons) > 0 or len(tightMuons) > 0: #Default to using electron if both tight electron and muon exist
            if len(tightElectrons) > 0:
                lepton = tightElectrons[0] #Default to using tight electron with greatest pT
            elif len(tightMuons) > 0:
                lepton = tightMuons[0] #Default to using tight muon with greatest pT

            #Calculate M_T
            deltaPhiMT = lepton.phi - event.MET_phi
            M_T = math.sqrt(2 * event.MET_pt * lepton.pt * (1 - math.cos(deltaPhiMT)))

            #Calculate M_T2^W 
            leptonTLorentz = lepton.p4()
            metTVector2 = ROOT.TVector2(event.MET_pt * math.cos(event.MET_phi), event.MET_pt * math.sin(event.MET_phi))
            M_T2W = Mt2Com_bisect.calculateMT2w(ljetVector, bjetVector, leptonTLorentz, metTVector2, "MT2w")
        
        #Tau candidates are counted
        tauCandidates = Collection(event, "Tau")
        #skimmedTaus = filter(lambda tau : tau.pt > 18 and abs(tau.eta) < 2.3 and tau.idMVAnewDM >= 31 and cleanJet(tau), tauCandidates)
        skimmedTaus = filter(lambda tau : tau.pt > 18 and abs(tau.eta) < 2.3 and tau.idMVAnewDM2017v2 >= 31 and cleanJet(tau), tauCandidates)
        ntaus = len(skimmedTaus)

        #Only calculate scale factors if sample is MC
        if self.isMC:
            #Calculate lepton scale factor weight
            leptonWeight = 1
            for tightElectron in tightElectrons:
                leptonWeight *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta)
            for tightMuon in tightMuons:
                leptonWeight *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta)
            #Calculate b-jet scale factor weight
            bjetWeight = self.btagTool.getWeight(centralJets)
            #Calculate PU weight
            puWeight = self.puTool.getWeight(event.Pileup_nTrueInt)
            #Calculate total event weight
            eventWeight = 1*leptonWeight*bjetWeight*puWeight
            #Calculate EWK and QCD k factors if a Gen V particles exists (Z or W)
            ewkWeight = 1
            qcdWeight = 1
            GenV = filter(lambda gen : (gen.pdgId == 23 or abs(gen.pdgId) == 24) and gen.status == 22, genParticles)
            if len(GenV) > 0:
                GenV_pt = GenV[0].pt
                ewkWeight *= getEWKW(GenV_pt)
                qcdWeight *= getQCDW(GenV_pt)
        

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

        #Signal region chosen here
        if self.signalRegion == "All":
            signalRegion = True
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
            self.out.fillBranch("njets", njets)
            self.out.fillBranch("nbjets", nbjets)
            #self.out.fillBranch("nbjetsHF", nbjetsHF)
            self.out.fillBranch("nfjets", nfjets)
            self.out.fillBranch("minDeltaPhi", minDeltaPhi)
            self.out.fillBranch("minDeltaPhi12", minDeltaPhi12)
            self.out.fillBranch("M_Tb", M_Tb)
            self.out.fillBranch("M_T", M_T)
            self.out.fillBranch("M_T2W", M_T2W)
            self.out.fillBranch("jet1p_TH_T", jet1p_TH_T)
            self.out.fillBranch("jet1_jetId", jet1_jetId)
            self.out.fillBranch("jet1_chHEF", jet1_chHEF)
            self.out.fillBranch("ntaus", ntaus)
            if self.isMC:
                self.out.fillBranch("leptonWeight", leptonWeight)
                self.out.fillBranch("bjetWeight", bjetWeight)
                self.out.fillBranch("puWeight", puWeight)
                self.out.fillBranch("eventWeight", eventWeight)
                self.out.fillBranch("ewkWeight", ewkWeight)
                self.out.fillBranch("qcdWeight", qcdWeight)
            return True
        else:
            return False

        #return True

analyze2016MC = lambda : CommonAnalysis("All",year=2016,isData=False)
analyze2016Data = lambda : CommonAnalysis("All",year=2016,isData=True)

#########################################################################################################################################

# #Select PostProcessor options here
# selection=None
# #outputDir = "outDir2016AnalysisSR/ttbarDM/"
# outputDir = "testSamples/"
# #inputbranches="python/postprocessing/analysis/keep_and_dropSR_in.txt"
# outputbranches="python/postprocessing/analysis/keep_and_dropSR_out.txt"
# #inputFiles=["samples/ttbarDM_Mchi1Mphi100_scalar_full1.root"]#,"samples/ttbarDM_Mchi1Mphi100_scalar_full2.root","samples/tDM_tChan_Mchi1Mphi100_scalar_full.root","samples/tDM_tWChan_Mchi1Mphi100_scalar_full.root"]
# inputFiles=["SingleElectron_2016H.root"]#,"SingleMuon_2016B_ver1.root","SingleMuon_2016B_ver2.root","SingleMuon_2016E.root"]
# jsonFile = "python/postprocessing/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"

# #p1=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[analyze2016MC()],postfix="_ModuleCommon_2016MC",noOut=False,outputbranchsel=outputbranches)#,jsonInput=jsonFile)
# p2=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[analyze2016Data()],postfix="_ModuleCommon_2016Data",noOut=False,outputbranchsel=outputbranches)#,jsonInput=jsonFile)
# #p1.run()
# p2.run()
