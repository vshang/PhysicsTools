from ROOT import *

#Select root file here
#rootfile = 'outDir2016AnalysisSR/ttbarDM_Mchi1Mphi100_scalar_full_SL.root'
rootfile = 'outDir2016AnalysisSR/ttbarDM_Mchi1Mphi100_scalar_full2_AH0l2bSR_optimized.root'

#Load root file
f = TFile.Open(rootfile, '')

#Get event tree
eventTree = f.Get('Events')

#Print out event IDs
nEntries = eventTree.GetEntries()
for i in range(nEntries):
    eventTree.GetEntry(i)
    eventID = int(eventTree.event)
    lumi = eventTree.luminosityBlock
    run = eventTree.run
    print (eventID, lumi, run)
