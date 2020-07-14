from ROOT import *

path = '/hdfs/store/user/vshang/SingleElectron_Run2017/SingleElectron/ModuleCommon_06282020/200628_021712/0000/'

sumevents = 0
for i in range(1,91):
    f = TFile.Open(path+'tree_'+str(i)+'.root','')
    t = f.Get('Events')
    nevents = t.GetEntries()
    sumevents += nevents
    print 'nevents in tree_'+str(i)+'.root : ', nevents

print 'sumevents : ', sumevents
