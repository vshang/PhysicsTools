#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

#from PhysicsTools.NanoAODTools.postprocessing.examples.exampleModule import *
#from PhysicsTools.NanoAODTools.postprocessing.analysis.exampleModuleTest import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.preselectSR import *
p=PostProcessor(".",inputFiles(),cut=None,modules=[preselectAH()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
#p=PostProcessor(".",inputFiles(),cut=None,modules=[exampleModuleConstr(),provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
p.run()

#Select PostProcessor options here
#preselection=None
#outputDir="."
#inputbranches="../python/postprocessing/2016Analysis/keep_and_dropSR_in.txt"
#outputbranches="../python/postprocessing/2016Analysis/keep_and_dropSR_out.txt"
#inputFiles=["../samples/ttbarDM_Mchi1Mphi100_scalar_full1.root", "../samples/ttbarDM_Mchi1Mphi100_scalar_full2.root"]#, "samples/tDM_tChan_Mchi1Mphi100_scalar_full.root", "samples/tDM_tWChan_Mchi1Mphi100_scalar_full.root"]

#preselectAH = lambda : preselectAnalysis("AH")

#p1=PostProcessor(outputDir,inputFiles(),cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("AH")],postfix="_AH",provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel=outputbranches)
#p2=PostProcessor(outputDir,inputFiles(),cut=preselection,branchsel=inputbranches,modules=[preselectAnalysis("SL")],postfix="_SL",provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel=outputbranches)
#p1=PostProcessor(outputDir,inputFiles(),cut=preselection,modules=[preselectAH()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False)
#p2=PostProcessor(outputDir,inputFiles(),cut=preselection,modules=[preselectAnalysis("SL")],postfix="_SL",provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False)
#p1.run()
#p2.run()

print "DONE"
os.system("ls -lR")


