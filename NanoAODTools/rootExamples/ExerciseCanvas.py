import ROOT

hist1 = ROOT.TH1F("hist1", "Gaussian; x value; Events", 50, -3, 3)
hist2 = ROOT.TH1F("hist2", "not Gaussian; x value; Events", 50, -3, 3)

hist1.FillRandom("gaus", 1000)
hist2.FillRandom("pol2", 500)

c = ROOT.TCanvas("canvas", "Example Canvas", 400, 400)
hist1.Draw()
hist2.Draw("same")

hist1.SetLineColor(ROOT.kRed)
hist2.SetLineColor(ROOT.kBlue)

legend = ROOT.TLegend(0.16, 0.63, 0.45, 0.91)
legend.AddEntry(hist1, "Gaussian", "l")
legend.AddEntry(hist2, "Polynomial", "l")
legend.Draw("same")

hist1b = ROOT.TH1F("hist1b", "Gaussian; x value; Events", 100, 0, 5)
hist2b = ROOT.TH1F("hist2b", "not Gaussian; x value; Events", 100, 0, 5)

hist1b.FillRandom("gaus", 1000)
hist2b.FillRandom("pol2", 500)

# hist1b = hist1.Clone()
# hist2b = hist2.Clone()

hist1b.Scale(1/hist1b.Integral())
hist2b.Scale(1/hist2b.Integral())

c2 = ROOT.TCanvas("canvas2", "Example Canvas 2", 400, 400)
hist1b.Draw()
hist2b.Draw("same")
legend2 = ROOT.TLegend(0.16, 0.63, 0.45, 0.91)
legend2.AddEntry(hist1b, "Gaussian_b", "l")
legend2.AddEntry(hist2b, "Polynomial_b", "l")
legend2.Draw("same")

hist1b.SetLineColor(ROOT.kGreen)
hist2b.SetLineColor(ROOT.kMagenta)

c.Print("canvas1.pdf")
c.SaveAs("canvas1.root")
c2.Print("canvas2.pdf")
c2.SaveAs("canvas2.root")
