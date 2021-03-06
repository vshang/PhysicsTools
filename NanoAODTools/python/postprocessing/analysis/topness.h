#pragma once

#include "TFitter.h"
#include "TMath.h"
#include <vector>
#include <math.h>
#include "TLorentzVector.h"
#include "JetUtil.h"
#include <iostream>

using namespace std;

// comments, see .C file

float topnessMinimization(TLorentzVector met, TLorentzVector lep, TLorentzVector bjet1, TLorentzVector bjet2, int version=1);

double topnessFunction(double pwx_, double pwy_, double pwz_, double pnz_,
                       double plx_, double ply_, double plz_, double ple_,
                       double pb1x_, double pb1y_, double pb1z_, double pb1e_,
                       double pb2x_, double pb2y_, double pb2z_, double pb2e_,
                       double pmx_, double pmy_, double pmz_, double pme_);

void minuitFunctionWrapper(int& nDim, double* gout, double& result, double* par, int flg);

double topnessFunctionV1(double pwx_, double pwy_, double pwz_, double pnz_,
                       double plx_, double ply_, double plz_, double ple_,
                       double pb1x_, double pb1y_, double pb1z_, double pb1e_,
                       double pb2x_, double pb2y_, double pb2z_, double pb2e_,
                       double pmx_, double pmy_, double pmz_, double pme_);

void minuitFunctionWrapperV1(int& nDim, double* gout, double& result, double* par, int flg);


float CalcTopness( int version, TLorentzVector MET,       TLorentzVector lep, vector<TLorentzVector> bjets,  vector<TLorentzVector> addjets);
float CalcTopness_(int version, float MET, float METphi, TLorentzVector lep, vector<TLorentzVector> bjets,  vector<TLorentzVector> addjets);

//#endif
