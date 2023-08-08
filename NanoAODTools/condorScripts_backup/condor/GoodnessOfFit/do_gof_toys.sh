#!/bin/sh
ulimit -s unlimited
set -x
export SCRAM_ARCH=slc7_amd64_gcc530
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram project CMSSW CMSSW_8_0_26_patch1
tar -zxvf Analysis_GoF_AH.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf HiggsAnalysis.tar.gz
tar -C CMSSW_8_0_26_patch1/src -zxvf CombineHarvester.tar.gz
cd CMSSW_8_0_26_patch1/src
scram b
eval `scram runtime -sh`
cd ../../GoF/


if [ -z "$1" ] ; then
    echo "Need to get job number!"
    exit 0
fi
ID="$(printf '%05d' "${1}")"
SEED1=`echo "72334+${1}" | bc`
combine -M GoodnessOfFit --algo=saturated -m 100 -d combinedCards_ModuleCommonSkim_05102023_RunII/tttDM_MChi1_MPhi100_scalar1b2b_AH.root -t 20 -s ${SEED1}

mv *.root ../
