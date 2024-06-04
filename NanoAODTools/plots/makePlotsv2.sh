#!/bin/sh
#Script to make plots with plot.py
#catAH=("AH0l0fSR" "AH0l1fSR" "AH0l2bSR" "AH1lTR" "AH1lWR" "AH2lZR" "AH0lQR" "AH0lZR")
#catAH=("AH0l0fSR" "AH0l1fSR" "AH0l2bSR" "AH1eTR" "AH1eWR" "AH2eZR" "AH1mTR" "AH1mWR" "AH2mZR" "AH0lQR")
#catAH=("AH0l0fSR" "AH0l1fSR" "AH0l2bSR" "AH0lSR")
#catAH=("AH" "AH1lTR" "AH1lWR" "AH2lZR" "AH0lQR" "AH0lZR")
#catAH=("AH" "AH0l0fSR" "AH0l1fSR" "AH0l2bSR")
#catAH=("AH")
catAH=()
#catSL=("SL1l0fT1SR" "SL1l0fT2SR" "SL1l0fT3SR" "SL1l1fT1SR" "SL1l1fT2SR" "SL1l1fT3SR" "SL1l2bT1SR" "SL1l2bT2SR" "SL1l2bT3SR" "SL2lTR" "SL1lWR")
#catSL=("SL1e0fT1SR" "SL1e0fT2SR" "SL1e0fT3SR" "SL1e1fT1SR" "SL1e1fT2SR" "SL1e1fT3SR" "SL1e2bT1SR" "SL1e2bT2SR" "SL1e2bT3SR" "SL2eTR" "SL1e1mTR" "SL1eWR" "SL1m0fT1SR" "SL1m0fT2SR" "SL1m0fT3SR" "SL1m1fT1SR" "SL1m1fT2SR" "SL1m1fT3SR" "SL1m2bT1SR" "SL1m2bT2SR" "SL1m2bT3SR" "SL2mTR" "SL1mWR")
catSL=("SL1l0fT1SR" "SL1l0fT2SR" "SL1l1fT1SR" "SL1l1fT2SR" "SL1l2bT1SR" "SL1l2bT2SR" "SL2lTR" "SL1lWR")
#catSL=("SL1l0fT1SR" "SL1l0fT2SR" "SL1l1fT1SR" "SL1l1fT2SR" "SL1l2bT1SR" "SL1l2bT2SR")
#catSL=("SL" "SL1l0fSR" "SL1l1fSR" "SL1l2bSR" "SL2lTR" "SL1lWR")
#catSL=("SL1lWR")
#catSL=()
#years=("2016" "2017" "2018")
#years=("2017" "2018")
years=("2018")

for year in ${years[@]}; do
    for cat in ${catAH[@]}; do
    	echo $cat$year
	nohup python plot2018.py -c ${cat} -f > ${cat}${year}.out &
    done
    for cat in ${catSL[@]}; do
	echo $cat$year
	nohup python plot2018.py -c ${cat} -f > ${cat}${year}.out &
    done
done

echo "Finished starting jobs for plots with plot.py"
