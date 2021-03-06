#Select event list text files to compare
nanoAOD1 = 'textOutput/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full1_AH0l1fSR_optimized18092019_eventList.txt'
nanoAOD2 = 'textOutput/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full2_AH0l1fSR_optimized18092019_eventList.txt'
# nanoAOD3 = 'textOutput/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full1_AH0lSR_optimized_18092019_eventList.txt'
# nanoAOD4 = 'textOutput/ttbarDM/ttbarDM_Mchi1Mphi100_scalar_full2_AH0lSR_optimized_18092019_eventList.txt'
miniAOD1 = 'textOutput/miniAOD/miniAOD_ttbarDM_Mchi1Mphi100_scalar_full_AH0l1fSR_test_optimized_24102019eventList.txt'
# miniAOD2 = 'textOutput/miniAOD/miniAOD_ttbarDM_Mchi1Mphi100_scalar_full_AH0l1fSR_optimized_eventList.txt'

#Create list of full nanoAOD events containing (eventID, lumi, run) 
with open(nanoAOD1, 'r') as f:
    nanoEventList1 = [line.strip() for line in f]
with open(nanoAOD2, 'r') as f:
    nanoEventList2 = [line.strip() for line in f]
# with open(nanoAOD3, 'r') as f:
#     nanoEventList3 = [line.strip() for line in f]
# with open(nanoAOD4, 'r') as f:
#     nanoEventList4 = [line.strip() for line in f]
nanoEventList = nanoEventList1 + nanoEventList2 #+ nanoEventList3 + nanoEventList4

#Create list of full miniAOD events containing (eventID, lumi, run)
miniEventList = []
with open(miniAOD1, 'r') as f:
    for line in f:
        line = str(line).replace(' ', '')
        line = line.split('*')
        miniEventList.append(line)
# with open(miniAOD2, 'r') as f:
#     for line in f:
#         line = str(line).replace(' ', '')
#         line = line.split('*')
#         miniEventList.append(line)
#miniEventList = [str((int(i[2]), int(i[3]), int(i[4]))) for i in miniEventList]
miniEventList = [str((int(i[2]), int(i[3]), 1)) for i in miniEventList]

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
print 'miniAOD events not in nanoAOD file:'
for miniEvent in miniEventList:
    if miniEvent not in nanoEventList:
        print '(eventID, lumi, run) = ', miniEvent
        nMissingMini += 1

#Pring summary info
print 'Total number of missing nanoAOD events in miniAOD file: ', nMissingNano, '||', 'Percent of nanoAOD files missing: ', nMissingNano/float(len(nanoEventList))*100,'%'
print 'Total number of missing miniAOD events in nanoAOD file: ', nMissingMini, '||', 'Percent of miniAOD files missing: ', nMissingMini/float(len(miniEventList))*100,'%'
