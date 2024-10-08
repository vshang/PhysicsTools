#!/bin/sh
# submitscr.sh 
# Script to create rundirs and corresponding submit files

# Create the name of the rundir
while :
do
    RUNDIR="SL1e0fT1SRv2"
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
executable = ./runplot_SL1e0fT1SRv2.sh
container_image = /cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7
output = ${RUNDIR}/runplot.stdoutD
error = ${RUNDIR}/runplot.stderr
log = ${RUNDIR}/runplot.condor_log
requirements = HAS_CMS_HDFS && HasSingularity
requestdisk = 20G
requestmemory = 16G
transfer_input_files = /afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/plots/plot2018.py,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/plots/samples2018.json,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/plots/data2018.json,/afs/hep.wisc.edu/home/vshang/public/tDM_nanoAOD/CMSSW_10_2_9/src/PhysicsTools/NanoAODTools/plots/utils.py
use_x509userproxy = True
queue
EOF

# submit the job
condor_submit "${SUBMIT}"
