from ROOT import *
import os
import datetime
import re

gStyle.SetOptStat(0)
f=TFile.Open('testSamples/SingleElectron_2017B_ModuleCommon_2017Data_correctedPFMET.root','')
t=f.Get('Events')

hist1=TH1F('hist1','PFMET vs corrected PFMET p_{T} distribution; p_{T}^{miss} (GeV); Events',20,0,200)
hist2=TH1F('hist2','PFMET vs corrected PFMET p_{T} distribution; p_{T}^{miss} (GeV); Events',20,0,200)
t.Draw('MET_pt>>hist1')
t.Draw('METcorrected_pt>>hist2')

hist1.SetBinContent(15,hist1.GetBinContent(15)+hist1.GetBinContent(16))
hist2.SetBinContent(15,hist2.GetBinContent(15)+hist2.GetBinContent(16))

c1=TCanvas('c1','c1',800,800)
hist1.Draw('hist')
hist2.Draw('hist same')

hist1.SetLineColor(kRed)
hist2.SetLineColor(kBlue)

legend=TLegend(0.4,0.65,0.85,0.85)
legend.AddEntry(hist1,'PFMET','l')
legend.AddEntry(hist2,'Corrected PFMET','l')
legend.Draw('same')
legend.SetBorderSize(0)
legend.SetFillStyle(0)

c1.SaveAs('PFMET_vs_correctedPFMET_pt.png')

hist3=TH1F('hist3','PFMET vs corrected PFMET #phi distribution; #phi^{miss}} (GeV); Events',20,-3.2,3.2)
hist4=TH1F('hist4','PFMET vs corrected PFMET #phi distribution; #phi^{miss} (GeV); Events',20,-3.2,3.2)
t.Draw('MET_phi>>hist3')
t.Draw('METcorrected_phi>>hist4')

c2=TCanvas('c2','c2',800,800)
hist3.Draw('hist')
hist4.Draw('hist same')

hist3.SetLineColor(kRed)
hist4.SetLineColor(kBlue)

legend=TLegend(0.4,0.65,0.85,0.85)
legend.AddEntry(hist3,'PFMET','l')
legend.AddEntry(hist4,'Corrected PFMET','l')
legend.Draw('same')
legend.SetBorderSize(0)
legend.SetFillStyle(0)

c2.SaveAs('PFMET_vs_correctedPFMET_phi.png')
