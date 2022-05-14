from ROOT import *

path = '/hdfs/store/user/vshang/signalMC/tDM_2017/DMPseudo_top_tChan_Mchi1_Mphi500_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/'

sumevents = 0
for i in range(4400,4800):
    if i == 4471:
        continue
    f = TFile.Open(path+'NANOAOD_'+str(i)+'.root','')
    t = f.Get('Events')
    nevents = t.GetEntries()
    sumevents += nevents
    #print 'nevents in tree_'+str(i)+'.root : ', nevents

print 'sumevents : ', sumevents
