#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="countEvents_05102023_2016"
    if [ ! -d "${RUNDIR}" ]; then 
	echo "using ${RUNDIR}"
	break
    fi
done

# actually create the directory
mkdir "${RUNDIR}"

# create the submit description file
SUBMIT="${RUNDIR}/submit"
cat > "${SUBMIT}" << EOF
executable = ./runhaddnano2016.sh
output = ${RUNDIR}/runhaddnano2016.stdoutD
error = ${RUNDIR}/runhaddnano2016.stderr
log = ${RUNDIR}/runhaddnano2016.condor_log
requestdisk = 300G
requestmemory = 32G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/scripts/haddnano.py,/nfs_scratch/vshang/condor/haddnano/countlist.txt,/nfs_scratch/vshang/condor/haddnano/filterList.py
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"
