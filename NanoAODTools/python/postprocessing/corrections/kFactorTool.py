from helper import modulepath, ensureTFile
import os, re
import math
from kfactors.get2016kfactors import *

path = modulepath+'/kfactors/'
#path = '/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/corrections/kfactors/'

class KFactorTool:

    def __init__(self, year=2016):
        #Load k-factor histograms from files

        assert year in [2016,2017,2018], "ElectronSFs: You must choose a year from: 2016, 2017, or 2018."
        self.year = year

        self.f_nlo_qcd = ensureTFile(path+'ZorW_NLO_corrections.root')

        self.nlo_qcd_WJets = self.f_nlo_qcd.Get('QCD_W')
        self.nlo_qcd_ZJets = self.f_nlo_qcd.Get('QCD_Z')

    def getEWKW(self, pt):
        return get2016EWKW(pt)
        # if self.year == 2016:
        #     return get2016EWKW(pt)
        # else:
        #     bin = self.nlo_ewk_WJets.GetXaxis().FindBin(pt)
        #     if bin == 0: bin = 1
        #     elif bin > self.nlo_ewk_WJets.GetXaxis().GetNbins(): bin -= 1
        #     sf = self.nlo_ewk_WJets.GetBinContent(bin)
        #     return sf

    def getEWKZ(self, pt):
        return get2016EWKZ(pt)
        # if self.year == 2016:
        #     return get2016EWKZ(pt)
        # else:
        #     bin = self.nlo_ewk_ZJets.GetXaxis().FindBin(pt)
        #     if bin == 0: bin = 1
        #     elif bin > self.nlo_ewk_ZJets.GetXaxis().GetNbins(): bin -= 1
        #     sf = self.nlo_ewk_ZJets.GetBinContent(bin)
        #     return sf

    def getQCDW(self, pt):
        if self.year == 2016:
            return get2016QCDW(pt)
        else:
            bin = self.nlo_qcd_WJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_WJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_WJets.GetBinContent(bin)
            return sf

    def getQCDZTo2Nu(self, pt):
        #return get2016QCDZ(pt)
        if self.year == 2016:
            return get2016QCDZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            return sf

    def getQCDZTo2L(self, pt):
        if self.year == 2016:
            return get2016QCDZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            return sf

    def getRenUpW(self, pt):
        if self.year == 2016:
            return get2016RenUpW(pt)
        else:
            bin = self.nlo_qcd_WJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_WJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_WJets.GetBinContent(bin)
            ratio = get2016RenUpW(pt)/get2016QCDW(pt)
            return sf*ratio

    def getRenDownW(self, pt):
        if self.year == 2016:
            return get2016RenDownW(pt)
        else:
            bin = self.nlo_qcd_WJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_WJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_WJets.GetBinContent(bin)
            ratio = get2016RenDownW(pt)/get2016QCDW(pt)
            return sf*ratio

    def getFacUpW(self, pt):
        if self.year == 2016:
            return get2016FacUpW(pt)
        else:
            bin = self.nlo_qcd_WJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_WJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_WJets.GetBinContent(bin)
            ratio = get2016FacUpW(pt)/get2016QCDW(pt)
            return sf*ratio

    def getFacDownW(self, pt):
        if self.year == 2016:
            return get2016FacDownW(pt)
        else:
            bin = self.nlo_qcd_WJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_WJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_WJets.GetBinContent(bin)
            ratio = get2016FacDownW(pt)/get2016QCDW(pt)
            return sf*ratio

    def getRenUpZTo2Nu(self, pt):
        if self.year == 2016:
            return get2016RenUpZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            ratio = get2016RenUpZ(pt)/get2016QCDZ(pt)
            return sf*ratio

    def getRenDownZTo2Nu(self, pt):
        if self.year == 2016:
            return get2016RenDownZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            ratio = get2016RenDownZ(pt)/get2016QCDZ(pt)
            return sf*ratio

    def getFacUpZTo2Nu(self, pt):
        if self.year == 2016:
            return get2016FacUpZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            ratio = get2016FacUpZ(pt)/get2016QCDZ(pt)
            return sf*ratio

    def getFacDownZTo2Nu(self, pt):
        if self.year == 2016:
            return get2016FacDownZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            ratio = get2016FacDownZ(pt)/get2016QCDZ(pt)
            return sf*ratio

    def getRenUpZTo2L(self, pt):
        if self.year == 2016:
            return get2016RenUpZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            ratio = get2016RenUpZ(pt)/get2016QCDZ(pt)
            return sf*ratio

    def getRenDownZTo2L(self, pt):
        if self.year == 2016:
            return get2016RenDownZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            ratio = get2016RenDownZ(pt)/get2016QCDZ(pt)
            return sf*ratio

    def getFacUpZTo2L(self, pt):
        if self.year == 2016:
            return get2016FacUpZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            ratio = get2016FacUpZ(pt)/get2016QCDZ(pt)
            return sf*ratio

    def getFacDownZTo2L(self, pt):
        if self.year == 2016:
            return get2016FacDownZ(pt)
        else:
            bin = self.nlo_qcd_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZJets.GetBinContent(bin)
            ratio = get2016FacDownZ(pt)/get2016QCDZ(pt)
            return sf*ratio
