import csv
from parsedata import *
import pandas as pd
import numpy as np
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filename = "ufo_awesome.tsv"

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

print len(ufo2.dfufo)
print ufo2.dfufo.describe()

docur = ufo2.dfufo['DateOccurred']
yearlist = [x.year for x in docur]
hist, binedges = np.histogram(yearlist)
print hist
print binedges





