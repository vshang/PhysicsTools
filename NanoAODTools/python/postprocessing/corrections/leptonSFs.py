import os
from ROOT import TFile
from scaleFactorTool import ScaleFactor

pathElectrons_10to20GeV = 'python/postprocessing/corrections/scaleFactors/electron/EGM2D_BtoH_low_RecoSF_Legacy2016.root'
pathElectrons_Over20GeV = 'python/postprocessing/corrections/scaleFactors/electron/EGM2D_BtoH_GT20GeV_RecoSF_Legacy2016.root'
pathMuons_ID_BCDEF = 'python/postprocessing/corrections/scaleFactors/muon/RunBCDEF_SF_ID.root'
pathMuons_ISO_BCDEF = 'python/postprocessing/corrections/scaleFactors/muon/RunBCDEF_SF_ISO.root'
pathMuons_ID_GH = 'python/postprocessing/corrections/scaleFactors/muon/RunGH_SF_ID.root'
pathMuons_ISO_GH = 'python/postprocessing/corrections/scaleFactors/muon/RunGH_SF_ISO.root'

class ElectronSFs:
    
    def __init__(self, year=2016):
        #Load histograms from files.
        
        assert year in [2016,2017,2018], "ElectronSFs: You must choose a year from: 2016, 2017, or 2018."
        
        if year==2016:
            self.sftool_10to20GeV = ScaleFactor(pathElectrons_10to20GeV,'EGamma_SF2D')
            self.sftool_Over20GeV  = ScaleFactor(pathElectrons_Over20GeV,'EGamma_SF2D')
        
    def getSF(self, pt, eta):
        #Get SF for single electron trigger.
        if pt < 20:
            return self.sftool_10to20GeV.getSF(pt,eta)
        elif pt > 20:
            return self.sftool_Over20GeV.getSF(pt,eta)
        else:
            print 'lepton pt not < 20 GeV or > 20 GeV, error!'
            exit(1)

class MuonSFs:

    def __init__(self, year=2016, run='B'):
        #Load histograms from files.
        
        assert year in [2016,2017,2018], "ElectronSFs: You must choose a year from: 2016, 2017, or 2018."
        assert run in ['B','C','D','E','F','G','H']
        
        if year==2016:
            if run in ['B','C','D','E','F']:
                self.sftool_ID = ScaleFactor(pathMuons_ID_BCDEF,'NUM_TightID_DEN_genTracks_eta_pt')
                self.sftool_ISO  = ScaleFactor(pathMuons_ISO_BCDEF,'NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt')
            elif run in ['G','H']:
                self.sftool_ID = ScaleFactor(pathMuons_ID_GH,'NUM_TightID_DEN_genTracks_eta_pt')
                self.sftool_ISO  = ScaleFactor(pathMuons_ISO_GH,'NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt')
        
    def getSF(self, pt, eta):
        #Get SF for single muon trigger.
        sf_ID = self.sftool_ID.getSF(pt,eta)
        sf_ISO = self.sftool_ISO.getSF(pt,eta)
        return sf_ID*sf_ISO
