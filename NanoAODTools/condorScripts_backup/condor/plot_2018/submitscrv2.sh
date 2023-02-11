#!/bin/sh
#Script to submit jobs to run plot.py
catAH=("AH0l0fSR" "AH0l1fSR" "AH0l2bSR" "AH0lQR")
catSL=("SL1l0fT1SR" "SL1l0fT2SR" "SL1l0fT3SR" "SL1l1fT1SR" "SL1l1fT2SR" "SL1l1fT3SR" "SL1l2bT1SR" "SL1l2bT2SR" "SL1l2bT3SR" "SL2lTR" "SL1lWR" "AH1lTR" "AH1lWR" "AH2lZR")
versions=("v1" "v2")

for cat in ${catAH[@]}; do
    echo $cat
    cd ${cat}
    ./submitscr_${cat}v1.sh
    ./submitscr_${cat}v2.sh
    ls
    cd ..
done

for cat in ${catSL[@]}; do
    echo $cat
    cd ${cat}
    if [ $cat = "SL2lTR" ]; then
	./submitscr_SL1e1mTRv1.sh
	./submitscr_SL1e1mTRv2.sh
    fi
    ./submitscr_${cat/l/e}v1.sh
    ./submitscr_${cat/l/e}v2.sh
    ./submitscr_${cat/l/m}v1.sh
    ./submitscr_${cat/l/m}v2.sh
    ls
    cd ..
done

echo "Finished submitting jobs for plot.py"
