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
#./haddnano.py tree__Run2018_all.root /hdfs/store/user/vshang/_Run2018//countEvents_12242022/*/*/tree*.root

# ./haddnano.py tree_MET_Run2018A_all.root $(./filterList.py "MET_Run2018A/MET/")
# ./haddnano.py tree_MET_Run2018B_all.root $(./filterList.py "MET_Run2018B/MET/")
# ./haddnano.py tree_MET_Run2018C_all.root $(./filterList.py "MET_Run2018C/MET/")
# ./haddnano.py tree_MET_Run2018D_all.root $(./filterList.py "MET_Run2018D/MET/")

# ./haddnano.py tree_SingleElectron_Run2018A_all.root $(./filterList.py "SingleElectron_Run2018A/EGamma/")
# ./haddnano.py tree_SingleElectron_Run2018B_all.root $(./filterList.py "SingleElectron_Run2018B/EGamma/")
# ./haddnano.py tree_SingleElectron_Run2018C_all.root $(./filterList.py "SingleElectron_Run2018C/EGamma/")
# ./haddnano.py tree_SingleElectron_Run2018D_all.root $(./filterList.py "SingleElectron_Run2018D/EGamma/")

# ./haddnano.py tree_SingleMuon_Run2018A_all.root $(./filterList.py "SingleMuon_Run2018A/SingleMuon/")
# ./haddnano.py tree_SingleMuon_Run2018B_all.root $(./filterList.py "SingleMuon_Run2018B/SingleMuon/")
# ./haddnano.py tree_SingleMuon_Run2018C_all.root $(./filterList.py "SingleMuon_Run2018C/SingleMuon/")
# ./haddnano.py tree_SingleMuon_Run2018D_all.root $(./filterList.py "SingleMuon_Run2018D/SingleMuon/")

./haddnano.py tree_ttbarDM_scalar_Run2018_all.root $(./filterList.py "ttbarDM_Run2018/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/")
./haddnano.py tree_ttbarDM_pseudoscalar_Run2018_all.root $(./filterList.py "ttbarDM_Run2018/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/")

./haddnano.py tree_ttH_Run2018_all.root $(./filterList.py "ttH_Run2018/ttH_HToInvisible_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/")

./haddnano.py tree_WminusH_Run2018_all.root $(./filterList.py "VH_Run2018/WminusH_WToQQ_HToInvisible_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/")
./haddnano.py tree_WplusH_Run2018_all.root $(./filterList.py "VH_Run2018/WplusH_WToQQ_HToInvisible_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/")
./haddnano.py tree_ZH_Run2018_all.root $(./filterList.py "VH_Run2018/ZH_ZToQQ_HToInvisible_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/")

./haddnano.py tree_TTToSemiLeptonic_Run2018_all.root $(./filterList.py "ttbarPlusJets_Run2018/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_TTTo2L2Nu_Run2018_all.root $(./filterList.py "ttbarPlusJets_Run2018/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/")

./haddnano.py tree_ST_s-channel_Run2018_all.root $(./filterList.py "singleTop_Run2018/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_ST_t-channel_top_Run2018_all.root $(./filterList.py "singleTop_Run2018/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/")
./haddnano.py tree_ST_t-channel_antitop_Run2018_all.root $(./filterList.py "singleTop_Run2018/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/")
./haddnano.py tree_ST_tW_top_Run2018_all.root $(./filterList.py "singleTop_Run2018/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_ST_tW_antitop_Run2018_all.root $(./filterList.py "singleTop_Run2018/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/")

./haddnano.py tree_WJetsToLNu_HT-70To100_Run2018_all.root $(./filterList.py "WPlusJets_Run2018/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-100To200_Run2018_all.root $(./filterList.py "WPlusJets_Run2018/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-200To400_Run2018_all.root $(./filterList.py "WPlusJets_Run2018/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-400To600_Run2018_all.root $(./filterList.py "WPlusJets_Run2018/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-600To800_Run2018_all.root $(./filterList.py "WPlusJets_Run2018/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-800To1200_Run2018_all.root $(./filterList.py "WPlusJets_Run2018/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-1200To2500_Run2018_all.root $(./filterList.py "WPlusJets_Run2018/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_WJetsToLNu_HT-2500ToInf_Run2018_all.root $(./filterList.py "WPlusJets_Run2018/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/")

./haddnano.py tree_DYJetsToLL_HT-100to200_Run2018_all.root $(./filterList.py "ZTo2L_Run2018/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-200to400_Run2018_all.root $(./filterList.py "ZTo2L_Run2018/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-400to600_Run2018_all.root $(./filterList.py "ZTo2L_Run2018/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-600to800_Run2018_all.root $(./filterList.py "ZTo2L_Run2018/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-800to1200_Run2018_all.root $(./filterList.py "ZTo2L_Run2018/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-1200to2500_Run2018_all.root $(./filterList.py "ZTo2L_Run2018/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/")
./haddnano.py tree_DYJetsToLL_HT-2500toInf_Run2018_all.root $(./filterList.py "ZTo2L_Run2018/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/")

./haddnano.py tree_ZJetsToNuNu_HT-100To200_Run2018_all.root $(./filterList.py "ZTo2Nu_Run2018/ZJetsToNuNu_HT-100To200_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-200To400_Run2018_all.root $(./filterList.py "ZTo2Nu_Run2018/ZJetsToNuNu_HT-200To400_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-400To600_Run2018_all.root $(./filterList.py "ZTo2Nu_Run2018/ZJetsToNuNu_HT-400To600_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-600To800_Run2018_all.root $(./filterList.py "ZTo2Nu_Run2018/ZJetsToNuNu_HT-600To800_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-800To1200_Run2018_all.root $(./filterList.py "ZTo2Nu_Run2018/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-1200To2500_Run2018_all.root $(./filterList.py "ZTo2Nu_Run2018/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/")
./haddnano.py tree_ZJetsToNuNu_HT-2500ToInf_Run2018_all.root $(./filterList.py "ZTo2Nu_Run2018/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/")

./haddnano.py tree_WWTo1L1Nu2Q_Run2018_all.root $(./filterList.py "WW_Run2018/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WWTo2L2Nu_Run2018_all.root $(./filterList.py "WW_Run2018/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/")
./haddnano.py tree_WWTo4Q_Run2018_all.root $(./filterList.py "WW_Run2018/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/")

./haddnano.py tree_WZTo1L1Nu2Q_Run2018_all.root $(./filterList.py "WZ_Run2018/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WZTo1L3Nu_Run2018_all.root $(./filterList.py "WZ_Run2018/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WZTo2L2Q_Run2018_all.root $(./filterList.py "WZ_Run2018/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WZTo2Q2Nu_Run2018_all.root $(./filterList.py "WZ_Run2018/WZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_WZTo3LNu_Run2018_all.root $(./filterList.py "WZ_Run2018/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/")

./haddnano.py tree_ZZTo2Q2Nu_Run2018_all.root $(./filterList.py "ZZ_Run2018/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_ZZTo4L_Run2018_all.root $(./filterList.py "ZZ_Run2018/ZZTo4L")
./haddnano.py tree_ZZTo2L2Q_Run2018_all.root $(./filterList.py "ZZ_Run2018/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/")
./haddnano.py tree_ZZTo2L2Nu_Run2018_all.root $(./filterList.py "ZZ_Run2018/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/")

./haddnano.py tree_TTWJetsToLNu_Run2018_all.root $(./filterList.py "TTV_Run2018/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/")
./haddnano.py tree_TTWJetsToQQ_Run2018_all.root $(./filterList.py "TTV_Run2018/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/")
./haddnano.py tree_TTZToQQ_Run2018_all.root $(./filterList.py "TTV_Run2018/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/")
./haddnano.py tree_TTZToLLNuNu_Run2018_all.root $(./filterList.py "TTV_Run2018/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/")

# ./haddnano.py tree_QCD_HT100to200_Run2018_all.root $(./filterList.py "QCD_Run2018/QCD_HT100to200_TuneCP5_13TeV_madgraphMLM-pythia8/")
# ./haddnano.py tree_QCD_HT200to300_Run2018_all.root $(./filterList.py "QCD_Run2018/QCD_HT200to300_TuneCP5_13TeV_madgraphMLM-pythia8/")
# ./haddnano.py tree_QCD_HT300to500_Run2018_all.root $(./filterList.py "QCD_Run2018/QCD_HT300to500_TuneCP5_13TeV_madgraphMLM-pythia8/")
# ./haddnano.py tree_QCD_HT500to700_Run2018_all.root $(./filterList.py "QCD_Run2018/QCD_HT500to700_TuneCP5_13TeV_madgraphMLM-pythia8/")
# ./haddnano.py tree_QCD_HT700to1000_Run2018_all.root $(./filterList.py "QCD_Run2018/QCD_HT700to1000_TuneCP5_13TeV_madgraphMLM-pythia8/")
# ./haddnano.py tree_QCD_HT1000to1500_Run2018_all.root $(./filterList.py "QCD_Run2018/QCD_HT1000to1500_TuneCP5_13TeV_madgraphMLM-pythia8/")
# ./haddnano.py tree_QCD_HT1500to2000_Run2018_all.root $(./filterList.py "QCD_Run2018/QCD_HT1500to2000_TuneCP5_13TeV_madgraphMLM-pythia8/")
# ./haddnano.py tree_QCD_HT2000toInf_Run2018_all.root $(./filterList.py "QCD_Run2018/QCD_HT2000toInf_TuneCP5_13TeV_madgraphMLM-pythia8/")

./haddnano.py tree_QCD_Pt_15to30_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_30to50_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_50to80_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_80to120_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_120to170_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_170to300_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_300to470_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_470to600_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_600to800_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_800to1000_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_1000to1400_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_1400to1800_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_1800to2400_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_2400to3200_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/")
./haddnano.py tree_QCD_Pt_3200toInf_Run2018_all.root $(./filterList.py "QCDPt_Run2018/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/")

./haddnano.py tree_WJetsToLNu_Pt-50To100_Run2018_all.root $(./filterList.py "WPlusJetsNLO_Run2018/WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8/")
./haddnano.py tree_WJetsToLNu_Pt-100To250_Run2018_all.root $(./filterList.py "WPlusJetsNLO_Run2018/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/")
./haddnano.py tree_WJetsToLNu_Pt-250To400_Run2018_all.root $(./filterList.py "WPlusJetsNLO_Run2018/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/")
./haddnano.py tree_WJetsToLNu_Pt-400To600_Run2018_all.root $(./filterList.py "WPlusJetsNLO_Run2018/WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8/")
./haddnano.py tree_WJetsToLNu_Pt-600ToInf_Run2018_all.root $(./filterList.py "WPlusJetsNLO_Run2018/WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/")

./haddnano.py tree_DY1JetsToLL_M-50_LHEZpT_50-150_Run2018_all.root $(./filterList.py "ZTo2LNLO_Run2018/DY1JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_DY1JetsToLL_M-50_LHEZpT_150-250_Run2018_all.root $(./filterList.py "ZTo2LNLO_Run2018/DY1JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_DY1JetsToLL_M-50_LHEZpT_250-400_Run2018_all.root $(./filterList.py "ZTo2LNLO_Run2018/DY1JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_DY1JetsToLL_M-50_LHEZpT_400-inf_Run2018_all.root $(./filterList.py "ZTo2LNLO_Run2018/DY1JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_DY2JetsToLL_M-50_LHEZpT_50-150_Run2018_all.root $(./filterList.py "ZTo2LNLO_Run2018/DY2JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_DY2JetsToLL_M-50_LHEZpT_150-250_Run2018_all.root $(./filterList.py "ZTo2LNLO_Run2018/DY2JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_DY2JetsToLL_M-50_LHEZpT_250-400_Run2018_all.root $(./filterList.py "ZTo2LNLO_Run2018/DY2JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_DY2JetsToLL_M-50_LHEZpT_400-inf_Run2018_all.root $(./filterList.py "ZTo2LNLO_Run2018/DY2JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")

./haddnano.py tree_Z1JetsToNuNu_M-50_LHEZpT_50-150_Run2018_all.root $(./filterList.py "ZTo2NuNLO_Run2018/Z1JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_Z1JetsToNuNu_M-50_LHEZpT_150-250_Run2018_all.root $(./filterList.py "ZTo2NuNLO_Run2018/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_Z1JetsToNuNu_M-50_LHEZpT_250-400_Run2018_all.root $(./filterList.py "ZTo2NuNLO_Run2018/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_Z1JetsToNuNu_M-50_LHEZpT_400-inf_Run2018_all.root $(./filterList.py "ZTo2NuNLO_Run2018/Z1JetsToNuNu_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_Z2JetsToNuNu_M-50_LHEZpT_50-150_Run2018_all.root $(./filterList.py "ZTo2NuNLO_Run2018/Z2JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_Z2JetsToNuNu_M-50_LHEZpT_150-250_Run2018_all.root $(./filterList.py "ZTo2NuNLO_Run2018/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_Z2JetsToNuNu_M-50_LHEZpT_250-400_Run2018_all.root $(./filterList.py "ZTo2NuNLO_Run2018/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/")
./haddnano.py tree_Z2JetsToNuNu_M-50_LHEZpT_400-inf_Run2018_all.root $(./filterList.py "ZTo2NuNLO_Run2018/Z2JetsToNuNU_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/")

#Copy output files directly to hdfs
#env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/Single_Run2018/MET/countEvents_12242022/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2018A/MET/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2018B/MET/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2018C/MET/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_MET_Run2018D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/MET_Run2018D/MET/countEvents_12242022/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2018A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2018A/EGamma/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2018B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2018B/EGamma/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2018C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2018C/EGamma/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleElectron_Run2018D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleElectron_Run2018D/EGamma/countEvents_12242022/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2018A_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2018A/SingleMuon/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2018B_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2018B/SingleMuon/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2018C_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2018C/SingleMuon/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_SingleMuon_Run2018D_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/SingleMuon_Run2018D/SingleMuon/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbarDM_scalar_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2018/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttbarDM_pseudoscalar_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarDM_Run2018/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ttH_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttH_Run2018/ttH_HToInvisible_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WminusH_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/VH_Run2018/WminusH_WToQQ_HToInvisible_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WplusH_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/VH_Run2018/WplusH_WToQQ_HToInvisible_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZH_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/VH_Run2018/ZH_ZToQQ_HToInvisible_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTToSemiLeptonic_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2018/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTTo2L2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ttbarPlusJets_Run2018/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_s-channel_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_t-channel_top_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_t-channel_antitop_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_tW_top_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ST_tW_antitop_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/singleTop_Run2018/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-70To100_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-100To200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-200To400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-400To600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-600To800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-800To1200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-1200To2500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_HT-2500ToInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJets_Run2018/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-100to200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-200to400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-400to600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-600to800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-800to1200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-1200to2500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DYJetsToLL_HT-2500toInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2L_Run2018/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-100To200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-100To200_13TeV-madgraph/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-200To400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-200To400_13TeV-madgraph/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-400To600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-400To600_13TeV-madgraph/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-600To800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-600To800_13TeV-madgraph/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-800To1200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-1200To2500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZJetsToNuNu_HT-2500ToInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2Nu_Run2018/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo1L1Nu2Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2018/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo2L2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2018/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WWTo4Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WW_Run2018/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo1L1Nu2Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo1L3Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo2L2Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo2Q2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WZTo3LNu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WZ_Run2018/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2Q2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2018/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo4L_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2018/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2L2Q_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2018/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_ZZTo2L2Nu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZZ_Run2018/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTWJetsToLNu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2018/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTWJetsToQQ_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2018/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTZToQQ_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2018/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_TTZToLLNuNu_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/TTV_Run2018/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/countEvents_12242022/tree_all.root

# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT100to200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT100to200_TuneCP5_13TeV_madgraphMLM-pythia8/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT200to300_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT200to300_TuneCP5_13TeV_madgraphMLM-pythia8/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT300to500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT300to500_TuneCP5_13TeV_madgraphMLM-pythia8/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT500to700_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT500to700_TuneCP5_13TeV_madgraphMLM-pythia8/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT700to1000_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT700to1000_TuneCP5_13TeV_madgraphMLM-pythia8/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT1000to1500_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT1000to1500_TuneCP5_13TeV_madgraphMLM-pythia8/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT1500to2000_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT1500to2000_TuneCP5_13TeV_madgraphMLM-pythia8/countEvents_12242022/tree_all.root
# env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_HT2000toInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCD_Run2018/QCD_HT2000toInf_TuneCP5_13TeV_madgraphMLM-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_15to30_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_30to50_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_50to80_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_80to120_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_120to170_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_170to300_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_300to470_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_470to600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_600to800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_800to1000_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1000to1400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1400to1800_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_1800to2400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_2400to3200_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_QCD_Pt_3200toInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/QCDPt_Run2018/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_Pt-50To100_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2018/WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_Pt-100To250_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2018/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_Pt-250To400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2018/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_Pt-400To600_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2018/WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_WJetsToLNu_Pt-600ToInf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/WPlusJetsNLO_Run2018/WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY1JetsToLL_M-50_LHEZpT_50-150_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2018/DY1JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY1JetsToLL_M-50_LHEZpT_150-250_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2018/DY1JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY1JetsToLL_M-50_LHEZpT_250-400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2018/DY1JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY1JetsToLL_M-50_LHEZpT_400-inf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2018/DY1JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY2JetsToLL_M-50_LHEZpT_50-150_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2018/DY2JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY2JetsToLL_M-50_LHEZpT_150-250_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2018/DY2JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY2JetsToLL_M-50_LHEZpT_250-400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2018/DY2JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_DY2JetsToLL_M-50_LHEZpT_400-inf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2LNLO_Run2018/DY2JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root

env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z1JetsToNuNu_M-50_LHEZpT_50-150_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2018/Z1JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z1JetsToNuNu_M-50_LHEZpT_150-250_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2018/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z1JetsToNuNu_M-50_LHEZpT_250-400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2018/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z1JetsToNuNu_M-50_LHEZpT_400-inf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2018/Z1JetsToNuNu_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z2JetsToNuNu_M-50_LHEZpT_50-150_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2018/Z2JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z2JetsToNuNu_M-50_LHEZpT_150-250_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2018/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z2JetsToNuNu_M-50_LHEZpT_250-400_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2018/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root
env -i X509_USER_PROXY=$X509_USER_PROXY gfal-copy -t 10000 -p tree_Z2JetsToNuNu_M-50_LHEZpT_400-inf_Run2018_all.root davs://pubxrootd.hep.wisc.edu:1094/store/user/vshang/ZTo2NuNLO_Run2018/Z2JetsToNuNU_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/countEvents_12242022/tree_all.root

#prevent condor from also transferring the output files back to the submit directory:
rm *.root
