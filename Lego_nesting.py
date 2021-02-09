#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:01:30 2021

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:35:46 2021

@author: fadewell
"""

import qrcode
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint
import visualisedictionary as vd
from IPython.display import Image
from iteration_utilities import deepflatten
import dpath.util
import cv2
import functools
from collections import defaultdict
from py2neo import Node, Relationship
from lazy_py2neo import Graph

#import reduce


OPQR = list()
OPQR_init=list()
OPQR_other = list()
location = []


# read the QRCODE image
img = cv2.imread("QRin77pp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
OPQR.append( f"{data}" )
OPQR_init.append(f'{data}')
OPQR_other.append(f'{data}')


def Heist(val1,val2,i,t):
    n = []
    x1=val2+str(i)
    n1 = val1.replace(str(val2+'p'),x1)
    n.append(n1)
    return(n[t])

def QRminator(dataN,bboxN):
    n_lines = len(bboxN)
    
    for i in range(n_lines):
            # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
        QRM=(f"{dataN}")
        if str(QRM[len(QRM)-2:]) == '-1':
               QRM= QRM.replace('-1','')
    return(QRM)

for i in range(1,9):
# read the QRCODE image
    inps = str("QRin77pp.png")
    sign = str('7p')
    img = cv2.imread(Heist(inps,sign,i,0))
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        OPQR.append(QRminator(data,bbox))


ind = list() 
db = list()  
dbQR = []


def replic(x):
    xnew=x.replace('[','').replace(']', '').replace(' ', '').replace("''", "")
    pnew = xnew.split(',')
    return(xnew,pnew)

for i in range(0,len(OPQR)):
    c = replic(str(OPQR[i]))[0]
    db.append([c])
    dbQR.append(replic(str(OPQR[i]))[1])
    ind.append(len(replic(str(OPQR[i]))[1]))

dQR = []
itd= []
axis0 = len(dbQR)

def fodb(var1,var2,var3):
    vqr =[]
    for j in range(var2):
        viv = int(var3[var1][j])
        vqr.append(viv)
    return (vqr)
    
for i in range(0,axis0):
    dQR.append(fodb(i,int(ind[i]),dbQR))

    itd.append(fodb(i,int(ind[i]),dbQR)[0])

    
locations= []
location =[]
numbers = []
img2 = cv2.imread("compressedEntriesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img2)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
number =  f"{data}"
number = number.replace('-1','')
numbers.append(number)


for i in range(1,9):
    inps = str("compressedEntriesp.png")
    sign = str('es')
    img2 = cv2.imread(Heist(inps,sign,i,0))
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img2)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        numbers.append(QRminator(data,bbox))


pages = []

img3 = cv2.imread("Entitiesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img3)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
page = f"{data}"
pages.append(page)



for i in range(1,9):
    inps =str('Entitiesp.png')
    sign = str('es')
    img3 = cv2.imread(Heist(inps,sign,i,0))
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img3)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        pages.append(QRminator(data,bbox))
            
sortcode = []
AmiQR = []
ggQR = []


def Sor_tr(val1,val2,val3):
    mqr = []
    for j in range(val2):
        a = j+1
        b = j
        c = val3[val1]
        d = c[b:a]
        d = int(d)
        mqr.append(d)
    return(mqr)

def Srt_tr(val1,val2,val3,val4):  
    lqr = [0]
    for j in range (1,val2):
        d2 = val3[val1]
        d3 = d2[val4[val1][j-1]:val4[val1][j]]
        d3= int(d3)
        lqr.append(d3)
    return(lqr)

QRlist = []
QRlist_init = []
QRlist_other=[]

def Unhc(val1,val2,val3):
    fqr=[0]
    for j in range(1,val2):
        e = str(val3[val1][j])
        f = len(e)/(j+1)
        f = int(f)
        fqr.append(f)
    return(fqr)

wtj = []
tCt = []


def twwt(val1,val2,val3,val4,val5):
    k=1 
    ftw =[]
    while k < val2:
        istr = str(val3[val1][k])
        j = (k+1)* val4[val1][k]
        ftw.append(j)
        k += 1
    i1= k
    fct=[0]    
    L= val2-2
    if val5 !=1:
        x=1
        while x<val5:
            fct.append(int(numbers[val1][x]))
            x+=1
    for i in range(i1-L,val2+1):
        h = ftw[i-2]
        for t in range (0,h,i):
            istr = str(val3[val1][i-1])
            j= istr[t:t+i]
            j = int(j)
            fct.append(j)
    return (ftw,fct)

for i in range(len(pages)):
    AmiQR.append(Sor_tr(i,len(pages[i]),pages))

    ggQR.append(Srt_tr(i,ind[i],numbers,dQR))

    QRlist.append(Unhc(i,ind[i],ggQR))   

    wtj.append(twwt(i,ind[i],ggQR,QRlist,itd[i])[0])

    tCt.append(twwt(i,ind[i],ggQR,QRlist,itd[i])[1])

    
    

file1 = open("Test_parts_N_Subs","r") 
files = [file1]
files_init = [file1]
files_other = [file1]
for i in range (1,9):
    files.append(open('Instr'+str(i),"r"))

duuxx = []

def DuuxX(F16):
    z = np.size(F16)
    ion = []
    for x in range(z):
       ion.append(F16)
    Stealth = str(F16).replace("[","").replace("]","").replace(","," ").replace("\'  \'"," ").replace("\'" , "").replace("\\n", "  ").replace("     ", 'rQr')
    return(Stealth)


for i in range(0,len(files)):
    dix= files[i].readlines()
    
    duuxx.append(DuuxX(dix))
    tCt[i].append(-1)

    files[i].close()

AmQR = []


def nom (val1,val2,val3):
    aqr = []
    for i in range (val2):
        a = val3[val1][i]
        b = val3[val1][i+1]
        c = (str(a)+str(b))
        aqr.append(c)
    return(aqr)

for z in range (len(pages)):
    AmQR.append(nom(z,len(pages[z])-1,tCt))


            
dax =[]
Subs = []  

def diXi(I,II,III):
    IV= III[I:II]
    IV = IV.replace('   ',',').replace('rQr ', '.')
    V = IV[:len(IV)-3]
    VI = III[I:II]
    VI = VI.replace('   ',',').replace('rQr ', '.').replace('PartS','Sub')
    VII= VI[:len(VI)]
    return(V,VII)
for i in range(len(duuxx)):
    if i == 0 :
        dax.append(diXi(tCt[i][1],tCt[i][len(tCt[i])-2],duuxx[i])[0])

    elif i!=0:
        dax.append(diXi(tCt[i][1],tCt[i][len(tCt[i])-2],duuxx[i])[1])

    
def daXi(XI,IV):
    XIV= XI.replace('.',',')
    XIV=XIV[:len(XI)]
    zerofill=XIV.split(',')
    XVI =IV.replace('rQr',',').replace(', ',',').replace('   ',',').replace('.',',')
    XVI = XVI[:len(XVI)-2]
    fill = XVI.split(',')
    return(fill,zerofill)

for i in range(0,len(dax)):
    if i != 0 :
        Subs.append(daXi(dax[0],dax[i])[0])
    elif i==0:
        Subs.append(daXi(dax[0],dax[i])[1])

        


AsN ={}   
Parts ={}
PartQRs = {}
i=2
init = str('0-')
Sub1st = duuxx[0].find('PartS1')
Subassemblies = 0
Subassembly = []
while i < np.size(tCt[0])-2:
    a= tCt[0][i]
    b= tCt[0][i-1]
    a = int(a)
    b= int(b)
    if int(tCt[0][i-1])<Sub1st:
        locations=(tCt[0][i-1],duuxx[0][b:a-4])
        location.append(locations)
        Dict={duuxx[0][b:a-4]:str(tCt[0][i-1])}
        Parts.update(Dict)
        AsN.update(Dict)
    elif int(tCt[0][i-1])>= Sub1st:
        Subassemblies=(str(tCt[0][i-1]),duuxx[0][b:a-4])
        Subassembly.append(Subassemblies)
        Dict={duuxx[0][b:a-4]:str(tCt[0][i-1])}
        PartQRs.update(Dict)
    i += 1
    
Subassembly= np.array(Subassembly)
Subassembly = np.transpose(Subassembly)
location= np.array(location)
location = np.transpose(location)
partlock = list(location[1])
partcode = location[0]
sub_lock = Subassembly[1]
sub_code = Subassembly[0]
AsN2={}
for i in range(len(Subassembly[1])):
    sub_lock[i]='Sub'+str(i+1)
    Dict={sub_lock[i]:sub_code[i]}
    AsN2.update(Dict)

Sub = {}
l = len(Subs)
Noder={}
Subx=list()
Suby= list()
Subz= list()
Subd= list()
AsN4={}
AsN4.update(AsN)
AsN4.update(AsN2)
def Customs(L,l1,l2,val):
    Subassembly={}        
    L= L+1               
    for i in range(val,L):
        Dict2 = {}
        k = len(l1[i])
        for j in range(0,k,2):
            Dict = {l1[i][j]:l2[i][j+1]}
            
            Dict.setdefault(l1[i][j])
            Dict2.update(Dict)
            SubN = {'Sub'+str(i):Dict2}
            
            for t in range(L-1):
                if l1[i][j]== sub_lock[t]:
                    Dict = {'Sub'+str(t+1):Subassembly['Sub'+str(t+1)]}
                    Dict.setdefault('Sub'+str(t+1))
                    Dict2.update(Dict)
                    SubN = {'Sub'+str(i):Dict2}
            Subassembly.update(SubN)
    return(Subassembly)

Sub = Customs(8,Subs,Subs,1)


def keywords(L,init):
    Termed = {}
    for i in range(1,l):
        k = len(init[i])
        for j in range(0,k,2):
            Dict = {init[i][j+1]:init[i][j+1]}
            Termed.update(Dict)
          #  print(Termed)
    return(Termed)
Trms= keywords(8,Subs)
Terms= keywords(8,Subs)
Term = list(Terms)
Trem =[]
count = 1
for i in Terms:
    Trem.append('id'+str(count))
    Dict = {Term[count-1]:'id '+str(count)}
    Terms.update(Dict)
    count+=1
Elements = []
Composition=[]
Dempt=[]
for i in range(1,l):
    k = len(Subs[i])
    Elem =[]
    Comp = []
    Demp = []
    for j in range(0,k,2):
        Elem.append(Subs[i][j+1])
        Comp.append(Subs[i][j])
        Demp.append(Subs[i][j])
    Elements.append(Elem)
    Composition.append(Comp)
    Dempt.append(Demp)

G = vd.KeysGraph(Sub)

G.draw('./test.png')
Image('./test.png')

def Sunest(L,l2,l1):
    Assembly ={}        
    l=L+1
    for i in range(1,l):
        Dict4 = {}
        Dict2={}
        Dict3 ={}
        k = len(Subs[i])
        E = Elements[i-1]
        for j in range(0,k,2):
            ln = Subs[i][j+1]
            lp =Subs[i][j+1]
            Dict = {Subs[i][j+1]:lp} 
            for c in range (1,l):
                
                if Subs[i][j]== sub_lock[c-1]:
                    Dict = {'Sub'+str(c):Assembly['Sub'+str(c)]}
                   # Dict = {Subs[i][j+1]:Dict}
                    for t in range(1,l):
                       r2 = len(Subs[t])
                       for ijk in range(0,r2,2):
                           if Subs[t][ijk]==Subs[i][j]:
                               Dict.update(Dict)
                               
                               print(i,t,j,ijk)
                               Dict3.update(Dict)
                               print(Dict3)
                               break
                    Dict = {lp:Dict3}
                    Dict2.update(Dict)
                    SubN = {'Sub'+str(i):Dict2}
                    print(i,c,lp)
                    
                    break
                    
                elif Subs[i][j] != sub_lock[c-1]:
                    r = len(Subs[c])
                    for y in range(0,r,2):
                        ln2 = Subs[c][y+1]
                        lp2 =Subs[c][y+1]
                      #  pd=l2[c][y]
                        pd2=l2[c][y]
                        for o in range(len(Term)):
                            for s in range(len(E)):
                                if ln2 == Term[o] and lp2 == E[s] and Term[o] == ln and i == c:
                                    Dict = {pd2:pd2}
                                    Dict4.update(Dict)
                                    Dict = {Subs[i][j+1]:Dict4}
                                    break
                            Dict2.update(Dict)
                Dict3={}
                Dict4={}
            SubN = {'Sub'+str(i):Dict2}
            
                
            Assembly.update(SubN)
    return(Assembly)

Partree = Sunest(8,Subs,0)

G = vd.KeysGraph({'Sub8':Partree['Sub8']})

G.draw('./test.png')
Image('./test.png')
