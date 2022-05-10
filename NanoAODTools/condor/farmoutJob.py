#!/usr/bin/env python3
import subprocess

farmout_call = 'farmoutAnalysisJobs tDM_Run2016'
farmout_call += ' --input-dir=/store/user/vshang/signalMC/tDM_2016/DMScalar_top_tWChan_Mchi1_Mphi50_TuneCP5_13TeV-madgraph-mcatnlo-pythia8'
farmout_call += ' --infer-cmssw-path'
farmout_call += ' --fwklite scripts/MCSignal2016.py'
#farmout_call += ' --input-basenames-not-unique'
farmout_call += ' --output-dir=/store/user/vshang/tbarDM_Run2016/ModuleCommonSkim_03092022'
farmout_call += ' --memory-requirements=16000'
farmout_call += ' --disk-requirements=50000'
farmout_call += ' --extra-inputs=../python/postprocessing/analysis/mt2w_bisect_cc.so,../python/postprocessing/analysis/mt2w_bisect.cc,../python/postprocessing/analysis/mt2w_bisect.h,../python/postprocessing/analysis/mt2w_bisect_cc.d,../python/postprocessing/analysis/mt2w_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/MT2Utility_cc.so,../python/postprocessing/analysis/MT2Utility.cc,../python/postprocessing/analysis/MT2Utility.h,../python/postprocessing/analysis/MT2Utility_cc.d,../python/postprocessing/analysis/MT2Utility_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/mt2bl_bisect_cc.so,../python/postprocessing/analysis/mt2bl_bisect.cc,../python/postprocessing/analysis/mt2bl_bisect.h,../python/postprocessing/analysis/mt2bl_bisect_cc.d,../python/postprocessing/analysis/mt2bl_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/Mt2Com_bisect_cc.so,../python/postprocessing/analysis/Mt2Com_bisect.cc,../python/postprocessing/analysis/Mt2Com_bisect.h,../python/postprocessing/analysis/Mt2Com_bisect_cc.d,../python/postprocessing/analysis/Mt2Com_bisect_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/lester_mt2_bisect.h,../python/postprocessing/analysis/XYMETCorrection.h,../python/postprocessing/analysis/topness_cc.so,../python/postprocessing/analysis/topness.cc,../python/postprocessing/analysis/topness.h,../python/postprocessing/analysis/topness_cc.d,../python/postprocessing/analysis/topness_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/JetUtil_cc.so,../python/postprocessing/analysis/JetUtil.cc,../python/postprocessing/analysis/JetUtil.h,../python/postprocessing/analysis/JetUtil_cc.d,../python/postprocessing/analysis/JetUtil_cc_ACLiC_dict_rdict.pcm,../python/postprocessing/analysis/keep_and_dropSR_out.txt'

subprocess.call(farmout_call,shell=True)
