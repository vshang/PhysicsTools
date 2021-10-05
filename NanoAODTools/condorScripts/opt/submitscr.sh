#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="SL1bSR"
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
executable = ./runopt.sh
output = ${RUNDIR}/runopt.stdoutD
error = ${RUNDIR}/runopt.stderr
log = ${RUNDIR}/runopt.condor_log
requirements = HAS_CMS_HDFS
requestdisk = 2G
requestmemory = 16G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/testCode/3skim_opt_code.py,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/testCode/DataSampleList_Skim.py,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/testCode/MCsampleList_Skim.py,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/testCode/cutopt.py,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/testCode/samples.py,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/testCode/selections.py,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/testCode/utils.py,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/testCode/variables.py
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"

