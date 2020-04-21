#2016 MC samples
#Cross sections ('xsec') are in units of femtobarns (fb)
samples2016 = { 
    #Signal
    'ttbarDM' : {
        'ttbarDM_Mchi1Mphi100' : { 'nevents' : 1, 'xsec' : 672.3, 'filepaths' : ['/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/outDir2016AnalysisSR/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full_ModuleCommon_All.root'] },
    }, 
    'tDM' : {
        'tChan_Mchi1Mphi100' : { 'nevents' : 1, 'xsec' : 268.3, 'filepaths' : ['/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/outDir2016AnalysisSR/tDM_tChan/tDM_tChan_Mchi1Mphi100_scalar_full_ModuleCommon_All.root'] },
        'tWChan_Mchi1Mphi100' : { 'nevents' : 1, 'xsec' : 55.49, 'filepaths' : ['/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/outDir2016AnalysisSR/tDM_tWChan/tDM_tWChan_Mchi1Mphi100_scalar_full_ModuleCommon_All.root'] },
    }, 
    #Background 
    'ttbarPlusJets' : {
        'TTTo2L2Nu' : { 'nevents' : 1, 'xsec' : 87310.0, 'filepaths' : ['/hdfs/store/user/vshang/ttbarPlusJets/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'TTToSemiLepton' : { 'nevents' : 1, 'xsec' : 364350.0, 'filepaths' : ['/hdfs/store/user/vshang/ttbarPlusJets/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    }, 
    'singleTop' : {
        'ST_s-channel' : { 'nevents' : 1, 'xsec' : 3360.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'ST_t-channel_antitop' : { 'nevents' : 1, 'xsec' : 80950.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'ST_t-channel_top' : { 'nevents' : 1, 'xsec' : 136020.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'ST_tW_antitop' : { 'nevents' : 1, 'xsec' : 35850.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'ST_tW_top' : { 'nevents' : 1, 'xsec' : 35850.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
    'WPlusJets' : {
        'HT70To100' : { 'nevents' : 1, 'xsec' : 1372000.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT100To200' : { 'nevents' : 1, 'xsec' : 1345000.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 359700.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 48910.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 12050.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 1329.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 5501.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 32.16, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
    'ZTo2L' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 147400.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 40990.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 5678.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 1367.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 630.4, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 151.4, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 3.565, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
    'ZTo2Nu' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 280350.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 77670.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 10730.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 2559.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 1179.6, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 288.33, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 6.945, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
    'WW' : {
        'WWTo1L1Nu' : { 'nevents' : 1, 'xsec' : 49997.0, 'filepaths' : ['/hdfs/store/user/vshang/WW/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'WWTo2L2Nu' : { 'nevents' : 1, 'xsec' : 12178.0, 'filepaths' : ['/hdfs/store/user/vshang/WW/WWTo2L2Nu_13TeV-powheg/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'WWTo4Q' : { 'nevents' : 1, 'xsec' : 51723.0, 'filepaths' : ['/hdfs/store/user/vshang/WW/WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
    'WZ' : {
        'WZTo1L1Nu' : { 'nevents' : 1, 'xsec' : 10710.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'WZTo1L3Nu' : { 'nevents' : 1, 'xsec' : 3033.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'WZTo2L2Q' : { 'nevents' : 1, 'xsec' : 5595.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'WZTo2Q2Nu' : { 'nevents' : 1, 'xsec' : 6488.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'WZTo3LNu' : { 'nevents' : 1, 'xsec' : 4429.65, 'filepaths' : ['/hdfs/store/user/vshang/WZ/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
    'ZZ' : {
        'ZZTo2Q2Nu' : { 'nevents' : 1, 'xsec' : 4040.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ/ZZTo2L2Nu_13TeV_powheg_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'ZZTo4L' : { 'nevents' : 1, 'xsec' : 1212.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ/ZZTo4L_13TeV_powheg_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'ZZTo4Q' : { 'nevents' : 1, 'xsec' : 6842.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ/ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'ZZTo2L2Q' : { 'nevents' : 1, 'xsec' : 3220.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'ZZTo2L2Nu' : { 'nevents' : 1, 'xsec' : 564.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ/ZZTo2L2Nu_13TeV_powheg_pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
    'TTV' : {
        'TTWJetsToLNu' : { 'nevents' : 1, 'xsec' : 204.3, 'filepaths' : ['/hdfs/store/user/vshang/TTV/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'TTWJetsToQQ' : { 'nevents' : 1, 'xsec' : 406.2, 'filepaths' : ['/hdfs/store/user/vshang/TTV/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'TTZToQQ' : { 'nevents' : 1, 'xsec' : 529.7, 'filepaths' : ['/hdfs/store/user/vshang/TTV/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'TTZToLLNuNu' : { 'nevents' : 1, 'xsec' : 252.9, 'filepaths' : ['/hdfs/store/user/vshang/TTV/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
    'QCD' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 27990000000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT200To300' : { 'nevents' : 1, 'xsec' : 1712000000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT300To500' : { 'nevents' : 1, 'xsec' : 347700000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT500To700' : { 'nevents' : 1, 'xsec' : 32100000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT700To1000' : { 'nevents' : 1, 'xsec' : 6831000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT1000To1500' : { 'nevents' : 1, 'xsec' : 1207000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT1500To2000' : { 'nevents' : 1, 'xsec' : 119900.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
        'HT2000ToInf' : { 'nevents' : 1, 'xsec' : 25240.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_withPUandBTagWeights/tree_all.root'] },
    },
}
