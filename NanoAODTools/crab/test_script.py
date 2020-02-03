samples = 'datasetinputs/ttbarPlusJets.txt'

with open(samples, 'r') as f:
    datasetinputs = [line.strip() for line in f]

for line in datasetinputs:
    print line
