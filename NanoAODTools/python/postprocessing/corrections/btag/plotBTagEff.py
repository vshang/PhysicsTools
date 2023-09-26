import os, sys
from ROOT import *

#Select settings here.
tagger = 'DeepCSV'   # Choose between CSVv2 and DeepCSV
wp = 'medium'      # Choose between loose, medium, and tight
year = 2018       # Choose between 2016, 2017, and 2018
channel = 'ttbar'

#Remove stats box from histograms
gStyle.SetOptStat(0)

# name of root file that contains final btag efficiencies for selected channel
if year == 2016:
  filename = tagger+'_2016_Moriond17_eff.root'
elif year == 2017:
  filename = tagger+'_2017_Fall17_eff.root'
elif year == 2018:  
  filename = tagger+'_2018_Autumn18_eff.root'

for flavor in ['b','c','udsg']:
    c = TCanvas('c', 'c', 1400, 800)
    histname_eff = 'eff_%s_%s_%s'%(tagger,flavor,wp)
    file = TFile(filename,'READ')
    dir = file.GetDirectory(channel)
    hist = dir.Get(histname_eff)
    hist.Draw('Colz')

    #histogram text/settings
    hist.SetTitle('')
    title = TLatex()
    title.SetTextSize(0.045)
    title.DrawLatexNDC(.12, .91, 'CMS')
    title.SetTextSize(0.03)
    title.DrawLatexNDC(.18, .91, '#bf{#it{Preliminary}}')
    title.SetTextSize(0.03)
    title_x = .76
    title_y = .91
    if year == 2016:
      title.DrawLatexNDC(title_x, title_y, '#bf{36.3 fb^{-1} (13 TeV)}')
    elif year == 2017:
      title.DrawLatexNDC(title_x, title_y, '#bf{41.5 fb^{-1} (13 TeV)}')
    elif year == 2018:
      title.DrawLatexNDC(title_x, title_y, '#bf{59.7 fb^{-1} (13 TeV)}')

    saveDir = 'plots/'
    if not os.path.exists(saveDir): os.makedirs(saveDir)
    c.SaveAs(saveDir+filename.replace('eff.root',histname_eff)+'.pdf')
