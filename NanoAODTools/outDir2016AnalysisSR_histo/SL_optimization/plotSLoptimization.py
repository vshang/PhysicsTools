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

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Define list of suffixes to use and dictionary of files for ttbar, tChan, and tWChan
suffixList = ['_SL1e0fSR', '_SL1m0fSR', '_SL1e1fSR', '_SL1m1fSR', '_SL1e2bSR', '_SL1m2bSR']
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

    ttbarFiles['f_ttbar1' + suffix + '_MT'] = TFile.Open(ttbar1 + suffix + '_MT' + '.root', '')
    ttbarFiles['f_ttbar2' + suffix + '_MT'] = TFile.Open(ttbar2 + suffix + '_MT' + '.root', '')
    tChanFiles['f_tChan' + suffix + '_MT'] = TFile.Open(tChan + suffix + '_MT' + '.root', '')
    tWChanFiles['f_tWChan' + suffix + '_MT'] = TFile.Open(tWChan + suffix + '_MT' + '.root', '')

    ttbarFiles['f_ttbar1' + suffix + '_MTandMT2W'] = TFile.Open(ttbar1 + suffix + '_MTandMT2W' + '.root', '')
    ttbarFiles['f_ttbar2' + suffix + '_MTandMT2W'] = TFile.Open(ttbar2 + suffix + '_MTandMT2W' + '.root', '')
    tChanFiles['f_tChan' + suffix + '_MTandMT2W'] = TFile.Open(tChan + suffix + '_MTandMT2W' + '.root', '')
    tWChanFiles['f_tWChan' + suffix + '_MTandMT2W'] = TFile.Open(tWChan + suffix + '_MTandMT2W' + '.root', '')
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

    ttbarEvents['ttbar1' + suffix + '_MT_eventTree'] = ttbarFiles['f_ttbar1' + suffix + '_MT'].Get('Events')
    ttbarEvents['ttbar2' + suffix + '_MT_eventTree'] = ttbarFiles['f_ttbar2' + suffix + '_MT'].Get('Events')
    tChanEvents['tChan' + suffix + '_MT_eventTree'] = tChanFiles['f_tChan' + suffix + '_MT'].Get('Events')
    tWChanEvents['tWChan' + suffix + '_MT_eventTree'] = tWChanFiles['f_tWChan' + suffix + '_MT'].Get('Events')

    ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'] = ttbarFiles['f_ttbar1' + suffix + '_MTandMT2W'].Get('Events')
    ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'] = ttbarFiles['f_ttbar2' + suffix + '_MTandMT2W'].Get('Events')
    tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'] = tChanFiles['f_tChan' + suffix + '_MTandMT2W'].Get('Events')
    tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'] = tWChanFiles['f_tWChan' + suffix + '_MTandMT2W'].Get('Events')
print("Got event trees")

##Create SL optimization plots for nbjets = 1 signal regions
##-----------------------------------------------------------------------------------------------

print("Creating SL1b histograms..")
#Define SL nbjets = 1 histograms
h_ttbarSL1b_MT = TH1F('h_ttbarSL1b_MT', 'SL1b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)
h_tbarSL1b_MT = TH1F('h_tbarSL1b_MT', 'SL1b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)
h_ttbarSL1b_MT2W = TH1F('h_ttbarSL1b_MT2W', 'SL1b M_{T2}^{W} distribution; M_{T2}^{W} (GeV); Events', 10, 0, 480)
h_tbarSL1b_MT2W = TH1F('h_tbarSL1b_MT2W', 'SL1b M_{T2}^{W} distribution; M_{T2}^{W} (GeV); Events', 10, 0, 480)
h_ttbarSL1b_minDeltaPhi = TH1F('h_ttbarSL1b_minDeltaPhi', 'SL1b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution; min\Delta\phi(jet_{1,2}, p_{T}^{miss}); Events', 10, 0, 3)
h_tbarSL1b_minDeltaPhi = TH1F('h_tbarSL1b_minDeltaPhi', 'SL1b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution; min\Delta\phi(jet_{1,2}, p_{T}^{miss}); Events', 10, 0, 3)
h_ttbarSL1b_MTb = TH1F('h_ttbarSL1b_MTb', 'SL1b M_{T}^{b} distribution; M_{T}^{b} (GeV); Events', 20, 0, 1000)
h_tbarSL1b_MTb = TH1F('h_tbarSL1b_MTb', 'SL1b M_{T}^{b} distribution; M_{T}^{b} (GeV); Events', 20, 0, 1000)


#Fill histograms
for suffix in suffixList:
    if '2b' in suffix: continue
    #Fill h_ttbarSL1b_MT
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL1b_MT.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].M_T)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL1b_MT.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].M_T)
    #Fill h_tbarSL1b_MT
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL1b_MT.Fill(tChanEvents['tChan' + suffix + '_eventTree'].M_T)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL1b_MT.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].M_T)
    #Fill h_ttbarSL1b_MT2W
    for i in range(ttbarEvents['ttbar1' + suffix + '_MT_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_MT_eventTree'].GetEntry(i)
        h_ttbarSL1b_MT2W.Fill(ttbarEvents['ttbar1' + suffix + '_MT_eventTree'].M_T2W)
    for i in range(ttbarEvents['ttbar2' + suffix + '_MT_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_MT_eventTree'].GetEntry(i)
        h_ttbarSL1b_MT2W.Fill(ttbarEvents['ttbar2' + suffix + '_MT_eventTree'].M_T2W)
    #Fill h_tbarSL1b_MT2W
    for i in range(tChanEvents['tChan' + suffix + '_MT_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_MT_eventTree'].GetEntry(i)
        h_tbarSL1b_MT2W.Fill(tChanEvents['tChan' + suffix + '_MT_eventTree'].M_T2W)
    for i in range(tWChanEvents['tWChan' + suffix + '_MT_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_MT_eventTree'].GetEntry(i)
        h_tbarSL1b_MT2W.Fill(tWChanEvents['tWChan' + suffix + '_MT_eventTree'].M_T2W)
    #Fill h_ttbarSL1b_minDeltaPhi and h_ttbarSL1b_MTb
    for i in range(ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'].GetEntry(i)
        h_ttbarSL1b_minDeltaPhi.Fill(ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'].minDeltaPhi12)
        h_ttbarSL1b_MTb.Fill(ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'].M_Tb)
    for i in range(ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'].GetEntry(i)
        h_ttbarSL1b_minDeltaPhi.Fill(ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'].minDeltaPhi12)
        h_ttbarSL1b_MTb.Fill(ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'].M_Tb)
    #Fill h_tbarSL1b_minDeltaPhi and h_tbarSL1b_MTb
    for i in range(tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'].GetEntry(i)
        h_tbarSL1b_minDeltaPhi.Fill(tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'].minDeltaPhi12)
        h_tbarSL1b_MTb.Fill(tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'].M_Tb)
    for i in range(tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'].GetEntry(i)
        h_tbarSL1b_minDeltaPhi.Fill(tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'].minDeltaPhi12)
        h_tbarSL1b_MTb.Fill(tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'].M_Tb)

#Draw SL1b  M_T distribution plot
print("Creating SL1b M_T distribution plot...")
if sameCanvas:
    c1b = TCanvas('c1b', 'SL1b optimization distributions')
    c1b.Divide(2,2)
    c1b.cd(1)
else:
    c1b_MT = TCanvas('c1b_MT', 'SL1b M_{T} distribution')
h_tbarSL1b_MT.Draw('hist')
h_ttbarSL1b_MT.Draw('hist same')
#Set tbar histogram options
h_tbarSL1b_MT.SetLineColor(kBlue)
h_tbarSL1b_MT.SetLineWidth(1)
h_tbarSL1b_MT.SetFillColor(kBlue)
h_tbarSL1b_MT.SetFillStyle(3003)
h_tbarSL1b_MT.SetMinimum(0)
h_tbarSL1b_MT.SetMaximum(18000)
#Set ttbar histogram options
h_ttbarSL1b_MT.SetLineColor(kRed)
h_ttbarSL1b_MT.SetLineStyle(2)
h_ttbarSL1b_MT.SetLineWidth(1)
h_ttbarSL1b_MT.SetFillColor(kRed)
h_ttbarSL1b_MT.SetFillStyle(3003)
h_ttbarSL1b_MT.SetMinimum(0)
h_ttbarSL1b_MT.SetMaximum(18000)
#Add legend
legend_SL1bMT = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL1bMT.AddEntry(h_tbarSL1b_MT, 'Scalar, t+DM', 'l')
legend_SL1bMT.AddEntry(h_ttbarSL1b_MT, 'Scalar, tt+DM', 'l')
legend_SL1bMT.Draw('same')
legend_SL1bMT.SetBorderSize(0)
#Save SL1b M_T distribution plot individually if desired
if not sameCanvas:
    c1b_MT.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL1b_MT_histo" + date + ".pdf")
print("Finished creating SL1b M_T distribution plot")

#Draw SL1b M_T2^W distribution plot 
print("Creating SL1b M_T2W distribution plot...")
if sameCanvas:
    c1b.cd(2)
else:
    c1b_MT2W = TCanvas('c1b_MT2W', 'SL1b M_{T2}^W distribution')
h_tbarSL1b_MT2W.Draw('hist')
h_ttbarSL1b_MT2W.Draw('hist same')
#Set tbar histogram options
h_tbarSL1b_MT2W.SetLineColor(kBlue)
h_tbarSL1b_MT2W.SetLineWidth(1)
h_tbarSL1b_MT2W.SetFillColor(kBlue)
h_tbarSL1b_MT2W.SetFillStyle(3003)
h_tbarSL1b_MT2W.SetMinimum(0)
h_tbarSL1b_MT2W.SetMaximum(2600)
#Set ttbar histogram options
h_ttbarSL1b_MT2W.SetLineColor(kRed)
h_ttbarSL1b_MT2W.SetLineStyle(2)
h_ttbarSL1b_MT2W.SetLineWidth(1)
h_ttbarSL1b_MT2W.SetFillColor(kRed)
h_ttbarSL1b_MT2W.SetFillStyle(3003)
h_ttbarSL1b_MT2W.SetMinimum(0)
h_ttbarSL1b_MT2W.SetMaximum(2600)
#Add legend
legend_SL1bMT2W = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL1bMT2W.AddEntry(h_tbarSL1b_MT2W, 'Scalar, t+DM', 'l')
legend_SL1bMT2W.AddEntry(h_ttbarSL1b_MT2W, 'Scalar, tt+DM', 'l')
legend_SL1bMT2W.Draw('same')
legend_SL1bMT2W.SetBorderSize(0)
#Save SL1b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c1b_MT2W.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL1b_MT2W_histo" + date + ".pdf")
print("Finished creating SL1b M_T2^W distribution plot")

#Draw SL1b minDeltaPhi distribution plot 
print("Creating SL1b minDeltaPhi distribution plot...")
if sameCanvas:
    c1b.cd(3)
else:
    c1b_minDeltaPhi = TCanvas('c1b_minDeltaPhi', 'SL1b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution')
h_tbarSL1b_minDeltaPhi.Draw('hist')
h_ttbarSL1b_minDeltaPhi.Draw('hist same')
#Set tbar histogram options
h_tbarSL1b_minDeltaPhi.SetLineColor(kBlue)
h_tbarSL1b_minDeltaPhi.SetLineWidth(1)
h_tbarSL1b_minDeltaPhi.SetFillColor(kBlue)
h_tbarSL1b_minDeltaPhi.SetFillStyle(3003)
h_tbarSL1b_minDeltaPhi.SetMinimum(0)
h_tbarSL1b_minDeltaPhi.SetMaximum(1000)
#Set ttbar histogram options
h_ttbarSL1b_minDeltaPhi.SetLineColor(kRed)
h_ttbarSL1b_minDeltaPhi.SetLineStyle(2)
h_ttbarSL1b_minDeltaPhi.SetLineWidth(1)
h_ttbarSL1b_minDeltaPhi.SetFillColor(kRed)
h_ttbarSL1b_minDeltaPhi.SetFillStyle(3003)
h_ttbarSL1b_minDeltaPhi.SetMinimum(0)
h_ttbarSL1b_minDeltaPhi.SetMaximum(1000)
#Add legend
legend_SL1bminDeltaPhi = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL1bminDeltaPhi.AddEntry(h_tbarSL1b_minDeltaPhi, 'Scalar, t+DM', 'l')
legend_SL1bminDeltaPhi.AddEntry(h_ttbarSL1b_minDeltaPhi, 'Scalar, tt+DM', 'l')
legend_SL1bminDeltaPhi.Draw('same')
legend_SL1bminDeltaPhi.SetBorderSize(0)
#Save SL1b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c1b_minDeltaPhi.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL1b_minDeltaPhi_histo" + date + ".pdf")
print("Finished creating SL1b minDeltaPhi distribution plot")

#Draw SL1b MTb distribution plot 
print("Creating SL1b MTb distribution plot...")
if sameCanvas:
    c1b.cd(4)
    c1b_4.SetLogy(1)
else:
    c1b_MTb = TCanvas('c1b_MTb', 'SL1b M_{T}^{b} distribution')
    c1b_MTb.SetLogy(1)
h_tbarSL1b_MTb.Draw('hist')
h_ttbarSL1b_MTb.Draw('hist same')
#Set tbar histogram options
h_tbarSL1b_MTb.SetLineColor(kBlue)
h_tbarSL1b_MTb.SetLineWidth(1)
h_tbarSL1b_MTb.SetFillColor(kBlue)
h_tbarSL1b_MTb.SetFillStyle(3003)
h_tbarSL1b_MTb.SetMinimum(10)
h_tbarSL1b_MTb.SetMaximum(1000)
#Set ttbar histogram options
h_ttbarSL1b_MTb.SetLineColor(kRed)
h_ttbarSL1b_MTb.SetLineStyle(2)
h_ttbarSL1b_MTb.SetLineWidth(1)
h_ttbarSL1b_MTb.SetFillColor(kRed)
h_ttbarSL1b_MTb.SetFillStyle(3003)
h_ttbarSL1b_MTb.SetMinimum(10)
h_ttbarSL1b_MTb.SetMaximum(1000)
#Add legend
legend_SL1bMTb = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL1bMTb.AddEntry(h_tbarSL1b_MTb, 'Scalar, t+DM', 'l')
legend_SL1bMTb.AddEntry(h_ttbarSL1b_MTb, 'Scalar, tt+DM', 'l')
legend_SL1bMTb.Draw('same')
legend_SL1bMTb.SetBorderSize(0)
#Save SL1b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c1b_MTb.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL1b_MTb_histo" + date + ".pdf")
print("Finished creating SL1b MTb distribution plot")

#Save SL1b distribution plots on same canvas if desired
if sameCanvas:
    c1b.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL1b_allOptimizations_histo" + date + ".pdf")

##Create SL optimization plots for nbjets = 2 signal regions
##-----------------------------------------------------------------------------------------------

print("Creating SL2b histograms..")
#Define SL nbjets = 2 histograms
h_ttbarSL2b_MT = TH1F('h_ttbarSL2b_MT', 'SL2b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)
h_tbarSL2b_MT = TH1F('h_tbarSL2b_MT', 'SL2b M_{T}^{W} distribution; M_{T} (GeV); Events', 10, 0, 400)
h_ttbarSL2b_MT2W = TH1F('h_ttbarSL2b_MT2W', 'SL2b M_{T2}^{W} distribution; M_{T2}^{W} (GeV); Events', 10, 0, 480)
h_tbarSL2b_MT2W = TH1F('h_tbarSL2b_MT2W', 'SL2b M_{T2}^{W} distribution; M_{T2}^{W} (GeV); Events', 10, 0, 480)
h_ttbarSL2b_minDeltaPhi = TH1F('h_ttbarSL2b_minDeltaPhi', 'SL2b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution; min\Delta\phi(jet_{1,2}, p_{T}^{miss}); Events', 10, 0, 3)
h_tbarSL2b_minDeltaPhi = TH1F('h_tbarSL2b_minDeltaPhi', 'SL2b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution; min\Delta\phi(jet_{1,2}, p_{T}^{miss}); Events', 10, 0, 3)
h_ttbarSL2b_MTb = TH1F('h_ttbarSL2b_MTb', 'SL2b M_{T}^{b} distribution; M_{T}^{b} (GeV); Events', 20, 0, 1000)
h_tbarSL2b_MTb = TH1F('h_tbarSL2b_MTb', 'SL2b M_{T}^{b} distribution; M_{T}^{b} (GeV); Events', 20, 0, 1000)


#Fill histograms
for suffix in suffixList:
    if '2b' not in suffix: continue
    #Fill h_ttbarSL2b_MT
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL2b_MT.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].M_T)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL2b_MT.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].M_T)
    #Fill h_tbarSL2b_MT
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL2b_MT.Fill(tChanEvents['tChan' + suffix + '_eventTree'].M_T)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL2b_MT.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].M_T)
    #Fill h_ttbarSL2b_MT2W
    for i in range(ttbarEvents['ttbar1' + suffix + '_MT_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_MT_eventTree'].GetEntry(i)
        h_ttbarSL2b_MT2W.Fill(ttbarEvents['ttbar1' + suffix + '_MT_eventTree'].M_T2W)
    for i in range(ttbarEvents['ttbar2' + suffix + '_MT_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_MT_eventTree'].GetEntry(i)
        h_ttbarSL2b_MT2W.Fill(ttbarEvents['ttbar2' + suffix + '_MT_eventTree'].M_T2W)
    #Fill h_tbarSL2b_MT2W
    for i in range(tChanEvents['tChan' + suffix + '_MT_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_MT_eventTree'].GetEntry(i)
        h_tbarSL2b_MT2W.Fill(tChanEvents['tChan' + suffix + '_MT_eventTree'].M_T2W)
    for i in range(tWChanEvents['tWChan' + suffix + '_MT_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_MT_eventTree'].GetEntry(i)
        h_tbarSL2b_MT2W.Fill(tWChanEvents['tWChan' + suffix + '_MT_eventTree'].M_T2W)
    #Fill h_ttbarSL2b_minDeltaPhi and h_ttbarSL2b_MTb
    for i in range(ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'].GetEntry(i)
        h_ttbarSL2b_minDeltaPhi.Fill(ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'].minDeltaPhi12)
        h_ttbarSL2b_MTb.Fill(ttbarEvents['ttbar1' + suffix + '_MTandMT2W_eventTree'].M_Tb)
    for i in range(ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'].GetEntry(i)
        h_ttbarSL2b_minDeltaPhi.Fill(ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'].minDeltaPhi12)
        h_ttbarSL2b_MTb.Fill(ttbarEvents['ttbar2' + suffix + '_MTandMT2W_eventTree'].M_Tb)
    #Fill h_tbarSL2b_minDeltaPhi and h_tbarSL2b_MTb
    for i in range(tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'].GetEntry(i)
        h_tbarSL2b_minDeltaPhi.Fill(tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'].minDeltaPhi12)
        h_tbarSL2b_MTb.Fill(tChanEvents['tChan' + suffix + '_MTandMT2W_eventTree'].M_Tb)
    for i in range(tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'].GetEntry(i)
        h_tbarSL2b_minDeltaPhi.Fill(tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'].minDeltaPhi12)
        h_tbarSL2b_MTb.Fill(tWChanEvents['tWChan' + suffix + '_MTandMT2W_eventTree'].M_Tb)

#Draw SL2b  M_T distribution plot
print("Creating SL2b M_T distribution plot...")
if sameCanvas:
    c2b = TCanvas('c2b', 'SL2b optimization distributions')
    c2b.Divide(2,2)
    c2b.cd(1)
else:
    c2b_MT = TCanvas('c2b_MT', 'SL2b M_{T} distribution')
h_ttbarSL2b_MT.Draw('hist')
h_tbarSL2b_MT.Draw('hist same')
#Set tbar histogram options
h_tbarSL2b_MT.SetLineColor(kBlue)
h_tbarSL2b_MT.SetLineWidth(1)
h_tbarSL2b_MT.SetFillColor(kBlue)
h_tbarSL2b_MT.SetFillStyle(3003)
h_tbarSL2b_MT.SetMinimum(0)
h_tbarSL2b_MT.SetMaximum(9000)
#Set ttbar histogram options
h_ttbarSL2b_MT.SetLineColor(kRed)
h_ttbarSL2b_MT.SetLineStyle(2)
h_ttbarSL2b_MT.SetLineWidth(1)
h_ttbarSL2b_MT.SetFillColor(kRed)
h_ttbarSL2b_MT.SetFillStyle(3003)
h_ttbarSL2b_MT.SetMinimum(0)
h_ttbarSL2b_MT.SetMaximum(9000)
#Add legend
legend_SL2bMT = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL2bMT.AddEntry(h_tbarSL2b_MT, 'Scalar, t+DM', 'l')
legend_SL2bMT.AddEntry(h_ttbarSL2b_MT, 'Scalar, tt+DM', 'l')
legend_SL2bMT.Draw('same')
legend_SL2bMT.SetBorderSize(0)
#Save SL2b M_T distribution plot individually if desired
if not sameCanvas:
    c2b_MT.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL2b_MT_histo" + date + ".pdf")
print("Finished creating SL2b M_T distribution plot")

#Draw SL2b M_T2^W distribution plot 
print("Creating SL2b M_T2W distribution plot...")
if sameCanvas:
    c2b.cd(2)
else:
    c2b_MT2W = TCanvas('c2b_MT2W', 'SL2b M_{T2}^W distribution')
h_tbarSL2b_MT2W.Draw('hist')
h_ttbarSL2b_MT2W.Draw('hist same')
#Set tbar histogram options
h_tbarSL2b_MT2W.SetLineColor(kBlue)
h_tbarSL2b_MT2W.SetLineWidth(1)
h_tbarSL2b_MT2W.SetFillColor(kBlue)
h_tbarSL2b_MT2W.SetFillStyle(3003)
h_tbarSL2b_MT2W.SetMinimum(0)
h_tbarSL2b_MT2W.SetMaximum(1700)
#Set ttbar histogram options
h_ttbarSL2b_MT2W.SetLineColor(kRed)
h_ttbarSL2b_MT2W.SetLineStyle(2)
h_ttbarSL2b_MT2W.SetLineWidth(1)
h_ttbarSL2b_MT2W.SetFillColor(kRed)
h_ttbarSL2b_MT2W.SetFillStyle(3003)
h_ttbarSL2b_MT2W.SetMinimum(0)
h_ttbarSL2b_MT2W.SetMaximum(1700)
#Add legend
legend_SL2bMT2W = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL2bMT2W.AddEntry(h_tbarSL2b_MT2W, 'Scalar, t+DM', 'l')
legend_SL2bMT2W.AddEntry(h_ttbarSL2b_MT2W, 'Scalar, tt+DM', 'l')
legend_SL2bMT2W.Draw('same')
legend_SL2bMT2W.SetBorderSize(0)
#Save SL2b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c2b_MT2W.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL2b_MT2W_histo" + date + ".pdf")
print("Finished creating SL2b M_T2^W distribution plot")

#Draw SL2b minDeltaPhi distribution plot 
print("Creating SL2b minDeltaPhi distribution plot...")
if sameCanvas:
    c2b.cd(3)
else:
    c2b_minDeltaPhi = TCanvas('c2b_minDeltaPhi', 'SL2b min\Delta\phi(j_{1,2}, p_{T}^{miss}) distribution')
h_tbarSL2b_minDeltaPhi.Draw('hist')
h_ttbarSL2b_minDeltaPhi.Draw('hist same')
#Set tbar histogram options
h_tbarSL2b_minDeltaPhi.SetLineColor(kBlue)
h_tbarSL2b_minDeltaPhi.SetLineWidth(1)
h_tbarSL2b_minDeltaPhi.SetFillColor(kBlue)
h_tbarSL2b_minDeltaPhi.SetFillStyle(3003)
h_tbarSL2b_minDeltaPhi.SetMinimum(0)
h_tbarSL2b_minDeltaPhi.SetMaximum(400)
#Set ttbar histogram options
h_ttbarSL2b_minDeltaPhi.SetLineColor(kRed)
h_ttbarSL2b_minDeltaPhi.SetLineStyle(2)
h_ttbarSL2b_minDeltaPhi.SetLineWidth(1)
h_ttbarSL2b_minDeltaPhi.SetFillColor(kRed)
h_ttbarSL2b_minDeltaPhi.SetFillStyle(3003)
h_ttbarSL2b_minDeltaPhi.SetMinimum(0)
h_ttbarSL2b_minDeltaPhi.SetMaximum(400)
#Add legend
legend_SL2bminDeltaPhi = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL2bminDeltaPhi.AddEntry(h_tbarSL2b_minDeltaPhi, 'Scalar, t+DM', 'l')
legend_SL2bminDeltaPhi.AddEntry(h_ttbarSL2b_minDeltaPhi, 'Scalar, tt+DM', 'l')
legend_SL2bminDeltaPhi.Draw('same')
legend_SL2bminDeltaPhi.SetBorderSize(0)
#Save SL2b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c2b_minDeltaPhi.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL2b_minDeltaPhi_histo" + date + ".pdf")
print("Finished creating SL2b minDeltaPhi distribution plot")

#Draw SL2b MTb distribution plot 
print("Creating SL2b MTb distribution plot...")
if sameCanvas:
    c2b.cd(4)
    c2b_4.SetLogy(1)
else:
    c2b_MTb = TCanvas('c2b_MTb', 'SL2b M_{T}^{b} distribution')
    c2b_MTb.SetLogy(1)
h_tbarSL2b_MTb.Draw('hist')
h_ttbarSL2b_MTb.Draw('hist same')
#Set tbar histogram options
h_tbarSL2b_MTb.SetLineColor(kBlue)
h_tbarSL2b_MTb.SetLineWidth(1)
h_tbarSL2b_MTb.SetFillColor(kBlue)
h_tbarSL2b_MTb.SetFillStyle(3003)
h_tbarSL2b_MTb.SetMinimum(10)
h_tbarSL2b_MTb.SetMaximum(500)
#Set ttbar histogram options
h_ttbarSL2b_MTb.SetLineColor(kRed)
h_ttbarSL2b_MTb.SetLineStyle(2)
h_ttbarSL2b_MTb.SetLineWidth(1)
h_ttbarSL2b_MTb.SetFillColor(kRed)
h_ttbarSL2b_MTb.SetFillStyle(3003)
h_ttbarSL2b_MTb.SetMinimum(10)
h_ttbarSL2b_MTb.SetMaximum(500)
#Add legend
legend_SL2bMTb = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL2bMTb.AddEntry(h_tbarSL2b_MTb, 'Scalar, t+DM', 'l')
legend_SL2bMTb.AddEntry(h_ttbarSL2b_MTb, 'Scalar, tt+DM', 'l')
legend_SL2bMTb.Draw('same')
legend_SL2bMTb.SetBorderSize(0)
#Save SL2b M_T2^W distribution plot individually if desired
if not sameCanvas:
    c2b_MTb.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "SL2b_MTb_histo" + date + ".pdf")
print("Finished creating SL2b MTb distribution plot")

#Save SL2b distribution plots on same canvas if desired
if sameCanvas:
    c2b.SaveAs("outDir2016AnalysisSR_histo/SL_optimization/" + date + "/SL2b_allOptimizations_histo" + date + ".pdf")
