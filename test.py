
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib import parse
import json
import csv
def getList():
    f=open('C:\\company.txt','r')
    allLines=f.readlines()
    return allLines

def getInfo(companyLiat):
    newList=[]
    for line in companyLiat:
        line=line.strip()
        if line not in newList:
            newList.append("http://api.tianyancha.com/services/v3/open/w/detail.json?name="+line)
    print("啦啦啦，公司名称我已经读完啦~~")
