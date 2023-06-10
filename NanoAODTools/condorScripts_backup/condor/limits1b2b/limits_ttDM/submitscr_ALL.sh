#!/bin/sh
#Script to submit jobs to run combine code in Analysis.tar.gz
massPoints=("50" "100" "150" "200" "250" "300" "350" "400" "450" "500")
mediatorTypes=("scalar" "pseudo")

echo "Submitting combine jobs for AH+SL+DL channel..."

for med in ${mediatorTypes[@]}; do
    for mass in ${massPoints[@]}; do
	echo $med $mass
	cd ${med}_${mass}
	./submitscr_ALL.sh
	ls
	cd ..
    done
done

echo "scalar 125"
cd scalar_125
sh submitscr_ALL.sh
ls
cd ..

echo "Finished submitting combine jobs for AH+SL+DL channel."
