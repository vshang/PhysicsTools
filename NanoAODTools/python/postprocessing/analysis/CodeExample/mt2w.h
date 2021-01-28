#ifndef MT2W_H
#define MT2W_H

#include "mt2w_bisect.h"
#include <vector>
#include "Math/LorentzVector.h"
#include "TMath.h"
#include "JetUtil.h"

using namespace std;

typedef ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > LorentzVector;

double mt2wWrapper(LorentzVector& lep, LorentzVector& jet_o, LorentzVector& jet_b, float met, float metphi);

//float CalculateMT2W (vector<LorentzVector> bjet, LorentzVector lep, LorentzVector metlv    );
float CalcMT2W( vector<LorentzVector> bjets, vector<LorentzVector> addjets,  LorentzVector lep, LorentzVector metlv    );
float CalcMT2W_(vector<LorentzVector> bjets, vector<LorentzVector> addjets,  LorentzVector lep, float met, float metphi);

#endif
