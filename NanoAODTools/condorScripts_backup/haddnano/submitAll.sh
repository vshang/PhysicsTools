#!/bin/sh
#Script to submit jobs to hadd all samples
signalMC=("tChan" "tWChan" "ttDM")
years=("2016" "2017" "2018")

#First submit jobs for private t/ttDM signal samples
for signal in ${signalMC[@]}; do
    echo $signal
    cd ${signal}
    for year in ${years[@]}; do
	./submitscr${year}.sh
    done
    ls
    cd ..
done

#Then submit jobs for 2016 ttH nanoAODv7 signal samples
cd ttH
./submitscr.sh
ls
cd ..

#Finally submit jobs for rest of Data/MC samples (from CRAB)
# for year in ${years[@]}; do
#     ./submitscr${year}.sh
#     ls
# done

echo "Finished submitting jobs to hadd samples"
