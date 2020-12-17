from helper import modulepath
from scaleFactorTool import ScaleFactor

pathElectrons = modulepath+'/scaleFactors/electron/'
pathMuons = modulepath+'/scaleFactors/muon/'

class ElectronSFs:

    def __init__(self, year=2016):
        #Load histograms from files.

        assert year in [2016,2017,2018], "ElectronSFs: You must choose a year from: 2016, 2017, or 2018."
        self.year = year

        if year==2016:
            self.sftool_10to20GeV = ScaleFactor(pathElectrons+'SF2016/EGM2D_BtoH_low_RecoSF_Legacy2016.root','EGamma_SF2D')
            self.sftool_Over20GeV  = ScaleFactor(pathElectrons+'SF2016/EGM2D_BtoH_GT20GeV_RecoSF_Legacy2016.root','EGamma_SF2D')
            self.sftool_ID = ScaleFactor(pathElectrons+'SF2016/2016LegacyReReco_ElectronTight.root','EGamma_SF2D')

        if year==2017:
            self.sftool_10to20GeV = ScaleFactor(pathElectrons+'SF2017/egammaEffi.txt_EGM2D_runBCDEF_passingRECO_lowEt.root','EGamma_SF2D')
            self.sftool_Over20GeV  = ScaleFactor(pathElectrons+'SF2017/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root','EGamma_SF2D')
            self.sftool_ID = ScaleFactor(pathElectrons+'SF2017/2017_ElectronTight.root','EGamma_SF2D')

        if year==2018:
            self.sftool_10to20GeV = ScaleFactor(pathElectrons+'SF2018/egammaEffi.txt_EGM2D_updatedAll.root','EGamma_SF2D')
            self.sftool_Over20GeV  = ScaleFactor(pathElectrons+'SF2018/egammaEffi.txt_EGM2D_updatedAll.root','EGamma_SF2D')
            self.sftool_ID = ScaleFactor(pathElectrons+'SF2018/2018_ElectronTight.root','EGamma_SF2D')
        
    def getSF(self, pt, eta, syst=0):
        #Get SF for electron ID and reconstruction efficiency. Set syst=1 to include up systematic error, syst=-1 to include down systematic error.
        sf_ID = self.sftool_ID.getSF(pt,eta,syst)
        if pt < 20:
            sf_EFF = self.sftool_10to20GeV.getSF(pt,eta,syst)
        elif pt > 20:
            sf_EFF = self.sftool_Over20GeV.getSF(pt,eta,syst)
        else:
            print 'lepton pt not < 20 GeV or > 20 GeV, error!'
            exit(1)
        return sf_ID*sf_EFF

class MuonSFs:

    def __init__(self, year=2016, run='B'):
        #Load histograms from files.
        
        assert year in [2016,2017,2018], "ElectronSFs: You must choose a year from: 2016, 2017, or 2018."
        assert run in ['B','C','D','E','F','G','H']
        self.year = year
        
        if year==2016:
            if run in ['B','C','D','E','F']:
                self.sftool_ID = ScaleFactor(pathMuons+'SF2016/EfficienciesStudies_2016_legacy_rereco_systematic_RunBCDEF_SF_ID.root','NUM_TightID_DEN_genTracks_eta_pt_syst')
                self.sftool_ISO  = ScaleFactor(pathMuons+'SF2016/EfficienciesStudies_2016_legacy_rereco_systematic_RunBCDEF_SF_ISO.root','NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_syst')
                self.sftool_Trigger = ScaleFactor(pathMuons+'SF2016/EfficienciesAndSF_RunBtoF.root','IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio')
            elif run in ['G','H']:
                self.sftool_ID = ScaleFactor(pathMuons+'SF2016/EfficienciesStudies_2016_legacy_rereco_systematic_RunGH_SF_ID.root','NUM_TightID_DEN_genTracks_eta_pt_syst')
                self.sftool_ISO  = ScaleFactor(pathMuons+'SF2016/EfficienciesStudies_2016_legacy_rereco_systematic_RunGH_SF_ISO.root','NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_syst')
                self.sftool_Trigger = ScaleFactor(pathMuons+'SF2016/EfficienciesAndSF_Period4.root','IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio')

        if year==2017:
            self.sftool_ID = ScaleFactor(pathMuons+'SF2017/RunBCDEF_SF_ID_syst.root','NUM_TightID_DEN_genTracks_pt_abseta_syst',ptvseta=False)
            self.sftool_ISO = ScaleFactor(pathMuons+'SF2017/RunBCDEF_SF_ISO_syst.root','NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta_syst',ptvseta=False)
            self.sftool_Trigger = ScaleFactor(pathMuons+'SF2017/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root','IsoMu27_PtEtaBins/abseta_pt_ratio')

        if year==2018: #See https://twiki.cern.ch/twiki/bin/view/CMS/MuonReferenceEffs2018 for more details on trigger weights
            self.sftool_ID = ScaleFactor(pathMuons+'SF2018/EfficienciesStudies_2018_rootfiles_RunABCD_SF_ID.root','NUM_TightID_DEN_TrackerMuons_pt_abseta_syst',ptvseta=False)
            self.sftool_ISO = ScaleFactor(pathMuons+'SF2018/EfficienciesStudies_2018_rootfiles_RunABCD_SF_ISO.root','NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta_syst',ptvseta=False)
            self.sftool_TriggerBeforeHLTUpdate = ScaleFactor(pathMuons+'SF2018/EfficienciesStudies_2018_trigger_EfficienciesAndSF_2018Data_BeforeMuonHLTUpdate.root','IsoMu24_PtEtaBins/abseta_pt_ratio')
            self.sftool_TriggerAfterHLTUpdate = ScaleFactor(pathMuons+'SF2018/EfficienciesStudies_2018_trigger_EfficienciesAndSF_2018Data_AfterMuonHLTUpdate.root','IsoMu24_PtEtaBins/abseta_pt_ratio')

    def getSF(self, pt, eta, syst=0):
        #Get SF for muon ID and isolation efficiency. Set syst=1 to include up systematic error, syst=-1 to include down systematic error.
        sf_ID = self.sftool_ID.getSF(pt,eta,syst)
        sf_ISO = self.sftool_ISO.getSF(pt,eta,syst)
        return sf_ID*sf_ISO

    def getWeight(self, pt, eta, run, syst=0):
        #Get weight for single muon trigger efficiency. 
        if self.year ==2018:
            if run < 316361:
                sf_Trigger = self.sftool_TriggerBeforeHLTUpdate.getSF(pt,eta,0)
            elif run >= 316361:
                sf_Trigger = self.sftool_TriggerAfterHLTUpdate.getSF(pt,eta,0)
        else:
            sf_Trigger = self.sftool_Trigger.getSF(pt,eta,0)
        if syst==0:
            return sf_Trigger
        elif syst==1:
            return 1.005*sf_Trigger
        elif syst==-1:
            return 0.995*sf_Trigger
        
