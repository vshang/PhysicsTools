from ROOT import *

path = '/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/python/postprocessing/corrections/pileup/'

#Load root files
Data_2016 = TFile.Open(path + 'PileupData_GoldenJSON_Full2016.root')
Data_2017 = TFile.Open(path + 'PileupHistogram-goldenJSON-13tev-2017-99bins_withVar.root')
Data_2018 = TFile.Open(path + 'PileupHistogram-goldenJSON-13tev-2018-100bins_withVar.root')
MC_2016 = TFile.Open(path + 'pileup_profile_Summer16.root')
MC_2017 = TFile.Open(path + 'mcPileup2017.root')
MC_2018 = TFile.Open(path + 'mcPileup2018.root')

#Get pileup histograms
hist_data2016 = Data_2016.Get('pileup')
hist_data2017 = Data_2017.Get('pileup')
hist_data2018 = Data_2018.Get('pileup')
hist_MC2016 = MC_2016.Get('pu_mc')
hist_MC2017 = MC_2017.Get('pu_mc')
hist_MC2018 = MC_2018.Get('pu_mc')

#Make 2016 ratio histogram
hist_datacopy2016 = TH1F('pileup_data2016', '2016 PU Data; Pileup_nTrueInt; ', 75, 0, 75)
for i in range(76):
    weight = hist_data2016.GetBinContent(i)
    hist_datacopy2016.SetBinContent(i, weight)
hist_MCcopy2016 = TH1F('pileup_MC2016', '2016 PU MC; Pileup_nTrueInt; ', 75, 0, 75)
hist_MCcopy2016 += hist_MC2016

hist_MCcopy2016.Scale(1./hist_MCcopy2016.Integral())
hist_datacopy2016.Scale(1./hist_datacopy2016.Integral())

hist_ratio2016 = TH1F('pileup_2016', '2016 PU Data/MC; Pileup_nTrueInt; weight', 75, 0, 75)
hist_ratio2016.Divide(hist_datacopy2016, hist_MCcopy2016)
for i in range(76):
    scale = hist_MCcopy2016.GetBinContent(i)
    if scale > 0:
        hist_ratio2016.SetBinError(i, hist_datacopy2016.GetBinError(i)/scale)

#Make 2017 ratio histogram
hist_datacopy2017 = TH1F('pileup_data2017', '2017 PU Data; Pileup_nTrueInt; ', 99, 0, 99)
for i in range(100):
    weight = hist_data2017.GetBinContent(i)
    hist_datacopy2017.SetBinContent(i, weight)
hist_MCcopy2017 = TH1F('pileup_MC2017', '2017 PU MC; Pileup_nTrueInt; ', 99, 0, 99)
hist_MCcopy2017 += hist_MC2017

hist_MCcopy2017.Scale(1./hist_MCcopy2017.Integral())
hist_datacopy2017.Scale(1./hist_datacopy2017.Integral())

hist_ratio2017 = TH1F('pileup_2017', '2017 PU Data/MC; Pileup_nTrueInt; weight', 99, 0, 99)
hist_ratio2017.Divide(hist_datacopy2017, hist_MCcopy2017)
for i in range(100):
    scale = hist_MCcopy2017.GetBinContent(i)
    if scale > 0:
        hist_ratio2017.SetBinError(i, hist_datacopy2017.GetBinError(i)/scale)

#Make 2018 ratio histogram
hist_datacopy2018 = TH1F('pileup_data2018', '2018 PU Data; Pileup_nTrueInt; ', 100, 0, 100)
for i in range(101):
    weight = hist_data2018.GetBinContent(i)
    hist_datacopy2018.SetBinContent(i, weight)
hist_MCcopy2018 = TH1F('pileup_MC2018', '2018 PU MC; Pileup_nTrueInt; ', 100, 0, 100)
for i in range(101):
    weight = hist_MC2018.GetBinContent(i)
    hist_MCcopy2018.SetBinContent(i, weight)

hist_MCcopy2018.Scale(1./hist_MCcopy2018.Integral())
hist_datacopy2018.Scale(1./hist_datacopy2018.Integral())

hist_ratio2018 = TH1F('pileup_2018', '2018 PU Data/MC; Pileup_nTrueInt; weight', 100, 0, 100)
hist_ratio2018.Divide(hist_datacopy2018, hist_MCcopy2018)
for i in range(101):
    scale = hist_MCcopy2018.GetBinContent(i)
    if scale > 0:
        hist_ratio2018.SetBinError(i, hist_datacopy2018.GetBinError(i)/scale)

hist_ratio2018.SetMaximum(5)

#Make new root file and save ratio histograms
ratio_file = TFile('pileup_ratio.root','RECREATE')
hist_ratio2016.Write()
hist_ratio2017.Write()
hist_ratio2018.Write()
