#Script to check and compare list of samples processed by Condor between ModuleCommonSkim and countEvents for ttH and ttbarDM 1,10 signal samples
from ROOT import *
import os

date = '02062024'
deleteFiles = True

print 'Date = ' + date
print 'deleteFiles = ' + str(deleteFiles)

#First check ttbarDM 1,10 signal samples
for year in ['2016','2017','2018']:
    for mediator in ['scalar','pseudo']:
        filelist_ModuleCommonSkim = [file for file in os.listdir('/hdfs/store/user/vshang/ttbarDM_Run' + year + '/ttbardm_10GeV_' + mediator + '_incl_' + year + '_nanoaod/ModuleCommonSkim_'+date+'/rootFiles/') if file.endswith('Skim.root')]
        filelist_countEvents = [file for file in os.listdir('/hdfs/store/user/vshang/ttbarDM_Run' + year + '/ttbardm_10GeV_' + mediator + '_incl_' + year + '_nanoaod/countEvents_'+date+'/rootFiles/') if file.endswith('Skim.root')]

        filelist_inBoth = list(set(filelist_ModuleCommonSkim).intersection(filelist_countEvents))
        print '\nCommon filelist for tt+DM 1,10 ' + mediator + ' ' + year + ' signal sample:\n' + str(filelist_inBoth)
        #Find samples not successfully processed by Condor for both ModuleCommonSkim and countEvents
        deletelist_ModuleCommonSkim = [file for file in filelist_ModuleCommonSkim if file not in filelist_inBoth]
        print '\n    List of files to delete in ModuleCommonSkim:\n    ' + str(deletelist_ModuleCommonSkim)
        deletelist_countEvents = [file for file in filelist_countEvents if file not in filelist_inBoth]
        print '\n    List of files to delete in countEvents:\n    ' + str(deletelist_countEvents)
        #Delete samples not processed for both ModuleCommonSkim and countEvents
        if deleteFiles:
            print '\n    Deleting extra files in ModuleCommonSkim and countEvents...'
            for file in deletelist_ModuleCommonSkim:
                if os.path.exists('/hdfs/store/user/vshang/ttbarDM_Run' + year + '/ttbardm_10GeV_' + mediator + '_incl_' + year + '_nanoaod/ModuleCommonSkim_'+date+'/rootFiles/' + file):
                    os.remove('/hdfs/store/user/vshang/ttbarDM_Run' + year + '/ttbardm_10GeV_' + mediator + '_incl_' + year + '_nanoaod/ModuleCommonSkim_'+date+'/rootFiles/' + file)
                else:
                    print 'File at ' + '/hdfs/store/user/vshang/ttbarDM_Run' + year + '/ttbardm_10GeV_' + mediator + '_incl_' + year + '_nanoaod/ModuleCommonSkim_'+date+'/rootFiles/' + file + ' does not exist'
            for file in deletelist_countEvents:
                if os.path.exists('/hdfs/store/user/vshang/ttbarDM_Run' + year + '/ttbardm_10GeV_' + mediator + '_incl_' + year + '_nanoaod/countEvents_'+date+'/rootFiles/' + file):
                    os.remove('/hdfs/store/user/vshang/ttbarDM_Run' + year + '/ttbardm_10GeV_' + mediator + '_incl_' + year + '_nanoaod/countEvents_'+date+'/rootFiles/' + file)
                else:
                    print 'File at ' + '/hdfs/store/user/vshang/ttbarDM_Run' + year + '/ttbardm_10GeV_' + mediator + '_incl_' + year + '_nanoaod/countEvents_'+date+'/rootFiles/' + file + ' does not exist'
            print '\n Finished deleting extra files.'

#Then check 2016 ttH signal samples
filelist_ModuleCommonSkim = [file for file in os.listdir('/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/ModuleCommonSkim_'+date+'/rootFiles/') if file.endswith('Skim.root')]
filelist_countEvents = [file for file in os.listdir('/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/countEvents_'+date+'/rootFiles/') if file.endswith('Skim.root')]

filelist_inBoth = list(set(filelist_ModuleCommonSkim).intersection(filelist_countEvents))
print '\nCommon filelist for 2016 ttH signal sample:\n' + str(filelist_inBoth)
#Find samples not successfully processed by Condor for both ModuleCommonSkim and countEvents
deletelist_ModuleCommonSkim = [file for file in filelist_ModuleCommonSkim if file not in filelist_inBoth]
print '\n    List of files to delete in ModuleCommonSkim:\n    ' + str(deletelist_ModuleCommonSkim)
deletelist_countEvents = [file for file in filelist_countEvents if file not in filelist_inBoth]
print '\n    List of files to delete in countEvents:\n    ' + str(deletelist_countEvents)
#Delete samples not processed for both ModuleCommonSkim and countEvents
if deleteFiles:
    print '\n    Deleting extra files in ModuleCommonSkim and countEvents...'
    for file in deletelist_ModuleCommonSkim:
        if os.path.exists('/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/ModuleCommonSkim_'+date+'/rootFiles/' + file):
            os.remove('/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/ModuleCommonSkim_'+date+'/rootFiles/' + file)
        else:
            print 'File at ' + '/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/ModuleCommonSkim_'+date+'/rootFiles/' + file + ' does not exist'
    for file in deletelist_countEvents:
        if os.path.exists('/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/countEvents_'+date+'/rootFiles/' + file):
            os.remove('/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/countEvents_'+date+'/rootFiles/' + file)
        else:
            print 'File at ' + '/hdfs/store/user/vshang/ttH_Run2016/ttH_HToInvisible_M125_TuneCUETP8M1_13TeV_powheg_pythia8_nanoAODv7/countEvents_'+date+'/rootFiles/' + file + ' does not exist'
    print '\n Finished deleting extra files.'
