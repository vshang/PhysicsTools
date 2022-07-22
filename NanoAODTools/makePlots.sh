#!/bin/sh
#Script to make plots with plot.py
catAH=("AH0l0fSR" "AH0l1fSR" "AH0l2bSR" "AH1lTR" "AH1lWR" "AH2lZR" "AH0lQR")
#catAH=("AH1lTR" "AH1lWR" "AH2lZR" "AH0lQR")
catSL=("SL1l0fT1SR" "SL1l0fT2SR" "SL1l0fT3SR" "SL1l1fT1SR" "SL1l1fT2SR" "SL1l1fT3SR" "SL1l2bT1SR" "SL1l2bT2SR" "SL1l2bT3SR" "SL2lTR" "SL1lWR")
#catSL=("SL2lTR" "SL1lWR")
#years=("2016" "2017" "2018")
years=("2016")

for year in ${years[@]}; do
    for cat in ${catAH[@]}; do
    	echo $cat$year
	nohup python plots/plot.py -c ${cat} -y ${year} -p > ${cat}${year}.out &
    	#nohup python plots/plot.py -c ${cat} -y ${year} -p > ${cat}${year}_ttDM_MChi1_MPhi100_scalar.out &
    done
    for cat in ${catSL[@]}; do
	echo $cat$year
	nohup python plots/plot.py -c ${cat} -y ${year} -p > ${cat}${year}.out &
	#nohup python plots/plot.py -c ${cat} -y ${year} -p > ${cat}${year}_ttDM_MChi1_MPhi100_scalar.out &
    done
done

echo "Finished making plots with plot.py"
