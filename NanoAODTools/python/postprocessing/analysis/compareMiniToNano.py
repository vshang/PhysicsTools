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
nDiff_elID = 0
nDiff_elPt = 0
nDiff_elEta = 0
nDiff_muID = 0
nDiff_muPt = 0
nDiff_muEta = 0
nDiff_muIso = 0
nDiff_METpt = 0
nDiff_jetPt = 0
nDiff_jetEta = 0
nDiff_jetCSV = 0

#Loop through every event in miniAOD file and compare to same event in nanoAOD file.
#Statements are printed when differences exist between miniAOD/nanoAOD files.
nEvents = miniEvents.GetEntries()
for i in range (nEvents):
    #Parameters to keep track of differences in miniAOD/nanoAOD branches
    nDiffExist = False
    diffExist_event = False
    diffExist_elID = False 
    diffExist_elPt = False
    diffExist_elEta = False
    diffExist_muID = False
    diffExist_muPt = False
    diffExist_muEta = False
    diffExist_muIso = False
    diffExist_METpt = False
    diffExist_jetPt = False
    diffExist_jetEta = False
    diffExist_jetCSV = False
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
        #Check if electron cut IDs match
        nElVetoNano = 0
        nElLooseNano = 0
        nElMediumNano = 0
        nElTightNano = 0
        nElVetoMini = 0
        nElLooseMini = 0
        nElMediumMini = 0
        nElTightMini = 0
        #Check miniAOD electron cut IDs
        for elVeto in miniEvents.el_isVetoElectron:
            nElVetoMini += elVeto
        for elLoose in miniEvents.el_isLooseElectron:
            nElLooseMini += elLoose
        for elMedium in miniEvents.el_isMediumElectron:
            nElMediumMini += elMedium
        for elTight in miniEvents.el_isTightElectron:
            nElTightMini += elTight
        #Check nanoAOD electron cut IDs
        for elCutBased in nanoEvents.Electron_cutBased_Sum16:
            if elCutBased == 1:
                nElVetoNano += 1
            if elCutBased == 2:
                nElVetoNano += 1
                nElLooseNano += 1
            if elCutBased == 3:
                nElVetoNano += 1
                nElLooseNano += 1
                nElMediumNano += 1
            if elCutBased == 4:
                nElVetoNano += 1
                nElLooseNano += 1
                nElMediumNano += 1
                nElTightNano += 1
        #Compare miniAOD to nanoAOD electron cut IDs
        if nElVetoMini != nElVetoNano:
            print 'Number of miniAOD veto electrons:', nElVetoMini, '||', 'Number of nanoAOD veto electrons:', nElVetoNano
            diffExist_elID = True
        if nElLooseMini != nElLooseNano:
            print 'Number of miniAOD loose electrons:', nElLooseMini, '||', 'Number of nanoAOD loose electrons:', nElLooseNano
            diffExist_elID = True
        if nElMediumMini != nElMediumNano:
            print 'Number of miniAOD medium electrons:', nElMediumMini, '||', 'Number of nanoAOD medium electrons:', nElMediumNano
            diffExist_elID = True
        if nElTightMini != nElTightNano:
            print 'Number of miniAOD tight electrons:', nElTightMini, '||', 'Number of nanoAOD tight electrons:', nElTightNano
        #     diffExist_elID = True
        #####################################################################
        #Check if electron pt and eta match within specified % error range
        elPtErr = 0.05
        elEtaErr = 0.05
        #Also check to see if electron pt and eta pass cut ID thresholds
        elPt_tightCut = 30
        elPt_vetoCut = 10
        elEta_tightCut = 2.1
        #Compare miniAOD to nanoAOD electron pt values
        elRange = min(len(miniEvents.el_pt), len(nanoEvents.Electron_pt))
        for elIndex in range(elRange):
            elPtMini = miniEvents.el_pt[elIndex]
            elPtNano = nanoEvents.Electron_pt[elIndex]
            if elPtMini != 0:
                elPtDiff = abs( elPtNano/float(elPtMini) - 1 )
            if elPtMini == 0:
                elPtDiff = abs( float(elPtNano) )
            if elPtDiff > elPtErr:
                diffExist_elPt = True
                print 'miniAOD electron pt:', elPtMini, '||', 'nanoAOD electron pt:', elPtNano, '||', '%% el_pt difference', elPtDiff*100
            if elPtMini > elPt_tightCut and elPtNano < elPt_tightCut:
                diffExist_elPt = True
                print 'miniAOD electron pt > ' + str(elPt_tightCut) + ':', elPtMini, '||',  'nanoAOD electron pt < ' + str(elPt_tightCut) + ':', elPtNano
            if elPtMini < elPt_tightCut and elPtNano > elPt_tightCut:
                diffExist_elPt = True
                print 'miniAOD electron pt < ' + str(elPt_tightCut) + ':', elPtMini, '||', 'nanoAOD electron pt > ' + str(elPt_tightCut) + ':', elPtNano
            if elPtMini > elPt_vetoCut and elPtNano < elPt_vetoCut:
                diffExist_elPt = True
                print 'miniAOD electron pt > ' + str(elPt_vetoCut) + ':', elPtMini, '||', 'nanoAOD electron pt < ' + str(elPt_vetoCut) + ':', elPtNano
            if elPtMini < elPt_vetoCut and elPtNano > elPt_vetoCut:
                diffExist_elPt = True
                print 'miniAOD electron pt < ' + str(elPt_vetoCut) + ':', elPtMini, '||', 'nanoAOD electron pt > ' + str(elPt_vetoCut) + ':', elPtNano
        #Compare miniAOD to nanoAOD electron eta values
            elEtaMini = miniEvents.el_eta[elIndex]
            elEtaNano = nanoEvents.Electron_eta[elIndex]
            if elEtaMini != 0:
                elEtaDiff = abs( elEtaNano/float(elEtaMini) - 1 )
            if elEtaMini == 0:
                elEtaDiff = abs( float(elEtaNano) )
            if elEtaDiff > elEtaErr:
                diffExist_elEta = True
                print 'miniAOD electron eta:', elEtaMini, '||', 'nanoAOD electron eta:', elEtaNano, '||', '%% el_eta difference', elEtaDiff*100
            if elEtaMini > elEta_tightCut and elEtaNano < elEta_tightCut:
                diffExist_elEta = True
                print 'miniAOD electron eta > ' + str(elEta_tightCut) + ':', elEtaMini,  '||', 'nanoAOD electron eta < ' + str(elEta_tightCut) + ':', elEtaNano
            if elEtaMini < elEta_tightCut and elEtaNano > elEta_tightCut:
                diffExist_elEta = True
                print 'miniAOD electron eta < ' + str(elEta_tightCut) + ':', elEtaMini,  '||', 'nanoAOD electron eta > ' + str(elEta_tightCut) + ':', elEtaNano
        #####################################################################
        #Check if muon cut IDs match
        nMuLooseNano = 0
        nMuMediumNano = 0
        nMuTightNano = 0
        nMuLooseMini = 0
        nMuMediumMini = 0
        nMuTightMini = 0
        #Check miniAOD and nanoAOD muon cut IDs
        for muIndexMini in range(len(miniEvents.mu_pt)):
            nMuLooseMini += miniEvents.mu_isLooseMuon[muIndexMini]
            nMuMediumMini += miniEvents.mu_isMediumMuon[muIndexMini]
            nMuTightMini += miniEvents.mu_isTightMuon[muIndexMini]
        for muIndexNano in range(len(nanoEvents.Muon_pt)):
            nMuLooseNano += nanoEvents.Muon_looseId[muIndexNano]
            nMuMediumNano += nanoEvents.Muon_mediumId[muIndexNano]
            nMuTightNano += nanoEvents.Muon_tightId[muIndexNano]
        #Compare miniAOD to nanoAOD electron cut IDs
        if nMuLooseMini != nMuLooseNano:
            print 'Number of miniAOD loose muons:', nMuLooseMini, '||', 'Number of nanoAOD loose muons:', nMuLooseNano
            diffExist_muID = True
        if nMuMediumMini != nMuMediumNano:
            print 'Number of miniAOD medium muons:', nMuMediumMini, '||', 'Number of nanoAOD medium muons:', nMuMediumNano
            diffExist_muID = True
        if nMuTightMini != nMuTightNano:
            print 'Number of miniAOD tight muons:', nMuTightMini, '||', 'Number of nanoAOD tight muons:', nMuTightNano
            diffExist_muID = True
        #####################################################################
        #Check if muon pt, eta, and relative isolation match within specified % error range
        muPtErr = 0.05
        muEtaErr = 0.05
        muIsoErr = 0.05
        #Also check to see if muon pt, eta, and relative isolation pass cut ID thresholds
        muPt_tightCut = 30
        muPt_looseCut = 10
        muEta_tightCut = 2.4
        muIso_looseCut = 0.25
        muIso_tightCut = 0.15
        #Compare miniAOD to nanoAOD muon pt values
        muRange = min(len(miniEvents.mu_pt), len(nanoEvents.Muon_pt))
        for muIndex in range(muRange):
            muPtMini = miniEvents.mu_pt[muIndex]
            muPtNano = nanoEvents.Muon_pt[muIndex]
            if muPtMini != 0:
                muPtDiff = abs( muPtNano/float(muPtMini) - 1 )
            if muPtMini == 0:
                muPtDiff = abs( float(muPtNano) )
            if muPtDiff > muPtErr:
                diffExist_muPt = True
                print 'miniAOD muon pt:', muPtMini, '||', 'nanoAOD muon pt:', muPtNano, '||', '%% mu_pt difference', muPtDiff*100
            if muPtMini > muPt_tightCut and muPtNano < muPt_tightCut:
                diffExist_muPt = True
                print 'miniAOD muon pt > ' + str(muPt_tightCut) + ':', muPtMini,  '||', 'nanoAOD muon pt < ' + str(muPt_tightCut) + ':', muPtNano
            if muPtMini < muPt_tightCut and muPtNano > muPt_tightCut:
                diffExist_muPt = True
                print 'miniAOD muon pt < ' + str(muPt_tightCut) + ':', muPtMini,  '||', 'nanoAOD muon pt > ' + str(muPt_tightCut) + ':', muPtNano
            if muPtMini > muPt_looseCut and muPtNano < muPt_looseCut:
                diffExist_muPt = True
                print 'miniAOD muon pt > ' + str(muPt_looseCut) + ':', muPtMini,  '||', 'nanoAOD muon pt < ' + str(muPt_looseCut) + ':', muPtNano
            if muPtMini < muPt_looseCut and muPtNano > muPt_looseCut:
                diffExist_muPt = True
                print 'miniAOD muon pt < ' + str(muPt_looseCut) + ':', muPtMini,  '||', 'nanoAOD muon pt > ' + str(muPt_looseCut) + ':', muPtNano
        #Compare miniAOD to nanoAOD muon eta values
            muEtaMini = miniEvents.mu_eta[muIndex]
            muEtaNano = nanoEvents.Muon_eta[muIndex]
            if muEtaMini != 0:
                muEtaDiff = abs( muEtaNano/float(muEtaMini) - 1 )
            if muEtaMini == 0:
                muEtaDiff = abs( float(muEtaNano) )
            if muEtaDiff > muEtaErr:
                diffExist_muEta = True
                print 'miniAOD muon eta:', muEtaMini, '||', 'nanoAOD muon eta:', muEtaNano, '||', '%% mu_eta difference', muEtaDiff*100
            if muEtaMini > muEta_tightCut and muEtaNano < muEta_tightCut:
                diffExist_muEta = True
                print 'miniAOD muon eta > ' + str(muEta_tightCut) + ':', muEtaMini,  '||', 'nanoAOD muon eta < ' + str(muEta_tightCut) + ':', muEtaNano
            if muEtaMini < muEta_tightCut and muEtaNano > muEta_tightCut:
                diffExist_muEta = True
                print 'miniAOD muon eta < ' + str(muEta_tightCut) + ':', muEtaMini,  '||', 'nanoAOD muon eta > ' + str(muEta_tightCut) + ':', muEtaNano
        #Compare miniAOD to nanoAOD muon relative isolation values
            muIsoMini = miniEvents.mu_pfDeltaCorrRelIso[muIndex]
            muIsoNano = nanoEvents.Muon_pfRelIso04_all[muIndex]
            if muIsoMini != 0:
                muIsoDiff = abs( muIsoNano/float(muIsoMini) - 1 )
            if muIsoMini == 0:
                muIsoDiff = abs( float(muIsoNano) )
            if muIsoDiff > muIsoErr:
                diffExist_muIso = True
                print 'miniAOD muon relative isolation:', muIsoMini, '||', 'nanoAOD muon relative isolation:', muIsoNano, '||', '%% mu_relIso difference', muIsoDiff*100
            if muIsoMini > muIso_tightCut and muIsoNano < muIso_tightCut:
                diffExist_muIso = True
                print 'miniAOD muon relative isolation > ' + str(muIso_tightCut) + ':', muIsoMini,  '||', 'nanoAOD muon relative isolation < ' + str(muIso_tightCut) + ':', muIsoNano
            if muIsoMini < muIso_tightCut and muIsoNano > muIso_tightCut:
                diffExist_muIso = True
                print 'miniAOD muon relative isolation < ' + str(muIso_tightCut) + ':', muIsoMini,  '||', 'nanoAOD muon relative isolation > ' + str(muIso_tightCut) + ':', muIsoNano
            if muIsoMini > muIso_looseCut and muIsoNano < muIso_looseCut:
                diffExist_muIso = True
                print 'miniAOD muon relative isolation > ' + str(muIso_looseCut) + ':', muIsoMini,  '||', 'nanoAOD muon relative isolation < ' + str(muIso_looseCut) + ':', muIsoNano
            if muIsoMini < muIso_looseCut and muIsoNano > muIso_looseCut:
                diffExist_muIso = True
                print 'miniAOD muon relative isolation < ' + str(muIso_looseCut) + ':', muIsoMini,  '||', 'nanoAOD muon relative isolation > ' + str(muIso_looseCut) + ':', muIsoNano
        #####################################################################
        #Check if miniAOD and nanoAOD MET_pt match within specified % error range
        METpt_Err = 0.05
        #Also check to see if miniAOD and nanoAOD MET_pt pass SL/AH cut thresholds
        METpt_SL = 160
        METpt_AH = 250
        #Compare miniAOD to nanoAOD MET_pt values
        METptMini = miniEvents.MET_et[0]
        METptNano = nanoEvents.MET_pt
        if METptMini != 0:
            METptDiff = abs( METptNano/float(METptMini) - 1 )
        if METptMini == 0:
            METptDiff = abs( float(METptNano) )
        if METptDiff > METpt_Err:
            diffExist_METpt = True
            print 'miniAOD MET_pt:', METptMini, '||', 'nanoAOD MET_pt:', METptNano, '||', '%% MET_pt difference', METptDiff*100
        if METptMini > METpt_SL and METptNano < METpt_SL:
            diffExist_METpt = True
            print 'miniAOD MET_pt > ' + str(METpt_SL) + ':', METptMini,  '||', 'nanoAOD MET_pt < ' + str(METpt_SL) + ':', METptNano
        if METptMini < METpt_SL and METptNano > METpt_SL:
            diffExist_METpt = True
            print 'miniAOD MET_pt < ' + str(METpt_SL) + ':', METptMini,  '||', 'nanoAOD MET_pt > ' + str(METpt_SL) + ':', METptNano
        if METptMini > METpt_AH and METptNano < METpt_AH:
            diffExist_METpt = True
            print 'miniAOD MET_pt > ' + str(METpt_AH) + ':', METptMini,  '||', 'nanoAOD MET_pt < ' + str(METpt_AH) + ':', METptNano
        if METptMini < METpt_AH and METptNano > METpt_AH:
            diffExist_METpt = True
            print 'miniAOD MET_pt < ' + str(METpt_AH) + ':', METptMini,  '||', 'nanoAOD MET_pt > ' + str(METpt_AH) + ':', METptNano
        #####################################################################
        #Check if jet pt, eta, and CSV match within specified % error range
        jetPtErr = 0.05
        jetEtaErr = 0.05
        jetCSVErr = 0.05
        #Also check to see if jet pt, eta, and CSV pass cut ID thresholds
        jetPt_Cut = 30
        jetEta_Cut = 2.4
        jetCSV_Cut = 0.8484
        #Compare miniAOD to nanoAOD jet pt values
        jetRange = min( len(miniEvents.jetAK4_pt), len(nanoEvents.Jet_pt) )
        for jetIndex in range(jetRange):
            jetPtMini = miniEvents.jetAK4_pt[jetIndex]
            jetPtNano = nanoEvents.Jet_pt[jetIndex]
            if jetPtMini != 0:
                jetPtDiff = abs( jetPtNano/float(jetPtMini) - 1 )
            if jetPtMini == 0:
                jetPtDiff = abs( float(jetPtNano) )
            if jetPtDiff > jetPtErr:
                diffExist_jetPt = True
                print 'miniAOD jet pt:', jetPtMini, '||', 'nanoAOD jet pt:', jetPtNano, '||', '%% jet_pt difference', jetPtDiff*100
            if jetPtMini > jetPt_Cut and jetPtNano < jetPt_Cut:
                diffExist_jetPt = True
                print 'miniAOD jet pt > ' + str(jetPt_Cut) + ':', jetPtMini,  '||', 'nanoAOD jet pt < ' + str(jetPt_Cut) + ':', jetPtNano
            if jetPtMini < jetPt_Cut and jetPtNano > jetPt_Cut:
                diffExist_jetPt = True
                print 'miniAOD jet pt < ' + str(jetPt_Cut) + ':', jetPtMini,  '||', 'nanoAOD jet pt > ' + str(jetPt_Cut) + ':', jetPtNano
        #Compare miniAOD to nanoAOD jet eta values 
            jetEtaMini = miniEvents.jetAK4_eta[jetIndex]
            jetEtaNano = nanoEvents.Jet_eta[jetIndex]
            if jetEtaMini != 0:
                jetEtaDiff = abs( jetEtaNano/float(jetEtaMini) - 1 )
            if jetEtaMini == 0:
                jetEtaDiff = abs( float(jetEtaNano) )
            if jetEtaDiff > jetEtaErr:
                diffExist_jetEta = True
                print 'miniAOD jet eta:', jetEtaMini, '||', 'nanoAOD jet eta:', jetEtaNano, '||', '%% jet_eta difference', jetEtaDiff*100
            if jetEtaMini > jetEta_Cut and jetEtaNano < jetEta_Cut:
                diffExist_jetEta = True
                print 'miniAOD jet eta > ' + str(jetEta_Cut) + ':', jetEtaMini,  '||', 'nanoAOD jet eta < ' + str(jetEta_Cut) + ':', jetEtaNano
            if jetEtaMini < jetEta_Cut and jetEtaNano > jetEta_Cut:
                diffExist_jetEta = True
                print 'miniAOD jet eta < ' + str(jetEta_Cut) + ':', jetEtaMini,  '||', 'nanoAOD jet eta > ' + str(jetEta_Cut) + ':', jetEtaNano
        #Compare miniAOD to nanoAOD jet CSV values 
            jetCSVMini = miniEvents.jetAK4_csv[jetIndex]
            jetCSVNano = nanoEvents.Jet_btagCSVV2[jetIndex]
            if jetCSVMini != 0:
                jetCSVDiff = abs( jetCSVNano/float(jetCSVMini) - 1 )
            if jetCSVMini == 0:
                jetCSVDiff = abs( float(jetCSVNano) )
            if jetCSVDiff > jetCSVErr:
                diffExist_jetCSV = True
                print 'miniAOD jet CSV:', jetCSVMini, '||', 'nanoAOD jet CSVV2:', jetCSVNano, '||', '%% jet_CSV difference', jetCSVDiff*100
            if jetCSVMini > jetCSV_Cut and jetCSVNano < jetCSV_Cut:
                diffExist_jetCSV = True
                print 'miniAOD jet CSV > ' + str(jetCSV_Cut) + ':', jetCSVMini,  '||', 'nanoAOD jet CSVV2 < ' + str(jetCSV_Cut) + ':', jetCSVNano
            if jetCSVMini < jetCSV_Cut and jetCSVNano > jetCSV_Cut:
                diffExist_jetCSV = True
                print 'miniAOD jet CSV < ' + str(jetCSV_Cut) + ':', jetCSVMini,  '||', 'nanoAOD jet CSVV2 > ' + str(jetCSV_Cut) + ':', jetCSVNano
        #####################################################################

    #Count number of differences between miniAOD/nanoAOD files
    if diffExist_event:
        nDiffExist = True
        nDiff_event += 1
    if diffExist_elID:
        nDiffExist = True
        nDiff_elID += 1
    if diffExist_elPt:
        nDiffExist = True
        nDiff_elPt += 1
    if diffExist_elEta:
        nDiffExist = True
        nDiff_elEta += 1
    if diffExist_muID:
        nDiffExist = True
        nDiff_muID += 1
    if diffExist_muPt:
        nDiffExist = True
        nDiff_muPt += 1
    if diffExist_muEta:
        nDiffExist = True
        nDiff_muEta += 1
    if diffExist_muIso:
        nDiffExist = True
        nDiff_muIso += 1
    if diffExist_METpt:
        nDiffExist = True
        nDiff_METpt += 1
    if diffExist_jetPt:
        nDiffExist = True
        nDiff_jetPt += 1
    if diffExist_jetEta:
        nDiffExist = True
        nDiff_jetEta += 1
    if diffExist_jetCSV:
        nDiffExist = True
        nDiff_jetCSV += 1
    #Only print event index and eventID if differences exist between miniAOD/nanoAOD event branches
    if nDiffExist:
        nDiff += 1
        print 'Event index:', i, 'Event ID:', eventID
        print '-------------------------------------------------'

print 'Comparison finished'
print 'Total number of events:', nEvents
print 'Total number of events with discrepancies:', nDiff, 'Percent of events with discrepancies:', (nDiff/float(nEvents))*100
print 'Total number of miniAOD events missing in nanoAOD file', nDiff_event, 'Percent of miniAOD events missing in nanoAOD file:', (nDiff_event/float(nEvents))*100
print 'Total number of events with different electron IDs:', nDiff_elID, 'Percent of events with different electron IDs:', (nDiff_elID/float(nEvents))*100
print 'Total number of events with different electron_pt:', nDiff_elPt, 'Percent of events with different electron_pt:', (nDiff_elPt/float(nEvents))*100
print 'Total number of events with different electron_eta:', nDiff_elEta, 'Percent of events with different electron_eta:', (nDiff_elEta/float(nEvents))*100
print 'Total number of events with different muon IDs:', nDiff_muID, 'Percent of events with different muon IDs:', (nDiff_muID/float(nEvents))*100
print 'Total number of events with different muon_pt:', nDiff_muPt, 'Percent of events with different muon_pt:', (nDiff_muPt/float(nEvents))*100
print 'Total number of events with different muon_eta:', nDiff_muEta, 'Percent of events with different muon_eta:', (nDiff_muEta/float(nEvents))*100
print 'Total number of events with different muon_iso:', nDiff_muIso, 'Percent of events with different muon_iso:', (nDiff_muIso/float(nEvents))*100
print 'Total number of events with different MET pt:', nDiff_METpt, 'Percent of events with different MET pt:', (nDiff_METpt/float(nEvents))*100
print 'Total number of events with different jet_pt:', nDiff_jetPt, 'Percent of events with different jet_pt:', (nDiff_jetPt/float(nEvents))*100
print 'Total number of events with different jet_eta:', nDiff_jetEta, 'Percent of events with different jet_eta:', (nDiff_jetEta/float(nEvents))*100
print 'Total number of events with different jet_CSV:', nDiff_jetCSV, 'Percent of events with different jet_CSV:', (nDiff_jetCSV/float(nEvents))*100
