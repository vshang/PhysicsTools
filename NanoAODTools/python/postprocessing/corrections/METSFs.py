from helper import modulepath, ensureTFile
import os, re

pathMET = modulepath+'/METTrigger/'

class METSFs:

    def __init__(self, year=2016, name="<noname>"):
        #Load histograms from files.

        assert year in [2016,2017,2018], "METSFs: You must choose a year from: 2016, 2017, or 2018."
        self.year = year
        self.name = name

        if year==2016:
            filename = pathMET+'MET_Trigger_SFs_2016.root'

        if year==2017:
            filename = pathMET+'MET_Trigger_SFs_2017.root'

        if year==2018:
            filename = pathMET+'MET_Trigger_SFs_2018.root'

        self.file = ensureTFile(filename)
        self.hist = self.file.Get('SF')
        if not self.hist:
          print '>>> ScaleFactor(%s).__init__: histogram "%s" does not exist in "%s"'%(self.name,histname,filename)
          exit(1)
        self.hist.SetDirectory(0)
        self.file.Close()
        
    def getSF(self, MET):
        #Get SF for MET trigger efficiency for a given MET pT bin
        bin = self.hist.GetXaxis().FindBin(MET)
        if bin==0: bin = 1
        sf = self.hist.GetBinContent(bin)
        return sf
