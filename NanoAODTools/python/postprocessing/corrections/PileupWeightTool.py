from helper import modulepath, ensureTFile
from ROOT import TFile
path = modulepath+"/pileup/"


class PileupWeightTool:
    
    def __init__( self, year=2016, sigma='central' ):
        """Load data and MC pilup profiles."""
        
        assert( year in [2016,2017,2018] ), "You must choose a year from: 2016, 2017, or 2018."
        assert( sigma in ['central','up','down'] ), "You must choose a s.d. variation from: 'central', 'up', or 'down'."
        
        if year==2016:
          self.datafile = ensureTFile( path+'PileupData_GoldenJSON_Full2016.root', 'READ')
          self.mcfile   = ensureTFile( path+'pileup_profile_Summer16.root', 'READ')
        elif year==2017:
          self.datafile = ensureTFile( path+'PileupHistogram-goldenJSON-13tev-2017-99bins_withVar.root', 'READ')
          self.mcfile   = ensureTFile( path+'mcPileup2017.root', 'READ')
        elif year==2018:
          self.datafile = ensureTFile( path+'PileupHistogram-goldenJSON-13tev-2018-100bins_withVar.root', 'READ')
          self.mcfile   = ensureTFile( path+'mcPileup2018.root', 'READ')

        if sigma=='central':
            self.datahist = self.datafile.Get('pileup')
        elif sigma=='up':
            self.datahist = self.datafile.Get('pileup_plus')
        elif sigma=='down':
            self.datahist = self.datafile.Get('pileup_minus')
        self.mchist = self.mcfile.Get('pu_mc')
        self.datahist.SetDirectory(0)
        self.mchist.SetDirectory(0)
        self.datahist.Scale(1./self.datahist.Integral())
        self.mchist.Scale(1./self.mchist.Integral())
        self.datafile.Close()
        self.mcfile.Close()
        
    
    def getWeight(self,npu):
        """Get pileup weight for a given number of pileup interactions."""
        data = self.datahist.GetBinContent(self.datahist.GetXaxis().FindBin(npu))
        mc   = self.mchist.GetBinContent(self.mchist.GetXaxis().FindBin(npu))
        if mc>0.:
          return data/mc
        print ">>> Warning! PileupWeightTools.getWeight: Could not make pileup weight for npu=%s data=%s, mc=%s"%(npu,data,mc)  
        return 1.
