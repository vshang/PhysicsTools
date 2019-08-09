import ROOT

#Construct graph with symmetric errors and 5 points
graph = ROOT.TGraphErrors(5)
graph.SetTitle("Example Graph")
graph.GetXaxis().SetTitle("x-axis")
graph.GetYaxis().SetTitle("y-axis")

#Set points 0-4 on graph
graph.SetPoint(0, 1.0, 2.1)
graph.SetPoint(1, 2.0, 2.9)
graph.SetPoint(2, 3.0, 4.05)
graph.SetPoint(3, 4.0, 5.2)
graph.SetPoint(4, 5.0, 5.95)

#Set the errors on x to 0.0 and the errors on y to 0.1
for i in range(5):
    graph.SetPointError(i, 0.0, 0.1)

#Draw the graph including the axes and error bars
graph.Draw("AP")

#Create a one dimensional function f(x) = ax + b and fit it to the graph
f = ROOT.TF1("f", "[0]*x+[1]", -2, 2)
graph.Fit("f")

#Obtain the two parameters a and b from the function and their estimated uncerstainties
a = f.GetParameter(0)
b = f.GetParameter(1)
a_err = f.GetParError(0)
b_err = f.GetParError(1)

print "a =", a
print "a_err =", a_err
print "b = ", b
print "b_err =", b_err

#Run with python -i ExerciseGraph.py
