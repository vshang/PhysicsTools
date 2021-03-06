from helper import modulepath, ensureTFile
import os, re

class ScaleFactor:
    
    def __init__(self, filename, histname, name="<noname>", ptvseta=True):
        #print '>>> ScaleFactor.init("%s","%s",name="%s",ptvseta=%r)'%(filename,histname,name,ptvseta)
        self.name     = name
        self.ptvseta  = ptvseta
        self.filename = filename
        self.file     = ensureTFile(filename)
        self.hist     = self.file.Get(histname)
        if not self.hist:
          print '>>> ScaleFactor(%s).__init__: histogram "%s" does not exist in "%s"'%(self.name,histname,filename)
          exit(1)
        self.hist.SetDirectory(0)
        self.file.Close()
        
        if ptvseta: self.getSF = self.getSF_ptvseta
        else:       self.getSF = self.getSF_etavspt
        
    def getSF_ptvseta(self, pt, eta, syst=0):
        """Get SF for a given pT, eta."""
        xbin = self.hist.GetXaxis().FindBin(eta)
        ybin = self.hist.GetYaxis().FindBin(pt)
        if xbin==0: xbin = 1
        elif xbin>self.hist.GetXaxis().GetNbins(): xbin -= 1
        if ybin==0: ybin = 1
        elif ybin>self.hist.GetYaxis().GetNbins(): ybin -= 1
        if syst == 0: #Don't include systematic error
            sf = self.hist.GetBinContent(xbin,ybin)
        elif syst > 0: #Include up systematic error
            sf = self.hist.GetBinContent(xbin,ybin) + self.hist.GetBinErrorUp(xbin,ybin)
        elif syst < 0: #Include down systematic error
            sf = self.hist.GetBinContent(xbin,ybin) - self.hist.GetBinErrorLow(xbin,ybin)
        #print "ScaleFactor(%s).getSF_ptvseta: pt = %6.2f, eta = %6.3f, sf = %6.3f"%(self.name,pt,eta,sf)
        return sf
        
    def getSF_etavspt(self, pt, eta, syst=0):
        """Get SF for a given pT, eta."""
        xbin = self.hist.GetXaxis().FindBin(pt)
        ybin = self.hist.GetYaxis().FindBin(eta)
        if xbin==0: xbin = 1
        elif xbin>self.hist.GetXaxis().GetNbins(): xbin -= 1
        if ybin==0: ybin = 1
        elif ybin>self.hist.GetYaxis().GetNbins(): ybin -= 1
        if syst == 0: #Don't include systematic error
            sf = self.hist.GetBinContent(xbin,ybin)
        elif syst > 0: #Include up systematic error
            sf = self.hist.GetBinContent(xbin,ybin) + self.hist.GetBinErrorUp(xbin,ybin)
        elif syst < 0: #Include down systematic error
            sf = self.hist.GetBinContent(xbin,ybin) - self.hist.GetBinErrorLow(xbin,ybin)
        #print "ScaleFactor(%s).getSF_etavspt: pt = %6.2f, eta = %6.3f, sf = %6.3f"%(self.name,pt,eta,sf)
        return sf
