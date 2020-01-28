# Correction Tools
Several tools to get corrections, efficiencies, scale factors (SFs), event weights, etc. Adapted from code in https://github.com/IzaakWN/NanoTreeProducer/tree/f62dae90bdab41f3414c2b91522237e198b6a100/corrections.

[Lepton efficiencies](#lepton-efficiencies)  
[B tagging tools](#b-tagging-tools)  

## Lepton efficiencies

General class for calculating lepton scale factors is contained in 'scaleFactorTool.py'. Specific electron and muon scale factors are calculated using the classes contained in 'leptonSFs.py'. 'ROOT' files containing 2D histograms of lepton scale factors based on pT and eta are saved in ['scaleFactors'](scaleFactors) for electrons and muons seperately.

Lepton scale factors have been included in the 'preselect.py' module by default during the initialization of the module, e.g.:
<pre>
class preselectAnalysis(Module):
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

Options for the lepton scale factors can be found in ['leptonSFs.py'](leptonSFs.py).

## B tagging tools

The process for  B tagging weights is split into three steps.

1. First run 'getBTagHist.py' by calling 'python getBTagHist.py' from the appropriate folder (PhysicsTools/NanoAODTools by default) over each sample to generate root files containing jet and bjet histograms. These are saved in ['btag'](btag) by default. Settings can be changed in 'getBTagHist.py'.
2. Modify 'makeBTagEff.py' in the ['btag'](btag) folder and run over the output root files generated by 'getBTagHist.py' by calling 'python makeBTagEff.py' from the appropriate folder (PhysicsTools/NanoAODTools/python/postprocessing/corrections/btag by default) to generate a single root file containing the bjet efficiencies for all the samples. 
3. Run 'preselect.py' to save the B tagging weights to the analysis output. 

The main class for calculating B tagging weights is contained in 'BTaggingTool.py'. `BTaggingTool.py` provides two classes: `BTagWPs` for saving the working points (WPs) per year and type of tagger, and `BTagWeightTool` to provide b tagging weights. Like the lepton scale factors, the B tagging scale factors are included in the 'preselect.py' module by default during the initialization of the module, e.g.:
<pre>
class preselectAnalysis(Module):
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