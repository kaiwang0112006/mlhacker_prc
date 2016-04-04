import csv
from parsedata import *

filename = "ufo_awesome.tsv"

ufo = ufoDeal()
ufo.readdata(filename)
ufo.checkdate()
ufo.checklocform()
print(ufo.cleandata[0])