from ROOT import *

#Select root files here
ttbar1 = 'outDir2016AnalysisSR/ttbarDM_Mchi1Mphi100_scalar_full1'
ttbar2 = 'outDir2016AnalysisSR/ttbarDM_Mchi1Mphi100_scalar_full2'
tChan = 'outDir2016AnalysisSR/tDM_tChan_Mchi1Mphi100_scalar_full'
tWChan = 'outDir2016AnalysisSR/tDM_tWChan_Mchi1Mphi100_scalar_full'

#Set sameCanvas to True for all nbjets = 1 on same Canvas and nbjets >= 2 plots on same Canvas, False if you want seperate plots
sameCanvas = True

#Set date for file names
date = '10042019'

#Set cross sections, lumi, and overall scale factor here
ttbarXSec = 672.3
tChanXSec = 268.3
tWChanXSec = 55.49
lumi = 35.9
scaleFactor = 20

#Set total number of events in samples here
nEvents_ttbar = 363143.0 
nEvents_tChan = 500000.0
nEvents_tWChan = 200000.0

#Weights are calculated here
ttbarWeight = ttbarXSec*lumi*scaleFactor/nEvents_ttbar
tChanWeight = tChanXSec*lumi*scaleFactor/nEvents_tChan
tWChanWeight = tWChanXSec*lumi*scaleFactor/nEvents_tWChan
#print ttbarWeight, tChanWeight, tWChanWeight

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Define list of suffixes to use and dictionary of files for ttbar, tChan, and tWChan
suffixList = ['_AH0l0fSR', '_AH0l1fSR', '_AH0l2bSR']
ttbarFiles = {}
tChanFiles = {}
tWChanFiles = {}

#Load root files 
print("Loading root files...")
for suffix in suffixList:
    ttbarFiles['f_ttbar1' + suffix] = TFile.Open(ttbar1 + suffix + '.root', '')
    ttbarFiles['f_ttbar2' + suffix] = TFile.Open(ttbar2 + suffix + '.root', '')
    tChanFiles['f_tChan' + suffix] = TFile.Open(tChan + suffix + '.root', '')
    tWChanFiles['f_tWChan' + suffix] = TFile.Open(tWChan + suffix + '.root', '')
print("Root files loaded")

#Get event trees
ttbarEvents = {}
tChanEvents = {}
tWChanEvents = {}

print("Getting event trees...")
for suffix in suffixList:
    ttbarEvents['ttbar1' + suffix + '_eventTree'] = ttbarFiles['f_ttbar1' + suffix].Get('Events')
    ttbarEvents['ttbar2' + suffix + '_eventTree'] = ttbarFiles['f_ttbar2' + suffix].Get('Events')
    tChanEvents['tChan' + suffix + '_eventTree'] = tChanFiles['f_tChan' + suffix].Get('Events')
    tWChanEvents['tWChan' + suffix + '_eventTree'] = tWChanFiles['f_tWChan' + suffix].Get('Events')
print("Got event trees")

##Create AH optimization plots for nbjets = 1 signal regions
##-----------------------------------------------------------------------------------------------

print("Creating AH1b histograms..")
#Define AH nbjets = 1 histograms
h_ttbarAH1b_minDeltaPhi = TH1F('h_ttbarAH1b_minDeltaPhi', 'AH1b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution; min\Delta\phi(jet_{1,2}, p_{T}^{miss}); Events', 15, 0, 3)
h_tbarAH1b_minDeltaPhi = TH1F('h_tbarAH1b_minDeltaPhi', 'AH1b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution; min\Delta\phi(jet_{1,2}, p_{T}^{miss}); Events', 15, 0, 3)
h_ttbarAH1b_MTb = TH1F('h_ttbarAH1b_MTb', 'AH1b M_{T}^{b} distribution; M_{T}^{b} (GeV); Events', 20, 0, 1000)
h_tbarAH1b_MTb = TH1F('h_tbarAH1b_MTb', 'AH1b M_{T}^{b} distribution; M_{T}^{b} (GeV); Events', 20, 0, 1000)


#Fill histograms
for suffix in suffixList:
    if '2b' in suffix: continue

    #Fill ttbar histograms
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarAH1b_minDeltaPhi.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].minDeltaPhi12, ttbarWeight)
        h_ttbarAH1b_MTb.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].M_Tb, ttbarWeight)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarAH1b_minDeltaPhi.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].minDeltaPhi12, ttbarWeight)
        h_ttbarAH1b_MTb.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].M_Tb, ttbarWeight)
    #Fill tbar histograms
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarAH1b_minDeltaPhi.Fill(tChanEvents['tChan' + suffix + '_eventTree'].minDeltaPhi12, tChanWeight)
        h_tbarAH1b_MTb.Fill(tChanEvents['tChan' + suffix + '_eventTree'].M_Tb, tChanWeight)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarAH1b_minDeltaPhi.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].minDeltaPhi12, tWChanWeight)
        h_tbarAH1b_MTb.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].M_Tb, tWChanWeight)

#Draw AH1b minDeltaPhi distribution plot
print("Creating AH1b minDeltaPhi distribution plot...")
if sameCanvas:
    c = TCanvas('c', 'AH optimization distributions')
    c.Divide(3,2)
    c.cd(1)
else:
    c1b_minDeltaPhi = TCanvas('c1b_MT', 'AH1b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution')
h_ttbarAH1b_minDeltaPhi.Draw('hist')
h_tbarAH1b_minDeltaPhi.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH1b_minDeltaPhi.SetLineColor(kRed)
h_ttbarAH1b_minDeltaPhi.SetLineStyle(2)
h_ttbarAH1b_minDeltaPhi.SetLineWidth(1)
h_ttbarAH1b_minDeltaPhi.SetFillColor(kRed)
h_ttbarAH1b_minDeltaPhi.SetFillStyle(3003)
h_ttbarAH1b_minDeltaPhi.SetMinimum(0)
h_ttbarAH1b_minDeltaPhi.SetMaximum(5000)
#Set tbar histogram options
h_tbarAH1b_minDeltaPhi.SetLineColor(kBlue)
h_tbarAH1b_minDeltaPhi.SetLineWidth(1)
h_tbarAH1b_minDeltaPhi.SetFillColor(kBlue)
h_tbarAH1b_minDeltaPhi.SetFillStyle(3003)
h_tbarAH1b_minDeltaPhi.SetMinimum(0)
h_tbarAH1b_minDeltaPhi.SetMaximum(5000)
#Add legend
legend_AH1bminDeltaPhi = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH1bminDeltaPhi.AddEntry(h_tbarAH1b_minDeltaPhi, 'Scalar, t+DM', 'l')
legend_AH1bminDeltaPhi.AddEntry(h_ttbarAH1b_minDeltaPhi, 'Scalar, tt+DM', 'l')
legend_AH1bminDeltaPhi.Draw('same')
legend_AH1bminDeltaPhi.SetBorderSize(0)
#Save AH1b minDeltaPhi distribution plot individually if desired
if not sameCanvas:
    c1b_minDeltaPhi.SaveAs("outDir2016AnalysisSR_histo/AH_optimization/" + date + "/AH1b_minDeltaPhi_histo" + date + ".pdf")
print("Finished creating AH1b minDeltaPhi distribution plot")

#Draw AH1b MTb distribution plot 
print("Creating MTb distribution plot...")
if sameCanvas:
    c.cd(2)
    c_2.SetLogy(1)
else:
    c1b_MTb = TCanvas('c1b_MTb', 'AH1b M_{T}^{b} distribution')
    c1b_MTb.SetLogy(1)
h_ttbarAH1b_MTb.Draw('hist')
h_tbarAH1b_MTb.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH1b_MTb.SetLineColor(kRed)
h_ttbarAH1b_MTb.SetLineStyle(2)
h_ttbarAH1b_MTb.SetLineWidth(1)
h_ttbarAH1b_MTb.SetFillColor(kRed)
h_ttbarAH1b_MTb.SetFillStyle(3003)
h_ttbarAH1b_MTb.SetMinimum(5)
h_ttbarAH1b_MTb.SetMaximum(10000)
#Set tbar histogram options
h_tbarAH1b_MTb.SetLineColor(kBlue)
h_tbarAH1b_MTb.SetLineWidth(1)
h_tbarAH1b_MTb.SetFillColor(kBlue)
h_tbarAH1b_MTb.SetFillStyle(3003)
h_tbarAH1b_MTb.SetMinimum(5)
h_tbarAH1b_MTb.SetMaximum(10000)
#Add legend
legend_AH1bMTb = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH1bMTb.AddEntry(h_tbarAH1b_MTb, 'Scalar, t+DM', 'l')
legend_AH1bMTb.AddEntry(h_ttbarAH1b_MTb, 'Scalar, tt+DM', 'l')
legend_AH1bMTb.Draw('same')
legend_AH1bMTb.SetBorderSize(0)
#Save AH1b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c1b_MTb.SaveAs("outDir2016AnalysisSR_histo/AH_optimization/" + date + "/AH1b_MTb_histo" + date + ".pdf")
print("Finished creating AH1b MTb distribution plot")

##Create AH optimization plots for nbjets = 2 signal regions
##-----------------------------------------------------------------------------------------------

print("Creating AH2b histograms..")
#Define AH nbjets = 2 histograms
h_ttbarAH2b_minDeltaPhi = TH1F('h_ttbarAH2b_minDeltaPhi', 'AH2b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution; min\Delta\phi(jet_{1,2}, p_{T}^{miss}); Events', 10, 0, 3)
h_tbarAH2b_minDeltaPhi = TH1F('h_tbarAH2b_minDeltaPhi', 'AH2b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution; min\Delta\phi(jet_{1,2}, p_{T}^{miss}); Events', 10, 0, 3)
h_ttbarAH2b_MTb = TH1F('h_ttbarAH2b_MTb', 'AH2b M_{T}^{b} distribution; M_{T}^{b} (GeV); Events', 20, 0, 1000)
h_tbarAH2b_MTb = TH1F('h_tbarAH2b_MTb', 'AH2b M_{T}^{b} distribution; M_{T}^{b} (GeV); Events', 20, 0, 1000)
h_ttbarAH2b_jet1pTHT = TH1F('h_ttbarAH2b_jet1pTHT', 'AH2b jet_{1}p_{T}/H_{T} distribution; jet_{1}p_{T}/H_{T}; Events', 20, 0, 1)
h_tbarAH2b_jet1pTHT = TH1F('h_tbarAH2b_jet1pTHT', 'AH2b jet_{1}p_{T}/H_{T} distribution; jet_{1}p_{T}/H_{T}; Events', 20, 0, 1)

#Fill histograms
for suffix in suffixList:
    if '2b' not in suffix: continue

    #Fill ttbar histograms
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarAH2b_minDeltaPhi.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].minDeltaPhi12, ttbarWeight)
        h_ttbarAH2b_MTb.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].M_Tb, ttbarWeight)
        h_ttbarAH2b_jet1pTHT.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].jet1p_TH_T, ttbarWeight)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarAH2b_minDeltaPhi.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].minDeltaPhi12, ttbarWeight)
        h_ttbarAH2b_MTb.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].M_Tb, ttbarWeight)
        h_ttbarAH2b_jet1pTHT.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].jet1p_TH_T, ttbarWeight)
    #Fill tbar histograms
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarAH2b_minDeltaPhi.Fill(tChanEvents['tChan' + suffix + '_eventTree'].minDeltaPhi12, tChanWeight)
        h_tbarAH2b_MTb.Fill(tChanEvents['tChan' + suffix + '_eventTree'].M_Tb, tChanWeight)
        h_tbarAH2b_jet1pTHT.Fill(tChanEvents['tChan' + suffix + '_eventTree'].jet1p_TH_T, tChanWeight)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarAH2b_minDeltaPhi.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].minDeltaPhi12, tWChanWeight)
        h_tbarAH2b_MTb.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].M_Tb, tWChanWeight)
        h_tbarAH2b_jet1pTHT.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].jet1p_TH_T, tWChanWeight)

#Draw AH2b minDeltaPhi distribution plot 
print("Creating minDeltaPhi distribution plot...")
if sameCanvas:
    c.cd(4)
else:
    c2b_minDeltaPhi = TCanvas('c2b_minDeltaPhi', 'AH2b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution')
h_ttbarAH2b_minDeltaPhi.Draw('hist')
h_tbarAH2b_minDeltaPhi.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH2b_minDeltaPhi.SetLineColor(kRed)
h_ttbarAH2b_minDeltaPhi.SetLineStyle(2)
h_ttbarAH2b_minDeltaPhi.SetLineWidth(1)
h_ttbarAH2b_minDeltaPhi.SetFillColor(kRed)
h_ttbarAH2b_minDeltaPhi.SetFillStyle(3003)
h_ttbarAH2b_minDeltaPhi.SetMinimum(0)
h_ttbarAH2b_minDeltaPhi.SetMaximum(3000)
#Set tbar histogram options
h_tbarAH2b_minDeltaPhi.SetLineColor(kBlue)
h_tbarAH2b_minDeltaPhi.SetLineWidth(1)
h_tbarAH2b_minDeltaPhi.SetFillColor(kBlue)
h_tbarAH2b_minDeltaPhi.SetFillStyle(3003)
h_tbarAH2b_minDeltaPhi.SetMinimum(0)
h_tbarAH2b_minDeltaPhi.SetMaximum(3000)
#Add legend
legend_AH2bminDeltaPhi = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH2bminDeltaPhi.AddEntry(h_tbarAH2b_minDeltaPhi, 'Scalar, t+DM', 'l')
legend_AH2bminDeltaPhi.AddEntry(h_ttbarAH2b_minDeltaPhi, 'Scalar, tt+DM', 'l')
legend_AH2bminDeltaPhi.Draw('same')
legend_AH2bminDeltaPhi.SetBorderSize(0)
#Save AH2b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c2b_minDeltaPhi.SaveAs("outDir2016AnalysisSR_histo/AH_optimization/" + date + "/AH2b_minDeltaPhi_histo" + date + ".pdf")
print("Finished creating AH2b minDeltaPhi distribution plot")

#Draw AH2b MTb distribution plot 
print("Creating MTb distribution plot...")
if sameCanvas:
    c.cd(5)
    c_5.SetLogy(1)
else:
    c2b_MTb = TCanvas('c2b_MTb', 'AH2b M_{T}^{b} distribution')
    c2b_MTb.SetLogy(1)
h_ttbarAH2b_MTb.Draw('hist')
h_tbarAH2b_MTb.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH2b_MTb.SetLineColor(kRed)
h_ttbarAH2b_MTb.SetLineStyle(2)
h_ttbarAH2b_MTb.SetLineWidth(1)
h_ttbarAH2b_MTb.SetFillColor(kRed)
h_ttbarAH2b_MTb.SetFillStyle(3003)
h_ttbarAH2b_MTb.SetMinimum(1)
h_ttbarAH2b_MTb.SetMaximum(10000)
#Set tbar histogram options
h_tbarAH2b_MTb.SetLineColor(kBlue)
h_tbarAH2b_MTb.SetLineWidth(1)
h_tbarAH2b_MTb.SetFillColor(kBlue)
h_tbarAH2b_MTb.SetFillStyle(3003)
h_tbarAH2b_MTb.SetMinimum(1)
h_tbarAH2b_MTb.SetMaximum(10000)
#Add legend
legend_AH2bMTb = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH2bMTb.AddEntry(h_tbarAH2b_MTb, 'Scalar, t+DM', 'l')
legend_AH2bMTb.AddEntry(h_ttbarAH2b_MTb, 'Scalar, tt+DM', 'l')
legend_AH2bMTb.Draw('same')
legend_AH2bMTb.SetBorderSize(0)
#Save AH2b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c2b_MTb.SaveAs("outDir2016AnalysisSR_histo/AH_optimization/" + date + "AH2b_MTb_histo" + date + ".pdf")
print("Finished creating AH2b MTb distribution plot")

#Draw AH2b jet1pTHT distribution plot 
print("Creating jet1pTHT distribution plot...")
if sameCanvas:
    c.cd(6)
else:
    c2b_jet1pTHT = TCanvas('c2b_jet1pTHT', 'AH2b jet_{1}p_{T}/H_{T} distribution')
h_ttbarAH2b_jet1pTHT.Draw('hist')
h_tbarAH2b_jet1pTHT.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH2b_jet1pTHT.SetLineColor(kRed)
h_ttbarAH2b_jet1pTHT.SetLineStyle(2)
h_ttbarAH2b_jet1pTHT.SetLineWidth(1)
h_ttbarAH2b_jet1pTHT.SetFillColor(kRed)
h_ttbarAH2b_jet1pTHT.SetFillStyle(3003)
h_ttbarAH2b_jet1pTHT.SetMinimum(0)
h_ttbarAH2b_jet1pTHT.SetMaximum(2000)
#Set tbar histogram options
h_tbarAH2b_jet1pTHT.SetLineColor(kBlue)
h_tbarAH2b_jet1pTHT.SetLineWidth(1)
h_tbarAH2b_jet1pTHT.SetFillColor(kBlue)
h_tbarAH2b_jet1pTHT.SetFillStyle(3003)
h_tbarAH2b_jet1pTHT.SetMinimum(0)
h_tbarAH2b_jet1pTHT.SetMaximum(2000)
#Add legend
legend_AH2bjet1pTHT = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH2bjet1pTHT.AddEntry(h_tbarAH2b_jet1pTHT, 'Scalar, t+DM', 'l')
legend_AH2bjet1pTHT.AddEntry(h_ttbarAH2b_jet1pTHT, 'Scalar, tt+DM', 'l')
legend_AH2bjet1pTHT.Draw('same')
legend_AH2bjet1pTHT.SetBorderSize(0)
#Save AH2b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c2b_jet1pTHT.SaveAs("outDir2016AnalysisSR_histo/AH_optimization/" + date + "AH2b_jet1pTHT_histo" + date + ".pdf")
print("Finished creating AH2b jet1pTHT distribution plot")

#Save AH distribution plots on same canvas if desired
if sameCanvas:
    c.SaveAs("outDir2016AnalysisSR_histo/AH_optimization/" + date + "/AH_allOptimizations_histo" + date + ".pdf")
