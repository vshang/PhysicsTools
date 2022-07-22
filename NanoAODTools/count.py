from ROOT import *

path = '/hdfs/store/user/vshang/signalMC/ttDM_2016/ttbardm_10GeV_scalar_incl_2016_nanoaod/'

sumevents = 0
for i in range(0,401):
    # if i == 4471:
    #     continue
    #f = TFile.Open(path+'NANOAOD_'+str(i)+'.root','')
    f = TFile.Open(path+'ttbarDM_nanoAOD_'+str(i)+'.root','')
    t = f.Get('Events')
    nevents = t.GetEntries()
    sumevents += nevents
    #print 'nevents in tree_'+str(i)+'.root : ', nevents

print 'sumevents : ', sumevents
