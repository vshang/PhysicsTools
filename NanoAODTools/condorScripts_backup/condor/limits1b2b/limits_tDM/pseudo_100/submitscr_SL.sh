#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="pseudo_100_SL"
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
executable = ./runcombine_SL.sh
output = ${RUNDIR}/runcombine_SL.stdoutD
error = ${RUNDIR}/runcombine_SL.stderr
log = ${RUNDIR}/runcombine_SL.condor_log
requestdisk = 20G
requestmemory = 16G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_8_0_26_patch1/src/HiggsAnalysis.tar.gz,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_8_0_26_patch1/src/Analysis_tDM.tar.gz
container_image = /cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"
