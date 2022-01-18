#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from PhysicsTools.NanoAODTools.postprocessing.corrections.getBTagHist import *


p=PostProcessor(".",inputFiles(),cut=None,branchsel=None,modules=[getBTagHist2017_DeepCSV()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel="keep_and_dropBTag_out.txt",histFileName="hist.root",histDirName="ttbar")
p.run()

print "DONE"
os.system("ls -lR")
