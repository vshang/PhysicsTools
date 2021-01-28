from helper import modulepath, ensureTFile
import os, re
import math
from kfactors.get2016kfactors import *

#path = modulepath+'/kfactors/'
path = '/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/corrections/kfactors/'

class KFactorTool:

    def __init__(self, year=2016):
        #Load k-factor histograms from files

        assert year in [2016,2017,2018], "ElectronSFs: You must choose a year from: 2016, 2017, or 2018."
        self.year = year

        self.f_nlo_ewk_WJets = ensureTFile(path+'merged_kfactors_wjets.root')
        self.f_nlo_ewk_ZJets = ensureTFile(path+'merged_kfactors_zjets.root')
        self.f_nlo_qcd_ZTo2Nu = ensureTFile(path+'kfac_znn_filter.root')
        self.f_nlo_qcd_ZTo2L = ensureTFile(path+'kfac_dy_filter.root')

        self.nlo_ewk_WJets = self.f_nlo_ewk_WJets.Get('kfactor_monojet_ewk')
        self.nlo_ewk_ZJets = self.f_nlo_ewk_ZJets.Get('kfactor_monojet_ewk')
        self.nlo_qcd_ZTo2Nu = self.f_nlo_qcd_ZTo2Nu.Get('kfac_znn_filter')
        self.nlo_qcd_ZTo2L = self.f_nlo_qcd_ZTo2L.Get('kfac_dy_filter')

    def getEWKW(self, pt):
        if self.year == 2016:
            return get2016EWKW(pt)
        else:
            bin = self.nlo_ewk_WJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_ewk_WJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_ewk_WJets.GetBinContent(bin)
            return sf

    def getEWKZ(self, pt):
        if self.year == 2016:
            return get2016EWKZ(pt)
        else:
            bin = self.nlo_ewk_ZJets.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_ewk_ZJets.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_ewk_ZJets.GetBinContent(bin)
            return sf

    def getQCDW(self, pt):
        if self.year == 2016:
            return get2016QCDW(pt)
        else:
            sf = 1.053*math.exp(-3.163e-3*pt)+0.746
            return sf

    def getQCDZTo2Nu(self, pt):
        if self.year == 2016:
            return get2016QCDZ(pt)
        else:
            bin = self.nlo_qcd_ZTo2Nu.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZTo2Nu.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZTo2Nu.GetBinContent(bin)
            return sf

    def getQCDZTo2L(self, pt):
        if self.year == 2016:
            return get2016QCDZ(pt)
        else:
            bin = self.nlo_qcd_ZTo2L.GetXaxis().FindBin(pt)
            if bin == 0: bin = 1
            elif bin > self.nlo_qcd_ZTo2L.GetXaxis().GetNbins(): bin -= 1
            sf = self.nlo_qcd_ZTo2L.GetBinContent(bin)
            return sf

    def getRenUpW(self, pt):
        return get2016RenUpW(pt)

    def getRenDownW(self, pt):
        return get2016RenDownW(pt)

    def getFacUpW(self, pt):
        return get2016FacUpW(pt)

    def getFacDownW(self, pt):
        return get2016FacDownW(pt)

    def getRenUpZ(self, pt):
        return get2016RenUpZ(pt)

    def getRenDownZ(self, pt):
        return get2016RenDownZ(pt)

    def getFacUpZ(self, pt):
        return get2016FacUpZ(pt)

    def getFacDownZ(self, pt):
        return get2016FacDownZ(pt)
