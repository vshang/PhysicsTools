#include "mt2w.h"


// This funcion is a wrapper for mt2w_bisect etc that takes LorentzVectors instead of doubles
double mt2wWrapper(LorentzVector& lep, LorentzVector& jet_o, LorentzVector& jet_b, float met, float metphi){

    // same for all MT2x variables
    double metx = met * cos( metphi );
    double mety = met * sin( metphi );

    double pl[4];     // Visible lepton
    double pb1[4];    // bottom on the same side as the visible lepton
    double pb2[4];    // other bottom, paired with the invisible W
    double pmiss[3];  // <unused>, pmx, pmy   missing pT

    int mydigit = 3;
    pl[0]    = JetUtil::round(lep.E(),   mydigit);
    pl[1]    = JetUtil::round(lep.Px(),  mydigit);
    pl[2]    = JetUtil::round(lep.Py(),  mydigit);
    pl[3]    = JetUtil::round(lep.Pz(),  mydigit);
    pb1[1]   = JetUtil::round(jet_o.Px(),mydigit);
    pb1[2]   = JetUtil::round(jet_o.Py(),mydigit);
    pb1[3]   = JetUtil::round(jet_o.Pz(),mydigit);
    pb2[1]   = JetUtil::round(jet_b.Px(),mydigit);
    pb2[2]   = JetUtil::round(jet_b.Py(),mydigit);
    pb2[3]   = JetUtil::round(jet_b.Pz(),mydigit);
    pmiss[0] = JetUtil::round(0.,        mydigit);
    pmiss[1] = JetUtil::round(metx,      mydigit);
    pmiss[2] = JetUtil::round(mety,      mydigit);

    pb1[0]   = JetUtil::round(jet_o.E(), mydigit);
    pb2[0]   = JetUtil::round(jet_b.E(), mydigit);

    mt2w_bisect::mt2w mt2w_event;
    mt2w_event.set_momenta(pl, pb1, pb2, pmiss);

    return mt2w_event.get_mt2w();
}



// 13 TeV implementation - full calculation needs JetUtil CSV ordering
float CalcMT2W(vector<LorentzVector> bjets, vector<LorentzVector> addjets,  LorentzVector lep, LorentzVector metlv){
  float met = metlv.Pt();
  float metphi = metlv.Phi();
  return CalcMT2W_(bjets,addjets,lep,met,metphi);
}

// 13 TeV implementation - full calculation needs JetUtil CSV ordering
float CalcMT2W_(vector<LorentzVector> bjets, vector<LorentzVector> addjets,  LorentzVector lep, float met, float metphi){
  if((bjets.size()+addjets.size())<2) return -999.;
  float min_mt2w = 9999;
  for (unsigned int i=0; i<bjets.size(); ++i){
    for (unsigned int j=i+1; j<bjets.size(); ++j){
      float c_mt2w = mt2wWrapper(lep, bjets[i], bjets[j], met, metphi);
      if (c_mt2w < min_mt2w)  min_mt2w = c_mt2w;
      c_mt2w = mt2wWrapper(lep, bjets[j], bjets[i], met, metphi);
      if (c_mt2w < min_mt2w)  min_mt2w = c_mt2w;
    }
    for (unsigned int j=0; j<addjets.size(); ++j){
      float c_mt2w = mt2wWrapper(lep, bjets[i], addjets[j], met, metphi);
      if (c_mt2w < min_mt2w)  min_mt2w = c_mt2w;
      c_mt2w = mt2wWrapper(lep, addjets[j], bjets[i], met, metphi);
      if (c_mt2w < min_mt2w)  min_mt2w = c_mt2w;
    }
  }
  if(bjets.size()==0){
    for (unsigned int j=1; j<addjets.size(); ++j){
      float c_mt2w = mt2wWrapper(lep, addjets[0], addjets[j], met, metphi);
      if (c_mt2w < min_mt2w)  min_mt2w = c_mt2w;
      c_mt2w = mt2wWrapper(lep, addjets[j], addjets[0], met, metphi);
      if (c_mt2w < min_mt2w)  min_mt2w = c_mt2w;
    }
  }
  return min_mt2w;
}
