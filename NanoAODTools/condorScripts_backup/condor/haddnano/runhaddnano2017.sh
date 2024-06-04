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
#./haddnano.py tree__Run2017_all.root /hdfs/store/user/vshang/_Run2017//countEvents_02062024/*/*/tree*.root

./haddnano.py tree_MET_Run2017B_all.root $(./filterList.py "MET_Run2017B/MET/")
./haddnano.py tree_MET_Run2017C_all.root $(./filterList.py "MET_Run2017C/MET/")
./haddnano.py tree_MET_Run2017D_all.root $(./filterList.py "MET_Run2017D/MET/")
./haddnano.py tree_MET_Run2017E_all.root $(./filterList.py "MET_Run2017E/MET/")
./haddnano.py tree_MET_Run2017F_all.root $(./filterList.py "MET_Run2017F/MET/")

./haddnano.py tree_SingleElectron_Run2017B_all.root $(./filterList.py "SingleElectron_Run2017B/SingleElectron/")
./haddnano.py tree_SingleElectron_Run2017C_all.root $(./filterList.py "SingleElectron_Run2017C/SingleElectron/")
./haddnano.py tree_SingleElectron_Run2017D_all.root $(./filterList.py "SingleElectron_Run2017D/SingleElectron/")
./haddnano.py tree_SingleElectron_Run2017E_all.root $(./filterList.py "SingleElectron_Run2017E/SingleElectron/")
./haddnano.py tree_SingleElectron_Run2017F_all.root $(./filterList.py "SingleElectron_Run2017F/SingleElectron/")

./haddnano.py tree_SingleMuon_Run2017B_all.root $(./filterList.py "SingleMuon_Run2017B/SingleMuon/")
./haddnano.py tree_SingleMuon_Run2017C_all.root $(./filterList.py "SingleMuon_Run2017C/SingleMuon/")
./haddnano.py tree_SingleMuon_Run2017D_all.root $(./filterList.py "SingleMuon_Run2017D/SingleMuon/")
./haddnano.py tree_SingleMuon_Run2017E_all.root $(./filterList.py "SingleMuon_Run2017E/SingleMuon/")
./haddnano.py tree_SingleMuon_Run2017F_all.root $(./filterList.py "SingleMuon_Run2017F/SingleMuon/")

./haddnano.py tree_SinglePhoton_Run2017B_all.root $(./filterList.py "SinglePhoton_Run2017B/SinglePhoton/")
./haddnano.py tree_SinglePhoton_Run2017C_all.root $(./filterList.py "SinglePhoton_Run2017C/SinglePhoton/")
./haddnano.py tree_SinglePhoton_Run2017D_all.root $(./filterList.py "SinglePhoton_Run2017D/SinglePhoton/")
./haddnano.py tree_SinglePhoton_Run2017E_all.root $(./filterList.py "SinglePhoton_Run2017E/SinglePhoton/")
./haddnano.py tree_SinglePhoton_Run2017F_all.root $(./filterList.py "SinglePhoton_Run2017F/SinglePhoton/")

./haddnano.py tree_ttbarDM_scalar_Run2017_all.root $(./filterList.py "ttbarDM_Run2017/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/")
./haddnano.py tree_ttbarDM_pseudoscalar_Run2017_all.root $(./filterList.py "ttbarDM_Run2017/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/")

./haddnano.py tree_ttH_Run2017_all.root $(./filterList.py "ttH_Run2017/ttH_HToInvisible_M125_13TeV_TuneCP5_powheg_pythia8/")

./haddnano.py tree_WminusH_Run2017_all.root $(./filterList.py "VH_Run2017/WminusH_WToQQ_HToInvisible_M125_13TeV_powheg_pythia8/")
./haddnano.py tree_WplusH_Run2017_all.root $(./filterList.py "VH_Run2017/WplusH_WToQQ_HToInvisible_M125_13TeV_powheg_pythia8/")
./haddnano.py tree_ZH_Run2017_all.root $(./filterList.py "VH_Run2017/ZH_ZToQQ_HToInvisible_M125_13TeV_powheg_pythia8/")

./haddnano.py tree_TTToSemiLeptonic_Run2017_all.root $(./filterList.py "ttbarPlusJets_Run2017/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_TTTo2L2Nu_Run2017_all.root $(./filterList.py "ttbarPlusJets_Run2017/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_TTToHadronic_Run2017_all.root $(./filterList.py "ttbarPlusJets_Run2017/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/")

./haddnano.py tree_ST_s-channel_Run2017_all.root $(./filterList.py "singleTop_Run2017/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_ST_t-channel_top_Run2017_all.root $(./filterList.py "singleTop_Run2017/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/")
./haddnano.py tree_ST_t-channel_antitop_Run2017_all.root $(./filterList.py "singleTop_Run2017/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/")
./haddnano.py tree_ST_tW_top_Run2017_all.root $(./filterList.py "singleTop_Run2017/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_ST_tW_antitop_Run2017_all.root $(./filterList.py "singleTop_Run2017/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/")

./haddnano.py tree_WJetsToLNu_HT-70To100_Run2017_all.root $(./filterList.py "WPlusJets_Run2017/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-100To200_Run2017_all.root $(./filterList.py "WPlusJets_Run2017/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-200To400_Run2017_all.root $(./filterList.py "WPlusJets_Run2017/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-400To600_Run2017_all.root $(./filterList.py "WPlusJets_Run2017/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-600To800_Run2017_all.root $(./filterList.py "WPlusJets_Run2017/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-800To1200_Run2017_all.root $(./filterList.py "WPlusJets_Run2017/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-1200To2500_Run2017_all.root $(./filterList.py "WPlusJets_Run2017/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-2500ToInf_Run2017_all.root $(./filterList.py "WPlusJets_Run2017/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/")

./haddnano.py tree_DYJetsToLL_HT-100to200_Run2017_all.root $(./filterList.py "ZTo2L_Run2017/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-200to400_Run2017_all.root $(./filterList.py "ZTo2L_Run2017/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-400to600_Run2017_all.root $(./filterList.py "ZTo2L_Run2017/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-600to800_Run2017_all.root $(./filterList.py "ZTo2L_Run2017/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-800to1200_Run2017_all.root $(./filterList.py "ZTo2L_Run2017/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-1200to2500_Run2017_all.root $(./filterList.py "ZTo2L_Run2017/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-2500toInf_Run2017_all.root $(./filterList.py "ZTo2L_Run2017/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/")

./haddnano.py tree_ZJetsToNuNu_HT-100To200_Run2017_all.root $(./filterList.py "ZTo2Nu_Run2017/ZJetsToNuNu_HT-100To200_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-200To400_Run2017_all.root $(./filterList.py "ZTo2Nu_Run2017/ZJetsToNuNu_HT-200To400_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-400To600_Run2017_all.root $(./filterList.py "ZTo2Nu_Run2017/ZJetsToNuNu_HT-400To600_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-600To800_Run2017_all.root $(./filterList.py "ZTo2Nu_Run2017/ZJetsToNuNu_HT-600To800_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-800To1200_Run2017_all.root $(./filterList.py "ZTo2Nu_Run2017/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-1200To2500_Run2017_all.root $(./filterList.py "ZTo2Nu_Run2017/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-2500ToInf_Run2017_all.root $(./filterList.py "ZTo2Nu_Run2017/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/")

./haddnano.py tree_WWTo1L1Nu2Q_Run2017_all.root $(./filterList.py "WW_Run2017/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WWTo2L2Nu_Run2017_all.root $(./filterList.py "WW_Run2017/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_WWTo4Q_Run2017_all.root $(./filterList.py "WW_Run2017/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/")

./haddnano.py tree_WZTo1L1Nu2Q_Run2017_all.root $(./filterList.py "WZ_Run2017/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WZTo1L3Nu_Run2017_all.root $(./filterList.py "WZ_Run2017/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/")
./haddnano.py tree_WZTo2L2Q_Run2017_all.root $(./filterList.py "WZ_Run2017/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WZTo2Q2Nu_Run2017_all.root $(./filterList.py "WZ_Run2017/WZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WZTo3LNu_Run2017_all.root $(./filterList.py "WZ_Run2017/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/")

./haddnano.py tree_ZZTo2Q2Nu_Run2017_all.root $(./filterList.py "ZZ_Run2017/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_ZZTo4L_Run2017_all.root $(./filterList.py "ZZ_Run2017/ZZTo4L_13TeV_powheg_pythia8/")
./haddnano.py tree_ZZTo2L2Q_Run2017_all.root $(./filterList.py "ZZ_Run2017/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_ZZTo2L2Nu_Run2017_all.root $(./filterList.py "ZZ_Run2017/ZZTo2L2Nu_13TeV_powheg_pythia8/")

./haddnano.py tree_TTWJetsToLNu_Run2017_all.root $(./filterList.py "TTV_Run2017/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/")
./haddnano.py tree_TTWJetsToQQ_Run2017_all.root $(./filterList.py "TTV_Run2017/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/")
./haddnano.py tree_TTZToQQ_Run2017_all.root $(./filterList.py "TTV_Run2017/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_TTZToLLNuNu_Run2017_all.root $(./filterList.py "TTV_Run2017/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/")

./haddnano.py tree_QCD_Pt_15to30_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_30to50_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_50to80_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_80to120_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_120to170_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_170to300_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_300to470_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_470to600_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_600to800_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_800to1000_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_1000to1400_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_1400to1800_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_1800to2400_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_2400to3200_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_3200toInf_Run2017_all.root $(./filterList.py "QCDPt_Run2017/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/")

# ./haddnano.py tree_W1JetsToLNu_LHEWpT_100-150_Run2017_all.root $(./filterList.py "WPlusJetsNLO_Run2017/W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_W1JetsToLNu_LHEWpT_150-250_Run2017_all.root $(./filterList.py "WPlusJetsNLO_Run2017/W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_W1JetsToLNu_LHEWpT_250-400_Run2017_all.root $(./filterList.py "WPlusJetsNLO_Run2017/W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_W1JetsToLNu_LHEWpT_400-inf_Run2017_all.root $(./filterList.py "WPlusJetsNLO_Run2017/W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_W2JetsToLNu_LHEWpT_100-150_Run2017_all.root $(./filterList.py "WPlusJetsNLO_Run2017/W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_W2JetsToLNu_LHEWpT_150-250_Run2017_all.root $(./filterList.py "WPlusJetsNLO_Run2017/W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_W2JetsToLNu_LHEWpT_250-400_Run2017_all.root $(./filterList.py "WPlusJetsNLO_Run2017/W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_W2JetsToLNu_LHEWpT_400-inf_Run2017_all.root $(./filterList.py "WPlusJetsNLO_Run2017/W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")

# ./haddnano.py tree_DY1JetsToLL_M-50_LHEZpT_50-150_Run2017_all.root $(./filterList.py "ZTo2LNLO_Run2017/DY1JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_DY1JetsToLL_M-50_LHEZpT_150-250_Run2017_all.root $(./filterList.py "ZTo2LNLO_Run2017/DY1JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_DY1JetsToLL_M-50_LHEZpT_250-400_Run2017_all.root $(./filterList.py "ZTo2LNLO_Run2017/DY1JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_DY1JetsToLL_M-50_LHEZpT_400-inf_Run2017_all.root $(./filterList.py "ZTo2LNLO_Run2017/DY1JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_DY2JetsToLL_M-50_LHEZpT_50-150_Run2017_all.root $(./filterList.py "ZTo2LNLO_Run2017/DY2JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_DY2JetsToLL_M-50_LHEZpT_150-250_Run2017_all.root $(./filterList.py "ZTo2LNLO_Run2017/DY2JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_DY2JetsToLL_M-50_LHEZpT_250-400_Run2017_all.root $(./filterList.py "ZTo2LNLO_Run2017/DY2JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_DY2JetsToLL_M-50_LHEZpT_400-inf_Run2017_all.root $(./filterList.py "ZTo2LNLO_Run2017/DY2JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")

# ./haddnano.py tree_Z1JetsToNuNu_M-50_LHEZpT_50-150_Run2017_all.root $(./filterList.py "ZTo2NuNLO_Run2017/Z1JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_Z1JetsToNuNu_M-50_LHEZpT_150-250_Run2017_all.root $(./filterList.py "ZTo2NuNLO_Run2017/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_Z1JetsToNuNu_M-50_LHEZpT_250-400_Run2017_all.root $(./filterList.py "ZTo2NuNLO_Run2017/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_Z1JetsToNuNu_M-50_LHEZpT_400-inf_Run2017_all.root $(./filterList.py "ZTo2NuNLO_Run2017/Z1JetsToNuNu_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_Z2JetsToNuNu_M-50_LHEZpT_50-150_Run2017_all.root $(./filterList.py "ZTo2NuNLO_Run2017/Z2JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_Z2JetsToNuNu_M-50_LHEZpT_150-250_Run2017_all.root $(./filterList.py "ZTo2NuNLO_Run2017/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_Z2JetsToNuNu_M-50_LHEZpT_250-400_Run2017_all.root $(./filterList.py "ZTo2NuNLO_Run2017/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
# ./haddnano.py tree_Z2JetsToNuNu_M-50_LHEZpT_400-inf_Run2017_all.root $(./filterList.py "ZTo2NuNLO_Run2017/Z2JetsToNuNU_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")

./haddnano.py tree_GluGluHToZZTo4L_Run2017_all.root $(./filterList.py "Other_Run2017/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/")
./haddnano.py tree_TTGJets_Run2017_all.root $(./filterList.py "Other_Run2017/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/")
./haddnano.py tree_ttHTobb_Run2017_all.root $(./filterList.py "Other_Run2017/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_ttHToNonbb_Run2017_all.root $(./filterList.py "Other_Run2017/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_TTTT_Run2017_all.root $(./filterList.py "Other_Run2017/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_tZq_Run2017_all.root $(./filterList.py "Other_Run2017/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_VHToNonbb_Run2017_all.root $(./filterList.py "Other_Run2017/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WWG_Run2017_all.root $(./filterList.py "Other_Run2017/WWG_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_WWW_Run2017_all.root $(./filterList.py "Other_Run2017/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_WWZ_Run2017_all.root $(./filterList.py "Other_Run2017/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_WZG_Run2017_all.root $(./filterList.py "Other_Run2017/WZG_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_WZZ_Run2017_all.root $(./filterList.py "Other_Run2017/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_ZH_HToBB_Run2017_all.root $(./filterList.py "Other_Run2017/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/")
./haddnano.py tree_ZZZ_Run2017_all.root $(./filterList.py "Other_Run2017/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_WminusH_HToBB_WToLNu_Run2017_all.root $(./filterList.py "Other_Run2017/WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/")
./haddnano.py tree_WplusH_HToBB_WToLNu_Run2017_all.root $(./filterList.py "Other_Run2017/WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/")
./haddnano.py tree_WminusH_HToBB_WToQQ_Run2017_all.root $(./filterList.py "Other_Run2017/WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8/")
./haddnano.py tree_WplusH_HToBB_WToQQ_Run2017_all.root $(./filterList.py "Other_Run2017/WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8/")

#Copy output files directly to hdfs
#env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Single_Run2017/MET/countEvents_02062024/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2017B/MET/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2017C/MET/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2017D/MET/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017E_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2017E/MET/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2017F_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2017F/MET/countEvents_02062024/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2017B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2017B/SingleElectron/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2017C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2017C/SingleElectron/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2017D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2017D/SingleElectron/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2017E_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2017E/SingleElectron/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2017F_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2017F/SingleElectron/countEvents_02062024/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2017B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2017B/SingleMuon/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2017C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2017C/SingleMuon/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2017D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2017D/SingleMuon/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2017E_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2017E/SingleMuon/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2017F_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2017F/SingleMuon/countEvents_02062024/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SinglePhoton_Run2017B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SinglePhoton_Run2017B/SinglePhoton/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SinglePhoton_Run2017C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SinglePhoton_Run2017C/SinglePhoton/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SinglePhoton_Run2017D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SinglePhoton_Run2017D/SinglePhoton/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SinglePhoton_Run2017E_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SinglePhoton_Run2017E/SinglePhoton/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SinglePhoton_Run2017F_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SinglePhoton_Run2017F/SinglePhoton/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbarDM_scalar_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2017/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbarDM_pseudoscalar_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2017/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttH_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttH_Run2017/ttH_HToInvisible_M125_13TeV_TuneCP5_powheg_pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WminusH_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/VH_Run2017/WminusH_WToQQ_HToInvisible_M125_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WplusH_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/VH_Run2017/WplusH_WToQQ_HToInvisible_M125_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZH_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/VH_Run2017/ZH_ZToQQ_HToInvisible_M125_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTToSemiLeptonic_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2017/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTTo2L2Nu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2017/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTToHadronic_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2017/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_s-channel_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2017/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_t-channel_top_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2017/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_t-channel_antitop_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2017/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_tW_top_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2017/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_tW_antitop_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2017/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-70To100_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-100To200_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-200To400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-400To600_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-600To800_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-800To1200_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-1200To2500_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-2500ToInf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2017/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-100to200_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-200to400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-400to600_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-600to800_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-800to1200_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-1200to2500_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-2500toInf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2017/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-100To200_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-100To200_13TeV-madgraph/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-200To400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-200To400_13TeV-madgraph/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-400To600_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-400To600_13TeV-madgraph/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-600To800_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-600To800_13TeV-madgraph/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-800To1200_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-1200To2500_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-2500ToInf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2017/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo1L1Nu2Q_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2017/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo2L2Nu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2017/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo4Q_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2017/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo1L1Nu2Q_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2017/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo1L3Nu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2017/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo2L2Q_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2017/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo2Q2Nu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2017/WZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo3LNu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2017/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2Q2Nu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2017/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo4L_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2017/ZZTo4L_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2L2Q_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2017/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2L2Nu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2017/ZZTo2L2Nu_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTWJetsToLNu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2017/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTWJetsToQQ_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2017/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTZToQQ_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2017/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTZToLLNuNu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2017/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_15to30_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_30to50_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_50to80_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_80to120_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_120to170_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_170to300_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_300to470_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_470to600_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_600to800_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_800to1000_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1000to1400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1400to1800_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1800to2400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_2400to3200_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_3200toInf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2017/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/countEvents_02062024/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_W1JetsToLNu_LHEWpT_100-150_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2017/W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_W1JetsToLNu_LHEWpT_150-250_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2017/W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_W1JetsToLNu_LHEWpT_250-400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2017/W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_W1JetsToLNu_LHEWpT_400-inf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2017/W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_W2JetsToLNu_LHEWpT_100-150_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2017/W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_W2JetsToLNu_LHEWpT_150-250_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2017/W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_W2JetsToLNu_LHEWpT_250-400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2017/W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_W2JetsToLNu_LHEWpT_400-inf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2017/W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY1JetsToLL_M-50_LHEZpT_50-150_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2017/DY1JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY1JetsToLL_M-50_LHEZpT_150-250_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2017/DY1JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY1JetsToLL_M-50_LHEZpT_250-400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2017/DY1JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY1JetsToLL_M-50_LHEZpT_400-inf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2017/DY1JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY2JetsToLL_M-50_LHEZpT_50-150_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2017/DY2JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY2JetsToLL_M-50_LHEZpT_150-250_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2017/DY2JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY2JetsToLL_M-50_LHEZpT_250-400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2017/DY2JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY2JetsToLL_M-50_LHEZpT_400-inf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2017/DY2JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z1JetsToNuNu_M-50_LHEZpT_50-150_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2017/Z1JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z1JetsToNuNu_M-50_LHEZpT_150-250_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2017/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z1JetsToNuNu_M-50_LHEZpT_250-400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2017/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z1JetsToNuNu_M-50_LHEZpT_400-inf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2017/Z1JetsToNuNu_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z2JetsToNuNu_M-50_LHEZpT_50-150_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2017/Z2JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z2JetsToNuNu_M-50_LHEZpT_150-250_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2017/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z2JetsToNuNu_M-50_LHEZpT_250-400_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2017/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z2JetsToNuNu_M-50_LHEZpT_400-inf_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2017/Z2JetsToNuNU_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_02062024/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_GluGluHToZZTo4L_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTGJets_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttHTobb_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttHToNonbb_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTTT_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_tZq_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_VHToNonbb_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWG_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WWG_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWW_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWZ_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZG_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WZG_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZZ_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZH_HToBB_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZZ_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WminusH_HToBB_WToLNu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WplusH_HToBB_WToLNu_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WminusH_HToBB_WToQQ_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WplusH_HToBB_WToQQ_Run2017_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Other_Run2017/WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8/countEvents_02062024/tree_all.root

#prevent condor from also transferring the output files back to the submit directory:
rm *.root
