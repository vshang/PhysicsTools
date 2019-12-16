if __name__ == '__main__':
 #####
 ##   User inputs 
 #####
 task          = 'Test_4' #Name of the task (e.g. Test, SignalRegion, ControlRegion, FullAnalysis, ...)
 analysis      = 'localTest' #Name of the analysis (e.g. VBFHN, LQtop, ...)
 unitsPerJob   = 1 #Units (usually number of root files) per job
 storageSite   = 'T2_US_Wisconsin'  #Site where you redirect the output
 datasetnames  = [ #Name of the folder created by crab and corresponding to its datasetinputs
#'TTWJetsToLNu'
'ttbarDM1'
                 ]
 datasetinputs = [ #Name of in the input dataset
#'/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM'
#'root://cmsxrootd.hep.wisc.edu///store/user/vshang/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full1.root' #Test 3
#'file:/hdfs/store/user/vshang/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full1.root' #Test 1
#'file:/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/samples/ttbarDM_Mchi1Mphi100_scalar_full1.root' #Test 2
                 ]

 #####
 ##   Multicrab configuration
 #####
 from CRABClient.UserUtilities import config, getUsernameFromSiteDB
 config = config()
 from CRABAPI.RawCommand import crabCommand
 from CRABClient.ClientExceptions import ClientException
 from httplib import HTTPException
 config.General.workArea = '%s' % (task) 
 
 def submit(config):
  try:
   crabCommand('submit', config = config)
  except HTTPException as hte:
   print "Failed submitting task: %s" % (hte.headers)
  except ClientException as cle:
   print "Failed submitting task: %s" % (cle)
 #####
 ##   Crab configuration
 #####
 for d in range(0,len(datasetnames)):
  config.section_('General')
  config.General.requestName      = datasetnames[d]
  config.General.transferLogs=True
  config.section_('JobType')
  config.JobType.pluginName       = 'Analysis'
  config.JobType.psetName         = 'PSet.py'
  config.JobType.scriptExe        = 'crab_script.sh'
  config.JobType.inputFiles =       ['crab_script.py','../scripts/haddnano.py']
   #hadd nano will not be needed once nano tools are in cmssw
  config.JobType.sendPythonFolder = True
  config.JobType.allowUndistributedCMSSW = True
  config.section_('Data')
  #config.Data.inputDataset        = datasetinputs[d]
  config.Data.userInputFiles      = [datasetinputs[d]]
  config.Data.inputDBS            = 'global'
  config.Data.splitting           = 'FileBased'
  #config.Data.splitting           = 'Automatic'
  #config.Data.totalUnits         = 2500 #With 'FileBased' splitting tells how many files to analyse
  config.Data.unitsPerJob         = unitsPerJob 
  config.Data.outLFNDirBase       = '/store/user/%s/%s' % (getUsernameFromSiteDB(),analysis) 
  config.Data.outputDatasetTag    = '%s' % (task) 
  config.Data.publication         = False
  config.section_('Site')
  config.Site.storageSite         = '%s' % (storageSite) 
  #config.Site.whitelist           = ['T2_US_Wisconsin']
  submit(config)