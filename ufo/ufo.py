import csv
from parsedata import *
import pandas as pd
import numpy as np
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filename = "ufo_awesome.tsv"

# find difference between two parse method
# ufo1 = ufoDeal()
# ufo1.readdata(filename)
# ufo1.checkdate()
# ufo1.checklocform()
# ufo1.filterByState()
# print len(ufo1.cleandata)
 
ufo2 = ufoPandas()
ufo2.formcolnum(filename)
ufo2.readdata()
ufo2.checkdate()
ufo2.filterBydateNA()
ufo2.checklocform()
ufo2.filterByState()

#print len(ufo2.dfufo)
#print ufo2.dfufo.describe()

ufodata = ufo2.dfufo[(ufo2.dfufo['DateOccurred']>='19900101')]

#ufodata['ym'] = pd.DatetimeIndex(ufodata['DateOccurred']).year
ufodata['ym'] = ufodata['DateOccurred'].apply( lambda d: str(d.year) + str(d.month)) 
dg = ufodata.groupby(['state','ym'])
# for index,count in dg.size().iteritems():
#     print index, count
# print list(dg.size().keys())
dgsize = dg.size()
drange = pd.date_range(start=min(ufodata['DateOccurred']), end=max(ufodata['DateOccurred']),freq="M")
data = {}
for state in set(ufodata['state']):
    data[state] = {}
    for dr in drange:
        key = (state,str(dr.year)+str(dr.month))
        try:
            data[state][dr] = dgsize[key]
            #data[state].append((dr,dgsize[key]))
        except:
            data[state][dr] = 0
            #data[state].append((dr,0))
yc = len(data)/5
if len(data) > yc*5:
    yc += 1
print yc

fig, axarr = plt.subplots(yc, 5,sharey=True, sharex=True)
startidx = 0
startidy = 0
statelist = sorted(data.keys())
for state in statelist:
    print startidy, startidx
    x = sorted(data[state].keys())
    y = [data[state][ix] for ix in x]
    subp = axarr[startidy, startidx]
    subp.plot(x, y)
    subp.set_title(state,fontsize=11)
    subp.yaxis.set_ticks(np.arange(0,100,50))
    subp.xaxis.set_ticks(pd.date_range(start=min(ufodata['DateOccurred']), end=max(ufodata['DateOccurred']),freq="72M"))
    startidx += 1
    if startidx == 5:
        startidx = 0
        startidy +=1
    
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
# demo doc http://matplotlib.org/examples/pylab_examples/subplots_demo.html
fig.autofmt_xdate()
fig.text(0.5, 0.1, 'Time', ha='center')
fig.text(0.05, 0.5, 'Number of UFO sightings', va='center', rotation='vertical')
#plt.show()
fig.subplots_adjust(wspace=0.1, hspace=0.8)
fig.set_size_inches(18.5, 10.5)
plt.show()
#fig.savefig('common_labels_text.png')
#plt.savefig('common_labels_text.png', dpi=300)






