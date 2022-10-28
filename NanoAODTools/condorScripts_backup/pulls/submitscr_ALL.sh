#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="RunII_ttDM_Mchi1_Mphi125_scalar_pulls_ALL"
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
executable = ./runpulls_ALL.sh
output = ${RUNDIR}/runpulls_ALL.stdoutD
error = ${RUNDIR}/runpulls_ALL.stderr
log = ${RUNDIR}/runpulls_ALL.condor_log
requestdisk = 100G
requestmemory = 64G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_8_0_26_patch1/src/HiggsAnalysis.tar.gz,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_8_0_26_patch1/src/Analysis_pulls.tar.gz,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_8_0_26_patch1/src/CombineHarvester.tar.gz
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"
