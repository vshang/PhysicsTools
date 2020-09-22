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

#Load Mt2Com_bisect.o object file that contains C++ code to calculate M_T2W for SL region (runLocal = False if running jobs through CRAB)
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
            self.btagTool = BTagWeightTool(self.btag,'medium',channel='ttbar',year=self.year)
            self.puTool = PileupWeightTool(year=self.year)
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
        if self.isMC:
            self.out.branch("leptonWeight", "F")
            self.out.branch("bjetWeight", "F")
            self.out.branch("puWeight", "F")
            self.out.branch("eventWeight", "F")
            self.out.branch("ewkWWeight", "F")
            self.out.branch("ewkZWeight", "F")
            self.out.branch("qcdWWeight", "F")
            self.out.branch("qcdZTo2NuWeight", "F")
            self.out.branch("qcdZTo2LWeight", "F")

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
            centralJetsEnumerate = filter(lambda j : ((30 < j[1].pt < 50 and j[1].puId == 7) or j[1].pt > 50) and abs(j[1].eta) < 2.4 and cleanJet(j[1]) and j[1].jetId == 7, enumerate(jets)) #Use tightLepVeto jet ID WP for 2016 with tight puId for jet_pt < 50
            forwardJetsEnumerate = filter(lambda j : ((30 < j[1].pt < 50 and j[1].puId == 7) or j[1].pt > 50) and 2.4 < abs(j[1].eta) < 4 and cleanJet(j[1]) and j[1].jetId == 7, enumerate(jets))
        else:
            centralJetsEnumerate = filter(lambda j : ((30 < j[1].pt < 50 and j[1].puId == 7) or j[1].pt > 50) and abs(j[1].eta) < 2.4 and cleanJet(j[1]) and j[1].jetId == 6, enumerate(jets)) #Use tightLepVeto jet ID WP for 2017 and 2018 with tight puId for jet_pt < 50
            forwardJetsEnumerate = filter(lambda j : ((30 < j[1].pt < 50 and j[1].puId == 7) or j[1].pt > 50) and 2.4 < abs(j[1].eta) < 4 and cleanJet(j[1]) and j[1].jetId == 6, enumerate(jets))

        btag_WP = getattr(BTagWPs(self.btag,self.year),'medium')
        if self.btag == 'CSVv2':
            bJetsEnumerate = filter(lambda j : j[1].btagCSVV2 > btag_WP, centralJetsEnumerate)
        elif self.btag == 'DeepCSV':
            bJetsEnumerate = filter(lambda j : j[1].btagDeepB > btag_WP, centralJetsEnumerate)

        njets = len(centralJetsEnumerate)
        nfjets = len(forwardJetsEnumerate)
        nbjets = len(bJetsEnumerate)

        centralJets = [j[1] for j in centralJetsEnumerate]
        forwardJets = [j[1] for j in forwardJetsEnumerate]
        bJets = [j[1] for j in bJetsEnumerate]
        #Also store index of each jet in collection
        index_centralJets = [j[0] for j in centralJetsEnumerate]
        index_forwardJets = [j[0] for j in forwardJetsEnumerate]
        index_bJets = [j[0] for j in bJetsEnumerate]

        #Apply MET corrections
        if self.year == 2017:
            METcorrected_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_pt, event.METFixEE2017_phi, event.run, 2017, self.isMC, event.PV_npvs)
        else:
            METcorrected_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.MET_pt, event.MET_phi, event.run, self.year, self.isMC, event.PV_npvs)
        METcorrected_pt = METcorrected_pt_phi[0]
        METcorrected_phi = METcorrected_pt_phi[1]

        #Calculate minDeltaPhi and minDeltaPhi(j_(1,2), missing pt) preselection variable of all central jets 
        minDeltaPhi = -9 #If there is less than 2 jets, set value to -9 to indicate  minDeltaPhi cannot be calculated
        minDeltaPhi12 = -9 #If there is less than 2 jets, set value to -9 to indicate minDeltaPhi12 cannot be calculated
        minDeltaPhi_puppi = -9 #If there is less than 2 jets, set value to -9 to indicate  minDeltaPhi_puppi cannot be calculated
        minDeltaPhi12_puppi = -9 #If there is less than 2 jets, set value to -9 to indicate minDeltaPhi12_puppi cannot be calculated
        if len(centralJets) > 1: #Should always be true for both SL and AH signal regions
            jet1 = centralJets[0] #jet1 (jet2) is the jet with the largest (second-largest) pt
            jet2 = centralJets[1]
            deltaPhi1 = min(abs(jet1.phi - METcorrected_phi), 2 * math.pi - abs(jet1.phi - METcorrected_phi)) #phi angle between jet1 and missing pt
            deltaPhi2 = min(abs(jet2.phi - METcorrected_phi), 2 * math.pi - abs(jet2.phi - METcorrected_phi)) #phi angle between jet2 and missing pt
            minDeltaPhi12 = min(deltaPhi1, deltaPhi2) #First calculate minDeltaPhi12
            deltaPhi1_puppi = min(abs(jet1.phi - event.PuppiMET_phi), 2 * math.pi - abs(jet1.phi - event.PuppiMET_phi)) #phi angle between jet1 and Puppi missing pt
            deltaPhi2_puppi = min(abs(jet2.phi - event.PuppiMET_phi), 2 * math.pi - abs(jet2.phi - event.PuppiMET_phi)) #phi angle between jet2 and Puppi missing pt
            minDeltaPhi12_puppi = min(deltaPhi1_puppi, deltaPhi2_puppi) #First calculate minDeltaPhi12_puppi 
            #Now calculate minDeltaPhi
            minDeltaPhi = min(abs(jet1.phi - METcorrected_phi), 2 * math.pi - abs(jet1.phi - METcorrected_phi)) #phi angle between jet1 and missing pt
            #Now calculate minDeltaPhi_puppi
            minDeltaPhi_puppi = min(abs(jet1.phi - event.PuppiMET_phi), 2 * math.pi - abs(jet1.phi - event.PuppiMET_phi)) #phi angle between jet1 and Puppi missing pt
            for i in range(1, len(centralJets)):
                jeti = centralJets[i]
                minDeltaPhi_i = min(abs(jeti.phi - METcorrected_phi), 2 * math.pi - abs(jeti.phi - METcorrected_phi)) #phi angle between jeti and missing pt
                minDeltaPhi_puppi_i = min(abs(jeti.phi - event.PuppiMET_phi), 2 * math.pi - abs(jeti.phi - event.PuppiMET_phi)) #phi angle between jeti and Puppi missing pt
                if minDeltaPhi_i < minDeltaPhi: #Choose lowest minDeltaPhi out of all central jets
                    minDeltaPhi = minDeltaPhi_i
                if minDeltaPhi_puppi_i < minDeltaPhi_puppi: #Choose lowest minDeltaPhi_puppi out of all central jets
                    minDeltaPhi_puppi = minDeltaPhi_puppi_i

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
        M_Tb_puppi = -9
        
        if len(bJets) > 0:
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

        #Calculate M_T, M_T2^W, and M_T2^ll using PFMET
        M_T = -9 #If there are no tight leptons, set value to -9 to indicate M_T cannot be calculated
        M_T2W = -9 #If there are no tight leptons, set value to -9 to indicate M_T2W cannot be calculated
        M_T2ll = -9 #If there are not exactly two tight leptons, set value to -9 to indicate M_T2ll cannot be calculated
        M_T_puppi = -9 #If there are no tight leptons, set value to -9 to indicate M_T_puppi cannot be calculated
        M_T2W_puppi = -9 #If there are no tight leptons, set value to -9 to indicate M_T2W_puppi cannot be calculated
        M_T2ll_puppi = -9 #If there are not exactly two tight leptons, set value to -9 to indicate M_T2ll_puppi cannot be calculated
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

            #Calculate M_T2^W 
            leptonTLorentz = lepton.p4()
            metTVector2 = ROOT.TVector2(METcorrected_pt * math.cos(METcorrected_phi), METcorrected_pt * math.sin(METcorrected_phi))
            PuppimetTVector2 = ROOT.TVector2(event.PuppiMET_pt * math.cos(event.PuppiMET_phi), event.PuppiMET_pt * math.sin(event.PuppiMET_phi))
            M_T2W = Mt2Com_bisect.calculateMT2w(ljetVector, bjetVector, leptonTLorentz, metTVector2, "MT2w")
            M_T2W_puppi = Mt2Com_bisect.calculateMT2w(ljetVector, bjetVector, leptonTLorentz, PuppimetTVector2, "MT2w")
            
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
        
        #Tau candidates are counted
        tauCandidates = Collection(event, "Tau")
        if self.isSignal:
            skimmedTaus = filter(lambda tau : tau.pt > 20 and abs(tau.eta) < 2.3 and tau.idMVAoldDM >= 31 and cleanJet(tau), tauCandidates)
        else:
            skimmedTaus = filter(lambda tau : tau.pt > 20 and abs(tau.eta) < 2.3 and tau.idMVAoldDM2017v2 >= 31 and cleanJet(tau), tauCandidates)
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
            ewkWWeight = 1
            ewkZWeight = 1
            qcdWWeight = 1
            qcdZTo2NuWeight = 1
            qcdZTo2LWeight = 1
            GenV = filter(lambda gen : (gen.pdgId == 23 or abs(gen.pdgId) == 24) and gen.status == 22, genParticles)
            if len(GenV) > 0:
                GenV_pt = GenV[0].pt
                ewkWWeight *= self.kFactorTool.getEWKW(GenV_pt)
                ewkZWeight *= self.kFactorTool.getEWKZ(GenV_pt)
                qcdWWeight *= self.kFactorTool.getQCDW(GenV_pt)
                qcdZTo2NuWeight *= self.kFactorTool.getQCDZTo2Nu(GenV_pt)
                qcdZTo2LWeight *= self.kFactorTool.getQCDZTo2L(GenV_pt)

        #Determine if there exists two tight electrons/muons such that their invariant mass m_ll is between 60-120 GeV and the hadronic recoil >= 250 GeV
        m_llExists = False
        m_ll = 0
        recoilPtMiss = 0
        m_llExists_puppi = False
        recoilPtMiss_puppi = 0
        lepton1_charge = 0
        lepton2_charge = 0
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
            if self.isMC:
                self.out.fillBranch("leptonWeight", leptonWeight)
                self.out.fillBranch("bjetWeight", bjetWeight)
                self.out.fillBranch("puWeight", puWeight)
                self.out.fillBranch("eventWeight", eventWeight)
                self.out.fillBranch("ewkWWeight", ewkWWeight)
                self.out.fillBranch("ewkZWeight", ewkZWeight)
                self.out.fillBranch("qcdWWeight", qcdWWeight)
                self.out.fillBranch("qcdZTo2NuWeight", qcdZTo2NuWeight)
                self.out.fillBranch("qcdZTo2LWeight", qcdZTo2LWeight)
            return True
        else:
            return False

        #return True

analyze2016MC = lambda : CommonAnalysis("All",year=2016,isData=False,isSignal=False,btag='DeepCSV')
analyze2016SignalMC = lambda : CommonAnalysis("All",year=2016,isData=False,isSignal=True,btag='DeepCSV')
analyze2016Data = lambda : CommonAnalysis("All",year=2016,isData=True,isSignal=False,btag='DeepCSV')

analyze2017MC = lambda : CommonAnalysis("All",year=2017,isData=False,isSignal=False,btag='DeepCSV')
analyze2017SignalMC = lambda : CommonAnalysis("All",year=2017,isData=False,isSignal=True,btag='DeepCSV')
analyze2017Data = lambda : CommonAnalysis("All",year=2017,isData=True,isSignal=False,btag='DeepCSV')

analyze2018MC = lambda : CommonAnalysis("All",year=2018,isData=False,isSignal=False,btag='DeepCSV')
analyze2018SignalMC = lambda : CommonAnalysis("All",year=2018,isData=False,isSignal=True,btag='DeepCSV')
analyze2018Data = lambda : CommonAnalysis("All",year=2018,isData=True,isSignal=False,btag='DeepCSV')

#########################################################################################################################################

if runLocal:
    #Select PostProcessor options here
    selection=None
    #outputDir = "outDir2016AnalysisSR/ttbarDM/"
    #outputDir = "testSamples/"
    outputDir = "."
    #inputbranches="python/postprocessing/analysis/keep_and_dropSR_in.txt"
    outputbranches="python/postprocessing/analysis/keep_and_dropSR_out.txt"
    inputFiles=["samples/ttbarDM_Mchi1Mphi100_scalar_full1.root","samples/ttbarDM_Mchi1Mphi100_scalar_full2.root","samples/tDM_tChan_Mchi1Mphi100_scalar_full.root","samples/tDM_tWChan_Mchi1Mphi100_scalar_full.root"]
    #inputFiles=["testSamples/SingleElectron_2016H.root"]#,"SingleMuon_2016B_ver1.root","SingleMuon_2016B_ver2.root","SingleMuon_2016E.root"]
    #inputFiles=["testSamples/ttbarPlusJets_Run2018.root"]
    #inputFiles=["testSamples/SingleElectron_2017B.root"]
    #inputFiles = ["testSamples/SingleElectron_2018A.root"]
    #inputFiles = ["testSamples/SingleElectron_2016H.root"]
    #jsonFile = "python/postprocessing/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
    #jsonFile = "python/postprocessing/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"
    #jsonFile = "python/postprocessing/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"

    p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[analyze2016SignalMC()],postfix="_ModuleCommon_2016MC_09142020",noOut=False,outputbranchsel=outputbranches)#,jsonInput=jsonFile)
    #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[analyze2016Data()],postfix="_ModuleCommon_2016Data",noOut=False,outputbranchsel=outputbranches,jsonInput=jsonFile)
    #p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[analyze2016MC()],postfix="_ModuleCommon_2018MC",noOut=False,outputbranchsel=outputbranches)
    p.run()
