#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="ModuleCommonSkim_03092022_2016"
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
executable = ./runhaddnano2016v2.sh
output = ${RUNDIR}/runhaddnano2016v2.stdoutD
error = ${RUNDIR}/runhaddnano2016v2.stderr
log = ${RUNDIR}/runhaddnano2016v2.condor_log
requirements = HAS_CMS_HDF
requestdisk = 200G
requestmemory = 32G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/scripts/haddnano.py,/nfs_scratch/vshang/condor/haddnano/filelist.txt,/nfs_scratch/vshang/condor/haddnano/filterList.py
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"
