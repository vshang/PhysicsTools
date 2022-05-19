#!/bin/sh
#Script to submit jobs to run combine code in Analysis.tar.gz
massPoints=("50" "100" "150" "200" "250" "300" "350" "400" "450" "500")
mediatorTypes=("scalar" "pseudo")
channel = "ALL"

echo "Submitting combine jobs for $channel channel..."

for med in ${mediatorTypes[@]}; do
    for mass in ${massPoints[@]}; do
	echo $med $mass
	cd ${med}_${mass}
	./submitscr_${channel}.sh
	ls
	cd ..
    done
done

echo "scalar 125"
cd scalar_125
./submitscr_{channel}.sh
ls
cd ..

echo "Finished submitting jobs for combine."
