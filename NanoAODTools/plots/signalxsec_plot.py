from ROOT import *
gROOT.SetBatch(True)
from MCsampleList import *
from DataSampleList import *
from utils import *
import os
import datetime
import re
import math

MCSamples = samples2016

xsec_ttbarscalar = []
xsec_ttbarpseudoscalar = []

print 'Getting signal process cross sections...'
for signal in MCSamples['ttbar scalar']:
    xsec_ttbarscalar.append([MCSamples['ttbar scalar'][signal]['mphi'],MCSamples['ttbar scalar'][signal]['xsec']])
for signal in MCSamples['ttbar pseudoscalar']:
    xsec_ttbarpseudoscalar.append([MCSamples['ttbar pseudoscalar'][signal]['mphi'],MCSamples['ttbar pseudoscalar'][signal]['xsec']])
print 'Got signal process cross sections'

xsec_ttbarscalar.sort()
xsec_ttbarpseudoscalar.sort()

nPoints = len(xsec_ttbarscalar)
plot_ttbarscalar = TGraph(nPoints)
plot_ttbarscalar.SetName('ttbarscalar')
plot_ttbarpseudoscalar = TGraph(nPoints)
plot_ttbarpseudoscalar.SetName('ttbarpseudoscalar')

# for i in range(nPoints):
#     print 'xsec ttbarscalar content ' + str(i) + ': ', str(xsec_ttbarscalar[i][0]), str(xsec_ttbarscalar[i][1])
#     print 'xsec ttbarpseudoscalar content ' + str(i) + ': ', str(xsec_ttbarpseudoscalar[i][0]), str(xsec_ttbarpseudoscalar[i][1])

print 'Filling TGraphs...'
for i in range(nPoints):
    plot_ttbarscalar.SetPoint(i,xsec_ttbarscalar[i][0], xsec_ttbarscalar[i][1])
    plot_ttbarpseudoscalar.SetPoint(i,xsec_ttbarpseudoscalar[i][0], xsec_ttbarpseudoscalar[i][1])

print 'Drawing canvas...'
c = TCanvas('c', 'c', 1000, 1000)
setCanvas(c)
c.SetLogy(1)

plot_ttbarscalar.SetLineColor(kRed)
plot_ttbarscalar.SetLineStyle(kDashDotted)
plot_ttbarscalar.SetLineWidth(3)

plot_ttbarpseudoscalar.SetLineColor(kBlue)
plot_ttbarpseudoscalar.SetLineStyle(kDotted)
plot_ttbarpseudoscalar.SetLineWidth(3)

graphLabel = '; M [GeV]; #sigma [fb]'
plot_multigraph = TMultiGraph('plot_multigraph', graphLabel)
plot_multigraph.Add(plot_ttbarscalar)
plot_multigraph.Add(plot_ttbarpseudoscalar)
plot_multigraph.Draw('AC')
plot_multigraph.GetXaxis().SetLimits(50,500)
plot_multigraph.SetMinimum(10.e-2)
plot_multigraph.GetXaxis().SetTitleSize(0.05)
plot_multigraph.GetYaxis().SetTitleSize(0.05)

legend = TLegend(0.47, 0.65, 0.9, 0.85)
legend.SetNColumns(1)
legend.AddEntry('ttbarscalar', '#scale[0.75]{#font[12]{tth#rightarrow b#bar{l}#nu#bar{b}l#bar{#nu}+#chi#bar{#chi}}}', 'l')
legend.AddEntry('ttbarpseudoscalar', '#scale[0.75]{#font[12]{tta#rightarrow b#bar{l}#nu#bar{b}l#bar{#nu}+#chi#bar{#chi}}}', 'l')
legend.Draw('same')

saveDirectory = 'signalMC'
if not os.path.exists( saveDirectory + '/' ) : os.makedirs( saveDirectory + '/' )
c.SaveAs(saveDirectory + '/' + 'signalxsec2016.pdf')
