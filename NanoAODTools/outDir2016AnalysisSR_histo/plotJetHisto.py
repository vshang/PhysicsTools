from ROOT import *

#Select root files here
ttbar = 'ttbarDM_Mchi1Mphi100_scalar'
tChan = 'tDM_tChan_Mchi1Mphi100_scalar'
tWChan = 'tDM_tWChan_Mchi1Mphi100_scalar'

#Set sameCanvas to True for all plots on same Canvas, False if you want seperate plots
sameCanvas = True

#t-channel events weighted by cross-section (in units of 10^-2 pb)
tChanWeight = 26.83
tWChanWeight = 5.549

#Remove stats box from histograms
gStyle.SetOptStat(0)

#Load root files 
f_ttbarAH = TFile.Open(ttbar + '_AH.root', '')
f_ttbarSL = TFile.Open(ttbar + '_SL.root', '')
f_tChanAH = TFile.Open(tChan + '_AH.root', '')
f_tChanSL = TFile.Open(tChan + '_SL.root', '')
f_tWChanAH = TFile.Open(tWChan + '_AH.root', '')
f_tWChanSL = TFile.Open(tWChan + '_SL.root', '')

#Get event trees
ttbarAH_eventTree = f_ttbarAH.Get('Events')
tChanAH_eventTree = f_tChanAH.Get('Events')
tWChanAH_eventTree = f_tWChanAH.Get('Events')

ttbarSL_eventTree = f_ttbarSL.Get('Events')
tChanSL_eventTree = f_tChanSL.Get('Events')
tWChanSL_eventTree = f_tWChanSL.Get('Events')

##Create AH njets, bjets, and MET_pt distribution plot 
##-----------------------------------------------------------------------------------------------

#Define AH njet histograms
h_ttbarAH_njets = TH1F('h_ttbarAH_njets', 'AH Jet distribution; number of AK4 jets; Normalized events', 12, 0, 12)
h_tbarAH_njets = TH1F('h_tbarAH_njets', 'AH Jet distribution; number of AK4 jets; Normalized events', 12, 0, 12)

#Define AH bjet histograms
h_ttbarAH_nbjets = TH1F('h_ttbarAH_nbjets', 'AH B-jet distribution; number of b-tagged AK4 jets; Normalized events', 5, 0, 5)
h_tbarAH_nbjets = TH1F('h_tbarAH_nbjets', 'AH B-jet distribution; number of b-tagged AK4 jets; Normalized events', 5, 0, 5)

#Define AH MET_pt histograms
h_ttbarAH_MET = TH1F('h_ttbarAH_MET', 'AH MET_pt distribution; E_{T} (GeV); Normalized events', 14, 250, 530)
h_tbarAH_MET = TH1F('h_tbarAH_MET', 'AH MET_pt distribution; E_{T} (GeV); Normalized events', 14, 250, 530)

#Fill ttbar histograms
nEntries_ttbarAH = ttbarAH_eventTree.GetEntries()
for i in range(nEntries_ttbarAH):
    ttbarAH_eventTree.GetEntry(i)
    h_ttbarAH_njets.Fill(ttbarAH_eventTree.njets)
    h_ttbarAH_nbjets.Fill(ttbarAH_eventTree.nbjets)
    h_ttbarAH_MET.Fill(ttbarAH_eventTree.MET_pt)

#Fill tbar histograms (t-channel + tW-channel), weighted by cross-section
nEntries_tChanAH = tChanAH_eventTree.GetEntries()
for i in range(nEntries_tChanAH):
    tChanAH_eventTree.GetEntry(i)
    h_tbarAH_njets.Fill(tChanAH_eventTree.njets, tChanWeight)
    h_tbarAH_nbjets.Fill(tChanAH_eventTree.nbjets, tChanWeight)
    h_tbarAH_MET.Fill(tChanAH_eventTree.MET_pt, tChanWeight)

nEntries_tWChanAH = tWChanAH_eventTree.GetEntries()
for i in range(nEntries_tChanAH):
    tWChanAH_eventTree.GetEntry(i)
    h_tbarAH_njets.Fill(tWChanAH_eventTree.njets, tWChanWeight)
    h_tbarAH_nbjets.Fill(tWChanAH_eventTree.nbjets, tWChanWeight)
    h_tbarAH_MET.Fill(tWChanAH_eventTree.MET_pt, tWChanWeight)

#Normalize histograms to unit area
h_ttbarAH_njets.Scale(1/h_ttbarAH_njets.Integral())
h_tbarAH_njets.Scale(1/h_tbarAH_njets.Integral())
h_ttbarAH_nbjets.Scale(1/h_ttbarAH_nbjets.Integral())
h_tbarAH_nbjets.Scale(1/h_tbarAH_nbjets.Integral())
h_ttbarAH_MET.Scale(1/h_ttbarAH_MET.Integral())
h_tbarAH_MET.Scale(1/h_tbarAH_MET.Integral())

#Draw AH jet distribution plot 
if sameCanvas:
    c = TCanvas('c', 'Jet distributions')
    c.Divide(3,2)
    c.cd(1)
else:
    c_njetsAH = TCanvas('c_njetsAH', 'AH jet distribution')
h_tbarAH_njets.Draw('hist')
h_ttbarAH_njets.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH_njets.SetLineColor(kRed)
h_ttbarAH_njets.SetLineStyle(9)
h_ttbarAH_njets.SetLineWidth(3)
h_ttbarAH_njets.SetFillColor(kRed)
h_ttbarAH_njets.SetFillStyle(3004)
h_ttbarAH_njets.SetMinimum(0)
h_ttbarAH_njets.SetMaximum(0.44)
#Set tbar histogram options
h_tbarAH_njets.SetLineColor(kBlue)
h_tbarAH_njets.SetLineWidth(3)
h_tbarAH_njets.SetFillColor(kBlue)
h_tbarAH_njets.SetFillStyle(3004)
h_tbarAH_njets.SetMinimum(0)
h_tbarAH_njets.SetMaximum(0.44)
#Add legend
legend_njetsAH = TLegend(0.46, 0.73, 0.75, 0.87)
legend_njetsAH.AddEntry(h_tbarAH_njets, 'Scalar, t+DM', 'l')
legend_njetsAH.AddEntry(h_ttbarAH_njets, 'Scalar, tt+DM', 'l')
legend_njetsAH.Draw('same')
legend_njetsAH.SetBorderSize(0)

#Draw AH b-jet distribution plot 
if sameCanvas:
    c.cd(2)
else:
    c_bjetsAH = TCanvas('c_bjetsAH', 'AH b-jet distribution')
h_tbarAH_nbjets.Draw('hist')
h_ttbarAH_nbjets.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH_nbjets.SetLineColor(kRed)
h_ttbarAH_nbjets.SetLineStyle(9)
h_ttbarAH_nbjets.SetLineWidth(3)
h_ttbarAH_nbjets.SetFillColor(kRed)
h_ttbarAH_nbjets.SetFillStyle(3004)
h_ttbarAH_nbjets.SetMinimum(0)
h_ttbarAH_nbjets.SetMaximum(0.84)
#Set tbar histogram options
h_tbarAH_nbjets.SetLineColor(kBlue)
h_tbarAH_nbjets.SetLineWidth(3)
h_tbarAH_nbjets.SetFillColor(kBlue)
h_tbarAH_nbjets.SetFillStyle(3004)
h_tbarAH_nbjets.SetMinimum(0)
h_tbarAH_nbjets.SetMaximum(0.84)
#Add legend
legend_nbjetsAH = TLegend(0.46, 0.73, 0.75, 0.87)
legend_nbjetsAH.AddEntry(h_tbarAH_nbjets, 'Scalar, t+DM', 'l')
legend_nbjetsAH.AddEntry(h_ttbarAH_nbjets, 'Scalar, tt+DM', 'l')
legend_nbjetsAH.Draw('same')
legend_nbjetsAH.SetBorderSize(0)

#Draw AH MET_pt distribution plot 
if sameCanvas:
    c.cd(3)
    c_3.SetLogy(1)
else:
    c_METAH = TCanvas('c_METAH', 'AH MET_pt distribution')
    c_METAH.SetLogy(1)
h_tbarAH_MET.Draw('hist')
h_ttbarAH_MET.Draw('hist same')
#Set ttbar histogram options
h_ttbarAH_MET.SetLineColor(kRed)
h_ttbarAH_MET.SetLineStyle(9)
h_ttbarAH_MET.SetLineWidth(3)
h_ttbarAH_MET.SetFillColor(kRed)
h_ttbarAH_MET.SetFillStyle(3004)
h_ttbarAH_MET.SetMinimum(0.005)
h_ttbarAH_MET.SetMaximum(1.01)
#Set tbar histogram options
h_tbarAH_MET.SetLineColor(kBlue)
h_tbarAH_MET.SetLineWidth(3)
h_tbarAH_MET.SetFillColor(kBlue)
h_tbarAH_MET.SetFillStyle(3004)
h_tbarAH_MET.SetMinimum(0.005)
h_tbarAH_MET.SetMaximum(1.01)
#Add legend
legend_METAH = TLegend(0.46, 0.73, 0.75, 0.87)
legend_METAH.AddEntry(h_tbarAH_MET, 'Scalar, t+DM', 'l')
legend_METAH.AddEntry(h_ttbarAH_MET, 'Scalar, tt+DM', 'l')
legend_METAH.Draw('same')
legend_METAH.SetBorderSize(0)


##Create SL njets, bjets, and MET_pt distribution plot 
##-----------------------------------------------------------------------------------------------

#Define SL njet histograms
h_ttbarSL_njets = TH1F('h_ttbarSL_njets', 'SL Jet distribution; number of AK4 jets; Normalized events', 12, 0, 12)
h_tbarSL_njets = TH1F('h_tbarSL_njets', 'SL Jet distribution; number of AK4 jets; Normalized events', 12, 0, 12)

#Define SL bjet histograms
h_ttbarSL_nbjets = TH1F('h_ttbarSL_nbjets', 'SL B-jet distribution; number of b-tagged AK4 jets; Normalized events', 5, 0, 5)
h_tbarSL_nbjets = TH1F('h_tbarSL_nbjets', 'SL B-jet distribution; number of b-tagged AK4 jets; Normalized events', 5, 0, 5)

#Define SL MET_pt histograms
h_ttbarSL_MET = TH1F('h_ttbarSL_MET', 'SL MET_pt distribution; E_{T} (GeV); Normalized events', 16, 160, 480)
h_tbarSL_MET = TH1F('h_tbarSL_MET', 'SL MET_pt distribution; E_{T} (GeV); Normalized events', 16, 160, 480)

#Fill ttbar histograms
nEntries_ttbarSL = ttbarSL_eventTree.GetEntries()
for i in range(nEntries_ttbarSL):
    ttbarSL_eventTree.GetEntry(i)
    h_ttbarSL_njets.Fill(ttbarSL_eventTree.njets)
    h_ttbarSL_nbjets.Fill(ttbarSL_eventTree.nbjets)
    h_ttbarSL_MET.Fill(ttbarSL_eventTree.MET_pt)

#Fill tbar histograms (t-channel + tW-channel), weighted by cross-section
nEntries_tChanSL = tChanSL_eventTree.GetEntries()
for i in range(nEntries_tChanSL):
    tChanSL_eventTree.GetEntry(i)
    h_tbarSL_njets.Fill(tChanSL_eventTree.njets, tChanWeight)
    h_tbarSL_nbjets.Fill(tChanSL_eventTree.nbjets, tChanWeight)
    h_tbarSL_MET.Fill(tChanSL_eventTree.MET_pt, tChanWeight)

nEntries_tWChanSL = tWChanSL_eventTree.GetEntries()
for i in range(nEntries_tChanSL):
    tWChanSL_eventTree.GetEntry(i)
    h_tbarSL_njets.Fill(tWChanSL_eventTree.njets, tWChanWeight)
    h_tbarSL_nbjets.Fill(tWChanSL_eventTree.nbjets, tWChanWeight)
    h_tbarSL_MET.Fill(tWChanSL_eventTree.MET_pt, tWChanWeight)

#Normalize histograms to unit area
h_ttbarSL_njets.Scale(1/h_ttbarSL_njets.Integral())
h_tbarSL_njets.Scale(1/h_tbarSL_njets.Integral())
h_ttbarSL_nbjets.Scale(1/h_ttbarSL_nbjets.Integral())
h_tbarSL_nbjets.Scale(1/h_tbarSL_nbjets.Integral())
h_ttbarSL_MET.Scale(1/h_ttbarSL_MET.Integral())
h_tbarSL_MET.Scale(1/h_tbarSL_MET.Integral())

#Draw SL jet distribution plot 
if sameCanvas:
    c.cd(4)
else:
    c_njetsSL = TCanvas('c_njetsSL', 'SL jet distribution')
h_tbarSL_njets.Draw('hist')
h_ttbarSL_njets.Draw('hist same')
#Set ttbar histogram options
h_ttbarSL_njets.SetLineColor(kRed)
h_ttbarSL_njets.SetLineStyle(9)
h_ttbarSL_njets.SetLineWidth(3)
h_ttbarSL_njets.SetFillColor(kRed)
h_ttbarSL_njets.SetFillStyle(3004)
h_ttbarSL_njets.SetMinimum(0)
h_ttbarSL_njets.SetMaximum(0.44)
#Set tbar histogram options
h_tbarSL_njets.SetLineColor(kBlue)
h_tbarSL_njets.SetLineWidth(3)
h_tbarSL_njets.SetFillColor(kBlue)
h_tbarSL_njets.SetFillStyle(3004)
h_tbarSL_njets.SetMinimum(0)
h_tbarSL_njets.SetMaximum(0.44)
#Add legend
legend_njetsSL = TLegend(0.46, 0.73, 0.75, 0.87)
legend_njetsSL.AddEntry(h_tbarSL_njets, 'Scalar, t+DM', 'l')
legend_njetsSL.AddEntry(h_ttbarSL_njets, 'Scalar, tt+DM', 'l')
legend_njetsSL.Draw('same')
legend_njetsSL.SetBorderSize(0)

#Draw SL b-jet distribution plot 
if sameCanvas:
    c.cd(5)
else:
    c_bjetsSL = TCanvas('c_bjetsSL', 'SL b-jet distribution')
h_tbarSL_nbjets.Draw('hist')
h_ttbarSL_nbjets.Draw('hist same')
#Set ttbar histogram options
h_ttbarSL_nbjets.SetLineColor(kRed)
h_ttbarSL_nbjets.SetLineStyle(9)
h_ttbarSL_nbjets.SetLineWidth(3)
h_ttbarSL_nbjets.SetFillColor(kRed)
h_ttbarSL_nbjets.SetFillStyle(3004)
h_ttbarSL_nbjets.SetMinimum(0)
h_ttbarSL_nbjets.SetMaximum(0.84)
#Set tbar histogram options
h_tbarSL_nbjets.SetLineColor(kBlue)
h_tbarSL_nbjets.SetLineWidth(3)
h_tbarSL_nbjets.SetFillColor(kBlue)
h_tbarSL_nbjets.SetFillStyle(3004)
h_tbarSL_nbjets.SetMinimum(0)
h_tbarSL_nbjets.SetMaximum(0.84)
#Add legend
legend_nbjetsSL = TLegend(0.46, 0.73, 0.75, 0.87)
legend_nbjetsSL.AddEntry(h_tbarSL_nbjets, 'Scalar, t+DM', 'l')
legend_nbjetsSL.AddEntry(h_ttbarSL_nbjets, 'Scalar, tt+DM', 'l')
legend_nbjetsSL.Draw('same')
legend_nbjetsSL.SetBorderSize(0)

#Draw SL MET_pt distribution plot 
if sameCanvas:
    c.cd(6)
    c_6.SetLogy(1)
else:
    c_METSL = TCanvas('c_METSL', 'SL MET_pt distribution')
    c_METSL.SetLogy(1)
h_tbarSL_MET.Draw('hist')
h_ttbarSL_MET.Draw('hist same')   
#Set ttbar histogram options
h_ttbarSL_MET.SetLineColor(kRed)
h_ttbarSL_MET.SetLineStyle(9)
h_ttbarSL_MET.SetLineWidth(3)
h_ttbarSL_MET.SetFillColor(kRed)
h_ttbarSL_MET.SetFillStyle(3004)
h_ttbarSL_MET.SetMinimum(0.005)
h_ttbarSL_MET.SetMaximum(1.01)
#Set tbar histogram options
h_tbarSL_MET.SetLineColor(kBlue)
h_tbarSL_MET.SetLineWidth(3)
h_tbarSL_MET.SetFillColor(kBlue)
h_tbarSL_MET.SetFillStyle(3004)
h_tbarSL_MET.SetMinimum(0.005)
h_tbarSL_MET.SetMaximum(1.01)
#Add legend
legend_METSL = TLegend(0.46, 0.73, 0.75, 0.87)
legend_METSL.AddEntry(h_tbarSL_MET, 'Scalar, t+DM', 'l')
legend_METSL.AddEntry(h_ttbarSL_MET, 'Scalar, tt+DM', 'l')
legend_METSL.Draw('same')
legend_METSL.SetBorderSize(0)
