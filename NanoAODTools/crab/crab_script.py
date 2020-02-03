#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from PhysicsTools.NanoAODTools.postprocessing.analysis.preselectSR import *
#from PhysicsTools.NanoAODTools.postprocessing.analysis.ModuleCommon import *

p=PostProcessor(".",inputFiles(),cut=None,modules=[preselectAll()],postfix="_All",provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False)
#p=PostProcessor(".",inputFiles(),cut=None,modules=[analyzeAll()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False)
p.run()

print "DONE"
os.system("ls -lR")
