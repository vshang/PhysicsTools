#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="ModuleCommonSkim_09222021_UL2017"
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
executable = ./runhaddnanoUL2017.sh
output = ${RUNDIR}/runhaddnanoUL2017.stdoutD
error = ${RUNDIR}/runhaddnanoUL2017.stderr
log = ${RUNDIR}/runhaddnanoUL2017.condor_log
requirements = HAS_CMS_HDFS
requestdisk = 200G
requestmemory = 32G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/scripts/haddnano.py
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"
