#Cross sections ('xsec') are in units of femtobarns (fb)

#2016 MC samples
samples2016 = { 
    #Signal
    'ttbar' : {
        'ttbarDM_Mchi1Mphi100' : { 'nevents' : 1, 'xsec' : 672.3, 'filepaths' : ['/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/outDir2016AnalysisSR/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full_ModuleCommon_2016MC.root'] },
    }, 
    'tbar' : {
        'tChan_Mchi1Mphi100' : { 'nevents' : 1, 'xsec' : 268.3, 'filepaths' : ['/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/outDir2016AnalysisSR/tDM_tChan/tDM_tChan_Mchi1Mphi100_scalar_full_ModuleCommon_2016MC.root'] },
        'tWChan_Mchi1Mphi100' : { 'nevents' : 1, 'xsec' : 55.49, 'filepaths' : ['/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/outDir2016AnalysisSR/tDM_tWChan/tDM_tWChan_Mchi1Mphi100_scalar_full_ModuleCommon_2016MC.root'] },
    }, 
    #Background 
    'ttbarPlusJets' : {
        'TTTo2L2Nu' : { 'nevents' : 1, 'xsec' : 87310.0, 'filepaths' : ['/hdfs/store/user/vshang/ttbarPlusJets_Run2016/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'TTToSemiLepton' : { 'nevents' : 1, 'xsec' : 364350.0, 'filepaths' : ['/hdfs/store/user/vshang/ttbarPlusJets_Run2016/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/ModuleCommon_06122020/tree_all.root'] },
    }, 
    'singleTop' : {
        'ST_s-channel' : { 'nevents' : 1, 'xsec' : 3360.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2016/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/ModuleCommon_06122020/tree_all.root'] },
        'ST_t-channel_antitop' : { 'nevents' : 1, 'xsec' : 80950.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2016/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/ModuleCommon_06122020/tree_all.root'] },
        'ST_t-channel_top' : { 'nevents' : 1, 'xsec' : 136020.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2016/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/ModuleCommon_06122020/tree_all.root'] },
        'ST_tW_antitop' : { 'nevents' : 1, 'xsec' : 35850.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2016/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/ModuleCommon_06122020/tree_all.root'] },
        'ST_tW_top' : { 'nevents' : 1, 'xsec' : 35850.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2016/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/ModuleCommon_06122020/tree_all.root'] },
    },
    'WPlusJets' : {
        'HT70To100' : { 'nevents' : 1, 'xsec' : 1372000.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT100To200' : { 'nevents' : 1, 'xsec' : 1345000.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 359700.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 48910.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 12050.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 1329.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 5501.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 32.16, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
    },
    'ZTo2L' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 147400.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 40990.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 5678.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 1367.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 630.4, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 151.4, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 3.565, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
    },
    'ZTo2Nu' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 280350.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ModuleCommon_06122020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 77670.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ModuleCommon_06122020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 10730.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ModuleCommon_06122020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 2559.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ModuleCommon_06122020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 1179.6, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ModuleCommon_06122020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 288.33, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ModuleCommon_06122020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 6.945, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ModuleCommon_06122020/tree_all.root'] },
    },
    'WW' : {
        'WWTo1L1Nu' : { 'nevents' : 1, 'xsec' : 49997.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2016/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'WWTo2L2Nu' : { 'nevents' : 1, 'xsec' : 12178.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2016/WWTo2L2Nu_13TeV-powheg/ModuleCommon_06122020/tree_all.root'] },
        'WWTo4Q' : { 'nevents' : 1, 'xsec' : 51723.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2016/WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06122020/tree_all.root'] },
    },
    'WZ' : {
        'WZTo1L1Nu2Q' : { 'nevents' : 1, 'xsec' : 10710.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2016/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'WZTo1L3Nu' : { 'nevents' : 1, 'xsec' : 3033.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2016/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'WZTo2L2Q' : { 'nevents' : 1, 'xsec' : 5595.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2016/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'WZTo2Q2Nu' : { 'nevents' : 1, 'xsec' : 6488.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2016/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'WZTo3LNu' : { 'nevents' : 1, 'xsec' : 4429.65, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2016/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/ModuleCommon_06122020/tree_all.root'] },
    },
    'ZZ' : {
        'ZZTo2Q2Nu' : { 'nevents' : 1, 'xsec' : 4040.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2016/ZZTo2L2Nu_13TeV_powheg_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'ZZTo4L' : { 'nevents' : 1, 'xsec' : 1212.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2016/ZZTo4L_13TeV_powheg_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'ZZTo4Q' : { 'nevents' : 1, 'xsec' : 6842.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2016/ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'ZZTo2L2Q' : { 'nevents' : 1, 'xsec' : 3220.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2016/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06122020/tree_all.root'] },
        'ZZTo2L2Nu' : { 'nevents' : 1, 'xsec' : 564.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2016/ZZTo2L2Nu_13TeV_powheg_pythia8/ModuleCommon_06122020/tree_all.root'] },
    },
    'TTV' : {
        'TTWJetsToLNu' : { 'nevents' : 1, 'xsec' : 204.3, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2016/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'TTWJetsToQQ' : { 'nevents' : 1, 'xsec' : 406.2, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2016/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'TTZToQQ' : { 'nevents' : 1, 'xsec' : 529.7, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2016/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'TTZToLLNuNu' : { 'nevents' : 1, 'xsec' : 252.9, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2016/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/ModuleCommon_06122020/tree_all.root'] },
    },
    'QCD' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 27990000000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2016/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT200To300' : { 'nevents' : 1, 'xsec' : 1712000000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2016/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT300To500' : { 'nevents' : 1, 'xsec' : 347700000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2016/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT500To700' : { 'nevents' : 1, 'xsec' : 32100000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2016/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT700To1000' : { 'nevents' : 1, 'xsec' : 6831000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2016/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT1000To1500' : { 'nevents' : 1, 'xsec' : 1207000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2016/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT1500To2000' : { 'nevents' : 1, 'xsec' : 119900.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2016/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
        'HT2000ToInf' : { 'nevents' : 1, 'xsec' : 25240.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2016/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommon_06122020/tree_all.root'] },
    },
}

#2017 MC samples
samples2017 = { 
    #Background 
    'ttbarPlusJets' : {
        'TTTo2L2Nu' : { 'nevents' : 1, 'xsec' : 87310.0, 'filepaths' : ['/hdfs/store/user/vshang/ttbarPlusJets_Run2017/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'TTToSemiLepton' : { 'nevents' : 1, 'xsec' : 364350.0, 'filepaths' : ['/hdfs/store/user/vshang/ttbarPlusJets_Run2017/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/ModuleCommon_06282020/tree_all.root'] },
    }, 
    'singleTop' : {
        'ST_s-channel' : { 'nevents' : 1, 'xsec' : 3740.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2017/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'ST_t-channel_antitop' : { 'nevents' : 1, 'xsec' : 67910.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2017/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'ST_t-channel_top' : { 'nevents' : 1, 'xsec' : 113300.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2017/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'ST_tW_antitop' : { 'nevents' : 1, 'xsec' : 34970.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2017/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'ST_tW_top' : { 'nevents' : 1, 'xsec' : 34910.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2017/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/ModuleCommon_06282020/tree_all.root'] },
    },
    'WPlusJets' : {
        'HT70To100' : { 'nevents' : 1, 'xsec' : 1292000.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT100To200' : { 'nevents' : 1, 'xsec' : 1395000.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 407900.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 57480.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 12870.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 5366.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 1074.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 8.001, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
    },
    'ZTo2L' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 161100.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 48660.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 6968.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 1743.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 805.2, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 193.3, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 3.468, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommon_06282020/tree_all.root'] },
    },
    'ZTo2Nu' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 302800.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ModuleCommon_06282020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 92590.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ModuleCommon_06282020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 13180.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ModuleCommon_06282020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 3257.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ModuleCommon_06282020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 1490.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ModuleCommon_06282020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 341.9, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ModuleCommon_06282020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 5.146, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ModuleCommon_06282020/tree_all.root'] },
    },
    'WW' : {
        'WWTo4Q' : { 'nevents' : 1, 'xsec' : 47730.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2017/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'WWTo2L2Nu' : { 'nevents' : 1, 'xsec' : 11080.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2017/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'WWTo1L1Nu2Q' : { 'nevents' : 1, 'xsec' : 80740.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2017/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06282020/tree_all.root'] },
    },
    'WZ' : {
        'WZTo1L1Nu2Q' : { 'nevents' : 1, 'xsec' : 11660.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2017/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06282020/tree_all.root'] },
        'WZTo1L3Nu' : { 'nevents' : 1, 'xsec' : 3342.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2017/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/ModuleCommon_06282020/tree_all.root'] },
        'WZTo2L2Q' : { 'nevents' : 1, 'xsec' : 6331.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2017/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06282020/tree_all.root'] },
        #'WZTo2Q2Nu' : { 'nevents' : 1, 'xsec' : , 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2017/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06282020/tree_all.root'] },
        'WZTo3LNu' : { 'nevents' : 1, 'xsec' : 5052.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2017/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/ModuleCommon_06282020/tree_all.root'] },
    },
    'ZZ' : {
        'ZZTo2Q2Nu' : { 'nevents' : 1, 'xsec' : 4564.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2017/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06282020/tree_all.root'] },
        'ZZTo4L' : { 'nevents' : 1, 'xsec' : 1325.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2017/ZZTo4L_13TeV_powheg_pythia8/ModuleCommon_06282020/tree_all.root'] },
        #'ZZTo4Q' : { 'nevents' : 1, 'xsec' : , 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2017/ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06282020/tree_all.root'] },
        'ZZTo2L2Q' : { 'nevents' : 1, 'xsec' : 3688.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2017/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommon_06282020/tree_all.root'] },
        'ZZTo2L2Nu' : { 'nevents' : 1, 'xsec' : 564.4, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2017/ZZTo2L2Nu_13TeV_powheg_pythia8/ModuleCommon_06282020/tree_all.root'] },
    },
    'TTV' : {
        'TTWJetsToLNu' : { 'nevents' : 1, 'xsec' : 214.9, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2017/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'TTWJetsToQQ' : { 'nevents' : 1, 'xsec' : 431.6, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2017/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'TTZToQQ' : { 'nevents' : 1, 'xsec' : 510.4, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2017/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'TTZToLLNuNu' : { 'nevents' : 1, 'xsec' : 243.2, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2017/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommon_06282020/tree_all.root'] },
    },
    'QCD' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 23700000000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2017/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT200To300' : { 'nevents' : 1, 'xsec' : 1547000000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2017/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT300To500' : { 'nevents' : 1, 'xsec' : 322600000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2017/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT500To700' : { 'nevents' : 1, 'xsec' : 29980000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2017/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT700To1000' : { 'nevents' : 1, 'xsec' : 6334000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2017/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT1000To1500' : { 'nevents' : 1, 'xsec' : 1088000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2017/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT1500To2000' : { 'nevents' : 1, 'xsec' : 99110.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2017/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/ModuleCommon_06282020/tree_all.root'] },
        'HT2000ToInf' : { 'nevents' : 1, 'xsec' : 20230.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2017/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/ModuleCommon_06282020/tree_all.root'] },
    },
}

#2018 MC samples
samples2018 = { 
    #Background 
    'ttbarPlusJets' : {
        'TTTo2L2Nu' : { 'nevents' : 1, 'xsec' : 87310.0, 'filepaths' : ['/hdfs/store/user/vshang/ttbarPlusJets_Run2018/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ttbarPlusJets_Run2018/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/tree_all.root'] },
        'TTToSemiLepton' : { 'nevents' : 1, 'xsec' : 364350.0, 'filepaths' : ['/hdfs/store/user/vshang/ttbarPlusJets_Run2018/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' :  ['/hdfs/store/user/vshang/ttbarPlusJets_Run2018/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/tree_all.root'] },
    }, 
    'singleTop' : {
        'ST_s-channel' : { 'nevents' : 1, 'xsec' : 3740.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/getBTagHist_07072020/tree_all.root'] },
        'ST_t-channel_antitop' : { 'nevents' : 1, 'xsec' : 67910.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/getBTagHist_07072020/tree_all.root'] },
        'ST_t-channel_top' : { 'nevents' : 1, 'xsec' : 113300.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/getBTagHist_07072020/tree_all.root'] },
        'ST_tW_antitop' : { 'nevents' : 1, 'xsec' : 34970.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/tree_all.root'] },
        'ST_tW_top' : { 'nevents' : 1, 'xsec' : 34910.0, 'filepaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/singleTop_Run2018/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/tree_all.root'] },
    },
    'WPlusJets' : {
        'HT70To100' : { 'nevents' : 1, 'xsec' : 1292000.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT100To200' : { 'nevents' : 1, 'xsec' : 1395000.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 407900.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 57480.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 12870.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 5366.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 1074.0, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 8.001, 'filepaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
    },
    'ZTo2L' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 161100.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 48660.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 6968.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 1743.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 805.2, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 193.3, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 3.468, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
    },
    'ZTo2Nu' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 302800.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-100To200_13TeV-madgraph/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-100To200_13TeV-madgraph/getBTagHist_07072020/tree_all.root'] },
        'HT200To400' : { 'nevents' : 1, 'xsec' : 92590.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-200To400_13TeV-madgraph/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-200To400_13TeV-madgraph/getBTagHist_07072020/tree_all.root'] },
        'HT400To600' : { 'nevents' : 1, 'xsec' : 13180.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-400To600_13TeV-madgraph/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-400To600_13TeV-madgraph/getBTagHist_07072020/tree_all.root'] },
        'HT600To800' : { 'nevents' : 1, 'xsec' : 3257.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-600To800_13TeV-madgraph/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-600To800_13TeV-madgraph/getBTagHist_07072020/tree_all.root'] },
        'HT800To1200' : { 'nevents' : 1, 'xsec' : 1490.0, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/getBTagHist_07072020/tree_all.root'] },
        'HT1200To2500' : { 'nevents' : 1, 'xsec' : 341.9, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/getBTagHist_07072020/tree_all.root'] },
        'HT2500ToInf' : { 'nevents' : 1, 'xsec' : 5.146, 'filepaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/getBTagHist_07072020/tree_all.root'] },
    },
    'WW' : {
        'WWTo4Q' : { 'nevents' : 1, 'xsec' : 47730.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2018/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WW_Run2018/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/tree_all.root'] },
        'WWTo2L2Nu' : { 'nevents' : 1, 'xsec' : 11080.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2018/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WW_Run2018/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/getBTagHist_07072020/tree_all.root'] },
        'WWTo1L1Nu2Q' : { 'nevents' : 1, 'xsec' : 80740.0, 'filepaths' : ['/hdfs/store/user/vshang/WW_Run2018/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WW_Run2018/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/tree_all.root'] },
    },
    'WZ' : {
        'WZTo1L1Nu2Q' : { 'nevents' : 1, 'xsec' : 11660.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/tree_all.root'] },
        'WZTo1L3Nu' : { 'nevents' : 1, 'xsec' : 3342.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/tree_all.root'] },
        'WZTo2L2Q' : { 'nevents' : 1, 'xsec' : 6331.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/tree_all.root'] },
        #'WZTo2Q2Nu' : { 'nevents' : 1, 'xsec' : , 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/tree_all.root'] },
        'WZTo3LNu' : { 'nevents' : 1, 'xsec' : 5052.0, 'filepaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/WZ_Run2018/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/getBTagHist_07072020/tree_all.root'] },
    },
    'ZZ' : {
        'ZZTo2Q2Nu' : { 'nevents' : 1, 'xsec' : 4564.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/tree_all.root'] },
        'ZZTo4L' : { 'nevents' : 1, 'xsec' : 1325.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/getBTagHist_07072020/tree_all.root'] },
        #'ZZTo4Q' : { 'nevents' : 1, 'xsec' : , 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/tree_all.root'] },
        'ZZTo2L2Q' : { 'nevents' : 1, 'xsec' : 3688.0, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/getBTagHist_07072020/tree_all.root'] },
        'ZZTo2L2Nu' : { 'nevents' : 1, 'xsec' : 564.4, 'filepaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/ZZ_Run2018/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/getBTagHist_07072020/tree_all.root'] },
    },
    'TTV' : {
        'TTWJetsToLNu' : { 'nevents' : 1, 'xsec' : 214.9, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2018/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/TTV_Run2018/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/getBTagHist_07072020/tree_all.root'] },
        'TTWJetsToQQ' : { 'nevents' : 1, 'xsec' : 431.6, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2018/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/TTV_Run2018/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/getBTagHist_07072020/tree_all.root'] },
        'TTZToQQ' : { 'nevents' : 1, 'xsec' : 510.4, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2018/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/TTV_Run2018/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/getBTagHist_07072020/tree_all.root'] },
        'TTZToLLNuNu' : { 'nevents' : 1, 'xsec' : 243.2, 'filepaths' : ['/hdfs/store/user/vshang/TTV_Run2018/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/TTV_Run2018/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/getBTagHist_07072020/tree_all.root'] },
    },
    'QCD' : {
        'HT100To200' : { 'nevents' : 1, 'xsec' : 23700000000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT200To300' : { 'nevents' : 1, 'xsec' : 1547000000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT300To500' : { 'nevents' : 1, 'xsec' : 322600000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT500To700' : { 'nevents' : 1, 'xsec' : 29980000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT700To1000' : { 'nevents' : 1, 'xsec' : 6334000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT1000To1500' : { 'nevents' : 1, 'xsec' : 1088000.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT1500To2000' : { 'nevents' : 1, 'xsec' : 99110.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
        'HT2000ToInf' : { 'nevents' : 1, 'xsec' : 20230.0, 'filepaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/hist_all.root'], 'eventpaths' : ['/hdfs/store/user/vshang/QCD_Run2018/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/getBTagHist_07072020/tree_all.root'] },
    },
}
