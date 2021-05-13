#! /usr/bin/env python

import os, multiprocessing
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory, gErrorIgnoreLevel
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph, TGraphErrors, TRandom3
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TF1, TFormula
import numpy as np
from samples import sample
from variables import variable
from selections import selection
from utils import *

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
parser.add_option("", "--batch", action="store_true", default=True, dest="batch")
parser.add_option("", "--saveplots", action="store_true", default=True, dest="saveplots")
parser.add_option("-m", "--mode", action="store", type="string", dest="mode", default="shape")
parser.add_option("", "--sys", action="store", type="string", dest="sys", default="")
parser.add_option("-N", "--name", action="store", type="string", dest="name", default="test")

(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)

########## SETTINGS ##########
gErrorIgnoreLevel = 2001
gStyle.SetOptStat(0)
gROOT.LoadMacro('functions.C')

#NTUPLEDIR   = "/mnt/t3nfs01/data01/shome/dpinna/SFrame/CMSSW_8_0_26_patch1/src/SFrame/DM/Analysis_Ntuples_200GeV/"
NTUPLEDIR   = "/mnt/t3nfs01/data01/shome/dpinna/SFrame/CMSSW_8_0_26_patch1/src/SFrame/DM/Analysis_Ntuples_fixTR/"

SIGNAL      = 1 # Signal magnification factor
RATIO       = 4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
NORM        = options.norm
PARALLELIZE = False
#BLIND       = False
BLIND       = True
LUMI        = 35867
RESIDUAL    = False
USEGARWOOD  = True

########## SAMPLES ##########
data = ["data_obs"]

back = ["QCD","DYJetsToNuNu_HT", "DYJetsToLL_HT","VV","ST","WJetsToLNu_HT","TTbarSL"]
#back = ["QCD","DYJetsToNuNu_HT", "DYJetsToLL_HT","VV","ST","WJetsToLNu_HT","TTbarV", "TTbar2L", "TTbar1L"]

sign = ['ttDM_MChi1_MPhi10_scalar', 'ttDM_MChi1_MPhi20_scalar', 'ttDM_MChi1_MPhi50_scalar', 'ttDM_MChi1_MPhi100_scalar', 'ttDM_MChi1_MPhi200_scalar', 'ttDM_MChi1_MPhi300_scalar', 'ttDM_MChi1_MPhi500_scalar', 'tDM_MChi1_MPhi10_scalar', 'tDM_MChi1_MPhi20_scalar', 'tDM_MChi1_MPhi50_scalar', 'tDM_MChi1_MPhi100_scalar', 'tDM_MChi1_MPhi200_scalar', 'tDM_MChi1_MPhi300_scalar', 'tDM_MChi1_MPhi500_scalar', 'tttDM_MChi1_MPhi10_scalar', 'tttDM_MChi1_MPhi20_scalar', 'tttDM_MChi1_MPhi50_scalar', 'tttDM_MChi1_MPhi100_scalar', 'tttDM_MChi1_MPhi200_scalar', 'tttDM_MChi1_MPhi300_scalar', 'tttDM_MChi1_MPhi500_scalar','ttDM_MChi1_MPhi10_pseudo', 'ttDM_MChi1_MPhi20_pseudo', 'ttDM_MChi1_MPhi50_pseudo', 'ttDM_MChi1_MPhi100_pseudo', 'ttDM_MChi1_MPhi200_pseudo', 'ttDM_MChi1_MPhi300_pseudo', 'ttDM_MChi1_MPhi500_pseudo', 'tDM_MChi1_MPhi10_pseudo', 'tDM_MChi1_MPhi20_pseudo', 'tDM_MChi1_MPhi50_pseudo', 'tDM_MChi1_MPhi100_pseudo', 'tDM_MChi1_MPhi200_pseudo', 'tDM_MChi1_MPhi300_pseudo', 'tDM_MChi1_MPhi500_pseudo', 'tttDM_MChi1_MPhi10_pseudo', 'tttDM_MChi1_MPhi20_pseudo', 'tttDM_MChi1_MPhi50_pseudo', 'tttDM_MChi1_MPhi100_pseudo', 'tttDM_MChi1_MPhi200_pseudo', 'tttDM_MChi1_MPhi300_pseudo', 'tttDM_MChi1_MPhi500_pseudo']

########## ######## ##########

jobs = []

def plot(var, cut,norm=False, nm1=False):
    ### Preliminary Operations ###
    doBinned = False
    if options.mode == "binned": doBinned = True

    fileRead = os.path.exists("combinedCards_"+options.name+"/fitDiagnostics_"+options.file+".root")
    print "combinedCards_"+options.name+"/fitDiagnostics_"+options.file+".root"
    print 'fileread', fileRead
    treeRead = not any(x==cut for x in ['0l', '1e', '1m', '2e', '2m', '1e1m', 'Gen', 'Trigger'])#(var in variable.keys()) # Read from treem

    back = ["QCD","DYJetsToNuNu_HT", "DYJetsToLL_HT","VV","ST","WJetsToLNu_HT","TTbarSL"]
        
    sign = ['ttDM_MChi1_MPhi10_scalar', 'ttDM_MChi1_MPhi20_scalar', 'ttDM_MChi1_MPhi50_scalar', 'ttDM_MChi1_MPhi100_scalar', 'ttDM_MChi1_MPhi200_scalar', 'ttDM_MChi1_MPhi300_scalar', 'ttDM_MChi1_MPhi500_scalar', 'tDM_MChi1_MPhi10_scalar', 'tDM_MChi1_MPhi20_scalar', 'tDM_MChi1_MPhi50_scalar', 'tDM_MChi1_MPhi100_scalar', 'tDM_MChi1_MPhi200_scalar', 'tDM_MChi1_MPhi300_scalar', 'tDM_MChi1_MPhi500_scalar', 'tttDM_MChi1_MPhi10_scalar', 'tttDM_MChi1_MPhi20_scalar', 'tttDM_MChi1_MPhi50_scalar', 'tttDM_MChi1_MPhi100_scalar', 'tttDM_MChi1_MPhi200_scalar', 'tttDM_MChi1_MPhi300_scalar', 'tttDM_MChi1_MPhi500_scalar','ttDM_MChi1_MPhi10_pseudo', 'ttDM_MChi1_MPhi20_pseudo', 'ttDM_MChi1_MPhi50_pseudo', 'ttDM_MChi1_MPhi100_pseudo', 'ttDM_MChi1_MPhi200_pseudo', 'ttDM_MChi1_MPhi300_pseudo', 'ttDM_MChi1_MPhi500_pseudo', 'tDM_MChi1_MPhi10_pseudo', 'tDM_MChi1_MPhi20_pseudo', 'tDM_MChi1_MPhi50_pseudo', 'tDM_MChi1_MPhi100_pseudo', 'tDM_MChi1_MPhi200_pseudo', 'tDM_MChi1_MPhi300_pseudo', 'tDM_MChi1_MPhi500_pseudo', 'tttDM_MChi1_MPhi10_pseudo', 'tttDM_MChi1_MPhi20_pseudo', 'tttDM_MChi1_MPhi50_pseudo', 'tttDM_MChi1_MPhi100_pseudo', 'tttDM_MChi1_MPhi200_pseudo', 'tttDM_MChi1_MPhi300_pseudo', 'tttDM_MChi1_MPhi500_pseudo']

    #signal definition
    if fileRead:
        #sign = ['tttDM_MChi1_MPhi10_scalar','tttDM_MChi1_MPhi100_scalar'] #for postfit plot
        sign = ['tttDM_MChi1_MPhi100_scalar']
        #sign = [] #for postfit plot
    if not fileRead and not options.limit:
        sign = ['tDM_MChi1_MPhi100_scalar', 'ttDM_MChi1_MPhi100_scalar'] #for normal plotting
        ##sign = ['tDM_MChi1_MPhi200_pseudo', 'ttDM_MChi1_MPhi200_pseudo'] #for normal plotting
        #sign = ['tDM_MChi1_MPhi100_scalar','ttDM_MChi1_MPhi100_scalar','tDM_MChi1_MPhi200_scalar','ttDM_MChi1_MPhi200_scalar'] #for normal plotting
    #bkg definition
    if not(fileRead or options.limit):
        back = ["QCD","DYJetsToNuNu_HT", "DYJetsToLL_HT","VV","ST","WJetsToLNu_HT","TTbarV", "TTbar2L", "TTbar1L"]
        
    if (cut).find('>250') or (cut).startswith('AH'):#for hadronic selections
        back = ["VV","ST","TTbarV", "TTbar2L", "TTbar1L","WJetsToLNu_HT","DYJetsToNuNu_HT","DYJetsToLL_HT", "QCD",]
        if fileRead or options.limit:
            back = ["VV","ST","TTbarSL", "WJetsToLNu_HT","DYJetsToNuNu_HT", "DYJetsToLL_HT"] #for postfit or limit


    binLow = ""
    binHigh = ""
    binName = ""
    if "binned" in cut:
        binLow = cut[cut.find("LowVal")+6:cut.find("HighVal")-1]
        binHigh = cut[cut.find("HighVal")+7:]
        binName = "bin_"+binLow+"_"+binHigh
        cut = cut[:cut.find("binned")]
    useformula = False
    if 'formula' in variable[var]:
        useformula = True
    channel = cut
    plotdir = cut
    plotname = var
    weight = "eventWeightLumi" #*(2.2/35.9)
    isBlind = BLIND and ('SR' in channel or 'ps' in channel)

    if fileRead:
        print 'WARNING: is reading from post-fit file'
        isBlind = False
        options.saveplots = True
        RESIDUAL = True
        SIGNAL = 1
        RATIO = 4
    elif isBlind:
        RATIO = 0
        SIGNAL = 1
    else: 
        RATIO = 4
        SIGNAL = 1 #20
        RESIDUAL = False
    showSignal = True if 'SR' in channel else False

    #print 'SIGNAL ', SIGNAL
    cutSplit = cut.split()
    for s in cutSplit:
        if s in selection.keys():
            plotdir = s
            cut  = cut.replace(s, selection[s])
            if not binLow == "":
                cut = cut + " && " + var + " > " + binLow + " && " + var + " < " + binHigh
   #if treeRead and cut in selection: cut  = cut.replace(cut, selection[cut])
    
    # Determine Primary Dataset
    pd = []
    if any(w in cut for w in ['1l', '1m', '2m', 'isWtoMN', 'isZtoMM', 'isTtoEM']): pd += [x for x in sample['data_obs']['files'] if 'SingleMuon' in x]
    if any(w in cut for w in ['1l', '1e', '2e', 'isWtoEN', 'isZtoEE']): pd += [x for x in sample['data_obs']['files'] if 'SingleElectron' in x]
    if any(w in cut for w in ['0l', 'isZtoNN']): pd += [x for x in sample['data_obs']['files'] if 'MET' in x]
    if len(pd)==0: raw_input("Warning: Primary Dataset not recognized, continue?")
    
    print "Plotting from", ("tree" if treeRead else "file"), var, "in", channel, "channel with:"
    # print "  dataset:", pd
    print "  cut    :", cut
    print "  cut    :", weight
    
    ### Create and fill MC histograms ###
    # Create dict
    file = {}
    tree = {}
    hist = {}
    
    ### Create and fill MC histograms ###
    for i, s in enumerate(data+back+sign):
        if fileRead:
            var = 'MET_pt'
            if channel.startswith('SL'): var = 'MET_sign'
            if channel.endswith('ZR'): var = 'FakeMET_pt'
            plotname = var

            hist[s] = TH1F(s, ";"+variable[var]['title']+";Events;"+('log' if variable[var]['log'] else ''), variable[var]['nbins'], variable[var]['min'],variable[var]['max'])

            if doBinned:
                bins = np.array([])
                if 'bins' in variable[var].keys():
                    bins = np.array(variable[var]['bins'] )
                else:
                    binsize = (variable[var]['max']-variable[var]['min'])/variable[var]['nbins']
                    bins = np.arange(variable[var]['min'], variable[var]['max'], binsize) #bins = np.arange(variable[var]['min'], variable[var]['max']+binsize, binsize) 
                bins = np.append(bins, 10000)

                for i in range(0,len(bins)-1):
                    rbin =  str(bins[i]) + "_" + str(bins[i+1])
                    
                    #fileName = "combinedCards_"+options.name+"/fitDiagnostics_"+options.file+".root" if not any(t in s for t in ['data','tDM']) else "rootfiles_"+options.name+"/"+channel+"bin_"+rbin+".root"
                    fileName = "combinedCards_"+options.name+"/fitDiagnostics_"+options.file+".root" if not any(t in s for t in ['tDM']) else "combinedCards_"+options.name+"/fitDiagnostics_"+options.file+"_noSaveUnc.root"
                    
                    sdummy = s
                    if 'data' in s: sdummy = "data"
                    
                    #histName = "shapes_fit_b/"+channel+"bin_"+rbin+"/"+s if not any(t in s for t in ['data','tDM']) else s
                    histName = "shapes_fit_b/"+channel+"bin_"+rbin+"/"+sdummy if not any(t in s for t in ['tDM']) else "shapes_prefit/"+channel+"bin_"+rbin+"/"+sdummy
                   
                    file[s] = TFile(fileName, "READ")
                    tmphist = file[s].Get(histName)

                    if tmphist:
                        if 'data' in s:
                            hist[s].SetBinContent(i+1, tmphist.Eval(1))
                            hist[s].SetBinError(i+1, math.sqrt(tmphist.Eval(1)))
                        else:
                            hist[s].SetBinContent(i+1, tmphist.GetBinContent(1))
                            hist[s].SetBinError(i+1, tmphist.GetBinError(1))
                    else: 
                        hist[s].SetBinContent(i+1, 0.)
                        hist[s].SetBinError(i+1, 0.)

                    if 'data' not in s: 
                        hist[s].SetMarkerSize(0)
            else:
                fileName = "combinedCards_"+options.name+"/fitDiagnostics_"+options.file+".root" if not s=='data_obs' else "rootfiles_"+options.name+"/"+channel+binName+".root"
                histName = "shapes_fit_b/"+channel+"/"+s if not s=='data_obs' else s
                file[s] = TFile(fileName, "READ")
                tmphist = file[s].Get(histName)

                if tmphist==None:
                    tmphist = hist[back[0]].Clone(s)
                    tmphist.Reset("MICES")
                    print "Histogram", histName, "not found in file", fileName

                if s=='data_obs': hist[s] = tmphist
                else:
                    hist[s] = hist['data_obs'].Clone(s)
                    hist[s].SetMarkerSize(0)
                    for i in range(tmphist.GetNbinsX()+1): hist[s].SetBinContent(i+1, tmphist.GetBinContent(i+1))

        elif treeRead: # Project from tree
            tree[s] = TChain("tree")
            for j, ss in enumerate(sample[s]['files']):
                if not 'data' in s or ('data' in s and ss in pd):
                    tree[s].Add(NTUPLEDIR + ss + ".root")
            if not binLow == "":
                hist[s] = TH1F(s, ";"+variable[var]['title']+";Events;"+('log' if variable[var]['log'] else ''), 1, float(binLow), float(binHigh))
            elif binLow == "" and  variable[var]['nbins']>0: 
                hist[s] = TH1F(s, ";"+variable[var]['title']+";Events;"+('log' if variable[var]['log'] else ''), variable[var]['nbins'], variable[var]['min'], variable[var]['max'])
            else: 
                hist[s] = TH1F(s, ";"+variable[var]['title']+";Events;"+('log' if variable[var]['log'] else ''), len(variable[var]['bins'])-1, array('f', variable[var]['bins']))
            hist[s].Sumw2()
            redFactorString = ""
            redFactorValue = ""
            #if isBlind and 'data' in s:
            if isBlind and 'data' in s and options.limit:
                print "1/ 15 of data"
                redFactorString = " && Entry$ % 15 == 1"
            #if isBlind and 'data' not in s:
            if isBlind and 'data' not in s and options.limit:
                print "1/ 15 of MC"
                redFactorValue = " / 15"
            cutstring = "("+weight+redFactorValue+")" + ("*("+cut+redFactorString+")" if len(cut)>0 else "")
            #cutstring = ("("+cut+redFactorString+")" if len(cut)>0 else "")
            if '-' in s: cutstring = cutstring.replace(cut, cut + "&& nBQuarks==" + s.split('-')[1][0])
            if useformula == True:
                tree[s].Project(s, variable[var]['formula'], cutstring)
            else:
                tree[s].Project(s, var, cutstring)         
            if not tree[s].GetTree()==None: hist[s].SetOption("%s" % tree[s].GetTree().GetEntriesFast())
        else: # Histogram written to file
            for j, ss in enumerate(sample[s]['files']):
                if not 'data' in s or ('data' in s and ss in pd):
                    file[ss] = TFile(NTUPLEDIR + ss + ".root", "R")
                    if file[ss].IsZombie():
                        print "WARNING: file", NTUPLEDIR + ss + ".root", "does not exist"
                        continue
                    tmphist = file[ss].Get(cut+"/"+var)
                    if tmphist==None: continue
                    if not s in hist.keys(): hist[s] = tmphist
                    else: hist[s].Add(tmphist)
        if hist[s].Integral() < 0: hist[s].Scale(0)
        hist[s].SetFillColor(sample[s]['fillcolor'])
        hist[s].SetFillStyle(sample[s]['fillstyle'])
        hist[s].SetLineColor(sample[s]['linecolor'])
        hist[s].SetLineStyle(sample[s]['linestyle'])
        hist[s].SetLineWidth(sample[s]['linewidth'])
        #if 'WJetsToLNu' in s and 'SL' in channel and 'WR' in channel: hist[s].Scale(1.30)
        #if 'TTbar' in s and 'SL' in channel and 'TR' in channel: hist[s].Scale(0.91)
    
    hist['BkgSum'] = hist[back[0]].Clone("BkgSum")
    hist['BkgSum'].Reset("MICES")
    hist['BkgSum'].Sumw2()
    for i, s in enumerate(back):  hist['BkgSum'].Add(hist[s], 1)
    hist['BkgSum'].Sumw2()
    if fileRead:
        hist['PreFit'] = hist['BkgSum'].Clone("PreFit")
        if doBinned:
            for i in range(0,len(bins)-1):
                rbin =  str(bins[i]) + "_" + str(bins[i+1])
                tmphist = file[back[0]].Get("shapes_prefit/"+channel+"bin_"+rbin+"/"+"total_background")

                if tmphist: hist['PreFit'].SetBinContent(i+1, tmphist.GetBinContent(1))
                else: hist['PreFit'].SetBinContent(i+1, 0.)
        else:
            tmphist = file[back[0]].Get("shapes_prefit/"+channel+"/"+"total_background")
            for i in range(tmphist.GetNbinsX()+1): hist['PreFit'].SetBinContent(i+1, tmphist.GetBinContent(i+1))
        addOverflow(hist['PreFit'], False)
        hist['PreFit'].SetLineStyle(2)
        hist['PreFit'].SetLineColor(617)#923
        hist['PreFit'].SetLineWidth(3)
        hist['PreFit'].SetFillStyle(0)
    hist['BkgSum'].SetFillStyle(3002)
    hist['BkgSum'].SetFillColor(1)
    hist['BkgSum'].SetLineColor(1)
    hist['BkgSum'].SetLineWidth(1)
    

    # Create data and Bkg sum histograms
#    if options.blind or 'SR' in channel:
#        hist['data_obs'] = hist['BkgSum'].Clone("data_obs")
#        hist['data_obs'].Reset("MICES")
    # Set histogram style
    hist[data[0]].SetMarkerStyle(20)
    hist[data[0]].SetMarkerSize(1.25)
    
    for i, s in enumerate(data+back+sign+['BkgSum']): addOverflow(hist[s], False) # Add overflow
    for i, s in enumerate(sign): hist[s].SetLineWidth(3)
    #for i, s in enumerate(sign): sample[s]['plot'] = True#sample[s]['plot'] and s.startswith(channel[:2])
    
    
    if norm:
        for i, s in enumerate(sign):
            hist[s].Scale(hist['BkgSum'].Integral()/hist[s].Integral())
#        for i, s in enumerate(back):
#            hist[s].SetFillStyle(3005)
#            hist[s].SetLineWidth(2)
#        #for i, s in enumerate(sign):
#        #    hist[s].SetFillStyle(0)
#        if not var=="Events":
#            sfnorm = hist[data[0]].Integral()/hist['BkgSum'].Integral()
#            print "Applying SF:", sfnorm
#            for i, s in enumerate(back+['BkgSum']): hist[s].Scale(sfnorm)
    
    if SIGNAL>1:# and 'SR' in channel:
        if not var=="Events":
            for i, s in enumerate(sign):
                hist[s].Scale(SIGNAL)

    # Create stack
    bkg = THStack("Bkg", ";"+hist['BkgSum'].GetXaxis().GetTitle()+";Events")
    for i, s in enumerate(back): bkg.Add(hist[s])
    
    
    # Legend
    if fileRead:
        #leg = TLegend(0.486, 0.471, 0.899, 0.911)
        leg = TLegend(0.486, 0.471, 0.599, 0.911)
    else:
        leg = TLegend(0.47, 0.53, 0.92, 0.91)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    if fileRead:
        leg.SetNColumns(2)
    else:
        leg.SetNColumns(3)
    leg.SetTextFont(42)
    if len(data) > 0:
        leg.AddEntry(hist[data[0]], sample[data[0]]['label'], "pe")
    for i, s in reversed(list(enumerate(back))):
        leg.AddEntry(hist[s], sample[s]['label'], "f")
        #leg.AddEntry(hist[s], sample[s]['label'], "l")
    if 'PreFit' not in hist:
        leg.AddEntry(hist['BkgSum'], sample['BkgSum']['label'], "f")
    else:
        leg.AddEntry(hist['BkgSum'], "Fit unc.", "f")
        if not showSignal:
            leg.AddEntry(hist['PreFit'], sample['PreFit']['label'], "l")
    if showSignal:
        for i, s in enumerate(sign):
           if SIGNAL>1:# and 'SR' in channel:
               if sample[s]['plot']: leg.AddEntry(hist[s], '%s (x%d)' %(sample[s]['label'],SIGNAL), "l")
           else:
               leg.AddEntry(0, "", "");
               leg.AddEntry(0, "", "");
               if 'PreFit' in hist: leg.AddEntry(hist['PreFit'], sample['PreFit']['label'], "l")
               if sample[s]['plot']: leg.AddEntry(hist[s], sample[s]['label'], "l")

    if fileRead:
        leg.SetY1(0.8-leg.GetNRows()*0.06)
        leg.SetX2(0.915)
    #else:
    #    leg.SetY1(0.9-leg.GetNRows()*0.05)
    
    # --- Display ---
    c1 = TCanvas("c1", hist.values()[0].GetXaxis().GetTitle(), 800, 800 if RATIO else 600)
    
    if RATIO:
        if RESIDUAL:
            c1.Divide(1, 3)
            setFitTopPad(c1.GetPad(1), RATIO)
            setFitBotPad(c1.GetPad(2), RATIO)
            setFitResPad(c1.GetPad(3), RATIO)
            c1.GetPad(1).SetLeftMargin(0.11)
            c1.GetPad(2).SetLeftMargin(0.11)
            c1.GetPad(3).SetLeftMargin(0.11)
        else:
            c1.Divide(1, 2)
            setTopPad(c1.GetPad(1), RATIO)
            setBotPad(c1.GetPad(2), RATIO)
    c1.cd(1)
    c1.GetPad(bool(RATIO)).SetTopMargin(0.06)
    c1.GetPad(bool(RATIO)).SetRightMargin(0.05)
    c1.GetPad(bool(RATIO)).SetLeftMargin(0.11)
    c1.GetPad(bool(RATIO)).SetTicks(1, 1)
    
    log = ("log" in hist['BkgSum'].GetZaxis().GetTitle())

    if log: c1.GetPad(bool(RATIO)).SetLogy()
        
    # Draw
    #bkg.Draw("HISTe") # stack
    bkg.Draw("HIST") # stack
    hist['BkgSum'].Draw("SAME, E2") # sum of bkg
    if not isBlind and len(data) > 0 and USEGARWOOD:
        graph = fixData(hist[data[0]], USEGARWOOD)
        graph.Draw("SAME, PE")
    if 'PreFit' in hist: hist['PreFit'].Draw("SAME, HIST")
    elif not isBlind:
        hist[data[0]].Draw("SAME, PE")
    if showSignal:
        for i, s in enumerate(sign):
            if sample[s]['plot']: hist[s].Draw("SAME, HIST") # signals Normalized, hist[s].Integral()*sample[s]['weight']
    #bkg.GetYaxis().SetTitleOffset(bkg.GetYaxis().GetTitleOffset()*1.08)
    bkg.GetYaxis().SetTitleOffset(bkg.GetYaxis().GetTitleOffset()*1.15)
    
    if channel.startswith('SL'):
        bkg.SetMaximum((100. if log else 1.6)*max(bkg.GetMaximum(), hist[data[0]].GetBinContent(hist[data[0]].GetMaximumBin())+hist[data[0]].GetBinError(hist[data[0]].GetMaximumBin())))
    else:
        bkg.SetMaximum((70. if log else 1.6)*max(bkg.GetMaximum(), hist[data[0]].GetBinContent(hist[data[0]].GetMaximumBin())+hist[data[0]].GetBinError(hist[data[0]].GetMaximumBin())))
    #bkg.SetMaximum((5. if log else 1.25)*max(bkg.GetMaximum(), hist[data[0]].GetBinContent(hist[data[0]].GetMaximumBin())+hist[data[0]].GetBinError(hist[data[0]].GetMaximumBin())))

    #if len(sign) > 0 and bkg.GetMaximum() < max(hist[sign[0]].GetMaximum(), hist[sign[-1]].GetMaximum()): bkg.SetMaximum(max(hist[sign[0]].GetMaximum(), hist[sign[-1]].GetMaximum())*1.25)
    if len(sign) > 0 and bkg.GetMaximum() < max(hist[sign[0]].GetMaximum(), hist[sign[-1]].GetMaximum()): bkg.SetMaximum(max(hist[sign[0]].GetMaximum(), hist[sign[-1]].GetMaximum())*(30. if log else 1.6))
    #bkg.SetMinimum(max(min(hist['BkgSum'].GetBinContent(hist['BkgSum'].GetMinimumBin()), hist[data[0]].GetMinimum()), 2.e-1)  if log else 0.)
    bkg.SetMinimum(max(min(hist['BkgSum'].GetBinContent(hist['BkgSum'].GetMinimumBin()), hist["VV"].GetMinimum()*2), 5.e-1)  if log else 0.)
    if log:
        #bkg.GetYaxis().SetNoExponent(bkg.GetMaximum() < 1.e4)
        bkg.GetYaxis().SetNoExponent(bkg.GetMaximum() < 1.e2)
        #bkg.GetYaxis().SetMoreLogLabels(True)
    else:
        bkg.GetYaxis().SetNoExponent(bkg.GetMaximum() < 1.e3)
    
    leg.Draw()
    if fileRead and isBlind:
        drawCMS(LUMI/15., "Preliminary")
    else:
        #drawCMS(LUMI, "Preliminary")
        drawCMS(LUMI, "")
    drawRegion(channel, True)
    drawAnalysis("DM"+channel[:2])
    drawOverflow()
    
    setHistStyle(bkg, 1.2 if RATIO else 1.1)
    setHistStyle(hist['BkgSum'], 1.2 if RATIO else 1.1)
       
    if RATIO:
        c1.cd(2)
        err = hist['BkgSum'].Clone("BkgErr;")
        err.SetTitle("")
        err.GetYaxis().SetTitle("Data / Bkg")
        for i in range(1, err.GetNbinsX()+1):
            err.SetBinContent(i, 1)
            if hist['BkgSum'].GetBinContent(i) > 0:
                err.SetBinError(i, hist['BkgSum'].GetBinError(i)/hist['BkgSum'].GetBinContent(i))
        if RESIDUAL: setFitBotStyle(err)
        else: setBotStyle(err)
        errLine = err.Clone("errLine")
        errLine.SetLineWidth(1)
        errLine.SetFillStyle(0)
        res = hist[data[0]].Clone("Residues")
        res_graph = fixDataRatio(hist[data[0]], USEGARWOOD)   #### stucked here
        for i in range(0, res.GetNbinsX()+1):
            if hist['BkgSum'].GetBinContent(i) > 0: 
                res.SetBinContent(i, res.GetBinContent(i)/hist['BkgSum'].GetBinContent(i))
                #res.SetBinError(i, res.GetBinError(i)/hist['BkgSum'].GetBinContent(i))
                res.SetBinError(i, res_graph.GetErrorY(i-1)/hist['BkgSum'].GetBinContent(i))
        if RESIDUAL: setFitBotStyle(res)
        else: setBotStyle(res)
        #err.GetXaxis().SetLabelOffset(err.GetXaxis().GetLabelOffset()*5)
        #err.GetXaxis().SetTitleOffset(err.GetXaxis().GetTitleOffset()*2)
        err.GetYaxis().SetRangeUser(0.5, 1.5)
        err.Draw("E2")
        if 'PreFit' in hist:
            #respre = hist[data[0]].Clone("ResiduesPreFit")
            #respre = hist['BkgSum'].Clone("ResiduesPreFit")
            respre = hist['PreFit'].Clone("ResiduesPreFit")
            #respre.Divide(hist['PreFit'])
            respre.Divide(hist['BkgSum'])
            respre.SetLineStyle(2)
            respre.SetLineColor(617)#923
            respre.SetLineWidth(3)
            respre.SetFillStyle(0)
            respre.Draw("SAME, HIST")
        errLine.Draw("SAME, HIST")
        if not isBlind and len(data) > 0:
            res.Draw("SAME, PE0")
            #graph_res = fixDataRatio(res, USEGARWOOD)
            #graph_res.Draw("SAME, PE0")
            # if len(err.GetXaxis().GetBinLabel(1))==0: # Bin labels: not a ordinary plot
            #     drawRatio(hist['data_obs'], hist['BkgSum'])
            #     drawStat(hist['data_obs'], hist['BkgSum'])
    
    c1.Update()

    if RATIO and RESIDUAL:
        c1.cd(3)

        f2 = TF1("myf","[0]",-100000,10000);
        f2.SetLineColor(1)
        f2.SetLineWidth(1)
        f2.SetLineStyle(3)
        f2.SetParameter(0,0);
       
      #c1.SetGrid(1,0)
        resFit = hist[data[0]].Clone("Residues")
        graph_resFit = fixDataRatio(hist[data[0]], USEGARWOOD)
        resFit.Reset("MICES")
        resFit.SetTitle("")
        #resFit.GetYaxis().SetTitle("Residuals")
        #resFit.GetYaxis().SetTitle("#frac{Data - Bkg}{#sqrt{#sigma_{Data}^{2}+#sigma_{Bkg}^{2}}}")
        resFit.GetYaxis().SetTitle("#frac{Data - Bkg}{unc.}")

        for i in range(0, res.GetNbinsX()+1):
            if hist['BkgSum'].GetBinContent(i) > 0:
                #print '--->  CHECK i', i , ' : data ', hist[data[0]].GetBinError(i), 'arwood ', graph_resFit.GetErrorY(i-1)
                resFit.SetBinContent(i, (hist[data[0]].GetBinContent(i)-hist['BkgSum'].GetBinContent(i))/( math.sqrt( math.pow(hist['BkgSum'].GetBinError(i),2)+math.pow(graph_resFit.GetErrorY(i-1),2)) ) )
        setFitResStyle(resFit)
        resFit.SetLineColor(15)
        resFit.SetFillColor(15)
        resFit.SetFillStyle(1001)
        resFit.Draw("HIST")
        f2.Draw("same")
        resFit.Draw("SAME,HIST")
        resFitLine = resFit.Clone("resFitLine")
        resFitLine.SetLineWidth(1)
        resFitLine.SetFillStyle(0)
        resFitLine.Draw("SAME, HIST")

    c1.Update()
    
    ##if gROOT.IsBatch() and options.saveplots: # and (treeRead and channel in selection.keys()):
    if options.saveplots: # and (treeRead and channel in selection.keys()):
        AddString = ""
        if not os.path.exists("plots_"+options.name+"/"+plotdir): os.makedirs("plots_"+options.name+"/"+plotdir)
        if fileRead:
            if RESIDUAL: AddString = "_PostFit_Residual"
            else:  AddString = "_PostFit"
            # c1.Print("plots_"+options.name+"/"+plotdir+"/"+plotname+binName+AddString+".root")
        c1.Print("plots_"+options.name+"/"+plotdir+"/"+plotname+binName+AddString+".pdf")
        # c1.Print("plots_"+options.name+"/"+plotdir+"_"+plotname+binName+AddString+".pdf")
        # c1.Print("plots_"+options.name+"/"+plotdir+"_"+plotname+binName+AddString+".root")
    
    # print table
    # if fileRead:
    #     graph = fixData(hist[data[0]], USEGARWOOD)
    printTable(hist, sign)
    
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")

    if gROOT.IsBatch() and not fileRead and (var == 'MET_pt' or (channel.startswith('SL') and var == 'MET_sign') or (channel.endswith('ZR') and var == 'FakeMET_pt')):
        saveHist(hist, channel+binName)

    
########## ######## ##########

def addSys(var, cut, sys):
    binLow = ""
    binHigh = ""
    binName = ""
    if "binned" in cut:
        binLow = cut[cut.find("LowVal")+6:cut.find("HighVal")-1]
        binHigh = cut[cut.find("HighVal")+7:]
        binName = "bin_"+binLow+"_"+binHigh
        cut = cut[:cut.find("binned")]

    channel = cut
    weight = "eventWeightLumi" #+ ("*stitchWeight" if any([x for x in back if x.endswith('b')]) else "")
    cut  = selection[cut]
    if not binLow == "":
        cut = cut + " && " + var + " > " + binLow + " && " + var + " < " + binHigh

    weightUp = weightDown = weight
    varUp = varDown = var
    cutUp = cutDown = cut

    # Systematics
    if sys=='CMS_scale_j':
        if var!="MET_sign": varUp = var.replace('pt', 'ptScaleUp')
        else: varUp = var.replace('sign', 'signScaleUp')
        if var!="MET_sign": varDown = var.replace('pt', 'ptScaleDown')
        else: varDown = var.replace('sign', 'signScaleDown')

        cutUp = cut.replace('MET_pt', 'MET_ptScaleUp')
        cutUp = cutUp.replace('Jets', 'JetsScaleUp')
        cutUp = cutUp.replace('12', '12ScaleUp')
        cutUp = cutUp.replace('mT>', 'mTScaleUp>')
        cutUp = cutUp.replace('mT2', 'mT2ScaleUp')

        cutDown = cut.replace('MET_pt', 'MET_ptScaleDown')
        cutDown = cutDown.replace('Jets', 'JetsScaleDown')
        cutDown = cutDown.replace('12', '12ScaleDown')
        cutDown = cutDown.replace('mT>', 'mTScaleDown>')
        cutDown = cutDown.replace('mT2', 'mT2ScaleDown')
    elif sys=='CMS_res_j':
        if var!="MET_sign": varUp = var.replace('pt', 'ptResUp')
        else: varUp = var.replace('sign', 'signResUp')
        if var!="MET_sign": varDown = var.replace('pt', 'ptResDown')
        else: varDown = var.replace('sign', 'signResDown')

        cutUp = cut.replace('MET_pt', 'MET_ptResUp')
        cutUp = cutUp.replace('Jets', 'JetsResUp')
        cutUp = cutUp.replace('12', '12ResUp')
        cutUp = cutUp.replace('mT>', 'mTResUp>')
        cutUp = cutUp.replace('mT2', 'mT2ResUp')

        cutDown = cut.replace('MET_pt', 'MET_ptResDown')
        cutDown = cutDown.replace('Jets', 'JetsResDown')
        cutDown = cutDown.replace('12', '12ResDown')
        cutDown = cutDown.replace('mT>', 'mTResDown>')
        cutDown = cutDown.replace('mT2', 'mT2ResDown')

    elif sys=='CMS_WqcdWeightRen': weightUp += "*WqcdWeightRenUp/WqcdWeight"; weightDown += "*WqcdWeightRenDown/WqcdWeight"
    elif sys=='CMS_WqcdWeightFac': weightUp += "*WqcdWeightFacUp/WqcdWeight"; weightDown += "*WqcdWeightFacDown/WqcdWeight"
    elif sys=='CMS_ZqcdWeightRen': weightUp += "*ZqcdWeightRenUp/ZqcdWeight"; weightDown += "*ZqcdWeightRenDown/ZqcdWeight"
    elif sys=='CMS_ZqcdWeightFac': weightUp += "*ZqcdWeightFacUp/ZqcdWeight"; weightDown += "*ZqcdWeightFacDown/ZqcdWeight"
    elif sys=='CMS_WewkWeight': weightUp += "/WewkWeight"; weightDown += ""
    elif sys=='CMS_ZewkWeight': weightUp += "/ZewkWeight"; weightDown += ""

    elif sys=='CMS_pdf': weightUp += "*PDFWeightUp/eventWeight"; weightDown += "*PDFWeightDown/eventWeight"

    elif sys=='CMS_HF': weightUp += "*1.20"; weightDown += "*0.8"
    #new HF
    elif sys=='CMS_HF_V': weightUp += "*(nBQuarks>=1 ? 1.2 : 1.)"; weightDown += "*(nBQuarks>=1 ? 0.8 : 1.)"
    elif sys=='CMS_HF_W': weightUp += "*(nBQuarks>=1 ? 1.2 : 1.)"; weightDown += "*(nBQuarks>=1 ? 0.8 : 1.)"
    elif sys=='CMS_HF_Z': weightUp += "*(nBQuarks>=1 ? 1.2 : 1.)"; weightDown += "*(nBQuarks>=1 ? 0.8 : 1.)"

    elif sys=='CMS_eff_b': weightUp += "*bTagWeightUp/bTagWeight"; weightDown += "*bTagWeightDown/bTagWeight"
    elif sys=='CMS_scale_pu': weightUp += "*puWeightUp/puWeight"; weightDown += "*puWeightDown/puWeight"
    elif sys=='CMS_scale_top': weightUp += "/TopWeight"; weightDown += ""

    elif sys=='CMS_eff_lep_trigger'  and (('2e' in channel or '1e' in channel) or ('2m' in channel or '1m' in channel)): 
        weightUp += "*triggerWeightUp/triggerWeight"; weightDown += "*triggerWeightDown/triggerWeight"
    #new lep trig
    elif sys=='CMS_trig_e' and ('2e' in channel or '1e' in channel): weightUp += "*1.020*triggerWeightUp/triggerWeight"; weightDown += "*0.980*triggerWeightDown/triggerWeight"
    elif sys=='CMS_trig_m' and ('2m' in channel or '1m' in channel): weightUp += "*1.002*triggerWeightUp/triggerWeight"; weightDown += "*0.998*triggerWeightDown/triggerWeight"

    elif sys=='CMS_eff_met_trigger'and not (('2e' in channel or '1e' in channel) or ('2m' in channel or '1m' in channel)):
        #weightUp += "*triggerWeightUp/triggerWeight"; weightDown += "*triggerWeightDown/triggerWeight"
        weightUp += "*1.02"; weightDown += "*0.98"

    elif (sys=='CMS_eff_e_old' and '2e' in channel) or (sys=='CMS_eff_e' and '1e' in channel): 
        weightUp += "*leptonWeightUp/leptonWeight"; weightDown += "*leptonWeightDown/leptonWeight"
    elif (sys=='CMS_eff_m_old' and '2m' in channel) or (sys=='CMS_eff_m' and '1m' in channel):
        weightUp += "*leptonWeightUp/leptonWeight"; weightDown += "*leptonWeightDown/leptonWeight"
    #new lep id/iso
    elif sys=='CMS_eff_e' and ('2e' in channel or '1e' in channel): weightUp += "*1.010*leptonWeightUp/leptonWeight"; weightDown += "*0.990*leptonWeightDown/leptonWeight"
    elif sys=='CMS_eff_m' and ('2m' in channel or '1m' in channel): weightUp += "*1.014*leptonWeightUp/leptonWeight"; weightDown += "*0.986*leptonWeightDown/leptonWeight"

    # elif sys=='QCDscale_ren': weightUp += "*QCDRenWeightUp"; weightDown += "*QCDRenWeightDown"
    # elif sys=='QCDscale_fac': weightUp += "*QCDFacWeightUp"; weightDown += "*QCDFacWeightDown"
    elif ('QCDscale' in sys and 'ren' in sys): weightUp += "*QCDRenWeightUp"; weightDown += "*QCDRenWeightDown"
    elif ('QCDscale' in sys and 'fac' in sys): weightUp += "*QCDFacWeightUp"; weightDown += "*QCDFacWeightDown"

    elif sys=='pdf_accept_2l' and ('2e' in channel or '2m' in channel): weightUp += "*(1.060)"; weightDown += "*(0.940)"
    elif sys=='pdf_accept_1l' and ('1e' in channel or '1m' in channel): weightUp += "*(1.030)"; weightDown += "*(0.970)"
    elif sys=='pdf_accept_0l' and ('0l' in channel): weightUp += "*(1.060)"; weightDown += "*(0.940)"

    # elif sys=='EWKscale_Z': weightDown += "/ZewkWeight"
    # elif sys=='EWKscale_W': weightDown += "/WewkWeight"

    else:
        print "Systematic", sys, "not applicable or not recognized."
    print 'channel ', channel, 'cut',cut 
    ### Create and fill MC histograms ###
    file = {}
    tree = {}
    hist = {}
    histUp = {}
    histDown = {}
    isBlind = BLIND and 'SR' in channel
    for i, s in enumerate(back+sign):
        tree[s] = TChain("tree")
        for j, ss in enumerate(sample[s]['files']): tree[s].Add(NTUPLEDIR + ss + ".root")
        if not binLow == "":
            hist[s] = TH1F(s, ";"+variable[var]['title']+";Events;"+('log' if variable[var]['log'] else ''), 1, float(binLow), float(binHigh))
        elif binLow == "" and variable[var]['nbins']>0:
            hist[s] = TH1F(s, ";"+variable[var]['title']+";Events;"+('log' if variable[var]['log'] else ''), variable[var]['nbins'], variable[var]['min'], variable[var]['max'])
        else:
            hist[s] = TH1F(s, ";"+variable[var]['title'], len(variable[var]['bins'])-1, array('f', variable[var]['bins']))

        hist[s].Sumw2()
        histUp[s] = hist[s].Clone(s+'Up')
        histDown[s] = hist[s].Clone(s+'Down')
        redFactorString = ""
        redFactorValue = ""
        #if isBlind and 'data' not in s and options.limit:
        if isBlind and 'data' not in s:
            print "1/ 15 of MC in sys"
            redFactorValue = " / 15"
        cutstring = ("*("+cut+")" if len(cut)>0 else "")
        cutstringUp   = ("*("+cutUp+")" if len(cut)>0 else "")
        cutstringDown = ("*("+cutDown+")" if len(cut)>0 else "")
        if '-' in s: cutstring = cutstring.replace(cut, cut + "&& nBQuarks==" + s.split('-')[1][0])
        tree[s].Project(s, var, "("+weight+redFactorValue+")" + cutstring)
 
        if 'HF' not in sys or 'QCDscale' not in sys :
            tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstring)
            tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstring)

        if 'HF' in sys and not 'HF_Z' in sys and not 'HF_W' in sys:
            if s.startswith('WJ') or s.startswith('ZJ') or s.startswith('DYJets'):
                tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstringDown)
            else:
                tree[s].Project(s+'Up', varUp, "("+weight+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weight+redFactorValue+")" + cutstringDown)

        if 'HF_Z' in sys:
            if s.startswith('ZJ') or s.startswith('DYJets'):
                tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstringDown)
            else:
                tree[s].Project(s+'Up', varUp, "("+weight+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weight+redFactorValue+")" + cutstringDown)

        if 'HF_W' in sys:
            if s.startswith('WJ'):
                tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstringDown)
            else:
                tree[s].Project(s+'Up', varUp, "("+weight+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weight+redFactorValue+")" + cutstringDown)

        if 'QCDscale' in sys:
            if 'TT' in sys and s.startswith('TTbarSL'):
                tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstringDown)
            elif 'VV' in sys and s.startswith('VV'):
                tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstringDown)
            elif 'O' in sys and not 'DM' in s and not s.startswith('TTbarSL') and not s.startswith('VV') and not s.startswith('WJ') and not s.startswith('DY'):    
                tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstringDown)
            elif ((sys=='QCDscale_ren' or sys=='QCDscale_fac') and not 'DM' in s):
                tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstringDown)
            else:
                tree[s].Project(s+'Up', varUp, "("+weight+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weight+redFactorValue+")" + cutstringDown)

        if 'scale_top' in sys:
            if s.startswith('ttDM') or s.startswith('tDM') or s.startswith('tttDM'):
                tree[s].Project(s+'Up', varUp, "("+weight+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weight+redFactorValue+")" + cutstringDown)
            else:
                tree[s].Project(s+'Up', varUp, "("+weightUp+redFactorValue+")" + cutstringUp)
                tree[s].Project(s+'Down', varDown, "("+weightDown+redFactorValue+")" + cutstringDown)


        hist[s].Scale(sample[s]['weight'] if hist[s].Integral() >= 0 else 0)
        hist[s].SetLineWidth(2)
        histUp[s].SetLineWidth(2)
        histDown[s].SetLineWidth(2)
        hist[s].SetLineColor(1)
        histUp[s].SetLineColor(629)
        histDown[s].SetLineColor(602)
    
    # Rescale normalization for QCD scales FIXME
    # if 'QCDscale' in sys:
    #     for s in back+sign:#['TTbar', 'TTbarSL', 'ST']:
    #         if s in hist and histUp[s].Integral() > 0. and histDown[s].Integral() > 0.:
    #             histUp[s].Scale(hist[s].Integral()/histUp_tot[s].Integral())
    #             histDown[s].Scale(hist[s].Integral()/histDown_tot[s].Integral())

    hist['BkgSum'] = hist[back[0]].Clone("BkgSum")
    hist['BkgSum'].Reset()
    histUp['BkgSum'] = hist['BkgSum'].Clone("BkgSumUp")
    histUp['BkgSum'].SetLineColor(629)
    histUp['BkgSum'].Reset()
    histDown['BkgSum'] = hist['BkgSum'].Clone("BkgSumDown")
    histDown['BkgSum'].SetLineColor(602)
    histDown['BkgSum'].Reset()

    for i, s in enumerate(back):
        hist['BkgSum'].Add(hist[s], 1)
        histUp['BkgSum'].Add(histUp[s], 1)
        histDown['BkgSum'].Add(histDown[s], 1)
    
    for i, s in enumerate(back+sign+['BkgSum']):
        addOverflow(hist[s], False)
        addOverflow(histUp[s], False)
        addOverflow(histDown[s], False)
    

    for i, s in enumerate(sign+['BkgSum']):
        c1 = TCanvas("c1", "Signals", 800, 800)
        c1.cd()
        gStyle.SetOptStat(0)
        gStyle.SetOptTitle(0)

        c1.Divide(1, 2)
        setTopPad(c1.GetPad(1), 4)
        setBotPad(c1.GetPad(2), 4)
        
        
        c1.cd(1)
        c1.GetPad(1).SetTopMargin(0.06)
        c1.GetPad(1).SetRightMargin(0.05)
        c1.GetPad(1).SetTicks(1, 1)
        c1.GetPad(1).SetLogy()

        histUp[s].SetMaximum(histUp[s].GetMaximum()*5)
        histUp[s].Draw("HIST")
        histDown[s].Draw("SAME, HIST")
        hist[s].Draw("SAME, HIST")
        drawCMS(-1, "Simulation", False)

        setHistStyle(histUp[s], 1.2)

        c1.cd(2)
        errUp = histUp[s].Clone("BkgUp;")
        errUp.Add(hist[s],-1)
        errUp.Divide(hist[s])
        errUp.SetTitle("")
        errUp.GetYaxis().SetTitle("#frac{shifted-central}{central}")
        errUp.GetYaxis().SetNdivisions(503)
        setBotStyle(errUp)
        errUp.GetYaxis().SetTitleSize(errUp.GetYaxis().GetTitleSize()*(2.5));
        errUp.GetYaxis().SetRangeUser(-0.15,0.15)
        errUp.Draw("HIST")
    
        errDown = histDown[s].Clone("BkgDown;")
        errDown.Add(hist[s],-1)
        errDown.Divide(hist[s])
        errDown.Draw("SAME, HIST")
    
        f1 = TF1("myfunc","[0]",-100000,10000);
        f1.SetLineColor(1)
        f1.SetLineStyle(7)
        f1.SetLineWidth(1)
        f1.SetParameter(0,0);
        f1.Draw("same")

        leg = TLegend(0.65, 0.80, 0.95, 0.80)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0) #1001
        leg.SetHeader(sys.replace('CMS', '').replace('_', ' '))
        leg.AddEntry(histUp[s], "Up", "l")
        leg.AddEntry(hist[s], "Central", "l")
        leg.AddEntry(histDown[s], "Down", "l")
        leg.SetY1(0.75-leg.GetNRows()*0.045)
        c1.cd(1)
        leg.Draw()

        if options.saveplots:
            if not os.path.exists("plotsSys_"+options.name+"/"+channel+binName): os.makedirs("plotsSys_"+options.name+"/"+channel+binName)
            c1.Print("plotsSys_"+options.name+"/"+channel+binName+"/"+sys+"_"+s+".png")
            c1.Print("plotsSys_"+options.name+"/"+channel+binName+"/"+sys+"_"+s+".pdf")
    
    saveHist(histUp, channel+binName, sys+'Up')
    saveHist(histDown, channel+binName, sys+'Down')

    print "Added systematic", sys, "to channel", channel


########## ######## ##########

def saveHist(hist, channel, directory='', addStat=False):
    
    # Blind
#    if BLIND and 'data_obs' in hist and 'SR' in channel:
#        rando = TRandom3()
#        hist['data_obs'].Reset()
#        hist['data_obs'].SetMarkerStyle(21)
#        for i in range(hist['data_obs'].GetNbinsX()):
        #this wiggles the pseudodata with a Poison 
        #-> different from Asimov dataset (-t -1 option), will give different obs/expected limits but thats ok
#            hist['data_obs'].SetBinContent(i+1, rando.Poisson( hist['BkgSum'].GetBinContent(i+1) ))
#            hist['data_obs'].SetBinContent(i+1, hist['BkgSum'].GetBinContent(i+1) )

    # Sanity check
#    smax = max(hist, key=lambda x: hist[x].Integral())
#    for s in hist.keys():
#        for i in range(hist[s].GetNbinsX()):
#            if not hist[s].GetBinContent(i+1)>0.: hist[s].SetBinContent(i+1, 1.e-4) # Sanity check
#            if math.isnan(hist[s].GetBinContent(i+1)) or math.isinf(hist[s].GetBinContent(i+1)): print "WARNING: in channel", channel, "bkg", s, "bin", i+1, "is nan or inf"
#            #print "checking", s, i, hist[s].GetBinContent(i+1)
    
    directorySys = directory.replace("Up","").replace("Down","")
    outFile = TFile("rootfiles_"+options.name+"/"+channel+directorySys+".root", "RECREATE" if len(directory)==0 else "UPDATE")
    outFile.cd()
    if len(directory) > 0:
        if not outFile.GetDirectory(directory): outFile.mkdir(directory)
        outFile.cd(directory)

    for s in sorted(hist.keys()):
        hist[s].Write(hist[s].GetName().replace('Up', '').replace('Down', ''))

    #outFile.cd("..")
    # Statistical MC uncertainty
    if addStat:
        nbins = hist['data_obs'].GetNbinsX()
        #CMS_stat_Z0b_bin57
        for s in sorted(hist.keys()):
            if 'data' in s: continue
            dirname = channel+"/Sys_"+s
            #if outFile.GetDirectory(dirname): outFile.rmdir(dirname)
            outFile.mkdir(dirname)
            outFile.cd(dirname)
            for k in range(1, nbins+1):
                sysname = "CMS_stat_%s_%s_bin%d" % (channel, s, k)
                histUp = hist[s].Clone(sysname+"Up")
                histUp.SetBinContent(k, histUp.GetBinContent(k) + histUp.GetBinError(k))
                histUp.Write()
                histDown = hist[s].Clone(sysname+"Down")
                histDown.SetBinContent(k, max(histDown.GetBinContent(k) - histDown.GetBinError(k), 1.e-6))
                histDown.Write()
            outFile.cd("..")
    
    outFile.Close()
    print "Histograms saved in file rootfiles_"+options.name+"/"+channel+directorySys+".root"

    


########## ######## ##########

def plotLimit():

    doBinned = False
    if options.mode == "binned": doBinned = True
    gROOT.SetBatch(True)
    try: os.stat("rootfiles_"+options.name) 
    except: os.mkdir("rootfiles_"+options.name)
#    os.system("rm rootfiles_"+options.name+"/*")

    cat = ["AH0l0fSR", "AH0l1fSR", "AH0l2bSR", "AH1eWR", "AH1mWR", "AH2eZR", "AH2mZR", "AH1eTR", "AH1mTR", "SL1e0fSR", "SL1e1fSR", "SL1m0fSR", "SL1m1fSR", "SL1e2bSR", "SL1m2bSR", "SL1eWR", "SL1mWR", "SL1e1mTR", "SL2eTR", "SL2mTR"]
    #cat = ["AH0l0fSR", "AH0l1fSR", "AH0l2bSR", "AH1eWR", "AH1mWR", "AH2eZR", "AH2mZR", "AH1eTR", "AH1mTR"]
     
    #sys = ['CMS_scale_j','CMS_res_j','CMS_WqcdWeightRen','CMS_WqcdWeightFac','CMS_ZqcdWeightRen','CMS_ZqcdWeightFac','CMS_WewkWeight','CMS_ZewkWeight','CMS_pdf','CMS_HF','CMS_eff_b', 'CMS_scale_pu', 'CMS_scale_top', 'CMS_eff_met_trigger', 'CMS_eff_lep_trigger','CMS_eff_e', 'CMS_eff_m', 'QCDscale_ren', 'QCDscale_fac']

    #sys = ['CMS_scale_j','CMS_res_j','CMS_WqcdWeightRen','CMS_WqcdWeightFac','CMS_WewkWeight','CMS_pdf','CMS_HF','CMS_eff_b', 'CMS_scale_pu', 'CMS_scale_top', 'CMS_eff_met_trigger', 'CMS_eff_lep_trigger', 'CMS_eff_lep', 'QCDscale_ren', 'QCDscale_fac']
    sys = ['CMS_scale_j','CMS_res_j','CMS_WqcdWeightRen','CMS_WqcdWeightFac','CMS_WewkWeight','CMS_pdf','CMS_HF','CMS_HF_V','CMS_eff_b', 'CMS_scale_pu', 'CMS_scale_top', 'CMS_eff_met_trigger', 'CMS_eff_lep_trigger','CMS_trig_m','CMS_trig_e', 'pdf_accept_2l','pdf_accept_1l','pdf_accept_0l','CMS_eff_e', 'CMS_eff_m','CMS_eff_e_old', 'CMS_eff_m_old','CMS_HF_Z','CMS_HF_W','CMS_ZqcdWeightRen','CMS_ZqcdWeightFac','CMS_ZewkWeight','QCDscale_ren', 'QCDscale_fac', 'QCDscale_ren_TT', 'QCDscale_fac_TT', 'QCDscale_ren_VV', 'QCDscale_fac_VV', 'QCDscale_ren_O', 'QCDscale_fac_O',]

    for thread,r in enumerate(cat):
        #fix these variables at some points, its confusing to hack the met significance
        var = 'MET_pt'
        if r.startswith('SL'): var = 'MET_sign' # correct binnning
        if r.endswith('ZR'): var = 'FakeMET_pt'
        
        if doBinned:
            bins = np.array([])
            if 'bins' in variable[var].keys():
                bins = np.array(variable[var]['bins'] )
            else:
                binsize = (variable[var]['max']-variable[var]['min'])/variable[var]['nbins']
                bins = np.arange(variable[var]['min'], variable[var]['max'], binsize)
                
            bins = np.append(bins, 10000) #add essentially infinite upper bound for the last bin
            
            for i in range(0,len(bins)-1):
                rbin =  r + "binned_LowVal" + str(bins[i]) + "_HighVal" + str(bins[i+1])
                #print "rbin:",rbin
                
                p = multiprocessing.Process(target=plot, args=(var, rbin, ))
                p.start()
                p.join()
        else: #shouls dump these pieces in a separate function, but fine for now
            print "Not really multi-threaded"
            #        plot(var, r)
            
            p = multiprocessing.Process(target=plot, args=(var, r, ))
            p.start()
            p.join()

    doSys = True
    if not doSys: return

    print "\n\n@ Main jobs have finished, now running uncertainties\n\n"    
    
    for s in sys:
        print "\n@ Running uncertainty", s, "\n"
        for r in cat:
            var = 'MET_pt'
            if r.startswith('SL'): var = 'MET_sign' # correct binnning
            if r.endswith('ZR'): var = 'FakeMET_pt'
            
            if doBinned:
                bins = np.array([])
                if 'bins' in variable[var].keys():
                    bins = np.array(variable[var]['bins'] )
                else:
                    binsize = (variable[var]['max']-variable[var]['min'])/variable[var]['nbins']
                    bins = np.arange(variable[var]['min'], variable[var]['max'], binsize)
                
                bins = np.append(bins, 10000) #add essentially infinite upper bound for the last bin
            
                for i in range(0,len(bins)-1):
                    rbin =  r + "binned_LowVal" + str(bins[i]) + "_HighVal" + str(bins[i+1])
                    print "rbin:",rbin
                    #       addSys(var, r, s)
                    p = multiprocessing.Process(target=addSys, args=(var, rbin, s, ))
                    p.start()
                    p.join()

            else:
                p = multiprocessing.Process(target=addSys, args=(var, r, s, ))
                p.start()
                p.join()
            
    print "\n\n@ Uncertainties have finished.\n\n"




def plotLimitBatch(sys=""):
    doBinned = False
    if options.mode == "binned": doBinned = True

    cat = ["AH0l0fSR", "AH0l1fSR", "AH0l2bSR", "AH1eWR", "AH1mWR", "AH2eZR", "AH2mZR", "AH1eTR", "AH1mTR", "SL1e0fSR", "SL1e1fSR", "SL1m0fSR", "SL1m1fSR", "SL1e2bSR", "SL1m2bSR", "SL1eWR", "SL1mWR", "SL1e1mTR", "SL2eTR", "SL2mTR"]
    #cat = ["AH0l0fSR", "AH0l1fSR", "AH0l2bSR", "AH1eWR", "AH1mWR", "AH2eZR", "AH2mZR", "AH1eTR", "AH1mTR"]
        
    for r in cat:
        #fix these variables at some points, its confusing to hack the met significance
        var = 'MET_pt'
        if r.startswith('SL'): var = 'MET_sign' # correct binnning
        if r.endswith('ZR'): var = 'FakeMET_pt'
        
        if doBinned:
            bins = np.array([])
            if 'bins' in variable[var].keys():
                bins = np.array(variable[var]['bins'] )
            else:
                binsize = (variable[var]['max']-variable[var]['min'])/variable[var]['nbins']
                bins = np.arange(variable[var]['min'], variable[var]['max'], binsize)
                
            bins = np.append(bins, 10000) #add essentially infinite upper bound for the last bin
            
            for i in range(0,len(bins)-1):
                rbin =  r + "binned_LowVal" + str(bins[i]) + "_HighVal" + str(bins[i+1])
                print "rbin:",rbin
                #multiprocessing doesn't actually work this way, but avoids a few memory issues with TH1 and canvases
                #                plot(var,rbin,)
                if sys=="":
                    print "running plotting"
                    p = multiprocessing.Process(target=plot, args=(var, rbin, ))
                    p.start()
                    p.join()
                    # plot(var,r,)
                else:
                    print "running systematic", sys
                    p = multiprocessing.Process(target=addSys, args=(var, rbin,sys, ))
                    p.start()
                    p.join()

        else: 
            #multiprocessing doesn't actually work this way, but avoids a few memory issues with TH1 and canvases
            if sys == "":
                print "running plotting"
                p = multiprocessing.Process(target=plot, args=(var, r, ))
                p.start()
                p.join()
#                plot(var,r,)
            else:
                print "running systematic", sys
                p = multiprocessing.Process(target=addSys, args=(var, r,sys, ))
                p.start()
                p.join()
#                addSys(var, r, sys, )
    return

    
########## ######## ##########

def plotAll():
    gROOT.SetBatch(True)
    
    hists = {}
    
#    file = TFile(NTUPLEDIR + "DYJetsToLL.root", 'READ')
#    file.cd()
#    # Looping over file content
#    for key in file.GetListOfKeys():
#        obj = key.ReadObj()
#        # Histograms
#        if obj.IsA().InheritsFrom('TH1'): continue
#        #    hists.append(obj.GetName())
#        # Tree
#        elif obj.IsA().InheritsFrom('TTree'): continue
#        # Directories
#        if obj.IsFolder() and obj.GetName() in ['0l', '1e', '1m', '2e', '2m', '1e1m']:
#            subdir = obj.GetName()
#            hists[subdir] = []
#            file.cd(subdir)
#            for subkey in file.GetDirectory(subdir).GetListOfKeys():
#                subobj = subkey.ReadObj()
#                if subobj.IsA().InheritsFrom('TH1'):
#                    hists[subdir].append(subobj.GetName())
#            file.cd('..')
#    file.Close() 
#    
#    for c, l in hists.iteritems():
#        #if not os.path.exists("plots/"+c):
#        #    os.mkdir("plots/"+c)
#        for h in l:
#            plot(h, c)
    
    for r in selection.keys():
        #for v in ['Lepton1_pt', 'Lepton1_pfIso', 'Lepton2_pt', 'Lepton2_pfIso', 'Jet1_pt', 'Jet1_csv', 'Jet2_pt', 'Jet2_csv', 'Jet3_pt', 'Jet3_csv', 'Jet4_pt', 'Jet4_csv', 'JetF_pt', 'mZ', 'V_pt', 'mT', 'mT2', 'MinDPhi', 'MinDPhi12', 'MET_pt', 'MET_sign', 'FakeMET_pt', 'nPV', 'nJets', 'nForwardJets', 'nBTagJets', 'nElectrons', 'nMuons', 'nTaus', 'HT', 'ST']:
        #for v in ['MET_sign','MET_pt','FakeMET_pt']: 
        #for v in ['nForwardJets','JetF_pt','JetF_eta','MET_sign']:
        #for v in ['MET_sign']:
        for v in ['MET_sign','MET_pt', 'mT', 'mT2', 'mTb','MinDPhi12', 'ratio_jet1pt_HT']:
            #plot(v, r)
            p = multiprocessing.Process(target=plot, args=(v,r,))
            jobs.append(p)
            p.start()
        p.join()


jobs = []
gROOT.SetBatch(True)
try: os.stat("rootfiles_"+options.name) 
except: os.mkdir("rootfiles_"+options.name)

if options.all: plotAll()
elif options.limit and options.batch: plotLimitBatch(options.sys)
elif options.limit and not options.batch: plotLimit()
elif options.signal: plotSignal(options.cut)
elif options.efficiency: plotEfficiency()
else: plot(options.variable, options.cut, options.norm)
#addSys('FakeMET_pt', 'AH2mZR', 'QCDscale_ren')
