# -*- coding: utf-8 -*- 
import csv
import time
import copy
class ufoDeal(object):
    def __init__(self):
        pass
    
    def readdata(self,filename,delimiter="\t"):
        self.data = []
        with open(filename) as fin:
            fcsv = csv.reader(fin,delimiter='\t')
            for eachline in fcsv:
                self.data.append(eachline)

                
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
        for eachline in self.cleandata :
            loc = eachline[2]
            if len(loc) >= 1:
                if loc[0] == ' ':
                    loc = loc[1:]
                loclist = loc.split(',')
                if len(loclist) == 2:
                    eachline[2] = loclist[0]
                    eachline.insert(3,loclist[1])
                else:
                    eachline[2] = "NA"
                    eachline.insert(3,"NA")
            else:
                eachline[2] = "NA"
                eachline.insert(3,"NA")   
                
                
            
        
        