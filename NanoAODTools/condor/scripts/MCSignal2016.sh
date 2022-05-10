#!/bin/sh
# Script for running analysis code on Condor
echo Found Proxy in: $X509_USER_PROXY
singularity exec --containall --no-home -B $(pwd) -B /cvmfs /cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7 python MCSignal2016.py
