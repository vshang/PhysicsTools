#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from PhysicsTools.NanoAODTools.postprocessing.analysis.ModuleCommon import *

p=PostProcessor(".",inputFiles(),cut=None,branchsel="keep_and_dropCount_out.txt",modules=[countEvents()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel="keep_and_dropCount_out.txt")
p.run()

print "DONE"
os.system("ls -lR")
