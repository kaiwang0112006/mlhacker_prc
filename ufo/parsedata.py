# -*- coding: utf-8 -*- 
import csv
import time
import copy
import pandas as pd
import numpy as np


class ufoPandas(object):
    def __init__(self):
        self.usstates = ["ak","al","ar","az","ca","co","ct","de","fl","ga","hi","ia","id","il","in","ks","ky","la","ma","md","me","mi","mn","mo","ms","mt","nc","nd","ne","nh","nj","nm","nv","ny","oh","ok","or","pa","ri","sc","sd","tn","tx","ut","va","vt","wa","wi","wv","wy"]
        self.data = []
        
    def formcolnum(self,filename):
        self.header = ["DateOccurred","DateReported","Location","ShortDescription","Duration","LongDescription"]

        with open(filename) as fin:
            fcsv = csv.reader(fin,delimiter='\t')
            for eachline in fcsv:    

                eachdict = {}
                for i in range(len(self.header)):
                    try:
                        eachdict[self.header[i]] = eachline[i]
                    except:
                        eachdict[self.header[i]] = 'NA'
                self.data.append(eachdict) 


    def readdata(self):
        self.dfufo = pd.DataFrame(self.data)
        
    def checkdate(self):
        self.dfufo = self.dfufo[(self.dfufo.DateOccurred.str.len() == 8) & (self.dfufo.DateReported.str.len() == 8)]
        self.dfufo['DateOccurred'] = pd.to_datetime(self.dfufo['DateOccurred'],format="%Y%m%d",coerce=True)
        self.dfufo['DateReported'] = pd.to_datetime(self.dfufo['DateReported'],format="%Y%m%d",coerce=True)
        
    def checklocform(self):
        self.dfufo['city'] = [x.split(',')[0].strip(' ').upper()  if (len(x.split(','))==2 and x.split(',')[1].strip(' ').lower() in self.usstates) else "NA" for x in self.dfufo['Location']]   
        self.dfufo['state'] = [x.split(',')[1].strip(' ').upper() if (len(x.split(','))==2 and x.split(',')[1].strip(' ').lower() in self.usstates) else "NA" for x in self.dfufo['Location']]   
    
    def filterByState(self):
        self.dfufo = self.dfufo[(self.dfufo['city'] != "NA") & (self.dfufo['state'] != "NA")]
        
    def filterBydateNA(self):
        self.dfufo = self.dfufo[self.dfufo['DateOccurred'].notnull() & self.dfufo['DateReported'].notnull()]
        self.dfufo = self.dfufo[self.dfufo['DateOccurred']>="19900101"]


                 
                 
class ufoDeal(object):
    def __init__(self):
        self.usstates = ["ak","al","ar","az","ca","co","ct","de","fl","ga","hi","ia","id","il","in","ks","ky","la","ma","md","me","mi","mn","mo","ms","mt","nc","nd","ne","nh","nj","nm","nv","ny","oh","ok","or","pa","ri","sc","sd","tn","tx","ut","va","vt","wa","wi","wv","wy"]
    
    def readdata(self,filename,delimiter="\t"):
        self.data = []
        with open(filename) as fin:
            fcsv = csv.reader(fin,delimiter='\t')
            for eachline in fcsv:
                if len(eachline) <6:
                    for i in range(len(eachline),6):
                        eachline.append('NA')
                self.data.append(eachline[:6])

                
    def checkdate(self):
        self.cleandata = []
        data = copy.deepcopy(self.data)
        errordateline = []
        for eachline in data:
            dateoccur = eachline[0]
            datereport = eachline[1]
            try:
                dateoccurtime = time.strptime(dateoccur, "%Y%m%d")
                datereporttime = time.strptime(datereport, "%Y%m%d")
                eachline[0] = dateoccurtime
                eachline[1] = datereporttime
                self.cleandata.append(eachline)
            except:
                errordateline.append(eachline)
    
    #���ۣ�R����������⣬������Ȼ�����������ͬ��clean data������ͬ��
    #https://github.com/johnmyleswhite/ML_for_Hackers/issues/39
    def checkdate2(self):
        errordateline = []
        for eachline in self.data:
            if eachline[0] == "ler@gnv.ifas.ufl.edu":
                print eachline
            dateoccur = eachline[0]
            datereport = eachline[1]
            if len(dateoccur)==8 and len(datereport)==8 :
                #dateoccurtime = time.strptime(dateoccur, "%Y%m%d")
                #datereporttime = time.strptime(datereport, "%Y%m%d")
                #eachline[0] = dateoccurtime
                #eachline[1] = datereporttime
                pass
            else:
                errordateline.append([eachline[0],eachline[1]])
 
        print len(errordateline)
        print len(self.data)
        
    def checklocform(self):
        for eachline in self.cleandata:
            loc = eachline[2]
            if len(loc) >= 1:
                loc = loc.lstrip(' ')
                loclist = loc.split(',')
                if len(loclist) == 2 and loclist[1].strip(' ').lower() in self.usstates:
                    eachline[2] = loclist[0].strip(' ')
                    eachline.insert(3,loclist[1].strip(' '))
                else:
                    eachline[2] = "NA"
                    eachline.insert(3,"NA")
            else:
                eachline[2] = "NA"
                eachline.insert(3,"NA")  
                
    def filterByState(self):
        data = copy.deepcopy(self.cleandata) 
        self.cleandata = []
        for eachline in data:
            if not (eachline[2] == 'NA' and eachline[3] == 'NA'):
                self.cleandata.append([eachline[2],eachline[3]]) 
                
                
            
        
        