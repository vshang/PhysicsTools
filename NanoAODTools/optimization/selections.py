#! /usr/bin/env python

#(abs(lepton1_eta)<1.4442 || abs(lepton1_eta)>1.566) && 
#0.9535

selection = {
    
    # # Hadronic category
    # #Cut-flow
    # "AH0lcutflow_ps" : "isZtoNN && MET_pt>250. && nJets>=3 && nBTagJets>=1",
    # "AH0lcutflow_psDphi" : "isZtoNN && MET_pt>250. && nJets>=3 && MinDPhi12>1 && nBTagJets>=1",
    # "AH0lcutflow_psDphiMtb" : "isZtoNN && MET_pt>250. && nJets>=3 && MinDPhi12>1 && mTb>180 && nBTagJets>=1",
    # "AH0lcutflow_psDphiMtb_1b" : "isZtoNN && MET_pt>250. && nJets>=3 && MinDPhi12>1 && mTb>180 && nBTagJets==1",
    # "AH0lcutflow_psDphiMtb_2b" : "isZtoNN && MET_pt>250. && nJets>=3 && MinDPhi12>1 && mTb>180 && nBTagJets>=2",
    # "AH0lcutflow_psDphiMtbHt" : "isZtoNN && MET_pt>250. && nJets>=3 && MinDPhi12>1 && mTb>180 && Jet1_pt/HT<0.5 && nBTagJets>=2",

    ##Presel - 2b
    #"AH0l2bps" : "isZtoNN && MET_pt>250. && nJets>=3 && nBTagJets>=2",

    # #Presel - 1b
    # "AH0lpsfs1b" : "isZtoNN && MET_pt>250. && MinDPhi12>1 && mTb>180 && nBTagJets==1",
    # "AH0lpsfs2b" : "isZtoNN && MET_pt>250. && MinDPhi12>1 && mTb>180 && Jet1_pt/HT<0.5 && nBTagJets>=2",
    # "AH0l0fps" : "isZtoNN && MET_pt>250. && nJets>=3 && nBTagJets==1 && nForwardJets==0",
    # "AH0l1fps" : "isZtoNN && MET_pt>250. && nJets>=3 && nBTagJets==1 && nForwardJets>=1",

    # #SRs - 2b
    "AH0l2bSR" : "isZtoNN && MET_pt>250. && nJets>=3 && MinDPhi12>1 && mTb>180 && Jet1_pt/HT<0.5 && nBTagJets>=2",#btag

    # #SRs - 1b
    "AH0l0fSR" : "isZtoNN && MET_pt>250. && nJets>=3 && nBTagJets==1 && nForwardJets==0 && MinDPhi12>1 && mTb>180",
    "AH0l1fSR" : "isZtoNN && MET_pt>250. && nJets>=3 && nBTagJets==1 && nForwardJets>=1 && MinDPhi12>1 && mTb>180",

    # # # # #V CR
    # # #"AH0lVR" : "isZtoNN && nElectrons==0 && nMuons==0 && MET_pt>250. && nJets>=3 && nBTagJets==0 && MinDPhi12>1.",

    #W CR
    "AH1eWR" : "isWtoEN && nElectrons==1 && nMuons==0 && nTaus==0 && MET_pt>250. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && mT<160. && nJets>=3 && nBTagJets==0",
    "AH1mWR" : "isWtoMN && nElectrons==0 && nMuons==1 && nTaus==0 && MET_pt>250. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && mT<160. && nJets>=3 && nBTagJets==0",
    
    # #Znunu CR
    "AH2eZR" : "isZtoEE && FakeMET_pt>250. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && (mZ>60. && mZ<120.) && nJets>=3  && Lepton2_pt>30. && abs(Lepton2_eta)<2.1 && Lepton2_id==4 && nMuons==0 && nElectrons==2 && nBTagJets==0",
    "AH2mZR" : "isZtoMM && FakeMET_pt>250. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && (mZ>60. && mZ<120.) && nJets>=3 && Lepton2_pt>30. && Lepton2_id==4 && Lepton2_pfIso<0.15 && nMuons==2 && nElectrons==0  && nBTagJets==0",

    #tt(1l) CR
    "AH1eTR" : "isWtoEN && MET_pt>250. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && mT<160. && nJets>=3 && nBTagJets>=1 && nElectrons==1 && nMuons==0 && MinDPhi12>1.",
    "AH1mTR" : "isWtoMN && MET_pt>250. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && mT<160. && nJets>=3 && nBTagJets>=1  && nElectrons==0 && nMuons==1 && MinDPhi12>1.",

    # "AH1eTR_dphi" : "isWtoEN && MET_pt>250. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && mT<160. && nJets>=3 && nBTagJets>=1 && nElectrons==1 && nMuons==0 && MinDPhi>1.",
    # "AH1mTR_dphi" : "isWtoMN && MET_pt>250. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && mT<160. && nJets>=3 && nBTagJets>=1  && nElectrons==0 && nMuons==1 && MinDPhi>1.",


    # Semileptonic category
    # # #Cut flow
    "SL1lps" : "((isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && (nJets>=2 && MET_pt>160. && nBTagJets>=1)",
    "SL1lpsmt" : "((isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && (nJets>=2 && MET_pt>160. && mT>160 && nBTagJets>=1)",
    "SL1lpsmtmt2w" : "((isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && (nJets>=2 && MET_pt>160. && mT>160 && mT2>200 && nBTagJets>=1)",

    # "SL1lpsmtmt2wdphi" : "((isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && (nJets>=2 && MET_pt>160. && mT>160 && mT2>200 && MinDPhi12>1.2 && nBTagJets>=1)",
    # "SL1lpsmtmt2wdphimtb" : "((isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && (nJets>=2 && MET_pt>160. && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180 && nBTagJets>=1)",

    # "SL1lpsmtmt2wdphimtb1b" : "((isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && (nJets>=2 && MET_pt>160. && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180 && nBTagJets==1)",
    # "SL1lpsmtmt2wdphimtb2b" : "((isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && (nJets>=2 && MET_pt>160. && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180 && nBTagJets>=2)",

    # # #Presel - 2b
    # "SL1lpsfs1b" : "((isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>26. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>26. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && nBTagJets==1 && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180",
    # "SL1lpsfs2b" : "((isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>26. && Lepton1_pfIso<0.15 && Lepton1_id==4) || (isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>26. && abs(Lepton1_eta)<2.1 && Lepton1_id==4)) && nBTagJets>=2 && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180",

    # "SL1m2bps" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets>=2",
    # "SL1m2bpsmt" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets>=2 && mT>160",
    # "SL1m2bpsmt2" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets>=2 && mT>160 && mT2>200",

    # "SL1e2bps" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets>=2 ",
    # "SL1e2bpsmt" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets>=2 && mT>160",
    # "SL1e2bpsmt2" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets>=2 && mT>160 && mT2>200",

    # #Presel - 1b
    "SL1m0fps" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets==0",
    "SL1m0fpsmt" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets==0 && mT>160",
    "SL1m0fpsmt2" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets==0 && mT>160 && mT2>200",

    # "SL1m1fps" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets>=1",
    # "SL1m1fpsmt" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets>=1 && mT>160",
    # "SL1m1fpsmt2" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets>=1 && mT>160 && mT2>200",

    # "SL1e0fps" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets==0 ",
    # "SL1e0fpsmt" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets==0 && mT>160",
    # "SL1e0fpsmt2" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets==0 && mT>160 && mT2>200",

    # "SL1e1fps" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets>=1 ",
    # "SL1e1fpsmt" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets>=1 && mT>160",
    # "SL1e1fpsmt2" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets>=1 && mT>160 && mT2>200",

    #SR - 2b
    "SL1m2bSR" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets>=2 && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180",
    "SL1e2bSR" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets>=2 && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180",

    #SR - 1b
    "SL1m0fSR" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets==0 && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180",
    "SL1m1fSR" : "isWtoMN && nElectrons==0 && nMuons==1 && MET_pt>160. && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets>=1 && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180",

    "SL1e0fSR" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets==0 && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180",
    "SL1e1fSR" : "isWtoEN && nElectrons==1 && nMuons==0 && MET_pt>160. && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && nJets>=2 && nBTagJets==1 && nForwardJets>=1 && mT>160 && mT2>200 && MinDPhi12>1.2 && mTb>180",
    
    #W CR
    "SL1mWR"  : "isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4  && nJets>=2 && nBTagJets==0 && MET_pt>160. && mT>160",
    "SL1eWR"  : "isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4  && nJets>=2 && nBTagJets==0 && MET_pt>160. && mT>160",    
    #HF
    # "SL1m0fWR"  : "isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4  && nJets>=2 && nBTagJets==0 && MET_pt>160. && mT>160 && nForwardJets==0",
    # "SL1m1fWR"  : "isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4  && nJets>=2 && nBTagJets==0 && MET_pt>160. && mT>160 && nForwardJets>=1",
    # "SL1e0fWR"  : "isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4  && nJets>=2 && nBTagJets==0 && MET_pt>160. && mT>160 && nForwardJets==0",    
    # "SL1e1fWR"  : "isWtoEN && nElectrons==1 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4  && nJets>=2 && nBTagJets==0 && MET_pt>160. && mT>160 && nForwardJets>=1",    

    # "SL1mWRmt"  : "isWtoMN && nElectrons==0 && nMuons==1 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4  && nJets>=2 && nBTagJets==0 && MET_pt>160.",

    #tt(2l) CR
    "SL2mTR" : "isZtoMM && nElectrons==0 && nMuons==2 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && Lepton2_pt>30. && Lepton2_pfIso<0.15 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160.",
    "SL2eTR" : "isZtoEE && nElectrons==2 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && Lepton2_pt>30. && abs(Lepton2_eta)<2.1 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160.",
    "SL1e1mTR" : "isTtoEM && nElectrons==1 && nMuons==1 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && Lepton2_pt>30. && Lepton2_pfIso<0.15 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160.", 

    # #HF
    # "SL2m0fTR" : "isZtoMM && nElectrons==0 && nMuons==2 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && Lepton2_pt>30. && Lepton2_pfIso<0.15 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160. && nForwardJets==0",
    # "SL2m1fTR" : "isZtoMM && nElectrons==0 && nMuons==2 && Lepton1_pt>30. && Lepton1_pfIso<0.15 && Lepton1_id==4 && Lepton2_pt>30. && Lepton2_pfIso<0.15 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160. && nForwardJets>=1",

    # "SL2e0fTR" : "isZtoEE && nElectrons==2 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && Lepton2_pt>30. && abs(Lepton2_eta)<2.1 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160. && nForwardJets==0",
    # "SL2e1fTR" : "isZtoEE && nElectrons==2 && nMuons==0 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && Lepton2_pt>30. && abs(Lepton2_eta)<2.1 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160. && nForwardJets>=1",

    # "SL1e1m0fTR" : "isTtoEM && nElectrons==1 && nMuons==1 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && Lepton2_pt>30. && Lepton2_pfIso<0.15 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160. && nForwardJets==0", 
    # "SL1e1m1fTR" : "isTtoEM && nElectrons==1 && nMuons==1 && Lepton1_pt>30. && abs(Lepton1_eta)<2.1 && Lepton1_id==4 && Lepton2_pt>30. && Lepton2_pfIso<0.15 && Lepton2_id==4 && nJets>=2 && nBTagJets>=1 && MET_pt>160. && nForwardJets>=1", 

}

