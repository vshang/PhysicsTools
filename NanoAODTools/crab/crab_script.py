#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

#from PhysicsTools.NanoAODTools.postprocessing.analysis.preselectSR import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.ModuleCommon import *

#Load Mt2Com_bisect.o object file that contains C++ code to calculate M_T2W for SL region 
# ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2w_bisect_cc.so")
# ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/MT2Utility_cc.so")
# ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2bl_bisect_cc.so")
# ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/Mt2Com_bisect_cc.so")

# print "gSystem load: ", ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2w_bisect_cc.so")
# print "gSystem load: ", ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/MT2Utility_cc.so")
# print "gSystem load: ", ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/mt2bl_bisect_cc.so")
# print "gSystem load: ", ROOT.gSystem.Load("/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/Mt2Com_bisect_cc.so")

#Mt2Com_bisect = ROOT.Mt2Com_bisect()

#p=PostProcessor(".",inputFiles(),cut=None,modules=[preselectAll()],postfix="_All",provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False)
p=PostProcessor(".",inputFiles(),cut=None,modules=[analyzeAll()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False)
p.run()

print "DONE"
os.system("ls -lR")
