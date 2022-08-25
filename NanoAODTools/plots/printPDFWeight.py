from ROOT import *
gROOT.SetBatch(True)
from MCsampleListv2 import *
from DataSampleList import *
from utils import *
import os
import datetime
import re
import math

year = 2017

if year == 2016:
    MCSamples = samples2016
elif year == 2017:
    MCSamples = samples2017
elif year == 2018:
    MCSamples = samples2018

for process in MCSamples:
    print 'Process: ', process
    for dataset in MCSamples[process]:
        print '    Dataset: ', dataset
        for filepath in MCSamples[process][dataset]['filepaths']:
            file = TFile.Open(filepath,'')
            tree = file.Get('Events')
            tree.GetEntry(1)
            pdfWeightUp = tree.pdfWeightUp
            pdfWeightDown = tree.pdfWeightDown
            print '        pdfWeightUp = ', pdfWeightUp, ' | pdfWeightDown = ', pdfWeightDown
