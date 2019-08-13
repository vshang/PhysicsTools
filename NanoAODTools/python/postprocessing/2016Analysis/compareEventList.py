#Select event list text files to compare
nanoAOD = 'textOutput/ttbarDM_Mchi1Mphi100_scalar_full_AH_eventList.txt'
miniAOD = 'textOutput/miniAOD_ttbarDM_Mchi1Mphi100_scalar_full_AH_eventList.txt'

#Create list of nanoAOD events containing (eventID, lumi, run) 
with open(nanoAOD, 'r') as f:
    nanoEventList = [line.strip() for line in f]

#Create list of miniAOD events containing (eventID, lumi, run)
miniEventList = []
with open(miniAOD, 'r') as f:
    for line in f:
        line = str(line).replace(' ', '')
        line = line.split('*')
        miniEventList.append(line)
miniEventList = [str((int(i[2]), int(i[3]), int(i[4]))) for i in miniEventList]

#Count number of missing events in nanoAOD/miniAOD file
nMissingNano = 0
nMissingMini = 0

#Print any nanoAOD events not found in miniAOD file
print 'nanoAOD events not in miniAOD file:'
for nanoEvent in nanoEventList:
    if nanoEvent not in miniEventList:
        print '(eventID, lumi, run) = ', nanoEvent
        nMissingNano += 1

#Print any miniAOD events not found in nanoAOD file
print 'miniAOD events no in nanoAOD file:'
for miniEvent in miniEventList:
    if miniEvent not in nanoEventList:
        print '(eventID, lumi, run) = ', miniEvent
        nMissingMini += 1

#Pring summary info
print 'Total number of missing nanoAOD events in miniAOE file: ', nMissingNano, 'Percent of nanoAOD files missing: ', nMissingNano/float(len(nanoEventList))*100,'%'
print 'Total number of missing miniAOD events in nanoAOD file: ', nMissingMini, 'Perecent of miniAOD files missing: ', nMissingMini/float(len(miniEventList))*100,'%'
