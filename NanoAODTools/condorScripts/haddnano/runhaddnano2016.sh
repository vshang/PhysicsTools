#!/bin/sh
#Script to merge nanoAOD root files using haddnano.py
set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_10_6_9
cd CMSSW_10_6_9
eval `scram runtime -sh`
cd ..
chmod u+x ./haddnano.py
#./haddnano.py tree__Run2016_all.root /hdfs/store/user/vshang/_Run2016//ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_MET_Run2016B_all.root /hdfs/store/user/vshang/MET_Run2016B/MET/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_MET_Run2016C_all.root /hdfs/store/user/vshang/MET_Run2016C/MET/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_MET_Run2016D_all.root /hdfs/store/user/vshang/MET_Run2016D/MET/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_MET_Run2016E_all.root /hdfs/store/user/vshang/MET_Run2016E/MET/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_MET_Run2016F_all.root /hdfs/store/user/vshang/MET_Run2016F/MET/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_MET_Run2016G_all.root /hdfs/store/user/vshang/MET_Run2016G/MET/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_MET_Run2016H_all.root /hdfs/store/user/vshang/MET_Run2016H/MET/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_SingleElectron_Run2016B_all.root /hdfs/store/user/vshang/SingleElectron_Run2016B/SingleElectron/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2016C_all.root /hdfs/store/user/vshang/SingleElectron_Run2016C/SingleElectron/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2016D_all.root /hdfs/store/user/vshang/SingleElectron_Run2016D/SingleElectron/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2016E_all.root /hdfs/store/user/vshang/SingleElectron_Run2016E/SingleElectron/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2016F_all.root /hdfs/store/user/vshang/SingleElectron_Run2016F/SingleElectron/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2016G_all.root /hdfs/store/user/vshang/SingleElectron_Run2016G/SingleElectron/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2016H_all.root /hdfs/store/user/vshang/SingleElectron_Run2016H/SingleElectron/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_SingleMuon_Run2016B_all.root /hdfs/store/user/vshang/SingleMuon_Run2016B/SingleMuon/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2016C_all.root /hdfs/store/user/vshang/SingleMuon_Run2016C/SingleMuon/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2016D_all.root /hdfs/store/user/vshang/SingleMuon_Run2016D/SingleMuon/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2016E_all.root /hdfs/store/user/vshang/SingleMuon_Run2016E/SingleMuon/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2016F_all.root /hdfs/store/user/vshang/SingleMuon_Run2016F/SingleMuon/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2016G_all.root /hdfs/store/user/vshang/SingleMuon_Run2016G/SingleMuon/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2016H_all.root /hdfs/store/user/vshang/SingleMuon_Run2016H/SingleMuon/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_ttbarDM_scalar_Run2016_all.root /hdfs/store/user/vshang/ttbarDM_Run2016/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ttbarDM_pseudoscalar_Run2016_all.root /hdfs/store/user/vshang/ttbarDM_Run2016/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_TTToSemilepton_Run2016_all.root /hdfs/store/user/vshang/ttbarPlusJets_Run2016/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_TTTo2L2Nu_Run2016_all.root /hdfs/store/user/vshang/ttbarPlusJets_Run2016/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_ST_s-channel_Run2016_all.root /hdfs/store/user/vshang/singleTop_Run2016/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ST_t-channel_top_Run2016_all.root /hdfs/store/user/vshang/singleTop_Run2016/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ST_t-channel_antitop_Run2016_all.root /hdfs/store/user/vshang/singleTop_Run2016/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ST_tW_top_Run2016_all.root /hdfs/store/user/vshang/singleTop_Run2016/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ST_tW_antitop_Run2016_all.root /hdfs/store/user/vshang/singleTop_Run2016/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_WJetsToLNu_HT-70To100_Run2016_all.root /hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-100To200_Run2016_all.root /hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-200To400_Run2016_all.root /hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-400To600_Run2016_all.root /hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-600To800_Run2016_all.root /hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-800To1200_Run2016_all.root /hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-1200To2500_Run2016_all.root /hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-2500ToInf_Run2016_all.root /hdfs/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_DYJetsToLL_HT-100to200_Run2016_all.root /hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-200to400_Run2016_all.root /hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-400to600_Run2016_all.root /hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-600to800_Run2016_all.root /hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-800to1200_Run2016_all.root /hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-1200to2500_Run2016_all.root /hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-2500toInf_Run2016_all.root /hdfs/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_ZJetsToNuNu_HT-100To200_Run2016_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-200To400_Run2016_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-400To600_Run2016_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-600To800_Run2016_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-800To1200_Run2016_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-1200To2500_Run2016_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-2500ToInf_Run2016_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_WWTo1L1Nu2Q_Run2016_all.root /hdfs/store/user/vshang/WW_Run2016/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WWTo2L2Nu_Run2016_all.root /hdfs/store/user/vshang/WW_Run2016/WWTo2L2Nu_13TeV-powheg/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WWTo4Q_Run2016_all.root /hdfs/store/user/vshang/WW_Run2016/WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_WZTo1L1Nu2Q_Run2016_all.root /hdfs/store/user/vshang/WZ_Run2016/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WZTo1L3Nu_Run2016_all.root /hdfs/store/user/vshang/WZ_Run2016/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WZTo2L2Q_Run2016_all.root /hdfs/store/user/vshang/WZ_Run2016/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WZTo2Q2Nu_Run2016_all.root /hdfs/store/user/vshang/WZ_Run2016/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_WZTo3LNu_Run2016_all.root /hdfs/store/user/vshang/WZ_Run2016/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_ZZTo2Q2Nu_Run2016_all.root /hdfs/store/user/vshang/ZZ_Run2016/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZZTo4L_Run2016_all.root /hdfs/store/user/vshang/ZZ_Run2016/ZZTo4L_13TeV_powheg_pythia8*/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZZTo4Q_Run2016_all.root /hdfs/store/user/vshang/ZZ_Run2016/ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZZTo2L2Q_Run2016_all.root /hdfs/store/user/vshang/ZZ_Run2016/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_ZZTo2L2Nu_Run2016_all.root /hdfs/store/user/vshang/ZZ_Run2016/ZZTo2L2Nu_13TeV_powheg_pythia8*/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_TTWJetsToLNu_Run2016_all.root /hdfs/store/user/vshang/TTV_Run2016/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_TTWJetsToQQ_Run2016_all.root /hdfs/store/user/vshang/TTV_Run2016/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_TTZToQQ_Run2016_all.root /hdfs/store/user/vshang/TTV_Run2016/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_TTZToLLNuNu_Run2016_all.root /hdfs/store/user/vshang/TTV_Run2016/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root

./haddnano.py tree_QCD_HT100to200_Run2016_all.root /hdfs/store/user/vshang/QCD_Run2016/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_QCD_HT200to300_Run2016_all.root /hdfs/store/user/vshang/QCD_Run2016/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_QCD_HT300to500_Run2016_all.root /hdfs/store/user/vshang/QCD_Run2016/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_QCD_HT500to700_Run2016_all.root /hdfs/store/user/vshang/QCD_Run2016/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_QCD_HT700to1000_Run2016_all.root /hdfs/store/user/vshang/QCD_Run2016/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_QCD_HT1000to1500_Run2016_all.root /hdfs/store/user/vshang/QCD_Run2016/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_QCD_HT1500to2000_Run2016_all.root /hdfs/store/user/vshang/QCD_Run2016/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root
./haddnano.py tree_QCD_HT2000toInf_Run2016_all.root /hdfs/store/user/vshang/QCD_Run2016/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/*/*/tree*.root

#Copy output files directly to hdfs
#env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Single_Run2016/MET/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2016B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2016B/MET/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2016C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2016C/MET/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2016D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2016D/MET/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2016E_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2016E/MET/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2016F_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2016F/MET/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2016G_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2016G/MET/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2016H_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2016H/MET/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2016B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2016B/SingleElectron/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2016C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2016C/SingleElectron/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2016D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2016D/SingleElectron/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2016E_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2016E/SingleElectron/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2016F_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2016F/SingleElectron/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2016G_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2016G/SingleElectron/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2016H_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2016H/SingleElectron/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2016B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2016B/SingleMuon/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2016C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2016C/SingleMuon/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2016D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2016D/SingleMuon/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2016E_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2016E/SingleMuon/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2016F_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2016F/SingleMuon/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2016G_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2016G/SingleMuon/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2016H_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2016H/SingleMuon/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbarDM_scalar_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2016/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbarDM_pseudoscalar_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2016/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTToSemilepton_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2016/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTTo2L2Nu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2016/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_s-channel_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2016/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_t-channel_top_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2016/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_t-channel_antitop_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2016/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_tW_top_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2016/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_tW_antitop_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2016/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-70To100_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-100To200_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-200To400_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-400To600_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-600To800_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-800To1200_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-1200To2500_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-2500ToInf_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2016/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-100to200_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-200to400_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-400to600_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-600to800_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-800to1200_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-1200to2500_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-2500toInf_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2016/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-100To200_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-200To400_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-400To600_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-600To800_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-800To1200_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-1200To2500_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-2500ToInf_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2016/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo1L1Nu2Q_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2016/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo2L2Nu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2016/WWTo2L2Nu_13TeV-powheg/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo4Q_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2016/WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo1L1Nu2Q_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2016/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo1L3Nu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2016/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo2L2Q_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2016/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo2Q2Nu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2016/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo3LNu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2016/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2Q2Nu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2016/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo4L_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2016/ZZTo4L_13TeV_powheg_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo4Q_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2016/ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2L2Q_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2016/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2L2Nu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2016/ZZTo2L2Nu_13TeV_powheg_pythia8/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTWJetsToLNu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2016/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTWJetsToQQ_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2016/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTZToQQ_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2016/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTZToLLNuNu_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2016/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/ModuleCommonSkim_09072021/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT100to200_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2016/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT200to300_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2016/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT300to500_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2016/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT500to700_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2016/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT700to1000_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2016/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT1000to1500_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2016/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT1500to2000_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2016/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT2000toInf_Run2016_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2016/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_09072021/tree_all.root

#prevent condor from also transferring the output files back to the submit directory:
rm *.root
