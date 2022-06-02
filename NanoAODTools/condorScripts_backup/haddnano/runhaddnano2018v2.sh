#!/bin/sh
#Script to merge nanoAOD root files using haddnano.py
set -x
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
scram project CMSSW CMSSW_10_6_9
cd CMSSW_10_6_9
eval `scram runtime -sh`
cd ..
chmod u+x ./haddnano.py
#./haddnano.py tree__Run2018_all.root /hdfs/store/user/vshang/_Run2018//ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_MET_Run2018A_all.root /hdfs/store/user/vshang/MET_Run2018A/MET/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_MET_Run2018B_all.root /hdfs/store/user/vshang/MET_Run2018B/MET/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_MET_Run2018C_all.root /hdfs/store/user/vshang/MET_Run2018C/MET/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_MET_Run2018D_all.root /hdfs/store/user/vshang/MET_Run2018D/MET/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_SingleElectron_Run2018A_all.root /hdfs/store/user/vshang/SingleElectron_Run2018A/EGamma/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2018B_all.root /hdfs/store/user/vshang/SingleElectron_Run2018B/EGamma/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2018C_all.root /hdfs/store/user/vshang/SingleElectron_Run2018C/EGamma/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_SingleElectron_Run2018D_all.root /hdfs/store/user/vshang/SingleElectron_Run2018D/EGamma/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_SingleMuon_Run2018A_all.root /hdfs/store/user/vshang/SingleMuon_Run2018A/SingleMuon/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2018B_all.root /hdfs/store/user/vshang/SingleMuon_Run2018B/SingleMuon/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2018C_all.root /hdfs/store/user/vshang/SingleMuon_Run2018C/SingleMuon/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_SingleMuon_Run2018D_all.root /hdfs/store/user/vshang/SingleMuon_Run2018D/SingleMuon/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_ttbarDM_scalar_Run2018_all.root /hdfs/store/user/vshang/ttbarDM_Run2018/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ttbarDM_pseudoscalar_Run2018_all.root /hdfs/store/user/vshang/ttbarDM_Run2018/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_TTToSemiLeptonic_Run2018_all.root /hdfs/store/user/vshang/ttbarPlusJets_Run2018/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_TTTo2L2Nu_Run2018_all.root /hdfs/store/user/vshang/ttbarPlusJets_Run2018/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_ST_s-channel_Run2018_all.root /hdfs/store/user/vshang/singleTop_Run2018/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ST_t-channel_top_Run2018_all.root /hdfs/store/user/vshang/singleTop_Run2018/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ST_t-channel_antitop_Run2018_all.root /hdfs/store/user/vshang/singleTop_Run2018/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ST_tW_top_Run2018_all.root /hdfs/store/user/vshang/singleTop_Run2018/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ST_tW_antitop_Run2018_all.root /hdfs/store/user/vshang/singleTop_Run2018/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_WJetsToLNu_HT-70To100_Run2018_all.root /hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-100To200_Run2018_all.root /hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-200To400_Run2018_all.root /hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-400To600_Run2018_all.root /hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-600To800_Run2018_all.root /hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-800To1200_Run2018_all.root /hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-1200To2500_Run2018_all.root /hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WJetsToLNu_HT-2500ToInf_Run2018_all.root /hdfs/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_DYJetsToLL_HT-100to200_Run2018_all.root /hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-200to400_Run2018_all.root /hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-400to600_Run2018_all.root /hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-600to800_Run2018_all.root /hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-800to1200_Run2018_all.root /hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-1200to2500_Run2018_all.root /hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_DYJetsToLL_HT-2500toInf_Run2018_all.root /hdfs/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_ZJetsToNuNu_HT-100To200_Run2018_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-200To400_Run2018_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-400To600_Run2018_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-600To800_Run2018_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-800To1200_Run2018_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-1200To2500_Run2018_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZJetsToNuNu_HT-2500ToInf_Run2018_all.root /hdfs/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_WWTo1L1Nu2Q_Run2018_all.root /hdfs/store/user/vshang/WW_Run2018/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WWTo2L2Nu_Run2018_all.root /hdfs/store/user/vshang/WW_Run2018/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WWTo4Q_Run2018_all.root /hdfs/store/user/vshang/WW_Run2018/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_WZTo1L1Nu2Q_Run2018_all.root /hdfs/store/user/vshang/WZ_Run2018/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WZTo1L3Nu_Run2018_all.root /hdfs/store/user/vshang/WZ_Run2018/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WZTo2L2Q_Run2018_all.root /hdfs/store/user/vshang/WZ_Run2018/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WZTo2Q2Nu_Run2018_all.root /hdfs/store/user/vshang/WZ_Run2018/WZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_WZTo3LNu_Run2018_all.root /hdfs/store/user/vshang/WZ_Run2018/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_ZZTo2Q2Nu_Run2018_all.root /hdfs/store/user/vshang/ZZ_Run2018/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZZTo4L_Run2018_all.root /hdfs/store/user/vshang/ZZ_Run2018/ZZTo4L*/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZZTo2L2Q_Run2018_all.root /hdfs/store/user/vshang/ZZ_Run2018/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_ZZTo2L2Nu_Run2018_all.root /hdfs/store/user/vshang/ZZ_Run2018/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_TTWJetsToLNu_Run2018_all.root /hdfs/store/user/vshang/TTV_Run2018/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_TTWJetsToQQ_Run2018_all.root /hdfs/store/user/vshang/TTV_Run2018/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_TTZToQQ_Run2018_all.root /hdfs/store/user/vshang/TTV_Run2018/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_TTZToLLNuNu_Run2018_all.root /hdfs/store/user/vshang/TTV_Run2018/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_QCD_HT100to200_Run2018_all.root /hdfs/store/user/vshang/QCD_Run2018/QCD_HT100to200_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_HT200to300_Run2018_all.root /hdfs/store/user/vshang/QCD_Run2018/QCD_HT200to300_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_HT300to500_Run2018_all.root /hdfs/store/user/vshang/QCD_Run2018/QCD_HT300to500_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_HT500to700_Run2018_all.root /hdfs/store/user/vshang/QCD_Run2018/QCD_HT500to700_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_HT700to1000_Run2018_all.root /hdfs/store/user/vshang/QCD_Run2018/QCD_HT700to1000_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_HT1000to1500_Run2018_all.root /hdfs/store/user/vshang/QCD_Run2018/QCD_HT1000to1500_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_HT1500to2000_Run2018_all.root /hdfs/store/user/vshang/QCD_Run2018/QCD_HT1500to2000_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_HT2000toInf_Run2018_all.root /hdfs/store/user/vshang/QCD_Run2018/QCD_HT2000toInf_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

./haddnano.py tree_QCD_Pt_15to30_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_30to50_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_50to80_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_80to120_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_120to170_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_170to300_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_300to470_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_470to600_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_600to800_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_800to1000_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1000to1400_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1400to1800_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_1800to2400_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_2400to3200_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root
./haddnano.py tree_QCD_Pt_3200toInf_Run2018_all.root /hdfs/store/user/vshang/QCDPt_Run2018/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/*/*/tree*.root

#Copy output files directly to hdfs
#env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Single_Run2018/MET/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2018A/MET/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2018B/MET/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2018C/MET/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2018D/MET/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2018A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2018A/EGamma/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2018B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2018B/EGamma/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2018C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2018C/EGamma/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2018D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2018D/EGamma/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2018A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2018A/SingleMuon/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2018B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2018B/SingleMuon/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2018C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2018C/SingleMuon/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2018D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2018D/SingleMuon/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbarDM_scalar_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2018/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbarDM_pseudoscalar_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2018/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTToSemiLeptonic_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2018/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTTo2L2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2018/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_s-channel_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_t-channel_top_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_t-channel_antitop_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_tW_top_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_tW_antitop_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-70To100_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-100To200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-200To400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-400To600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-600To800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-800To1200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-1200To2500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-2500ToInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-100to200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-200to400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-400to600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-600to800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-800to1200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-1200to2500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-2500toInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-100To200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-200To400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-400To600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-600To800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-800To1200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-1200To2500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-2500ToInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo1L1Nu2Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2018/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo2L2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2018/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo4Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2018/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo1L1Nu2Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo1L3Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo2L2Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo2Q2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo3LNu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2Q2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2018/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo4L_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2018/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2L2Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2018/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2L2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2018/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTWJetsToLNu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2018/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTWJetsToQQ_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2018/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTZToQQ_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2018/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTZToLLNuNu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2018/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT100to200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT100to200_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT200to300_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT200to300_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT300to500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT300to500_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT500to700_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT500to700_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT700to1000_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT700to1000_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT1000to1500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT1000to1500_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT1500to2000_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT1500to2000_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT2000toInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT2000toInf_TuneCP5_13TeV_madgraphMLM-pythia8/ModuleCommonSkim_03092022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_15to30_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_30to50_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_50to80_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_80to120_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_120to170_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_170to300_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_300to470_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_470to600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_600to800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_800to1000_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1000to1400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1400to1800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1800to2400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_2400to3200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_3200toInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/ModuleCommonSkim_03092022/tree_all.root

#prevent condor from also transferring the output files back to the submit directory:
rm *.root
