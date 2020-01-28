#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

#from PhysicsTools.NanoAODTools.postprocessing.examples.exampleModule import *
#from PhysicsTools.NanoAODTools.postprocessing.analysis.exampleModuleTest import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.preselectSR import *

p1=PostProcessor(".",inputFiles(),cut=None,modules=[preselectAll()],postfix="_All",provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False)
#p2=PostProcessor(outputDir,inputFiles(),cut=preselection,modules=[preselectSL()],postfix="_SL",provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False)
p1.run()
#p2.run()

print "DONE"
os.system("ls -lR")
