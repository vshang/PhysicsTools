from ROOT import *
from MCsampleList import *
from DataSampleList import *
from utils import *
import os
import datetime
import re
import math

print 'Getting tfile and event trees...'
#samples2016['ttbarPlusJets']['TFile'] = TFile.Open(samples2016['ttbarPlusJets']['TTTo2L2Nu']['filepaths'][0],'')
#samples2016['ttbarPlusJets']['eventTree'] = samples2016['ttbarPlusJets']['TFile'].Get('Events')
file = TFile.Open('../SingleElectron_2017C_v7_ModuleCommon_2017Data.root','')
tree = file.Get('Events')
file_old = TFile.Open('../SingleElectron_2017C_v7_ModuleCommon_2017Data_old.root','')
tree_old = file_old.Get('Events')

print 'Got Tfile and event tree'

hists = {}
hists['Ele35'] = TH1F('Ele35', 'HLT_Ele35_WPTight_Gsf; Leading electron p_{T}; Events', 20, 0, 200)
hists['Ele32old'] = TH1F('Ele32old', 'Old passEle32WPTightGsf2017; Leading electron p_{T}; Events', 20, 0, 200)
hists['Ele32new'] = TH1F('Ele32new', 'New passEle32WPTightGsf2017; Leading electron p_{T}; Events', 20, 0, 200)

def drawHist(eventTree, cut, name):
    print 'drawing hist...'
    hist = TH1F('hist', '; Electron p_{T}; Events', 20, 0, 200)
    var = 'Electron_pt[index_tightElectrons[0]]'
    eventTree.Draw(var+'>>hist', cut)
    hists[name] += hist
    print 'finished drawing hist'


#drawHist(samples2016['ttbarPlusJets']['eventTree'])
drawHist(tree, 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && HLT_Ele35_WPTight_Gsf', 'Ele35')
drawHist(tree_old, 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && passEle32WPTightGsf2017', 'Ele32old')
drawHist(tree, 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && passEle32WPTightGsf2017', 'Ele32new')

for name in hists:
    print 'nentries in ' + name + ' = ', hists[name].GetEntries()
c1 = TCanvas('c1', 'c1', 800, 800)
hists['Ele35'].Draw('hist')
c1.SaveAs('HLT_Ele35_WPTight_Gsf.png')

c2 = TCanvas('c2', 'c2', 800, 800)
hists['Ele32old'].Draw('hist')
c2.SaveAs('passEle32WPTightGsf2017_old.png')

c3 = TCanvas('c3', 'c3', 800, 800)
hists['Ele32new'].Draw('hist')
c3.SaveAs('passEle32WPTightGsf2017_new.png')
