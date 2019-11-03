from ROOT import *

#Select root files here
ttbar1 = 'outDir2016AnalysisSR/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full1'
ttbar2 = 'outDir2016AnalysisSR/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full2'
tChan = 'outDir2016AnalysisSR/tDM_tChan/tDM_tChan_Mchi1Mphi100_scalar_full'
tWChan = 'outDir2016AnalysisSR/tDM_tWChan/tDM_tWChan_Mchi1Mphi100_scalar_full'

#Set sameCanvas to True for all nbjets = 1 on same Canvas and nbjets >= 2 plots on same Canvas, False if you want seperate plots
sameCanvas = False

#Set date for file names
date = '10302019'

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
suffixList = ['_SL1e0fSR', '_SL1m0fSR', '_SL1e1fSR', '_SL1m1fSR', '_SL1e2bSR', '_SL1m2bSR', '_AH0l0fSR', '_AH0l1fSR', '_AH0l2bSR']
ttbarFiles = {}
tChanFiles = {}
tWChanFiles = {}

#Load root files 
print("Loading root files...")
for suffix in suffixList:
    ttbarFiles['f_ttbar1' + suffix] = TFile.Open(ttbar1 + suffix + '_optimized.root', '')
    ttbarFiles['f_ttbar2' + suffix] = TFile.Open(ttbar2 + suffix + '_optimized.root', '')
    tChanFiles['f_tChan' + suffix] = TFile.Open(tChan + suffix + '_optimized.root', '')
    tWChanFiles['f_tWChan' + suffix] = TFile.Open(tWChan + suffix + '_optimized.root', '')
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

##Create SL jet distribution plots after optimized SL selections
##-----------------------------------------------------------------------------------------------

print("Creating SL jet histograms..")
#Define SL njets and nfjets histograms
h_ttbarSL1b_njets = TH1F('h_ttbarSL1b_njets', 'SL1b central jets distribution; number of AK4 jets, Events; Events', 12, 0, 12)
h_tbarSL1b_njets = TH1F('h_tbarSL1b_njets', 'SL1b central jets distribution; number of AK4 jets, Events; Events', 12, 0, 12)
h_ttbarSL1b_nfjets = TH1F('h_ttbarSL1b_nfjets', 'SL1b forward jets distribution; number of forward AK4 jets, Events; Events', 9, 0, 9)
h_tbarSL1b_nfjets = TH1F('h_tbarSL1b_nfjets', 'SL1b forward jets distribution; number of forward AK4 jets, Events; Events', 9, 0, 9)

h_ttbarSL2b_njets = TH1F('h_ttbarSL2b_njets', 'SL2b central jets distribution; number of AK4 jets, Events; Events', 12, 0, 12)
h_tbarSL2b_njets = TH1F('h_tbarSL2b_njets', 'SL2b central jets distribution; number of AK4 jets, Events; Events', 12, 0, 12)
h_ttbarSL2b_nfjets = TH1F('h_ttbarSL2b_nfjets', 'SL2b forward jets distribution; number of forward AK4 jets, Events; Events', 9, 0, 9)
h_tbarSL2b_nfjets = TH1F('h_tbarSL2b_nfjets', 'SL2b forward jets distribution; number of forward AK4 jets, Events; Events', 9, 0, 9)


#Fill SL1b histograms
for suffix in suffixList:
    if ('2b' in suffix) or ('AH' in suffix): continue

    #Fill ttbar histograms
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL1b_njets.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].njets, ttbarWeight)
        h_ttbarSL1b_nfjets.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].nfjets, ttbarWeight)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL1b_njets.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].njets, ttbarWeight)
        h_ttbarSL1b_nfjets.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].nfjets, ttbarWeight)
    #Fill tbar histograms
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL1b_njets.Fill(tChanEvents['tChan' + suffix + '_eventTree'].njets, tChanWeight)
        h_tbarSL1b_nfjets.Fill(tChanEvents['tChan' + suffix + '_eventTree'].nfjets, tChanWeight)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL1b_njets.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].njets, tWChanWeight)
        h_tbarSL1b_nfjets.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].nfjets, tWChanWeight)

#Fill SL2b histograms
for suffix in suffixList:
    if ('2b' not in suffix) or ('AH' in suffix): continue

    #Fill ttbar histograms
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL2b_njets.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].njets, ttbarWeight)
        h_ttbarSL2b_nfjets.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].nfjets, ttbarWeight)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarSL2b_njets.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].njets, ttbarWeight)
        h_ttbarSL2b_nfjets.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].nfjets, ttbarWeight)
    #Fill tbar histograms
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL2b_njets.Fill(tChanEvents['tChan' + suffix + '_eventTree'].njets, tChanWeight)
        h_tbarSL2b_nfjets.Fill(tChanEvents['tChan' + suffix + '_eventTree'].nfjets, tChanWeight)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarSL2b_njets.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].njets, tWChanWeight)
        h_tbarSL2b_nfjets.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].nfjets, tWChanWeight)

#Draw SL1b njets distribution plot
print("Creating SL1b njets distribution plot...")
if sameCanvas:
    cSL = TCanvas('cSL', 'SL jet distributions')
    cSL.Divide(2,2)
    cSL.cd(1)
else:
    cSL1b_njets = TCanvas('cSL1b_njets', 'SL1b central jets distribution')
h_ttbarSL1b_njets.Draw('hist')
h_tbarSL1b_njets.Draw('hist same')
#Set ttbar histogram options
h_ttbarSL1b_njets.SetLineColor(kRed)
h_ttbarSL1b_njets.SetLineStyle(2)
h_ttbarSL1b_njets.SetLineWidth(1)
h_ttbarSL1b_njets.SetFillColor(kRed)
h_ttbarSL1b_njets.SetFillStyle(3003)
h_ttbarSL1b_njets.SetMinimum(0)
h_ttbarSL1b_njets.SetMaximum(1500)
#Set tbar histogram options
h_tbarSL1b_njets.SetLineColor(kBlue)
h_tbarSL1b_njets.SetLineWidth(1)
h_tbarSL1b_njets.SetFillColor(kBlue)
h_tbarSL1b_njets.SetFillStyle(3003)
h_tbarSL1b_njets.SetMinimum(0)
h_tbarSL1b_njets.SetMaximum(1500)
#Add legend
legend_SL1bnjets = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL1bnjets.AddEntry(h_tbarSL1b_njets, 'Scalar, t+DM', 'l')
legend_SL1bnjets.AddEntry(h_ttbarSL1b_njets, 'Scalar, tt+DM', 'l')
legend_SL1bnjets.Draw('same')
legend_SL1bnjets.SetBorderSize(0)
#Save SL1b njets distribution plot individually if desired
if not sameCanvas:
    cSL1b_njets.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/njetsSL1b_histo" + date + ".pdf")
print("Finished creating SL1b njets distribution plot")

#Draw SL1b nfjets distribution plot
print("Creating SL1b nfjets distribution plot...")
if sameCanvas:
    cSL.cd(2)
else:
    cSL1b_nfjets = TCanvas('cSL1b_nfjets', 'SL1b forward jets distribution')
h_ttbarSL1b_nfjets.Draw('hist')
h_tbarSL1b_nfjets.Draw('hist same')
#Set ttbar histogram options
h_ttbarSL1b_nfjets.SetLineColor(kRed)
h_ttbarSL1b_nfjets.SetLineStyle(2)
h_ttbarSL1b_nfjets.SetLineWidth(1)
h_ttbarSL1b_nfjets.SetFillColor(kRed)
h_ttbarSL1b_nfjets.SetFillStyle(3003)
h_ttbarSL1b_nfjets.SetMinimum(0)
h_ttbarSL1b_nfjets.SetMaximum(2000)
#Set tbar histogram options
h_tbarSL1b_nfjets.SetLineColor(kBlue)
h_tbarSL1b_nfjets.SetLineWidth(1)
h_tbarSL1b_nfjets.SetFillColor(kBlue)
h_tbarSL1b_nfjets.SetFillStyle(3003)
h_tbarSL1b_nfjets.SetMinimum(0)
h_tbarSL1b_nfjets.SetMaximum(2000)
#Add legend
legend_SL1bnfjets = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL1bnfjets.AddEntry(h_tbarSL1b_nfjets, 'Scalar, t+DM', 'l')
legend_SL1bnfjets.AddEntry(h_ttbarSL1b_nfjets, 'Scalar, tt+DM', 'l')
legend_SL1bnfjets.Draw('same')
legend_SL1bnfjets.SetBorderSize(0)
#Save SL1b nfjets distribution plot individually if desired
if not sameCanvas:
    cSL1b_nfjets.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/nfjetsSL1b_histo" + date + ".pdf")
print("Finished creating SL1b nfjets distribution plot")

#Draw SL2b njets distribution plot
print("Creating SL2b njets distribution plot...")
if sameCanvas:
    cSL.cd(3)
else:
    cSL2b_njets = TCanvas('cSL2b_njets', 'SL2b central jets distribution')
h_ttbarSL2b_njets.Draw('hist')
h_tbarSL2b_njets.Draw('hist same')
#Set ttbar histogram options
h_ttbarSL2b_njets.SetLineColor(kRed)
h_ttbarSL2b_njets.SetLineStyle(2)
h_ttbarSL2b_njets.SetLineWidth(1)
h_ttbarSL2b_njets.SetFillColor(kRed)
h_ttbarSL2b_njets.SetFillStyle(3003)
h_ttbarSL2b_njets.SetMinimum(0)
h_ttbarSL2b_njets.SetMaximum(500)
#Set tbar histogram options
h_tbarSL2b_njets.SetLineColor(kBlue)
h_tbarSL2b_njets.SetLineWidth(1)
h_tbarSL2b_njets.SetFillColor(kBlue)
h_tbarSL2b_njets.SetFillStyle(3003)
h_tbarSL2b_njets.SetMinimum(0)
h_tbarSL2b_njets.SetMaximum(500)
#Add legend
legend_SL2bnjets = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL2bnjets.AddEntry(h_tbarSL2b_njets, 'Scalar, t+DM', 'l')
legend_SL2bnjets.AddEntry(h_ttbarSL2b_njets, 'Scalar, tt+DM', 'l')
legend_SL2bnjets.Draw('same')
legend_SL2bnjets.SetBorderSize(0)
#Save SL2b njets distribution plot individually if desired
if not sameCanvas:
    cSL2b_njets.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/njetsSL2b_histo" + date + ".pdf")
print("Finished creating SL2b njets distribution plot")

#Draw SL2b nfjets distribution plot
print("Creating SL2b nfjets distribution plot...")
if sameCanvas:
    cSL.cd(4)
else:
    cSL2b_nfjets = TCanvas('cSL2b_nfjets', 'SL2b forward jets distribution')
h_ttbarSL2b_nfjets.Draw('hist')
h_tbarSL2b_nfjets.Draw('hist same')
#Set ttbar histogram options
h_ttbarSL2b_nfjets.SetLineColor(kRed)
h_ttbarSL2b_nfjets.SetLineStyle(2)
h_ttbarSL2b_nfjets.SetLineWidth(1)
h_ttbarSL2b_nfjets.SetFillColor(kRed)
h_ttbarSL2b_nfjets.SetFillStyle(3003)
h_ttbarSL2b_nfjets.SetMinimum(0)
h_ttbarSL2b_nfjets.SetMaximum(1000)
#Set tbar histogram options
h_tbarSL2b_nfjets.SetLineColor(kBlue)
h_tbarSL2b_nfjets.SetLineWidth(1)
h_tbarSL2b_nfjets.SetFillColor(kBlue)
h_tbarSL2b_nfjets.SetFillStyle(3003)
h_tbarSL2b_nfjets.SetMinimum(0)
h_tbarSL2b_nfjets.SetMaximum(1000)
#Add legend
legend_SL2bnfjets = TLegend(0.46, 0.73, 0.75, 0.87)
legend_SL2bnfjets.AddEntry(h_tbarSL2b_nfjets, 'Scalar, t+DM', 'l')
legend_SL2bnfjets.AddEntry(h_ttbarSL2b_nfjets, 'Scalar, tt+DM', 'l')
legend_SL2bnfjets.Draw('same')
legend_SL2bnfjets.SetBorderSize(0)
#Save SL2b nfjets distribution plot individually if desired
if not sameCanvas:
    cSL2b_nfjets.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/nfjetsSL2b_histo" + date + ".pdf")
print("Finished creating SL2b nfjets distribution plot")

#Save SL optimized jet distribution plots on same canvas if desired
if sameCanvas:
    cSL.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/alljetsSL_histo" + date + ".pdf")

##Create AH jet distribution plots after optimized AH selections
##-----------------------------------------------------------------------------------------------

print("Creating AH jet histograms..")
#Define AH njets and nfjets histograms
h_ttbarAH1b_njets = TH1F('h_ttbarAH1b_njets', 'AH1b central jets distribution; number of AK4 jets, Events; Events', 12, 0, 12)
h_tbarAH1b_njets = TH1F('h_tbarAH1b_njets', 'AH1b central jets distribution; number of AK4 jets, Events; Events', 12, 0, 12)
h_ttbarAH1b_nfjets = TH1F('h_ttbarAH1b_nfjets', 'AH1b forward jets distribution; number of forward AK4 jets, Events; Events', 9, 0, 9)
h_tbarAH1b_nfjets = TH1F('h_tbarAH1b_nfjets', 'AH1b forward jets distribution; number of forward AK4 jets, Events; Events', 9, 0, 9)

h_ttbarAH2b_njets = TH1F('h_ttbarAH2b_njets', 'AH2b central jets distribution; number of AK4 jets, Events; Events', 12, 0, 12)
h_tbarAH2b_njets = TH1F('h_tbarAH2b_njets', 'AH2b central jets distribution; number of AK4 jets, Events; Events', 12, 0, 12)
h_ttbarAH2b_nfjets = TH1F('h_ttbarAH2b_nfjets', 'AH2b forward jets distribution; number of forward AK4 jets, Events; Events', 9, 0, 9)
h_tbarAH2b_nfjets = TH1F('h_tbarAH2b_nfjets', 'AH2b forward jets distribution; number of forward AK4 jets, Events; Events', 9, 0, 9)


#Fill AH1b histograms
for suffix in suffixList:
    if ('2b' in suffix) or ('SL' in suffix): continue

    #Fill ttbar histograms
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarAH1b_njets.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].njets, ttbarWeight)
        h_ttbarAH1b_nfjets.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].nfjets, ttbarWeight)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarAH1b_njets.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].njets, ttbarWeight)
        h_ttbarAH1b_nfjets.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].nfjets, ttbarWeight)
    #Fill tbar histograms
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarAH1b_njets.Fill(tChanEvents['tChan' + suffix + '_eventTree'].njets, tChanWeight)
        h_tbarAH1b_nfjets.Fill(tChanEvents['tChan' + suffix + '_eventTree'].nfjets, tChanWeight)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarAH1b_njets.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].njets, tWChanWeight)
        h_tbarAH1b_nfjets.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].nfjets, tWChanWeight)

#Fill AH2b histograms
for suffix in suffixList:
    if ('2b' not in suffix) or ('SL' in suffix): continue

    #Fill ttbar histograms
    for i in range(ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar1' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarAH2b_njets.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].njets, ttbarWeight)
        h_ttbarAH2b_nfjets.Fill(ttbarEvents['ttbar1' + suffix + '_eventTree'].nfjets, ttbarWeight)
    for i in range(ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntries()):
        ttbarEvents['ttbar2' + suffix + '_eventTree'].GetEntry(i)
        h_ttbarAH2b_njets.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].njets, ttbarWeight)
        h_ttbarAH2b_nfjets.Fill(ttbarEvents['ttbar2' + suffix + '_eventTree'].nfjets, ttbarWeight)
    #Fill tbar histograms
    for i in range(tChanEvents['tChan' + suffix + '_eventTree'].GetEntries()):
        tChanEvents['tChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarAH2b_njets.Fill(tChanEvents['tChan' + suffix + '_eventTree'].njets, tChanWeight)
        h_tbarAH2b_nfjets.Fill(tChanEvents['tChan' + suffix + '_eventTree'].nfjets, tChanWeight)
    for i in range(tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntries()):
        tWChanEvents['tWChan' + suffix + '_eventTree'].GetEntry(i)
        h_tbarAH2b_njets.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].njets, tWChanWeight)
        h_tbarAH2b_nfjets.Fill(tWChanEvents['tWChan' + suffix + '_eventTree'].nfjets, tWChanWeight)

#Draw AH1b njets distribution plot
print("Creating AH1b njets distribution plot...")
if sameCanvas:
    cAH = TCanvas('cAH', 'AH jet distributions')
    cAH.Divide(2,2)
    cAH.cd(1)
else:
    cAH1b_njets = TCanvas('cAH1b_njets', 'AH1b central jets distribution')
h_ttbarAH1b_njets.Draw('hist')
h_tbarAH1b_njets.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH1b_njets.SetLineColor(kRed)
h_ttbarAH1b_njets.SetLineStyle(2)
h_ttbarAH1b_njets.SetLineWidth(1)
h_ttbarAH1b_njets.SetFillColor(kRed)
h_ttbarAH1b_njets.SetFillStyle(3003)
h_ttbarAH1b_njets.SetMinimum(0)
h_ttbarAH1b_njets.SetMaximum(8000)
#Set tbar histogram options
h_tbarAH1b_njets.SetLineColor(kBlue)
h_tbarAH1b_njets.SetLineWidth(1)
h_tbarAH1b_njets.SetFillColor(kBlue)
h_tbarAH1b_njets.SetFillStyle(3003)
h_tbarAH1b_njets.SetMinimum(0)
h_tbarAH1b_njets.SetMaximum(8000)
#Add legend
legend_AH1bnjets = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH1bnjets.AddEntry(h_tbarAH1b_njets, 'Scalar, t+DM', 'l')
legend_AH1bnjets.AddEntry(h_ttbarAH1b_njets, 'Scalar, tt+DM', 'l')
legend_AH1bnjets.Draw('same')
legend_AH1bnjets.SetBorderSize(0)
#Save AH1b njets distribution plot individually if desired
if not sameCanvas:
    cAH1b_njets.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/njetsAH1b_histo" + date + ".pdf")
print("Finished creating AH1b njets distribution plot")

#Draw AH1b nfjets distribution plot
print("Creating AH1b nfjets distribution plot...")
if sameCanvas:
    cAH.cd(2)
else:
    cAH1b_nfjets = TCanvas('cAH1b_nfjets', 'AH1b forward jets distribution')
h_ttbarAH1b_nfjets.Draw('hist')
h_tbarAH1b_nfjets.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH1b_nfjets.SetLineColor(kRed)
h_ttbarAH1b_nfjets.SetLineStyle(2)
h_ttbarAH1b_nfjets.SetLineWidth(1)
h_ttbarAH1b_nfjets.SetFillColor(kRed)
h_ttbarAH1b_nfjets.SetFillStyle(3003)
h_ttbarAH1b_nfjets.SetMinimum(0)
h_ttbarAH1b_nfjets.SetMaximum(15000)
#Set tbar histogram options
h_tbarAH1b_nfjets.SetLineColor(kBlue)
h_tbarAH1b_nfjets.SetLineWidth(1)
h_tbarAH1b_nfjets.SetFillColor(kBlue)
h_tbarAH1b_nfjets.SetFillStyle(3003)
h_tbarAH1b_nfjets.SetMinimum(0)
h_tbarAH1b_nfjets.SetMaximum(15000)
#Add legend
legend_AH1bnfjets = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH1bnfjets.AddEntry(h_tbarAH1b_nfjets, 'Scalar, t+DM', 'l')
legend_AH1bnfjets.AddEntry(h_ttbarAH1b_nfjets, 'Scalar, tt+DM', 'l')
legend_AH1bnfjets.Draw('same')
legend_AH1bnfjets.SetBorderSize(0)
#Save AH1b nfjets distribution plot individually if desired
if not sameCanvas:
    cAH1b_nfjets.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/nfjetsAH1b_histo" + date + ".pdf")
print("Finished creating AH1b nfjets distribution plot")

#Draw AH2b njets distribution plot
print("Creating AH2b njets distribution plot...")
if sameCanvas:
    cAH.cd(3)
else:
    cAH2b_njets = TCanvas('cAH2b_njets', 'AH2b central jets distribution')
h_ttbarAH2b_njets.Draw('hist')
h_tbarAH2b_njets.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH2b_njets.SetLineColor(kRed)
h_ttbarAH2b_njets.SetLineStyle(2)
h_ttbarAH2b_njets.SetLineWidth(1)
h_ttbarAH2b_njets.SetFillColor(kRed)
h_ttbarAH2b_njets.SetFillStyle(3003)
h_ttbarAH2b_njets.SetMinimum(0)
h_ttbarAH2b_njets.SetMaximum(1500)
#Set tbar histogram options
h_tbarAH2b_njets.SetLineColor(kBlue)
h_tbarAH2b_njets.SetLineWidth(1)
h_tbarAH2b_njets.SetFillColor(kBlue)
h_tbarAH2b_njets.SetFillStyle(3003)
h_tbarAH2b_njets.SetMinimum(0)
h_tbarAH2b_njets.SetMaximum(1500)
#Add legend
legend_AH2bnjets = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH2bnjets.AddEntry(h_tbarAH2b_njets, 'Scalar, t+DM', 'l')
legend_AH2bnjets.AddEntry(h_ttbarAH2b_njets, 'Scalar, tt+DM', 'l')
legend_AH2bnjets.Draw('same')
legend_AH2bnjets.SetBorderSize(0)
#Save AH2b njets distribution plot individually if desired
if not sameCanvas:
    cAH2b_njets.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/njetsAH2b_histo" + date + ".pdf")
print("Finished creating AH2b njets distribution plot")

#Draw AH2b nfjets distribution plot
print("Creating AH2b nfjets distribution plot...")
if sameCanvas:
    cAH.cd(4)
else:
    cAH2b_nfjets = TCanvas('cAH2b_nfjets', 'AH2b forward jets distribution')
h_ttbarAH2b_nfjets.Draw('hist')
h_tbarAH2b_nfjets.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH2b_nfjets.SetLineColor(kRed)
h_ttbarAH2b_nfjets.SetLineStyle(2)
h_ttbarAH2b_nfjets.SetLineWidth(1)
h_ttbarAH2b_nfjets.SetFillColor(kRed)
h_ttbarAH2b_nfjets.SetFillStyle(3003)
h_ttbarAH2b_nfjets.SetMinimum(0)
h_ttbarAH2b_nfjets.SetMaximum(2500)
#Set tbar histogram options
h_tbarAH2b_nfjets.SetLineColor(kBlue)
h_tbarAH2b_nfjets.SetLineWidth(1)
h_tbarAH2b_nfjets.SetFillColor(kBlue)
h_tbarAH2b_nfjets.SetFillStyle(3003)
h_tbarAH2b_nfjets.SetMinimum(0)
h_tbarAH2b_nfjets.SetMaximum(2500)
#Add legend
legend_AH2bnfjets = TLegend(0.46, 0.73, 0.75, 0.87)
legend_AH2bnfjets.AddEntry(h_tbarAH2b_nfjets, 'Scalar, t+DM', 'l')
legend_AH2bnfjets.AddEntry(h_ttbarAH2b_nfjets, 'Scalar, tt+DM', 'l')
legend_AH2bnfjets.Draw('same')
legend_AH2bnfjets.SetBorderSize(0)
#Save AH2b nfjets distribution plot individually if desired
if not sameCanvas:
    cAH2b_nfjets.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/nfjetsAH2b_histo" + date + ".pdf")
print("Finished creating AH2b nfjets distribution plot")

#Save AH optimized jet distribution plots on same canvas if desired
if sameCanvas:
    cAH.SaveAs("outDir2016AnalysisSR_histo/optimized_jets/" + date + "/alljetsAH_histo" + date + ".pdf")
