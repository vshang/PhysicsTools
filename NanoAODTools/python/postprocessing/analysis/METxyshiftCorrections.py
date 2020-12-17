import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *

runLocal = True

if runLocal:
    ROOT.gROOT.ProcessLine(".L /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/XYMETCorrection.h")
else:
    ROOT.gROOT.ProcessLine(".L XYMETCorrection.h")

#Module to apply MET xy-shift corrections before nanoAOD JES/JER corrections (https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETRun2Corrections#xy_Shift_Correction_MET_phi_modu)
class METxyshiftCorrector(Module):
    def __init__(self, year=2016, isData=False):
        self.year = year
        self.isData = isData
        self.isMC = not self.isData

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("METxyshift_pt",  "F");
        self.out.branch("METxyshift_phi", "F");
        self.out.branch("METxyshift_MetUnclustEnUpDeltaX", "F");
        self.out.branch("METxyshift_MetUnclustEnUpDeltaY", "F");
        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #Apply EE noise fix for 2017 (https://twiki.cern.ch/twiki/bin/viewauth/CMS/ExoPreapprovalChecklist)
        if self.year == 2017:
            METxyshift_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.METFixEE2017_pt, event.METFixEE2017_phi, event.run, 2017, self.isMC, event.PV_npvs)
            
            METxyshift_pt = METxyshift_pt_phi[0]
            METxyshift_phi = METxyshift_pt_phi[1]
            METxyshift_MetUnclustEnUpDeltaX = event.METFixEE2017_MetUnclustEnUpDeltaX
            METxyshift_MetUnclustEnUpDeltaY = event.METFixEE2017_MetUnclustEnUpDeltaY

        else:
            METxyshift_pt_phi = ROOT.METXYCorr_Met_MetPhi(event.MET_pt, event.MET_phi, event.run, 2017, self.isMC, event.PV_npvs)
            
            METxyshift_pt = METxyshift_pt_phi[0]
            METxyshift_phi = METxyshift_pt_phi[1]
            METxyshift_MetUnclustEnUpDeltaX = event.MET_MetUnclustEnUpDeltaX
            METxyshift_MetUnclustEnUpDeltaY = event.MET_MetUnclustEnUpDeltaY

        self.out.fillBranch("METxyshift_pt",  METxyshift_pt);
        self.out.fillBranch("METxyshift_phi", METxyshift_phi);
        self.out.fillBranch("METxyshift_MetUnclustEnUpDeltaX", METxyshift_MetUnclustEnUpDeltaX);
        self.out.fillBranch("METxyshift_MetUnclustEnUpDeltaY", METxyshift_MetUnclustEnUpDeltaY);
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

METxyshiftCorrector2016Data = lambda : METxyshiftCorrector(year=2016, isData=True) 
METxyshiftCorrector2016MC = lambda : METxyshiftCorrector(year=2016, isData=False) 

METxyshiftCorrector2017Data = lambda : METxyshiftCorrector(year=2017, isData=True) 
METxyshiftCorrector2017MC = lambda : METxyshiftCorrector(year=2017, isData=False) 

METxyshiftCorrector2018Data = lambda : METxyshiftCorrector(year=2018, isData=True) 
METxyshiftCorrector2018MC = lambda : METxyshiftCorrector(year=2018, isData=False) 

jetmetCorrector2017MC = createJMECorrector(isMC=True, dataYear=2017, jesUncert="Total", metBranchName="METFixEE2017")
jetmetCorrector2018MC = createJMECorrector(isMC=True, dataYear=2018, jesUncert="Total", applyHEMfix=True)

inputFiles = ["testSamples/ttbarPlusJets_Run2018.root"]
#inputFiles = ["testSamples/SingleElectron_2016H.root"]
outputDir = "."
selection=None
outputbranches="python/postprocessing/analysis/keep_and_drop_out.txt"


p=PostProcessor(outputDir,inputFiles,cut=selection,branchsel=None,modules=[METxyshiftCorrector2018MC(),jetmetCorrector2018MC()],postfix="_JESJERxyshiftcorrected",noOut=False,outputbranchsel=outputbranches)#,jsonInput=jsonFile)
p.run()
 
