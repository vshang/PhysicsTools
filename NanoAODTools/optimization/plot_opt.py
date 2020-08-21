#! /usr/bin/env python

import os, multiprocessing
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph, TGraphErrors
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine

from samples import sample
from variables import variable
from selections import selection
from utils import *

from cutopt import fillCutValues
from cutopt import fillSigBkgArrays
from cutopt import searchBestCut
from cutopt import calcFOM

########## SETTINGS ##########

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="")
parser.add_option("-c", "--cut", action="store", type="string", dest="cut", default="")
parser.add_option("-n", "--norm", action="store_true", default=False, dest="norm")
parser.add_option("-e", "--eff", action="store_true", default=False, dest="efficiency")
parser.add_option("-s", "--sign", action="store_true", default=False, dest="signal")
parser.add_option("-a", "--all", action="store_true", default=False, dest="all")
parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
parser.add_option("-B", "--blind", action="store_true", default=False, dest="blind")
parser.add_option("-f", "--file", action="store", type="string", dest="file", default="")
parser.add_option("-l", "--limit", action="store_true", default=False, dest="limit")
(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)

########## SETTINGS ##########

gROOT.LoadMacro('functions.C')
gStyle.SetOptStat(0)

#NTUPLEDIR   = "/shome/clseitz/CMS/SingleTopDM/test/CMSSW_8_0_26_patch1/src/SFrame/DM/EventShapes_Dec6_Antuple/"
NTUPLEDIR   = "/mnt/t3nfs01/data01/shome/dpinna/SFrame/CMSSW_8_0_26_patch1/src/SFrame/DM/Analysis_Ntuples_fixTR/"
SIGNAL      = 1 # Signal magnification factor
RATIO       = 4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
NORM        = options.norm
PARALLELIZE = False
BLIND       = True
LUMI        = 35867

########## SAMPLES ##########
data = ["data_obs"]
#back = ["VV", "ST", "TTbarSL", "WJetsToLNu_HT", "DYJetsToNuNu_HT", "DYJetsToLL_HT", "QCD"]
back = ["QCD","DYJetsToNuNu_HT", "DYJetsToLL_HT","VV","ST","WJetsToLNu_HT","TTbarSL"]
#back = ["DYJetsToNuNu_HT", "DYJetsToLL_HT", "WJetsToLNu_HT","ST", "TTbar", "QCD"]
#back = ["TTbar", "WJetsToLNu_HT", "DYJetsToNuNu_HT","QCD"]
sign = ['tDM_MChi1_MPhi100_scalar']
#sign = ['tDM_MChi1_MPhi100', 'tDM_MChi1_MPhi300']
#sign = []
########## ######## ##########

########## ######## ##########

jobs = []

def plot(var, cut, norm=False, nm1=False):
    ### Preliminary Operations ###
    fileRead = os.path.exists(options.file)
    treeRead = not any(x==cut for x in ['0l', '1e', '1m', '2e', '2m', '1e1m', 'Gen', 'Trigger']) # Read from tree
    channel = cut
    plotdir = cut
    plotname = var
    weight = "eventWeightLumi" #*(2.2/35.9)
    isBlind = BLIND and 'SR' in channel
    showSignal = True#('SR' in channel)
    cutSplit = cut.split()
    for s in cutSplit:
        if s in selection.keys():
            plotdir = s
            cut  = cut.replace(s, selection[s])
    #if treeRead and cut in selection: cut  = cut.replace(cut, selection[cut])
    
    # Determine Primary Dataset
    pd = []
    #print cut
    if any(w in cut for w in ['1l', '1m', '2m', 'isWtoMN', 'isZtoMM', 'isTtoEM']): pd += [x for x in sample['data_obs']['files'] if 'SingleMuon' in x]
    if any(w in cut for w in ['1l', '1e', '2e', 'isWtoEN', 'isZtoEE']): pd += [x for x in sample['data_obs']['files'] if 'SingleElectron' in x]
    if any(w in cut for w in ['0l', 'isZtoNN']): pd += [x for x in sample['data_obs']['files'] if 'MET' in x]
    if len(pd)==0: raw_input("Warning: Primary Dataset not recognized, continue?")
    
    print "Plotting from", ("tree" if treeRead else "file"), var, "in", channel, "channel with:"
    print "  dataset:", pd
    print "  cut    :", cut
    print "  cut    :", weight
    
    print "preparing cut grid"
    # fillCutValues(0.,0.2,4,1,
    #               0.,0.4,4,1,
    #               0.,0.5,5,1,
    #               0.,1.,5,1,
    #               0.,0.2,4,1
    #               ) 

    # fillCutValues(0.,3.2,4,2,
    #               0.,3.2,4,1,
    #               0.,3.2,4,2,
    #               0.,3.2,4,1,
    #               0.,1.,5,2
    #               ) 

    # fillCutValues(0.,3.2,4,1,
    #               0.,3.2,4,1,
    #               0.,3.2,4,2,
    #               0.,3.2,4,2,
    #               0.,400.,4,2
    #               ) 

    fillCutValues(100.,400,30,1,
                  0.,0.,1,1,
                  0.,0.,1,1,
                  0.,0.,1,1,
                  0.,0.,1,1
                  ) 

    ### Create and fill MC histograms ###
    # Create dict
    file = {}
    tree = {}
    hist = {}
    

    #variables = ["mTb","mT2","mT","MinLepMetDPhi","MinLepJetDPhi"]
    #'mTb','topMass','WMass','HT','Dphi_topb','Dphi_Wb','Dphi_topMET','Dphi_WMET'
    #variables = ["mTb","WdRMass","topdRMass","MET_pt","MET_pt"]
    #variables = ["Dphi_topb","Dphi_Wb","Dphi_topMET","Dphi_WMET","MET_pt"]

    #variables = ["aplanarityFT","CFT","circularityFT","sphericity_AZFT","DFT"]
    #variables = ["Dphi_topb","Dphi_topMET","Dphi_Wb","Dphi_WMET","Jet1_pt/HT"]
    #variables = ["MaxBJetMetDPhi","MinBJetMetDPhi","minDphiJet1BJet","minDphiJet2BJet","pt_bjet"]
    #variables = ["cosTheta_bb","topdRMass","topdRMass","WdRMass","WdRMass"]
    #variables = ["Jet1_pt/HT","MET_pt","MET_pt","MET_pt","MET_pt"]

    #variables = ["MinDPhi12","MET_pt","MET_pt","MET_pt","MET_pt"]
    variables = ["mT2","MET_pt","MET_pt","MET_pt","MET_pt"]
    #variables = ["MET_pt","MET_pt","MET_pt","MET_pt","MET_pt"]


    ### Create and fill MC histograms ###
    for i, s in enumerate(data+back+sign):
        print "reading tree"
        tree[s] = TChain("tree")
        for j, ss in enumerate(sample[s]['files']):
            if not 'data' in s or ('data' in s and ss in pd):
                tree[s].Add(NTUPLEDIR + ss + ".root")
        
        if variable[var]['nbins']>0: hist[s] = TH1F(s, ";"+variable[var]['title']+";Events;"+('log' if variable[var]['log'] else ''), variable[var]['nbins'], variable[var]['min'], variable[var]['max'])
        else: hist[s] = TH1F(s, ";"+variable[var]['title']+";Events;"+('log' if variable[var]['log'] else ''), len(variable[var]['bins'])-1, array('f', variable[var]['bins']))
        
        hist[s].Sumw2()
        cutstring = "("+weight+")" + ("*("+cut+")" if len(cut)>0 else "")
        if '-' in s: cutstring = cutstring.replace(cut, cut + "&& nBQuarks==" + s.split('-')[1][0])

        if s.startswith("tDM") or s.startswith("ttDM"):
            isSignal=True
            fillSigBkgArrays(isSignal,variables,tree[s],weight,s,cut)
        elif not(s.startswith("data")):
            isSignal=False
            fillSigBkgArrays(isSignal,variables,tree[s],weight,s,cut)

    print "searching for best cuts"
    searchBestCut()

jobs = []

plot(options.variable, options.cut)

