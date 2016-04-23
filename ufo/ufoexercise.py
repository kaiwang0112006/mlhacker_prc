import csv
from parsedata import *
import pandas as pd
import numpy as np

filename = "ufo_awesome.tsv"

# ufo = ufoDeal()
# ufo.readdata(filename)
# ufo.checkdate()
# #ufo.checklocform()
# #ufo.filterByState()
# print len(ufo.data)
# 
# ufo = ufoPandas()
# ufo.formcolnum(filename)
# ufo.readdata()
# ufo.checkdate()
# #ufo.checklocform()
# #ufo.filterByState()
# ufo.filterBydateNA()
# print len(ufo.dfufo)
# print ufo.dfufo.dtypes
# #print ufo.dfufo.loc[ufo.dfufo['DateOccurred'] == '19940000']
# # print pd.to_datetime(np.nan,coerce=True) == pd.to_datetime(np.nan,coerce=True)
# print type(ufo.dfufo.loc[[8652]]['DateOccurred'])
# # print ufo.dfufo.loc[[8651]]['DateOccurred'] == pd.to_datetime(np.nan,coerce=True)



ufo = ufoPandas()
ufo.formcolnum(filename)
ufo.readdata()

ufo.dfufo['DateOccurred'] = pd.to_datetime(ufo.dfufo['DateOccurred'],coerce=False)


for i in range(len(ufo.dfufo)):
    if type(ufo.dfufo.iloc[i]['DateOccurred']) == type('a'):
        ufo.dfufo.iloc[i]['DateOccurred'] = 'NA'
print ufo.dfufo.iloc[8651]['DateOccurred']

rowlist = ufo.dfufo[:10].values.tolist()
print type(rowlist)
print rowlist

