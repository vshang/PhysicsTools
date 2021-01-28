#include "example.h"


int main(){
    vector<LorentzVector> jets;//lorentz vector of all jets
    vector<float> btag;// btag discriminator value - between 0-1 the higher the more likely a jet is a b-tagged jet
    vector<bool> jid;//passes jetID requirement, is true >99%
    
    float btagged = 0.90;//for jets with values above this are considered

    /* Define the event */
    float met = 60.164054871;
    float metphi = 0.61534303427;

    // Identified lepton
    LorentzVector lep(15.622756958,29.060853958,1.0357201099,33.010417938);

    // Jets, b-tagging, and jet-resolution
    //LorentzVector j1(-154.34786987,-95.917778015,-502.48416138,535.081604);
    LorentzVector j1(100, 50, 50, 100);
    float b1 = 0.675;
    bool id1 = true;

    //LorentzVector j2(9.410118103,-52.559776306,150.97743225,160.78645325);
    LorentzVector j2(100, 50, 50, 100);
    float b2 = 0.564;
    bool id2 = true;

    //LorentzVector j3(49.700946808,-8.7576665878,-108.4271698,120.35206604);
    LorentzVector j3(100, 50, 50, 100);
    float b3 = 0.987;
    bool id3 = true;

    //LorentzVector j4(-42.24382019,20.526990891,30.697292328,56.885437012);
    LorentzVector j4(100, 5, 50, 100);
    float b4 = 0.125;
    bool id4 = true;

    //LorentzVector j5(42.017311096,-12.269251823,34.797512054,57.173427582);
    LorentzVector j5(100, 50, 50, 100);
    float b5 = 0.799;
    bool id5 = true;

    jets.push_back(j1); jets.push_back(j2); jets.push_back(j3); jets.push_back(j4); jets.push_back(j5);
    btag.push_back(b1); btag.push_back(b2); btag.push_back(b3); btag.push_back(b4); btag.push_back(b5);
    jid.push_back(id1); jid.push_back(id2); jid.push_back(id3); jid.push_back(id4); jid.push_back(id5);

    vector<int> jetIndexSortedBtag = JetUtil::JetIndexCSVsorted(btag, jets, jid, 30., 2.4, true);
    for(unsigned int i = 0; i<jetIndexSortedBtag.size(); ++i){
      cout << "jetIndex " << "i = " << jetIndexSortedBtag[i] << endl;
    }
    
    vector<LorentzVector> bjets; vector<LorentzVector> additionaljets;
    for(unsigned int idx = 0; idx<jetIndexSortedBtag.size(); ++idx){
        if(btag.at(jetIndexSortedBtag[idx])>btagged) bjets.push_back(jets.at(jetIndexSortedBtag[idx]) );
        else if(bjets.size()<=1 && (bjets.size()+additionaljets.size())<3) additionaljets.push_back(jets.at(jetIndexSortedBtag[idx]) );
    }

    cout << "len(bjets) = " << bjets.size() << endl;
    cout << "len(additionaljets) = " << additionaljets.size() << endl;

    // Call MT2w and chi2 calculations.
    float MT2W = CalcMT2W_(bjets,additionaljets,lep,met, metphi);
    float tmod = CalcTopness_(1,met,metphi,lep,bjets,additionaljets);
    float tmod2 = CalcTopness_(2,met,metphi,lep,bjets,additionaljets);

    // Print results.
    cout << "MT2W = " << MT2W << endl;
    cout << "tmod = " << tmod << endl;
    cout << "tmod2 = " << tmod2 << endl;

    return 0.;
}
