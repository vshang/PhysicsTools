if __name__ == '__main__':
 #####
 ##   User inputs 
 #####
 task          = 'ModuleCommon_08092020' #Name of the task (e.g. Test, SignalRegion, ControlRegion, FullAnalysis, ...)
 #task          = 'getBTagHist_DeepCSV_08062020'
 analysis      = 'QCD' #Name of the analysis (e.g. VBFHN, LQtop, ...)
 year          = '2018'
 unitsPerJob   = 1 #Units (usually number of root files) per job
 #unitsPerJob = 1000
 storageSite   = 'T2_US_Wisconsin'  #Site where you redirect the output
 # datasetnames  = [ #Name of the folder created by crab and corresponding to its datasetinputs
# 'TTTo2L2Nu', 
# 'TTToSemilepton'
# #'TTWJetsToLNu'
# #'ttbarDM1'
#                  ]

 #Set appropriate text file containing DAS file paths for input datasets
 samples = 'datasetinputs'+year+'/'+analysis+'_Run'+year+'.txt'
 #samples = 'datasetinputs/ttbarPlusJets.txt' 
 #samples = 'datasetinputs/singleTop.txt' 
 #samples = 'datasetinputs/WPlusJets.txt'
 #samples = 'datasetinputs/ZTo2L.txt'
 #samples = 'datasetinputs/ZTo2Nu.txt'
 #samples = 'datasetinputs/WW.txt'
 #samples = 'datasetinputs/WZ.txt'
 #samples = 'datasetinputs/ZZ.txt'
 #samples = 'datasetinputs/TTV.txt'
 #samples = 'datasetinputs/QCD.txt'
 with open(samples, 'r') as f:
  datasetinputs = [line.strip() for line in f]

 Mt2Com_files = ['../python/postprocessing/analysis/mt2w_bisect_cc.so', '../python/postprocessing/analysis/mt2w_bisect.cc', '../python/postprocessing/analysis/mt2w_bisect.h', '../python/postprocessing/analysis/mt2w_bisect_cc.d', '../python/postprocessing/analysis/MT2Utility_cc.so', '../python/postprocessing/analysis/MT2Utility.cc', '../python/postprocessing/analysis/MT2Utility.h', '../python/postprocessing/analysis/MT2Utility_cc.d', '../python/postprocessing/analysis/mt2bl_bisect_cc.so', '../python/postprocessing/analysis/mt2bl_bisect.cc', '../python/postprocessing/analysis/mt2bl_bisect.h', '../python/postprocessing/analysis/mt2bl_bisect_cc.d', '../python/postprocessing/analysis/Mt2Com_bisect_cc.so', '../python/postprocessing/analysis/Mt2Com_bisect.cc', '../python/postprocessing/analysis/Mt2Com_bisect.h', '../python/postprocessing/analysis/Mt2Com_bisect_cc.d','../python/postprocessing/analysis/lester_mt2_bisect.h']

 #####
 ##   Multicrab configuration
 #####
 from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
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
 #for d in range(0,len(datasetnames)):
 for d in range(0,len(datasetinputs)):
  config.section_('General')
  config.General.requestName      = analysis + '_Run' + year + '_sample%d' % d #datasetnames[d]
  config.General.transferLogs=True
  config.section_('JobType')
  config.JobType.pluginName       = 'Analysis'
  config.JobType.psetName         = 'PSet.py'
  config.JobType.scriptExe        = 'crab_script.sh'
  #config.JobType.inputFiles      =  ['crab_script.py','../scripts/haddnano.py','../python/postprocessing/analysis/keep_and_dropSR_out.txt','../python/postprocessing/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'] + Mt2Com_files
  #config.JobType.inputFiles      =  ['crab_script.py','../scripts/haddnano.py','../python/postprocessing/analysis/keep_and_dropSR_out.txt','../python/postprocessing/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'] + Mt2Com_files
  config.JobType.inputFiles      =  ['crab_script.py','../scripts/haddnano.py','../python/postprocessing/analysis/keep_and_dropSR_out.txt','../python/postprocessing/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'] + Mt2Com_files
  #config.JobType.inputFiles       = ['crab_script.py','../scripts/haddnano.py','../python/postprocessing/analysis/keep_and_dropBTag_out.txt']
   #hadd nano will not be needed once nano tools are in cmssw
  #config.JobType.outputFiles = ['hist.root'] #Enable for making BTag histograms using getBTagHist.py
  config.JobType.sendPythonFolder = True
  config.JobType.allowUndistributedCMSSW = True
  config.section_('Data')
  config.Data.inputDataset        = datasetinputs[d]
  #config.Data.userInputFiles      = [datasetinputs[d]]
  config.Data.inputDBS            = 'global'
  config.Data.splitting           = 'FileBased'
  #config.Data.splitting           = 'Automatic'
  #config.Data.totalUnits         = 2500 #With 'FileBased' splitting tells how many files to analyse
  config.Data.unitsPerJob         = unitsPerJob 
  #config.Data.outLFNDirBase       = '/store/user/%s/%s' % (getUsernameFromSiteDB(),analysis) #No longer works with CRAB 
  config.Data.outLFNDirBase       = '/store/user/%s/%s' % ('vshang',analysis+'_Run'+year)
  config.Data.outputDatasetTag    = '%s' % (task) 
  config.Data.publication         = False
  config.section_('Site')
  config.Site.storageSite         = '%s' % (storageSite) 
  #config.Site.whitelist           = ['T2_US_Wisconsin']
  submit(config)
