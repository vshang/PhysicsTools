#!/usr/bin/env python3
#Condor script for processing private t+DM signal samples with analysis code in python/postprocessing/analysis/ModuleCommon.py
import subprocess

#Settings for which sample directories to run over
#Years = ['2016', '2017', '2018']
Years = ['2016']
signalMassPoints = ['Mchi1_Mphi50', 'Mchi1_Mphi100', 'Mchi1_Mphi150', 'Mchi1_Mphi200', 'Mchi1_Mphi250', 'Mchi1_Mphi300', 'Mchi1_Mphi350', 'Mchi1_Mphi400', 'Mchi1_Mphi450', 'Mchi1_Mphi500']
#signalTypes = ['tChan', 'tWChan']
signalTypes = ['tChan']
#mediatorTypes = ['Scalar', 'Pseudo']
mediatorTypes = ['Scalar']
analysis = 'ModuleCommonSkim_03092022'

#Loop over each sample directory and submit separate farmout job
for year in Years:
    for signalMassPoint in signalMassPoints:
        for signalType in signalTypes:
            for mediatorType in mediatorTypes:
                farmout_call = 'farmoutAnalysisJobs '+signalType+mediatorType+year+'_'+signalMassPoint+'_'+analysis
                farmout_call += ' --output-dir=/store/user/vshang/tDM_Run'+year+'/DM'+mediatorType+'_top_'+signalType+'_'+signalMassPoint+'_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/'+analysis+'/rootFiles/'
                farmout_call += ' --input-dir=/store/user/vshang/signalMC/tDM_'+year+'/DM'+mediatorType+'_top_'+signalType+'_'+signalMassPoint+'_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/'
                farmout_call += ' --submit-dir=/nfs_scratch/vshang/tDM_'+year+'/'+signalType+mediatorType+year+'_'+signalMassPoint+'_'+analysis
                farmout_call += ' --infer-cmssw-path'
                farmout_call += ' --fwklite scripts/MCSignal'+year+'.py'
                #farmout_call += ' --input-basenames-not-unique'
                farmout_call += ' --job-generates-output-name'
                farmout_call += ' --memory-requirements=16000'
                farmout_call += ' --disk-requirements=50000'
                farmout_call += ' --extra-inputs=../python/postprocessing/analysis/mt2w_bisect_cc.so,../python/postprocessing/analysis/mt2w_bisect.cc,../python/postprocessing/analysis/mt2w_bisect.h,../python/postprocessing/analysis/mt2w_bisect_cc.d,../python/postprocessing/analysis/mt2w_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/MT2Utility_cc.so,../python/postprocessing/analysis/MT2Utility.cc,../python/postprocessing/analysis/MT2Utility.h,../python/postprocessing/analysis/MT2Utility_cc.d,../python/postprocessing/analysis/MT2Utility_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/mt2bl_bisect_cc.so,../python/postprocessing/analysis/mt2bl_bisect.cc,../python/postprocessing/analysis/mt2bl_bisect.h,../python/postprocessing/analysis/mt2bl_bisect_cc.d,../python/postprocessing/analysis/mt2bl_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/Mt2Com_bisect_cc.so,../python/postprocessing/analysis/Mt2Com_bisect.cc,../python/postprocessing/analysis/Mt2Com_bisect.h,../python/postprocessing/analysis/Mt2Com_bisect_cc.d,../python/postprocessing/analysis/Mt2Com_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/lester_mt2_bisect.h,../python/postprocessing/analysis/XYMETCorrection.h,../python/postprocessing/analysis/topness_cc.so,../python/postprocessing/analysis/topness.cc,../python/postprocessing/analysis/topness.h,../python/postprocessing/analysis/topness_cc.d,../python/postprocessing/analysis/topness_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/JetUtil_cc.so,../python/postprocessing/analysis/JetUtil.cc,../python/postprocessing/analysis/JetUtil.h,../python/postprocessing/analysis/JetUtil_cc.d,../python/postprocessing/analysis/JetUtil_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/keep_and_dropSR_out.txt'
                subprocess.call(farmout_call,shell=True)
