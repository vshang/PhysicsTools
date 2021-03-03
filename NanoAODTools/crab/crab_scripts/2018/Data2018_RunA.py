#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from PhysicsTools.NanoAODTools.postprocessing.analysis.ModuleCommon import *
#from PhysicsTools.NanoAODTools.postprocessing.corrections.getBTagHist import *

#jsonFile = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt" 
#jsonFile = "Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
jsonFile = "Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"

#p=PostProcessor(".",inputFiles(),cut=None,branchsel=None,modules=[analyze2016MC_Skim()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel="keep_and_dropSR_out.txt")
p=PostProcessor(".",inputFiles(),cut=None,branchsel=None,modules=[jetmetCorrector2018DataA(),analyze2018Data_Skim()],provenance=True,fwkJobReport=True,jsonInput=jsonFile,noOut=False,outputbranchsel="keep_and_dropSR_out.txt")
#p=PostProcessor(".",inputFiles(),cut=None,branchsel=None,modules=[getBTagHist2018_DeepCSV()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel="keep_and_dropBTag_out.txt",histFileName="hist.root",histDirName="ttbar")
p.run()

print "DONE"
os.system("ls -lR")
