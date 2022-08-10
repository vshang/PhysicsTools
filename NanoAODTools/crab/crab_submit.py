if __name__ == '__main__':
 #####
 ##   User inputs 
 #####
 task          = 'ModuleCommonSkim_07252022' #Name of the task (e.g. Test, SignalRegion, ControlRegion, FullAnalysis, ...)
 #task          = 'getBTagHist_12222021'
 unitsPerJob   = 1 #Units (usually number of root files) per job
 #unitsPerJob = 1000
 storageSite   = 'T2_US_Wisconsin'  #Site where you redirect the output
 getBTagHist = False

 #####
 ##   Helper function to set appropriate text file containing DAS file paths for input datasets
 #####
 def getDatasetinputs(analysis, year, run):
  samples = 'datasetinputs'+year+'/'+analysis+'_Run'+year+run+'.txt'
  with open(samples, 'r') as f:
   dataset = [line.strip() for line in f]
  return dataset

 C_files = ['../python/postprocessing/analysis/mt2w_bisect_cc.so', '../python/postprocessing/analysis/mt2w_bisect.cc', '../python/postprocessing/analysis/mt2w_bisect.h', '../python/postprocessing/analysis/mt2w_bisect_cc.d', '../python/postprocessing/analysis/MT2Utility_cc.so', '../python/postprocessing/analysis/MT2Utility.cc', '../python/postprocessing/analysis/MT2Utility.h', '../python/postprocessing/analysis/MT2Utility_cc.d', '../python/postprocessing/analysis/mt2bl_bisect_cc.so', '../python/postprocessing/analysis/mt2bl_bisect.cc', '../python/postprocessing/analysis/mt2bl_bisect.h', '../python/postprocessing/analysis/mt2bl_bisect_cc.d', '../python/postprocessing/analysis/Mt2Com_bisect_cc.so', '../python/postprocessing/analysis/Mt2Com_bisect.cc', '../python/postprocessing/analysis/Mt2Com_bisect.h', '../python/postprocessing/analysis/Mt2Com_bisect_cc.d','../python/postprocessing/analysis/lester_mt2_bisect.h','../python/postprocessing/analysis/XYMETCorrection.h','../python/postprocessing/analysis/topness_cc.so','../python/postprocessing/analysis/topness.cc','../python/postprocessing/analysis/topness.h','../python/postprocessing/analysis/topness_cc.d','../python/postprocessing/analysis/JetUtil_cc.so','../python/postprocessing/analysis/JetUtil.cc','../python/postprocessing/analysis/JetUtil.h','../python/postprocessing/analysis/JetUtil_cc.d']

 #####
 ##   Submit command
 #####
 from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
 config = config()
 from CRABAPI.RawCommand import crabCommand
 from CRABClient.ClientExceptions import ClientException
 from httplib import HTTPException
 config.General.workArea = '%s' % (task) 
 
 def submit(config, analysis, year, isData, isSignal, run, datasetinputs, index):
  config.General.requestName      = analysis + '_Run' + year + run + '_sample%d' % index
  config.General.transferLogs=True
  config.section_('JobType')
  config.JobType.pluginName       = 'Analysis'
  config.JobType.psetName         = 'PSet.py'
  if isData:
   crab_script = 'crab_scripts/' + year + '/Data' + year + '_Run' + run
  else:
   if isSignal:
    crab_script = 'crab_scripts/' + year + '/MCSignal' + year
   else:
    crab_script = 'crab_scripts/' + year + '/MC' + year
  if getBTagHist:
   crab_script = 'crab_scripts/BTag/crab_script_BTag' + year
  config.JobType.scriptExe       = crab_script + '.sh'
  config.JobType.inputFiles      =  [crab_script + '.py','../scripts/haddnano.py','../python/postprocessing/analysis/keep_and_dropSR_out.txt','../python/postprocessing/analysis/keep_and_dropCount_out.txt','../python/postprocessing/data/json/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt','../python/postprocessing/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt','../python/postprocessing/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt','../python/postprocessing/data/json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt','../python/postprocessing/data/json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'] + C_files
  #hadd nano will not be needed once nano tools are in cmssw
  if getBTagHist:
   config.JobType.inputFiles       = [crab_script + '.py','../scripts/haddnano.py','../python/postprocessing/analysis/keep_and_dropBTag_out.txt']
   #config.JobType.outputFiles = ['hist.root'] #Enable for making BTag histograms using getBTagHist.py
  config.JobType.sendPythonFolder = True
  config.JobType.allowUndistributedCMSSW = True
  #config.JobType.maxJobRuntimeMin = 2630
  #config.JobType.maxMemoryMB      = 4000
  config.section_('Data')
  config.Data.inputDataset        = datasetinputs[index]
  #config.Data.userInputFiles      = [datasetinputs[index]]
  config.Data.inputDBS            = 'global'
  config.Data.splitting           = 'FileBased'
  #config.Data.splitting           = 'Automatic'
  #config.Data.totalUnits         = 2500 #With 'FileBased' splitting tells how many files to analyse
  config.Data.unitsPerJob         = unitsPerJob 
  #config.Data.outLFNDirBase       = '/store/user/%s/%s' % (getUsernameFromSiteDB(),analysis) #No longer works with CRAB 
  config.Data.outLFNDirBase       = '/store/user/%s/%s' % ('vshang',analysis+'_Run'+year+run)
  config.Data.outputDatasetTag    = '%s' % (task) 
  config.Data.publication         = False
  config.section_('Site')
  config.Site.storageSite         = '%s' % (storageSite) 
  #config.Site.whitelist           = ['T2_US_Wisconsin']
  try:
   crabCommand('submit', config = config)
  except HTTPException as hte:
   print "Failed submitting task: %s" % (hte.headers)
  except ClientException as cle:
   print "Failed submitting task: %s" % (cle)

 #####
 ##   Wrapping the submit command
 #####
 from multiprocessing import Process
 def submitWrapper(analysis, year, isData, isSignal, run, datasetinputs):
  for d in range(0,len(datasetinputs)):
   p = Process(target=submit, args=(config, analysis, year, isData, isSignal, run, datasetinputs, d))
   p.start()
   p.join()

 #####
 ##   Submit all samples
 #####
 runs2016 = ['B','C','D','E','F','G','H']
 runs2017 = ['B','C','D','E','F']
 runs2018 = ['A','B','C','D']
 isData = True
 isSignal = False
 
 # for run in runs2016:
 #  submitWrapper('MET', '2016', isData, isSignal, run, getDatasetinputs('MET', '2016', run))
 #  submitWrapper('SingleElectron', '2016', isData, isSignal, run, getDatasetinputs('SingleElectron', '2016', run))
 #  submitWrapper('SingleMuon', '2016', isData, isSignal, run, getDatasetinputs('SingleMuon', '2016', run))
 #  submitWrapper('SinglePhoton', '2016', isData, isSignal, run, getDatasetinputs('SinglePhoton', '2016', run))
 # for run in runs2017:
 #  submitWrapper('MET', '2017', isData, isSignal, run, getDatasetinputs('MET', '2017', run))
 #  submitWrapper('SingleElectron', '2017', isData, isSignal, run, getDatasetinputs('SingleElectron', '2017', run))
 #  submitWrapper('SingleMuon', '2017', isData, isSignal, run, getDatasetinputs('SingleMuon', '2017', run))
 #  submitWrapper('SinglePhoton', '2017', isData, isSignal, run, getDatasetinputs('SinglePhoton', '2017', run))
 # for run in runs2018:
 #  submitWrapper('MET', '2018', isData, isSignal, run, getDatasetinputs('MET', '2018', run))
 #  submitWrapper('SingleElectron', '2018', isData, isSignal, run, getDatasetinputs('SingleElectron', '2018', run))
 #  submitWrapper('SingleMuon', '2018', isData, isSignal, run, getDatasetinputs('SingleMuon', '2018', run))
 
 isData = False
 run = ''
 datasetnames = ['ttbarDM']
 #datasetnames = ['ttbarPlusJets','singleTop','WPlusJets','ZTo2L','ZTo2Nu','WW','WZ','ZZ','TTV','QCD']
 #datasetnames = ['ttH','VH','ttbarDM','ttbarPlusJets','singleTop','WPlusJets','ZTo2L','ZTo2Nu','WW','WZ','ZZ','TTV','QCD']#,'WPlusJetsNLO','ZTo2LNLO','ZTo2NuNLO']
 #years = ['UL2016']
 years = ['2016']
 #years = ['2016','2017','2018']
 for year in years:
  for dataset in datasetnames:
   if dataset == 'ttbarDM' or dataset == 'QCDPt' or dataset == 'ttH' or dataset == 'VH':
    submitWrapper(dataset, year, isData, True, '', getDatasetinputs(dataset, year, run=''))
   else:
    submitWrapper(dataset, year, isData, isSignal, '', getDatasetinputs(dataset, year, run=''))
 
