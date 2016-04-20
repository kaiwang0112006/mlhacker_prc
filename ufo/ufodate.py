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

def convertpytime(t):
    try:
        return time.strptime(t, "%Y%m%d")
    except:
        return np.nan

filename = "ufo_awesome.tsv"

ufo1 = ufoDeal()
ufo1.readdata(filename)
ufo1.checkdate()
#ufo1.checklocform()
#ufo1.filterByState()
print len(ufo1.cleandata)


data = ufo1.cleandata[40657:40660]
selfdata = []
selfheader = ["DateOccurred","DateReported","Location","ShortDescription","Duration","LongDescription"]

for eachline in data:    

    eachdict = {}
    for i in range(len(selfheader)):
        try:
            eachdict[selfheader[i]] = eachline[i]
        except:
            eachdict[selfheader[i]] = 'NA'
    selfdata.append(eachdict) 
selfdata[0]['DateOccurred'] = 'aaa'
selfdata[1]['DateOccurred'] = '14000630'
selfdata[2]['DateOccurred'] = '19940000'
dfufo = pd.DataFrame(selfdata)
print dfufo
dfufo['DateOccurred'] = dfufo['DateOccurred'].apply(lambda d: convertpytime(d))

print dfufo.dtypes
 
# ufo2 = ufoPandas()
# ufo2.formcolnum(filename)
# ufo2.readdata()
# ufo2.checkdate()
# #ufo.checklocform()
# #ufo.filterByState()
# ufo2.filterBydateNA()
# print len(ufo2.dfufo)
# print ufo2.dfufo.iloc[40657]
# print ufo2.dfufo.iloc[40658]
# print ufo2.dfufo.iloc[40659]
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
#     if temp != ufo1.cleandata[i]:
#         print temp
#         print ufo1.cleandata[i]
#         print i 
#         break


# nothing print out, need to check duplicate
# data = {}
# for eachline in ufo1.cleandata:
#     key = tuple(eachline)
#     if not key in data:
#         data[key] = 1
#     else:
#         data[key] += 1
#         print key

    






