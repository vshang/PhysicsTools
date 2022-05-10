#ifndef JETUTIL_H
#define JETUTIL_H


#include "TMath.h"
#include <vector>
#include "TLorentzVector.h"
#include <math.h>

using namespace std;

namespace JetUtil
{

  // comments, see .C
  double round(double input, int digits);
  bool   CompareLV(TLorentzVector lv1, TLorentzVector lv2);
  float  DeltaPhi(float phi1, float phi2);
  float  deltaPhi(TLorentzVector jet1, TLorentzVector jet2);
  float  DeltaR(float phi1, float phi2, float eta1, float eta2);
  float  deltaR(TLorentzVector jet1, TLorentzVector jet2);

  vector<TLorentzVector> BJetSelector(vector<TLorentzVector > jets, vector<float> btagvalues, float bjetdiscr=0.890, unsigned int minbjets=2, unsigned int minaddbjets=2, int versionAddjets=2);
  vector<int>           JetIndexCSVsorted(vector<float> btagvalues, vector<TLorentzVector > jets, vector<bool> jid, float minpt=30., float maxeta=2.5, bool passjid=true);

}//end namespace 

#endif
