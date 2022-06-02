#!/bin/sh
#Script to merge binned histogram root files with systematics for all categories using hadd
#Remember to use spaces to seperate elements of list, not commas
#catSL=("SL1l0fSR" "SL1l1fSR" "SL1l2bSR" "SL1l0fT1SR" "SL1l0fT2SR" "SL1l0fT3SR" "SL1l1fT1SR" "SL1l1fT2SR" "SL1l1fT3SR" "SL1l2bT1SR" "SL1l2bT2SR" "SL1l2bT3SR" "SL2lTR" "SL1lWR")
catAH=("AH0l0fSR" "AH0l1fSR" "AH0l2bSR" "AH1lTR" "AH1lWR" "AH2lZR" "AH0lQR")
catSL=("SL1l0fT1SR" "SL1l0fT2SR" "SL1l0fT3SR" "SL1l1fT1SR" "SL1l1fT2SR" "SL1l1fT3SR" "SL1l2bT1SR" "SL1l2bT2SR" "SL1l2bT3SR" "SL2lTR" "SL1lWR")
#catAH=("AH0l0fSR" "AH0l1fSR" "AH0l2bSR" "AH0lQR")
binsSL=("250_290" "290_330" "330_370" "370_410" "410_450" "450_490" "490_530")
binsAH=("250_270" "270_290" "290_310" "310_330" "330_350" "350_370" "370_390" "390_410" "410_430" "430_450" "450_470" "470_490" "490_510" "510_530" "530_550")
#binsAH=()

for cat in ${catSL[@]}; do
    for bin in ${binsSL[@]}; do
	echo $cat $bin
	outputRootFile="${cat}bin_${bin}.root"
	rootFile1="/hdfs/store/user/vshang/binnedHists/ModuleCommonSkim_03092022/2018/combined_elemuon_channels/default/${cat}bin_${bin}.root"
	rootFile2="/hdfs/store/user/vshang/binnedHists/ModuleCommonSkim_03092022/2018/combined_elemuon_channels/test/${cat}bin_${bin}.root"
	hadd ${outputRootFile} ${rootFile1} ${rootFile2}
    done
done

for cat in ${catAH[@]}; do
    for bin in ${binsAH[@]}; do
	echo $cat $bin
	outputRootFile="${cat}bin_${bin}.root"
	rootFile1="/hdfs/store/user/vshang/binnedHists/ModuleCommonSkim_03092022/2018/combined_elemuon_channels/default/${cat}bin_${bin}.root"
	rootFile2="/hdfs/store/user/vshang/binnedHists/ModuleCommonSkim_03092022/2018/combined_elemuon_channels/test/${cat}bin_${bin}.root"
	hadd ${outputRootFile} ${rootFile1} ${rootFile2}
    done
done
