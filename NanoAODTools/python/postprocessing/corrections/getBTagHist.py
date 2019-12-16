import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.corrections.BTaggingTool import *

class getBTagHist(Module):
    def __init__(self,tagger,wp,year,channel):
        
        assert(year in [2016,2017,2018]), "You must choose a year from: 2016, 2017, or 2018."
        assert(tagger in ['CSVv2','DeepCSV']), "BTagWeightTool: You must choose a tagger from: CSVv2, DeepCSV!"
        assert(wp in ['loose','medium','tight']), "BTagWeightTool: You must choose a WP from: loose, medium, tight!"

        self.writeHistFile = True
        self.tagger = tagger
        self.wp = wp
        self.year = year
        self.channel = channel

        threshold = getattr(BTagWPs(tagger,year),wp)
        if 'deep' in tagger.lower():
          self.tagged = lambda j: j.btagDeepB>threshold
        else:
          self.tagged = lambda j: j.btagCSVV2>threshold

    def beginJob(self,histFile=None,histDirName=None):
        Module.beginJob(self,histFile,histDirName)
        
        self.hist_b = createEfficiencyMap('%s_%s_%s'%(self.tagger,'b',self.wp))
        self.hist_c = createEfficiencyMap('%s_%s_%s'%(self.tagger,'c',self.wp))
        self.hist_udsg = createEfficiencyMap('%s_%s_%s'%(self.tagger,'udsg',self.wp))
        self.hist_b_all = createEfficiencyMap('%s_%s_%s_all'%(self.tagger,'b',self.wp))
        self.hist_c_all = createEfficiencyMap('%s_%s_%s_all'%(self.tagger,'c',self.wp))
        self.hist_udsg_all = createEfficiencyMap('%s_%s_%s_all'%(self.tagger,'udsg',self.wp))

        self.addObject(self.hist_b)
        self.addObject(self.hist_c)
        self.addObject(self.hist_udsg)
        self.addObject(self.hist_b_all)
        self.addObject(self.hist_c_all)
        self.addObject(self.hist_udsg_all)

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go 
to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")

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

        #Calculate and fill bjet efficiency histograms
        centralJets = filter(lambda j : j.pt > 30 and abs(j.eta) < 2.4 and cleanJet(j) and j.jetId > 0, jets) #Define central jets
        for jet in centralJets:
            flavor = flavorToString(jet.hadronFlavour)
            if flavor == 'b':
                self.hist_b_all.Fill(jet.pt,jet.eta)
                if self.tagged(jet):
                    self.hist_b.Fill(jet.pt,jet.eta)
            elif flavor == 'c':
                self.hist_c_all.Fill(jet.pt,jet.eta)
                if self.tagged(jet):
                    self.hist_c.Fill(jet.pt,jet.eta)
            elif flavor == 'udsg':
                self.hist_udsg_all.Fill(jet.pt,jet.eta)
                if self.tagged(jet):
                    self.hist_udsg.Fill(jet.pt,jet.eta)


        return True

testModule = lambda : getBTagHist('CSVv2','medium',2016,'ttbar')

#########################################################################################################################################

#Select PostProcessor options here
preselection=None
outputDir = "python/postprocessing/corrections/btag/ttbar/"
inputFiles=["samples/ttbarDM_Mchi1Mphi100_scalar_full1.root"]#, "samples/ttbarDM_Mchi1Mphi100_scalar_full2.root", "samples/tDM_tChan_Mchi1Mphi100_scalar_full.root", "samples/tDM_tWChan_Mchi1Mphi100_scalar_full.root"]

p=PostProcessor(".",inputFiles,cut=preselection,branchsel=None,modules=[testModule()],noOut=True,histFileName=outputDir+"ttbarDM_Mchi1Mphi100_scalar_full1_btagHists.root",histDirName="ttbar")
p.run()