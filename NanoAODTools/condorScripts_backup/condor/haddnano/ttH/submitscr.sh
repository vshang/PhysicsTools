#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="ttH_2016_ModuleCommonSkim_12242022"
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
executable = ./runhaddnano.sh
output = ${RUNDIR}/runhaddnano.stdoutD
error = ${RUNDIR}/runhaddnano.stderr
log = ${RUNDIR}/runhaddnano.condor_log
requestdisk = 50G
requestmemory = 16G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/scripts/haddnano.py,/nfs_scratch/vshang/condor/haddnano/filelist_signal.txt,/nfs_scratch/vshang/condor/haddnano/filterList_signal.py
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"
