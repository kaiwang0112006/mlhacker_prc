import csv
from parsedata import *
import pandas as pd
import numpy as np
import time
from datetime import datetime

def convertTime(t):
    tstruct = str(t.to_pydatetime()).split()[0].replace('-','')
    tt = time.strptime(str(tstruct), "%Y%m%d") 
    return tt

filename = "ufo_awesome.tsv"

ufo1 = ufoDeal()
ufo1.readdata(filename)
ufo1.checkdate()
#ufo1.checklocform()
#ufo1.filterByState()
print len(ufo1.cleandata)

 
ufo2 = ufoPandas()
ufo2.formcolnum(filename)
ufo2.readdata()
ufo2.checkdate()
#ufo.checklocform()
#ufo.filterByState()
ufo2.filterBydateNA()
print len(ufo2.dfufo)

# ufo1 and ufo2 have different length

# header = ["DateOccurred","DateReported","Location","ShortDescription","Duration","LongDescription"]
# for i in range(len(ufo2.dfufo)):
#     temp = []
#     for h in header:
#         if h == "DateOccurred" or h == "DateReported":
#             tin = convertTime(ufo2.dfufo.iloc[i][h])
#         else:
#             tin = ufo2.dfufo.iloc[i][h]
#         temp.append(tin)
#     if temp not in ufo1.cleandata:
#         print temp
#         print ufo1.cleandata[i]
#         print i 
#         break
# nothing print out, need to check duplicate
print len(set(ufo1.cleandata))
    






