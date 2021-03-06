# Correction Tools
Several tools to get corrections, efficiencies, scale factors (SFs), event weights, etc. Adapted from code in https://github.com/IzaakWN/NanoTreeProducer/tree/f62dae90bdab41f3414c2b91522237e198b6a100/corrections.

[Lepton efficiencies](#lepton-efficiencies)  
[B tagging tools](#b-tagging-tools) 
[Pileup reweighting](#pileup-reweighting)
[V+Jets NLO K-factors](#v+jets-nlo-k-factors)

## Lepton efficiencies

General class for calculating lepton scale factors is contained in [scaleFactorTool.py](scaleFactorTool). Specific electron and muon scale factors are calculated using the classes contained in [leptonSFs.py](leptonSFs.py). ROOT files containing 2D histograms of lepton scale factors based on pT and eta are saved in [scaleFactors](scaleFactors) for electrons and muons seperately.

Lepton scale factors have been included in the ModuleCommon.py module by default during the initialization of the module, e.g.:
<pre>
class CommonAnalysis(Module):
    def __init__(self, signalRegion):
        self.signalRegion = signalRegion
        self.nEvent = 0
        self.eleSFs = ElectronSFs(year=2016)
        self.muSFs = MuonSFs(year=2016)	
	...

    def analyze(self, event):
    	...

    	leptonWeight = 1
        for tightElectron in tightElectrons:
            leptonWeight *= self.eleSFs.getSF(tightElectron.pt, tightElectron.eta)
        for tightMuon in tightMuons:
            leptonWeight *= self.muSFs.getSF(tightMuon.pt, tightMuon.eta)

	...
</pre>

Options for the lepton scale factors can be found in [leptonSFs.py](leptonSFs.py).

## B tagging tools

The process for B tagging weights is split into five steps.

1. First run [getBTagHist.py](getBTagHist.py] by calling 'python getBTagHist.py' from the appropriate folder (PhysicsTools/NanoAODTools by default) over each sample to generate root files containing jet and bjet histograms as well as a TTree containing nEvents (used for getting nevents). These are saved in [btag](btag) by default. Settings can be changed in [getBTagHist.py](getBTagHist.py).
2. For each process, merge all histograms into single root file hist_all.root using hadd and merge all trees into single root file tree_all.root using haddnano.py.
2. Modify [BTagSampleList.py](BTagSampleList.py) in the [btag](btag) folder to list the output root files generated by [getBTagHist.py](getBTagHist.py).
3. Run [makeBTagEff.py](makeBTagEff) from the appropriate folder (PhysicsTools/NanoAODTools/python/postprocessing/corrections/btag by default) by calling 'python makeBTagEff.py' to generate a single root file containing the bjet efficiencies for all the samples. 
3. Run 'ModuleCommon.py' to save the B tagging weights to the analysis output. 

The main class for calculating B tagging weights is contained in [BTaggingTool.py](BTaggingTool). [BTaggingTool.py](BTaggingTool.py) provides two classes: `BTagWPs` for saving the working points (WPs) per year and type of tagger, and `BTagWeightTool` to provide b tagging weights. Like the lepton scale factors, the B tagging scale factors are included in the ModuleCommon.py module by default during the initialization of the module, e.g.:
<pre>
class CommonAnalysis(Module):
    def __init__(self, signalRegion):
        self.signalRegion = signalRegion
        self.nEvent = 0
	...
	self.btagTool = BTagWeightTool('CSVv2','medium',channel='ttbar',year=2016)

    def analyze(self, event):
    	...

    	bjetWeight = self.btagTool.getWeight(centralJets)

	...
</pre>

## Pileup reweighting

[PileupWeightTool.py](PileupWeightTool) provides the pileup event weight based on the PU distributions in data and MC stored in the [pileup](pileup) folder. Like the lepton and btag scale factors, pileup reweighting is included by default during the initialization of the module, e.g.: 
<pre>
class CommonAnalysis(Module):
    def __init__(self, signalRegion):
        self.signalRegion = signalRegion
        self.nEvent = 0
	...
	self.puTool = PileupWeightTool(year=2016)

    def analyze(self, event):
    	...

    	puWeight = self.puTool.getWeight(event.Pileup_nTrueInt)

	...
</pre>

## V+Jets NLO K-factors

Main class for calculating V+Jets NLO K-factors is contained in [kFactorTool.py](kFactorTool.py). All k-factors are stored in the folder [kfactors](kfactors). 2016 k-factors are stored in python file [get2016kfactors.py](get2016kfactors.py) while 2017/2018 k-factors are stored in root files contained in [kfactors](kfactors). K-factors for a given run year only depend on  pT of parent V particle. Selection of correct parent V particle is done in  ModuleCommon.py like so: 
<pre>
GenV = filter(lambda gen : (gen.pdgId == 23 or abs(gen.pdgId) == 24) and gen.status == 22, genParticles)
</pre>
Like the lepton and b-tagging scale factors, k-factors are included in the 'ModuleCommon.py' module by default during the initialization of the module, e.g.:
<pre>
class CommonAnalysis(Module):
      def analyze(self,event):
      ...

      self.kFactorTool = KFactorTool(year=2016)

      def analyze(self, event):
      ...

      ewkWWeight = self.kFactorTool.getEWKW(GenV_pt)

      ...
</pre>


