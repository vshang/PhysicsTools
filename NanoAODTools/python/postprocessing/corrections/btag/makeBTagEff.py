import os, sys
from ROOT import *

#Select settings here
tagger = 'CSVv2'   # Choose between CSVv2 and DeepDSV
wp = 'medium'      # Choose between loose, medium, and tight
year = 2016        # Choose between 2016, 2017, and 2018
channel = 'ttbar'
samples=[channel+'/ttbarDM_Mchi1Mphi100_scalar_full1_btagHists.root'] # List of root files that contain btag histograms
outfilename = 'CSVv2_2016_Moriond17_eff.root'                        # name of root file that contains final btag efficiencies for selected channel


# Define helper functions for plotting
def makeTitle(tagger,wp,flavor,channel,year):
  flavor = flavor.replace('_',' ')
  if ' b ' in flavor:
    flavor = 'b quark'
  elif ' c ' in flavor:
    flavor = 'c quark'
  else:
    flavor = 'light-flavor'
  string = "%s, %s %s WP (%s, %d)"%(flavor,tagger,wp,channel.replace('tau',"#tau_{h}").replace('mu',"#mu").replace('ele',"e"),year)
  return string
  

def ensureTDirectory(file,dirname):
  dir = file.GetDirectory(dirname)
  if not dir:
    dir = file.mkdir(dirname)
    print ">>>   created directory %s in %s" % (dirname,file.GetName())
  dir.cd()
  return dir


# PREPARE numerator and denominator histograms per flavor
nhists  = {}
hists   = {}
histdir = channel
for flavor in ['b','c','udsg']:
    histname = '%s_%s_%s'%(tagger,flavor,wp)
    hists[histname] = None        # numerator
    hists[histname+'_all'] = None # denominator

# ADD numerator and denominator histograms
for filename in samples:
    print ">>>   %s"%(filename)
    file = TFile(filename,'READ')
    if not file or file.IsZombie():
        print ">>>   Warning! getBTagEfficiencies: Could not open %s. Ignoring..."%(filename)
        continue
    for histname in hists:
        histpath = "%s/%s"%(histdir,histname)
        hist = file.Get(histpath)
        if not hist:
            print ">>>   Warning! makeBTagEff: Could not open histogram '%s' in %s. Ignoring..."%(histpath,filename)        
            dir = file.Get(histdir)
            if dir: dir.ls()
            continue
        if hists[histname]==None:
            hists[histname] = hist.Clone(histname)
            hists[histname].SetDirectory(0)
            nhists[histname] = 1
        else:
            hists[histname].Add(hist)
            nhists[histname] += 1
    file.Close()

# CHECK
if len(nhists)>0:
    print ">>>   added %d MC hists:"%(sum(nhists[n] for n in nhists))
    for histname, nhist in nhists.iteritems():
        print ">>>     %-26s%2d"%(histname+':',nhist)
else:
    print ">>>   no histograms added !"

# DIVIDE and SAVE histograms
print ">>>   writing to %s..."%(outfilename)
file = TFile(outfilename,'RECREATE') 
ensureTDirectory(file,channel)
for histname, hist in hists.iteritems():
    if 'all' in histname:
        continue
    histname_all = histname+'_all'
    histname_eff = 'eff_'+histname
    print ">>>     writing %s..."%(histname)
    print ">>>     writing %s..."%(histname_all)
    print ">>>     writing %s..."%(histname_eff)
    hist_all = hists[histname_all]
    hist = hist.Clone(histname_eff)
    hist.SetTitle(makeTitle(tagger,wp,histname_eff,channel,year))
    hist.Divide(hist_all)
    hist.Write(histname_eff,TH2F.kOverwrite)
file.Close()
print ">>> "

