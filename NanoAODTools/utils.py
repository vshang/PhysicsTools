from ROOT import *
import os

def setCanvas(Canvas):
    Canvas.SetRightMargin(0.05)
    Canvas.SetLeftMargin(0.14)
    Canvas.SetTicks(1, 1)

def setTopPad(TopPad,r=4):
    TopPad.SetPad("TopPad", "", 0., 1./r, 1.0, 1.0, 0, -1, 0)
    TopPad.SetTopMargin(0.24/r+0.04)
    TopPad.SetBottomMargin(3*0.04/r)
    TopPad.SetRightMargin(0.05)
    TopPad.SetLeftMargin(0.14)
    TopPad.SetTicks(1, 1)

def setBotPad(BotPad, r=4):
    BotPad.SetPad("BotPad", "", 0., 0., 1.0, 1./r, 0, -1, 0)
    BotPad.SetTopMargin(r/100.)
    BotPad.SetBottomMargin(r/10.)
    BotPad.SetRightMargin(0.05)
    BotPad.SetLeftMargin(0.14)
    BotPad.SetTicks(1, 1)

def setBotStyle(h, r=4, fixRange=True):
    h.GetXaxis().SetLabelSize(h.GetXaxis().GetLabelSize()*(r-1))
    h.GetXaxis().SetLabelOffset(h.GetXaxis().GetLabelOffset()*(r-1))
    h.GetXaxis().SetTitleSize(h.GetXaxis().GetTitleSize()*(r-1))
    h.GetYaxis().SetLabelSize(h.GetYaxis().GetLabelSize()*(r-1))
    h.GetYaxis().SetNdivisions(505)
    h.GetYaxis().SetTitleSize(h.GetYaxis().GetTitleSize()*(r-1))
    h.GetYaxis().SetTitleOffset((h.GetYaxis().GetTitleOffset()+1)/(r-1))
    if fixRange:
        #h.GetYaxis().SetRangeUser(-0.3, 2.3)
        h.GetYaxis().SetRangeUser(0.4,1.6)
        for i in range(1, h.GetNbinsX()+1):
            if h.GetBinContent(i)<1.e-6:
                h.SetBinContent(i, -1.e-6)

def setHistStyle(hist, r=1.1):
    hist.GetXaxis().SetTitleSize(hist.GetXaxis().GetTitleSize()*r*r)
    hist.GetYaxis().SetTitleSize(hist.GetYaxis().GetTitleSize()*r*r)
    hist.GetXaxis().SetLabelSize(hist.GetXaxis().GetLabelSize()*r)
    hist.GetYaxis().SetLabelSize(hist.GetYaxis().GetLabelSize()*r)
    hist.GetXaxis().SetLabelOffset(hist.GetXaxis().GetLabelOffset()*r*r*r*r*r*r)
    hist.GetXaxis().SetTitleOffset(hist.GetXaxis().GetTitleOffset()*r)
    hist.GetYaxis().SetTitleOffset(hist.GetYaxis().GetTitleOffset())
