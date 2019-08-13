from  ROOT import *

#Select miniAOD and nanoAOD root files to compare
miniAOD = 'samples/flatTuple_1.root'
nanoAOD = 'samples/ttbarDM_Mchi1Mphi100_scalar_full.root'

#Load root files
f_mini = TFile.Open(miniAOD)
f_nano = TFile.Open(nanoAOD)

#Get event trees
miniEvents = f_mini.Get('ntuplizer/tree')
nanoEvents = f_nano.Get('Events')
#Build dictionary called 'nanoEventsIndex' where the keys are eventID's and the values are the 
#indices for nanoEvents corresponding to the eventID's
print('Building nanoEventsIndex dictionary...')
nanoEventsIndex = {}
nEventsNano = nanoEvents.GetEntries()
for eventIndex in range(nEventsNano):
    if eventIndex/1000.0 == eventIndex/1000:
        print 'Stored up to index', eventIndex
    nanoEvents.GetEntry(eventIndex)
    nanoEventID = nanoEvents.event
    nanoEventsIndex[nanoEventID] = eventIndex
print('nanoEventsIndex Dictionary complete.')

#Main comparison code
###################################################################################

#Parameters to count number of differences between miniAOD/nanoAOD files
nDiff = 0
nDiff_event = 0
nDiff_el = 0
nDiff_mu = 0
nDiff_MET = 0
nDiff_jet = 0
nDiff_bjet = 0

#Loop through every event in miniAOD file and compare to same event in nanoAOD file.
#Statements are printed when differences exist between miniAOD/nanoAOD files.
nEvents = miniEvents.GetEntries()
for i in range (nEvents):
    #Parameters to keep track of differences in miniAOD/nanoAOD branches
    nDiffExist = False
    diffExist_event = False
    diffExist_el = False 
    diffExist_mu = False
    diffExist_MET = False
    diffExist_jet = False
    diffExist_bjet = False
    #First get event ID of miniAOD event
    miniEvents.GetEntry(i)
    eventID = miniEvents.EVENT_event
    if eventID not in nanoEventsIndex: #miniAOD event not found in nanoAOD file (should never occur)
        print 'miniAOD event does not exist in nanoAOD file'
        diffExist_event = True
    else: #miniAOD event found in nanoAOD file (should always be the case)
        nanoIndex = nanoEventsIndex[eventID] #Find nanoEvents index corresponding to miniAOD eventID
        nanoEvents.GetEntry(nanoIndex) #Get event with same ID from nanoAOD file
        
        #####################################################################
        #Count number of veto electrons in miniAOD/nanoAOD files
        nElVetoMini = 0
        nElVetoNano = 0

        elRangeMini = len(miniEvents.el_pt)
        elRangeNano = len(nanoEvents.Electron_pt)
        for i in range(elRangeMini):
            if miniEvents.el_isVetoElectron[i] == 1 and miniEvents.el_pt[i] > 10 and ( abs(miniEvents.el_eta[i]) < 1.4442 or ( abs(miniEvents.el_eta[i]) > 1.566 and abs(miniEvents.el_eta[i]) < 2.1 ) ):
                nElVetoMini += 1
        for i in range(elRangeNano):
            if nanoEvents.Electron_cutBased_Sum16[i] != 0 and nanoEvents.Electron_pt[i] > 10 and ( abs(nanoEvents.Electron_eta[i]) < 1.4442 or ( abs(nanoEvents.Electron_eta[i]) > 1.566 and abs(nanoEvents.Electron_eta[i]) < 2.1 ) ):
                nElVetoNano += 1

        #Check if AH electron selection cuts match
        if ( nElVetoMini == 0 and nElVetoNano != 0 ) or ( nElVetoMini != 0 and nElVetoNano == 0 ):
            diffExist_el = True
            print 'Number of miniAOD veto electrons:', nElVetoMini, '||', 'Number of nanoAOD veto electrons:', nElVetoNano

        #####################################################################
        #Count number of veto muons in miniAOD/nanoAOD files
        nMuLooseMini = 0
        nMuLooseNano = 0

        muRangeMini = len(miniEvents.mu_pt)
        muRangeNano = len(nanoEvents.Muon_pt)
        for i in range(muRangeMini):
            if miniEvents.mu_isLooseMuon[i] == 1 and miniEvents.mu_pt[i] > 10 and abs(miniEvents.mu_eta[i]) < 2.4 and miniEvents.mu_pfDeltaCorrRelIso[i] < 0.25:
                nMuLooseMini += 1
        for i in range(muRangeNano):
            if nanoEvents.Muon_looseId[i] == 1 and nanoEvents.Muon_pt[i] > 10 and abs(nanoEvents.Muon_eta[i]) < 2.4 and nanoEvents.Muon_pfRelIso04_all[i] < 0.25:
                nMuLooseNano += 1

        #Check if AH muon selection cuts match
        if ( nMuLooseMini == 0 and nMuLooseNano != 0 ) or ( nMuLooseMini != 0 and nMuLooseNano == 0 ):
            diffExist_mu = True
            print 'Number of miniAOD loose muons:', nMuLooseMini, '||', 'Number of nanoAOD loose muons:', nMuLooseNano

        #####################################################################
        #Check if AH MET_pt selection cuts match
        METpt_AH = 250
        METptMini = miniEvents.MET_et[0]
        METptNano = nanoEvents.MET_pt
        if METptMini != 0:
            METptDiff = abs( METptNano/float(METptMini) - 1 )
        if METptMini == 0:
            METptDiff = abs( float(METptNano) )
        if ( METptMini > 250 and METptNano < 250 ) or ( METptMini < 250 and METptNano > 250 ):
            diffExist_MET = True
            print 'miniAOD MET_pt:', METptMini, '||', 'nanoAOD MET_pt:', METptNano, '||', '%% MET_pt difference', METptDiff*100

        #####################################################################
        #Count number of jets and bjets
        njetsMini = 0
        njetsNano = 0
        nbjetsMini = 0
        nbjetsNano = 0

        jetRangeMini = len(miniEvents.jetAK4_pt)
        jetRangeNano = len(nanoEvents.Jet_pt)
        for i in range(jetRangeMini):
            if miniEvents.jetAK4_pt[i] > 30 and abs(miniEvents.jetAK4_eta[i]) < 2.4:
                njetsMini += 1
                if miniEvents.jetAK4_csv[i] > 0.8484:
                    nbjetsMini += 1
        for i in range(jetRangeNano):
            if nanoEvents.Jet_pt[i] > 30 and abs(nanoEvents.Jet_eta[i]) < 2.4:
                njetsNano += 1
                if nanoEvents.Jet_btagCSVV2[i] > 0.8484:
                    nbjetsNano += 1

        #Check if number of jets for AH region match
        if ( njetsMini >= 3 and njetsNano < 3 ) or ( njetsMini < 3 and njetsNano >= 3 ):
            diffExist_jet = True
            print 'Number of miniAOD jets:', njetsMini, '||', 'Number of nanoAOD jets:', njetsNano
        #Check if number of bjets for AH region match
        if nbjetsMini != nbjetsNano:
            diffExist_bjet = True
            print 'Number of miniAOD bjets:', nbjetsMini, '||', 'Number of nanoAOD bjets:', nbjetsNano

        #####################################################################

    #Count number of differences between miniAOD/nanoAOD files
    if diffExist_event:
        nDiffExist = True
        nDiff_event += 1
    if diffExist_el:
        nDiffExist = True
        nDiff_el += 1
    if diffExist_mu:
        nDiffExist = True
        nDiff_mu += 1
    if diffExist_MET:
        nDiffExist = True
        nDiff_MET += 1
    if diffExist_jet:
        nDiffExist = True
        nDiff_jet += 1
    if diffExist_bjet:
        nDiff_bjet += 1
    #Only print event index and eventID if differences exist between miniAOD/nanoAOD event branches
    if nDiffExist:
        nDiff += 1
        print 'Event index:', i, 'Event ID:', eventID
        print '-------------------------------------------------'

print 'Comparison finished'
print 'Total number of events:', nEvents
print 'Total number of events with discrepancies:', nDiff, 'Percent of events with discrepancies:', (nDiff/float(nEvents))*100
print 'Total number of miniAOD events missing in nanoAOD file', nDiff_event, 'Percent of miniAOD events missing in nanoAOD file:', (nDiff_event/float(nEvents))*100
print 'Total number of events with discrepancy in veto electron selection:', nDiff_el, 'Percent of events with discrepancy in veto electron selection:', (nDiff_el/float(nEvents))*100
print 'Total number of events with discrepancy in loose muon selection:', nDiff_mu, 'Percent of events with discrepancy in veto muon selection:', (nDiff_mu/float(nEvents))*100
print 'Total number of events with discrepancy in MET_pt cut:', nDiff_MET, 'Percent of events with discrepancy in MET_pt cut:', (nDiff_MET/float(nEvents))*100
print 'Total number of events with discrepancy in njets cut:', nDiff_jet, 'Percent of events with discrepancy in njets cut:', (nDiff_jet/float(nEvents))*100
print 'Total number of events with discrepancy in nbjets cut:', nDiff_bjet, 'Percent of events with discrepancy in nbjets cut:', (nDiff_bjet/float(nEvents))*100
