def get2016EWKW(pt):
    weight = 1
    if pt < 170:
        weight = 0.94269
    elif 170 <= pt < 200:
        weight = 0.902615
    elif 200 <= pt < 230:
        weight = 0.898827
    elif 230 <= pt < 260:
        weight = 0.959081
    elif 260 <= pt < 290:
        weight = 0.891248
    elif 290 <= pt < 320:
        weight = 0.860188
    elif 320 <= pt < 350:
        weight = 0.884811
    elif 350 <= pt < 390:
        weight = 0.868131
    elif 390 <= pt < 430:
        weight = 0.848655
    elif 430 <= pt < 470:
        weight = 0.806186
    elif 470 <= pt < 510:
        weight = 0.848507
    elif 510 <= pt < 550:
        weight = 0.83763
    elif 550 <= pt < 590:
        weight = 0.792152
    elif 590 <= pt < 640:
        weight = 0.730731
    elif 640 <= pt < 690:
        weight = 0.778061
    elif 690 <= pt < 740:
        weight = 0.771811
    elif 740 <= pt < 790:
        weight = 0.795004
    elif 790 <= pt < 840:
        weight = 0.757859
    elif 840 <= pt < 900:
        weight = 0.709571
    elif 900 <= pt < 960:
        weight = 0.702751
    elif 960 <= pt < 1020:
        weight = 0.657821
    elif 1020 <= pt < 1090:
        weight = 0.762559
    elif 1090 <= pt < 1160:
        weight = 0.845925
    elif pt >= 1160:
        weight = 0.674034
    
    return weight

def get2016QCDW(pt):
    weight = 1
    if pt < 170:
        weight = 1.43896
    elif 170 <= pt < 200:
        weight = 1.45307
    elif 200 <= pt < 230:
        weight = 1.41551
    elif 230 <= pt < 260:
        weight = 1.42199
    elif 260 <= pt < 290:
        weight = 1.3477
    elif 290 <= pt < 320:
        weight = 1.35302
    elif 320 <= pt < 350:
        weight = 1.34289
    elif 350 <= pt < 390:
        weight = 1.32474
    elif 390 <= pt < 430:
        weight = 1.23267
    elif 430 <= pt < 470:
        weight = 1.22641
    elif 470 <= pt < 510:
        weight = 1.23149
    elif 510 <= pt < 550:
        weight = 1.21593
    elif 550 <= pt < 590:
        weight = 1.16506
    elif 590 <= pt < 640:
        weight = 1.01718
    elif 640 <= pt < 690:
        weight = 1.01575
    elif 690 <= pt < 740:
        weight = 1.05425
    elif 740 <= pt < 790:
        weight = 1.05992
    elif 790 <= pt < 840:
        weight = 1.01503
    elif 840 <= pt < 900:
        weight = 1.01761
    elif 900 <= pt < 960:
        weight = 0.947194
    elif 960 <= pt < 1020:
        weight = 0.932754
    elif 1020 <= pt < 1090:
        weight = 1.00849
    elif 1090 <= pt < 1160:
        weight = 0.94805
    elif pt >= 1160:
        weight = 0.86956
    
    return weight

###########################################################################################

def get2016EWKZ(pt):
    weight = 1
    if pt < 170:
        weight = 0.970592
    elif 170 <= pt < 200:
        weight = 0.964424
    elif 200 <= pt < 230:
        weight = 0.956695
    elif 230 <= pt < 260:
        weight = 0.948747
    elif 260 <= pt < 290:
        weight = 0.941761
    elif 290 <= pt < 320:
        weight = 0.934246
    elif 320 <= pt < 350:
        weight = 0.927089
    elif 350 <= pt < 390:
        weight = 0.919181
    elif 390 <= pt < 430:
        weight = 0.909926
    elif 430 <= pt < 470:
        weight = 0.900911
    elif 470 <= pt < 510:
        weight = 0.892561
    elif 510 <= pt < 550:
        weight = 0.884353
    elif 550 <= pt < 590:
        weight = 0.8761
    elif 590 <= pt < 640:
        weight = 0.867687
    elif 640 <= pt < 690:
        weight = 0.858047
    elif 690 <= pt < 740:
        weight = 0.849014
    elif 740 <= pt < 790:
        weight = 0.840317
    elif 790 <= pt < 840:
        weight = 0.832017
    elif 840 <= pt < 900:
        weight = 0.823545
    elif 900 <= pt < 960:
        weight = 0.814596
    elif 960 <= pt < 1020:
        weight = 0.806229
    elif 1020 <= pt < 1090:
        weight = 0.798038
    elif 1090 <= pt < 1160:
        weight = 0.789694
    elif pt >= 1160:
        weight = 0.781163
    
    return weight

def get2016QCDZ(pt):
    weight = 1
    if pt < 170:
        weight = 1.47528
    elif 170 <= pt < 200:
        weight = 1.5428
    elif 200 <= pt < 230:
        weight = 1.49376
    elif 230 <= pt < 260:
        weight = 1.39119
    elif 260 <= pt < 290:
        weight = 1.40538
    elif 290 <= pt < 320:
        weight = 1.44661
    elif 320 <= pt < 350:
        weight = 1.38176
    elif 350 <= pt < 390:
        weight = 1.37381
    elif 390 <= pt < 430:
        weight = 1.29145
    elif 430 <= pt < 470:
        weight = 1.33452
    elif 470 <= pt < 510:
        weight = 1.25765
    elif 510 <= pt < 550:
        weight = 1.24265
    elif 550 <= pt < 590:
        weight = 1.24331
    elif 590 <= pt < 640:
        weight = 1.16187
    elif 640 <= pt < 690:
        weight = 1.07349
    elif 690 <= pt < 740:
        weight = 1.10748
    elif 740 <= pt < 790:
        weight = 1.06617
    elif 790 <= pt < 840:
        weight = 1.05616
    elif 840 <= pt < 900:
        weight = 1.1149
    elif 900 <= pt < 960:
        weight = 1.03164
    elif 960 <= pt < 1020:
        weight = 1.06872
    elif 1020 <= pt < 1090:
        weight = 0.981645
    elif 1090 <= pt < 1160:
        weight = 0.81729
    elif pt >= 1160:
        weight = 0.924246

    return weight
