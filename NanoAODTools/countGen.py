from ROOT import *

path = '/hdfs/store/user/vshang/WPlusJetsNLO_Run2018/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/ModuleCommonSkim_12242022/tree_all.root'

file = TFile.Open(path,'')
runsTree = file.Get('Runs')
nRuns = runsTree.GetEntries()

nevents = 0
for i in range(nRuns):
    runsTree.GetEntry(i)
    nevents += runsTree.genEventCount

print 'sumGenEvents: ', nevents
