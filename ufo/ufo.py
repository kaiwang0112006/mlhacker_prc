import csv
from parsedata import *
import pandas as pd
import numpy as np

filename = "ufo_awesome.tsv"

# ufo = ufoDeal()
# ufo.readdata(filename)
# ufo.checkdate()
# ufo.checklocform()
#ufo.filterByState()


ufo = ufoPandas()
ufo.formcolnum(filename)
ufo.readdata()
ufo.checkdate()
#ufo.checklocform()
#ufo.filterByState()

print len(ufo.dfufo)
print ufo.dfufo.dtypes
