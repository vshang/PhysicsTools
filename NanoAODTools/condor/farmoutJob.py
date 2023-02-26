#!/usr/bin/env python3
#Condor script for processing private t+DM signal samples with analysis code in python/postprocessing/analysis/ModuleCommon.py
import subprocess
import os

#Settings for which sample directories to run over
Years = ['2016', '2017', '2018']
#Years = ['2018']
#signalMassPoints = ['Mchi1_Mphi10', 'Mchi1_Mphi50', 'Mchi1_Mphi100', 'Mchi1_Mphi150', 'Mchi1_Mphi200', 'Mchi1_Mphi250', 'Mchi1_Mphi300', 'Mchi1_Mphi350', 'Mchi1_Mphi400', 'Mchi1_Mphi450', 'Mchi1_Mphi500']
signalMassPoints = []
signalTypes = ['tChan', 'tWChan']
#signalTypes = ['tWChan']
mediatorTypes = ['Scalar', 'Pseudo']
#mediatorTypes = ['Scalar']
#analysis = 'ModuleCommonSkim_02092023'
analysis = 'countEvents_02092023'
countNEntries = True
input_files = '../python/postprocessing/analysis/mt2w_bisect_cc.so,../python/postprocessing/analysis/mt2w_bisect.cc,../python/postprocessing/analysis/mt2w_bisect.h,../python/postprocessing/analysis/mt2w_bisect_cc.d,../python/postprocessing/analysis/mt2w_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/MT2Utility_cc.so,../python/postprocessing/analysis/MT2Utility.cc,../python/postprocessing/analysis/MT2Utility.h,../python/postprocessing/analysis/MT2Utility_cc.d,../python/postprocessing/analysis/MT2Utility_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/mt2bl_bisect_cc.so,../python/postprocessing/analysis/mt2bl_bisect.cc,../python/postprocessing/analysis/mt2bl_bisect.h,../python/postprocessing/analysis/mt2bl_bisect_cc.d,../python/postprocessing/analysis/mt2bl_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/Mt2Com_bisect_cc.so,../python/postprocessing/analysis/Mt2Com_bisect.cc,../python/postprocessing/analysis/Mt2Com_bisect.h,../python/postprocessing/analysis/Mt2Com_bisect_cc.d,../python/postprocessing/analysis/Mt2Com_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/lester_mt2_bisect.h,../python/postprocessing/analysis/XYMETCorrection.h,../python/postprocessing/analysis/topness_cc.so,../python/postprocessing/analysis/topness.cc,../python/postprocessing/analysis/topness.h,../python/postprocessing/analysis/topness_cc.d,../python/postprocessing/analysis/topness_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/JetUtil_cc.so,../python/postprocessing/analysis/JetUtil.cc,../python/postprocessing/analysis/JetUtil.h,../python/postprocessing/analysis/JetUtil_cc.d,../python/postprocessing/analysis/JetUtil_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/keep_and_dropSR_out.txt,../python/postprocessing/analysis/keep_and_dropCount_out.txt'

#Loop over each sample directory and submit separate farmout job
for year in Years:
    #First do tDM signal samples
    for signalMassPoint in signalMassPoints:
        for signalType in signalTypes:
            for mediatorType in mediatorTypes:
                farmout_call = 'farmoutAnalysisJobs '+signalType+mediatorType+year+'_'+signalMassPoint+'_'+analysis
                farmout_call += ' --output-dir=/store/user/vshang/tDM_Run'+year+'/DM'+mediatorType+'_top_'+signalType+'_'+signalMassPoint+'_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/'+analysis+'/rootFiles/'
                farmout_call += ' --input-dir=/store/user/vshang/signalMC/tDM_'+year+'/DM'+mediatorType+'_top_'+signalType+'_'+signalMassPoint+'_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/'
                farmout_call += ' --submit-dir=/nfs_scratch/vshang/tDM_'+year+'_'+analysis+'/'+signalType+mediatorType+year+'_'+signalMassPoint
                farmout_call += ' --infer-cmssw-path'
                if countNEntries:
                    farmout_call += ' --fwklite scripts/condor_script_count.py'
                else:
                    farmout_call += ' --fwklite scripts/MCSignal'+year+'.py'
                #farmout_call += ' --input-basenames-not-unique'
                farmout_call += ' --job-generates-output-name'
                farmout_call += ' --memory-requirements=16000'
                farmout_call += ' --disk-requirements=50000'
                farmout_call += ' --extra-inputs='+input_files
                if not os.path.exists('/hdfs/store/user/vshang/tDM_Run'+year+'/DM'+mediatorType+'_top_'+signalType+'_'+signalMassPoint+'_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/'+analysis+'/rootFiles/'): 
                    os.makedirs('/hdfs/store/user/vshang/tDM_Run'+year+'/DM'+mediatorType+'_top_'+signalType+'_'+signalMassPoint+'_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/'+analysis+'/rootFiles/')
                subprocess.call(farmout_call,shell=True)
    #Then do ttDM Mchi1_Mphi10 ttDM samples
    for medType in ['scalar', 'pseudo']:
        farmout_call = 'farmoutAnalysisJobs ttbarDM'+medType+year+'_Mchi1_Mphi10_'+analysis
        farmout_call += ' --output-dir=/store/user/vshang/ttbarDM_Run'+year+'/ttbardm_10GeV_'+medType+'_incl_'+year+'_nanoaod/'+analysis+'/rootFiles/'
        farmout_call += ' --input-dir=/store/user/vshang/signalMC/ttDM_'+year+'/ttbardm_10GeV_'+medType+'_incl_'+year+'_nanoaod/'
        farmout_call += ' --submit-dir=/nfs_scratch/vshang/ttbarDM_'+year+'_'+analysis+'/'+medType+year+'_Mchi1_Mphi10'
        farmout_call += ' --infer-cmssw-path'
        if countNEntries:
            farmout_call += ' --fwklite scripts/condor_script_count.py'
        else:
            farmout_call += ' --fwklite scripts/MCSignal'+year+'.py'
        #farmout_call += ' --input-basenames-not-unique'
        farmout_call += ' --job-generates-output-name'
        farmout_call += ' --memory-requirements=16000'
        farmout_call += ' --disk-requirements=50000'
        farmout_call += ' --extra-inputs='+input_files
        if not os.path.exists('/hdfs/store/user/vshang/ttbarDM_Run'+year+'/ttbardm_10GeV_'+medType+'_incl_'+year+'_nanoaod/'+analysis+'/rootFiles/'):
            os.makedirs('/hdfs/store/user/vshang/ttbarDM_Run'+year+'/ttbardm_10GeV_'+medType+'_incl_'+year+'_nanoaod/'+analysis+'/rootFiles/')
        subprocess.call(farmout_call,shell=True)
#Finally do ttH(H->inv) 2016 nanoAODv7 sample
farmout_call = 'farmoutAnalysisJobs ttH2016_'+analysis
farmout_call += ' --output-dir=/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/'+analysis+'/rootFiles/'
farmout_call += ' --input-dir=/store/user/vshang/signalMC/ttH_2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8/'
farmout_call += ' --submit-dir=/nfs_scratch/vshang/ttH_2016'+'_'+analysis+'/'
farmout_call += ' --infer-cmssw-path'
if countNEntries:
    farmout_call += ' --fwklite scripts/condor_script_count.py'
else:
    farmout_call += ' --fwklite scripts/MC2016.py'
#farmout_call += ' --input-basenames-not-unique'
farmout_call += ' --job-generates-output-name'
farmout_call += ' --memory-requirements=16000'
farmout_call += ' --disk-requirements=50000'
farmout_call += ' --extra-inputs='+input_files
if not os.path.exists('/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/'+analysis+'/rootFiles/'):
    os.makedirs('/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/'+analysis+'/rootFiles/')
subprocess.call(farmout_call,shell=True)
    
