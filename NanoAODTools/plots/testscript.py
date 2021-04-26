from ROOT import *
from MCsampleList import *
from DataSampleList import *
from utils import *
import os
import datetime
import re
import math

print 'Getting tfile and event trees...'
samples2016['ttbarPlusJets']['TFile'] = TFile.Open(samples2016['ttbarPlusJets']['TTTo2L2Nu']['filepaths'][0],'')
samples2016['ttbarPlusJets']['eventTree'] = samples2016['ttbarPlusJets']['TFile'].Get('Events')
print 'Got Tfile and event tree'

hists = {}
hists['test'] = TH1F('test', '', 15, 250, 550)

def drawHist(eventTree):
    print 'drawing hist...'
    hist = TH1F('hist', '', 15, 250, 550)
    cut = 'nTightElectrons == 1 && nVetoElectrons == 1 && nLooseMuons == 0 && njets >= 2 && nbjets >= 1 && METcorrected_pt >= 250'
    var = 'METcorrected_pt'
    eventTree.Draw(var+'>>hist', cut)
    hists['test'] += hist
    print 'finished drawing hist'


drawHist(samples2016['ttbarPlusJets']['eventTree'])

print 'nentries = ', hists['test'].GetEntries()
c = TCanvas('c', 'c', 800, 800)
hists['test'].Draw('hist')
c.SaveAs('test_hist.png')


