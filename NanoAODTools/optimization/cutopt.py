import os, multiprocessing
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory, gDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH2F, THStack, TGraph, TGraphAsymmErrors
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TBox, TMath
import numpy as np

#Variables definitions

ncuts = 5
nfoms = 3

init_cutValue = [ [ 0 for y in range( 2 ) ] for x in range( ncuts ) ]
nstepCut      = [0] * 10
cutValues     = [ [ 0 for y in range( 100 ) ] for x in range( 10 ) ]

nstepsMAX = 30

nSigPassed = np.array([[[[[0]*nstepsMAX]*nstepsMAX]*nstepsMAX]*nstepsMAX]*nstepsMAX,dtype='f')
#np.indices((nstepsMAX,nstepsMAX,nstepsMAX,nstepsMAX,nstepsMAX), dtype='f')
nBkgPassed = np.array([[[[[0]*nstepsMAX]*nstepsMAX]*nstepsMAX]*nstepsMAX]*nstepsMAX,dtype='f')
#np.indices((nstepsMAX,nstepsMAX,nstepsMAX,nstepsMAX,nstepsMAX), dtype='f')

indexBestCuts = [[0 for x in range(10)] for y in range(10)]

cutDir = [0] * 10


#Function to fill the cut values

def fillCutValues( x1min, x1max, step1, cutdir1,
                   x2min, x2max, step2, cutdir2,
                   x3min, x3max, step3, cutdir3,
                   x4min, x4max, step4, cutdir4,
                   x5min, x5max, step5, cutdir5):

    init_cutValue[0][0] = x1min
    init_cutValue[0][1] = x1max
    nstepCut[0] = step1
    cutDir[0] = cutdir1
  
    init_cutValue[1][0] = x2min
    init_cutValue[1][1] = x2max
    nstepCut[1] = step2
    cutDir[1] = cutdir2

    init_cutValue[2][0] = x3min
    init_cutValue[2][1] = x3max
    nstepCut[2] = step3
    cutDir[2] = cutdir3  
  
    init_cutValue[3][0] = x4min
    init_cutValue[3][1] = x4max
    nstepCut[3] = step4
    cutDir[3] = cutdir4

    init_cutValue[4][0] = x5min
    init_cutValue[4][1] = x5max
    nstepCut[4] = step5
    cutDir[4] = cutdir5
 
    #Checking the cuts that are being applied
    # print "checking cuts applied : "
    # print "ncuts ", ncuts

    for j in range(ncuts):
        #print "range(nstepCut[j]) ", range(nstepCut[j])
        for n in range(nstepCut[j]):
            if cutDir[j]==1:
                cutValues[j][n] = init_cutValue[j][0] + (init_cutValue[j][1]-init_cutValue[j][0])/nstepCut[j] *n
            else:
                cutValues[j][n] = init_cutValue[j][1] - (init_cutValue[j][1]-init_cutValue[j][0])/nstepCut[j] *n 
            # print "cut values for j",j,"and n",n
            # print cutValues[j][n],
  
    for j1 in range(nstepCut[0]):
        for j2 in range(nstepCut[1]):
            for j3 in range(nstepCut[2]):
                for j4 in range(nstepCut[3]):
                    for j5 in range(nstepCut[4]):
                        #print j1,j2,j3,j4,j5
                        nSigPassed[j1][j2][j3][j4][j5] = 0
                        nBkgPassed[j1][j2][j3][j4][j5] = 0



#Fills the sig and bkg array with the #events passing certain cut combination
def fillSigBkgArrays(isSignal,variable,tree,wt,s,cut):

    #print "entering fill Bkg/Sign"
    cutstring = "("+wt+")" + "*(" + cut

    for j1 in range(nstepCut[0]):

        #print "j1 ", j1

        if cutDir[0]==1: cut1 = " && "+variable[0]+">"+str(cutValues[0][j1])
        elif cutDir[0]==2: cut1 =" && "+variable[0]+"<"+str(cutValues[0][j1])

        for j2 in range(nstepCut[1]):
            if cutDir[1]==1: cut2 = " && "+variable[1]+">"+str(cutValues[1][j2])
            elif cutDir[1]==2: cut2 =" && "+variable[1]+"<"+str(cutValues[1][j2])

            for j3 in range(nstepCut[2]):
                if cutDir[2]==1: cut3 = " && "+variable[2]+">"+str(cutValues[2][j3])
                elif cutDir[2]==2: cut3 =" && "+variable[2]+"<"+str(cutValues[2][j3])

                for j4 in range(nstepCut[3]):
                    if cutDir[3]==1: cut4 = " && "+variable[3]+">"+str(cutValues[3][j4])
                    elif cutDir[3]==2: cut4 =" && "+variable[3]+"<"+str(cutValues[3][j4])

                    for j5 in range(nstepCut[4]):

                        if cutDir[4]==1: cut5 = " && "+variable[4]+">"+str(cutValues[4][j5])+")"
                        elif cutDir[4]==2: cut5 =" && "+variable[4]+"<"+str(cutValues[4][j5])+")"

                        cutTot=cutstring+cut1+cut2+cut3+cut4+cut5
                        
                        # print "j1, j2, j3, j4,j5", j1,j2,j3,j4,j5
                        # print "cut in cutopt ", cutTot

                        if isSignal:
                            hTree = TH1F(s,s,100,0,1000)
                            
                            var = "MET_pt"

                            tree.Draw('%s>>%s(%s,%s,%s)' %(var,s,100,100,1450),'(%s)' %(cutTot),"goff")
                            hTree = gDirectory.Get(s)
                            hTree.SetDirectory(0)

                            nSigPassed[j1][j2][j3][j4][j5] += hTree.Integral() 
                            # print "1. j: ", j1,j2,j3,j4,j5
                            # print "--sample ", s, "integral",nSigPassed[j1][j2][j3][j4][j5]
                            #nSigPassedUnWt[j1][j2][j3][j4][j5] += 1; 
                            #nSigPassedErr[j1][j2][j3][j4][j5] += wt * wt; 
                        else :
         
                            hTree = TH1F(s,s,100,0,1000)
                            
                            var = "MET_pt"
                            tree.Draw('%s>>%s(%s,%s,%s)' %(var,s,100,100,1450),'(%s)' %(cutTot),"goff")

                            hTree = gDirectory.Get(s)
                            hTree.SetDirectory(0)
                            
                            nBkgPassed[j1][j2][j3][j4][j5] += hTree.Integral()
                            # print "--sample ", s, "integral",nBkgPassed[j1][j2][j3][j4][j5]
                            # print "--sample ", s, "integral",hTree.Integral()
                            #nBkgPassedUnWt[j1][j2][j3][j4][j5] += 1; 
                            #nBkgPassedErr[j1][j2][j3][j4][j5] += wt * wt; 


#Calculating FOM from s and b values
#def calFOM(s,b,sErr,bErr,res):
def calcFOM(s,b,res):

    # if (s+b)>0:
    #     res[0] = s/math.sqrt(s+b)
    #     res[1] = pow(1/math.sqrt(s+b) -1/(2*pow(s+b,1.5)),2)  * sErr* sErr + pow( s/(2 * pow(s+b,1.5)),2) * bErr * bErr
    #     res[1] = math.sqrt ( res[1])
    print "calculating FOM with:"
    print "-------- s", s
    print "-------- b", b
    

    if b>0:
        #res[0] = s/math.sqrt(b)
        res[0] = s/(math.sqrt(b))
        res[1] = s/math.sqrt(b+1)

    if b > 1:
        Z = 2*((s+b)*math.log((s+b)/b)-s)
        absZ = math.fabs(Z)
        if absZ != 0:
            res[2] = Z*math.sqrt(absZ)/absZ
        else:
            res[2] = 0.0

    #print "FOMS:"
    #print "s/math.sqrt(b):",res[0]
    #print "s/math.sqrt(b+1)",res[1]
    #print "2*((s+b)*math.log((s+b)/b)-s)",res[2]


def searchBestCut():
  
    #histo_FOM = TH1F("histo_FOM","histo_FOM",nstepCut[0],init_cutValue[0][0], init_cutValue[0][1])
    histo_FOM = TGraph()

    print "Finding the optimized selection"

    bestFOMs = [0] * 10
    sbest = [0] * 10 
    bbest = [0] * 10

    res = [0] * 10
  
    for j1 in range(nstepCut[0]):
        for j2 in range(nstepCut[1]):
            for j3 in range(nstepCut[2]):
                for j4 in range(nstepCut[3]):
                    for j5 in range(nstepCut[4]):
                        
                        s = nSigPassed[j1][j2][j3][j4][j5];
                        b = nBkgPassed[j1][j2][j3][j4][j5];
	      
                        print 'calculating FOM'
                        print "j ", j1, j2, j3, j4, j5 
                        calcFOM(s,b,res);

                        #histo_FOM.Fill(init_cutValue[0][0]+j1*((init_cutValue[0][1]-init_cutValue[0][0])/nstepCut[0]),res[0])
                        histo_FOM.SetPoint(j1,init_cutValue[0][0]+j1*((init_cutValue[0][1]-init_cutValue[0][0])/nstepCut[0]),res[0])

                        for n in range(nfoms):
                            if (res[n])>bestFOMs[n]:
                                # print "####### found better FOM"
                                # print "checking cuts of FOM"
                                # print "j ", j1, j2, j3, j4, j5

                                #bestFOMs[n] = res[2*n];
                                bestFOMs[n] = res[n];
                                indexBestCuts[n][0] = j1; 
                                indexBestCuts[n][1] = j2; 
                                indexBestCuts[n][2] = j3;
                                indexBestCuts[n][3] = j4; 
                                indexBestCuts[n][4] = j5; 
		  
                                # print "best cuts"
                                # print "1",indexBestCuts[n][0]
                                # print "2",indexBestCuts[n][1]
                                # print "3",indexBestCuts[n][2]
                                # print "4",indexBestCuts[n][3]
                                # print "5",indexBestCuts[n][4]

                                sbest[n] = s; 
                                bbest[n] = b; 
		  
    f = TFile("mt2.root","UPDATE");
    
    c1 = TCanvas("c1","c1",800, 800)
    c1.cd(1)
    RATIO = 0

    c1.GetPad(bool(RATIO)).SetTopMargin(0.06)
    c1.GetPad(bool(RATIO)).SetRightMargin(0.05)
    c1.GetPad(bool(RATIO)).SetLeftMargin(0.12)
    c1.GetPad(bool(RATIO)).SetTicks(1, 1)
    c1.cd(1)

    # histo_FOM.SetStats(0)
    # histo_FOM.SetTitle("")
    # histo_FOM.GetYaxis().SetTitleOffset(1.25)
    # histo_FOM.GetXaxis().SetTitleOffset(1.25)
    histo_FOM.SetFillColor(0)
    histo_FOM.SetMarkerStyle(20)
    histo_FOM.SetMarkerSize(1.25)

    histo_FOM.GetYaxis().SetTitle("FOM = s/#sqrt{b}")
    #histo_FOM.GetXaxis().SetTitle("m_{T}^{W} (GeV)")
    histo_FOM.GetXaxis().SetTitle("m_{T2}^{W} (GeV)")
    #histo_FOM.GetXaxis().SetTitle("min #Delta #varphi (jet_{1,2}-#slash{E}_{T})")
    histo_FOM.GetXaxis().SetTitleOffset(1.1);
    histo_FOM.GetYaxis().SetTitleOffset(1.45);


    histo_FOM.Draw("AP")
    histo_FOM.Write("mT2_JesDown")
    #c1.Print("test.pdf")

    f.Write()

    text_file = open("ttDM100_AH0l1fSR_1b.txt", "w")

    for n in range(nfoms):
        text_file.write("best cuts for fom: %f %f %f %f\n " % (n,bestFOMs[n],sbest[n],bbest[n]))
        #text_file.write("best cuts for fom: %f %f %f %f %f %f" % (n,bestFOMs[n],sbest[n],bbest[n],sbestUnWt[n],bbestUnWt[n]))
        for j in range(ncuts):
            #print "checking cut value for j",j,"and n",indexBestCuts[n][j]
            #print cutValues[j][indexBestCuts[n][j]]
            text_file.write("%f  " % cutValues[j][indexBestCuts[n][j]])
        text_file.write("\n")
    text_file.close()
  
