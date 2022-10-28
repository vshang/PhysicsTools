#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="tWChan_2018_ModuleCommonSkim_09242022"
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
executable = ./runhaddnano2018.sh
output = ${RUNDIR}/runhaddnano2018.stdoutD
error = ${RUNDIR}/runhaddnano2018.stderr
log = ${RUNDIR}/runhaddnano2018.condor_log
requestdisk = 200G
requestmemory = 32G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/scripts/haddnano.py,/nfs_scratch/vshang/condor/haddnano/filelist_signal.txt,/nfs_scratch/vshang/condor/haddnano/filterList_signal.py
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"
