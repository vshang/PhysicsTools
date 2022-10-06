#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

from PhysicsTools.NanoAODTools.postprocessing.analysis.ModuleCommon import *
#from PhysicsTools.NanoAODTools.postprocessing.corrections.getBTagHist import *

#jsonFile = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt" 
#jsonFile = "Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
#jsonFile = "Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"

with open(os.getenv("INPUT")) as f:
    inputFiles = [line.strip() for line in f]

p=PostProcessor(".",inputFiles,cut=None,branchsel=None,modules=[jetmetCorrector2016MC(),analyze2016MC_Skim()],provenance=True,fwkJobReport=True,noOut=False,outputbranchsel="keep_and_dropSR_out.txt")
#p=PostProcessor(".",inputFiles(),cut=None,branchsel=None,modules=[jetmetCorrector2016DataH(),analyze2016Data_Skim()],provenance=True,fwkJobReport=True,jsonInput=jsonFile,noOut=False,outputbranchsel="keep_and_dropSR_out.txt")
#p=PostProcessor(".",inputFiles(),cut=None,branchsel=None,modules=[getBTagHist2018_DeepCSV()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel="keep_and_dropBTag_out.txt",histFileName="hist.root",histDirName="ttbar")
p.run()

print "DONE"
os.system("ls -lR")
