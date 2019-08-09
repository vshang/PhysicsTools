import ROOT

#Create a histogram with 10 bins ranging from 0 to 100 with title "Example Histogram", x-axis label "x", and y-axis label "y-axis"
hist = ROOT.TH1F("hist", "Example Histogram; x; y-axis", 10, 0, 100)

#Fill the histogram with the following numbers: 11.3, 25.4, 18.1
hist.Fill(11.3)
hist.Fill(25.4)
hist.Fill(18.1)

#Fill the histogram with the square of all integers from 0 to 9
for i in range(10):
   hist.Fill(i*i)

#Draw the histogram
hist.Draw()

#Calculate the mean value and the rms and show it on the screen
mean = hist.GetMean()
rms = hist.GetRMS()
print "mean = ", mean, "rms = ", rms

#Calculate the integral of the histogram
integral = hist.Integral()
print "integral = ", integral

#Identify the bin with the maximum number of entries 
maxBin = hist.GetMaximumBin()
print "maximum bin number:", maxBin

#Calculate the maximum bin content
maxBinEntries = hist.GetBinContent(maxBin)
print "maxBinEntries:", maxBinEntries

#Set the y-axis label to entries
hist.GetYaxis().SetTitle("entries")

#Set the line color of the histogram to red
hist.SetLineColor(ROOT.kRed)

#Run with python -i ExerciseHist.py
