#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

from PhysicsTools.NanoAODTools.postprocessing.analysis.ModuleCommon import *

with open(os.getenv("INPUT")) as f:
    inputFiles = [line.strip() for line in f]

p=PostProcessor(".",inputFiles,cut=None,branchsel="keep_and_dropCount_out.txt",modules=[countEvents()],provenance=True,fwkJobReport=True,noOut=False,outputbranchsel="keep_and_dropCount_out.txt")
p.run()

print "DONE"
os.system("ls -lR")
