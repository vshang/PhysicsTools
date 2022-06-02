from ROOT import *

path = '/hdfs/store/user/vshang/signalMC/tDM_2016/DMPseudo_top_tWChan_Mchi1_Mphi50_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/'

sumevents = 0
for i in range(250,500):
    # if i == 4471:
    #     continue
    f = TFile.Open(path+'NANOAOD_'+str(i)+'.root','')
    t = f.Get('Events')
    nevents = t.GetEntries()
    sumevents += nevents
    #print 'nevents in tree_'+str(i)+'.root : ', nevents

print 'sumevents : ', sumevents
