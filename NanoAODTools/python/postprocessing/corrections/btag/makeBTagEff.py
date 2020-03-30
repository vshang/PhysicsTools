import os, sys
from ROOT import *
from MCsampleList import *
from BTagSampleList import *

#Select settings here. Filepaths to btag histograms are contained in BTagSampleList. MCsampleList contains path to MC samples (for cross section normalization).
tagger = 'CSVv2'   # Choose between CSVv2 and DeepDSV
wp = 'medium'      # Choose between loose, medium, and tight
year = 2016        # Choose between 2016, 2017, and 2018
channel = 'ttbar'
outfilename = 'CSVv2_2016_Moriond17_eff.root'                        # name of root file that contains final btag efficiencies for selected channel
lumi = 35.9        # Set luminosity (fb^-1) for normalizing MC samples by cross section

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

#Get number of events in MC background root files 
for process in samples2016:
    for dataset in samples2016[process]:
        nevents = 0
        for filepath in samples2016[process][dataset]['filepaths']:
            samples2016[process][dataset][filepath+'_TFile'] = TFile.Open(filepath,'')
            samples2016[process][dataset][filepath+'_Events'] = samples2016[process][dataset][filepath+'_TFile'].Get('Events')
            nevents += samples2016[process][dataset][filepath+'_Events'].GetEntries()
        btagSamples2016[process][dataset]['nevents'] = nevents

# PREPARE numerator and denominator histograms per flavor
nhists  = {}
hists   = {}
histdir = channel
for flavor in ['b','c','udsg']:
    histname = '%s_%s_%s'%(tagger,flavor,wp)
    hists[histname] = None        # numerator
    hists[histname+'_all'] = None # denominator

# ADD numerator and denominator histograms
for process in btagSamples2016:
    for dataset in btagSamples2016[process]:
        for filename in btagSamples2016[process][dataset]['filepaths']:
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
                    #Weight btag histograms by MC sample cross sections
                    weight = btagSamples2016[process][dataset]['xsec']*lumi/btagSamples2016[process][dataset]['nevents']
                    hists[histname].Add(hist,weight)
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

