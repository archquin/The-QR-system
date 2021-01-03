#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:43:36 2021

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 09:50:44 2021

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:07:29 2021

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 05:31:04 2021

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:00:13 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 02:27:06 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:32:24 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 21:56:12 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 07:39:09 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 05:54:29 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:46:43 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 19:00:53 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:37:54 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:24:20 2020

@author: fadewell
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 17:26:05 2020

@author: fadewell
"""

import qrcode
import numpy as np
import matplotlib.pyplot as plt
import pprint
import visualisedictionary as vd
from IPython.display import Image
from iteration_utilities import deepflatten
import dpath.util
import cv2


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
    x2=val2+str(i)+'2'
    n2= val1.replace(str(val2+'p'),x2)
    n.append(n2)
    x3=val2+str(i)+'3'
    n3= val1.replace(str(val2+'p'),x3)
    n.append(n3)
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

for i in range(1,12):
# read the QRCODE image
    inps = str("QRin77pp.png")
    sign = str('7p')
    img = cv2.imread(Heist(inps,sign,i,0))
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    imgi = cv2.imread(Heist(inps,sign,i,1))
    data2, bbox2, straight_qrcode2 = detector.detectAndDecode(imgi)
    im0gi = cv2.imread(Heist(inps,sign,i,2))
    data3, bbox3, straight_qrcode3 = detector.detectAndDecode(im0gi)
# if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        OPQR.append(QRminator(data,bbox))
        print(f"QRCode data:\n{data2}")
        OPQR_init.append(QRminator(data2,bbox2))
        print(f"QRCode data:\n{data3}")
        OPQR_other.append(QRminator(data3,bbox3))

ind = list() 
ind_init=list()   
ind_other=list()    
db = list()  
dbb= list()
ddbb=list()
dbQR = []
dbQR_init = []
dbQR_other =[]

def replic(x):
    xnew=x.replace('[','').replace(']', '').replace(' ', '').replace("''", "")
    pnew = xnew.split(',')
    return(xnew,pnew)

for i in range(0,len(OPQR)):
    c = replic(str(OPQR[i]))[0]
    db.append([c])
    dbQR.append(replic(str(OPQR[i]))[1])
    ind.append(len(replic(str(OPQR[i]))[1]))
    cc = replic(str(OPQR_init[i]))[0]
    dbb.append([cc])
    dbQR_init.append(replic(str(OPQR_init[i]))[1])
    ind_init.append(len(replic(str(OPQR_init[i]))[1]))
    ccc = replic(str(OPQR_other[i]))[0]
    ddbb.append([ccc])
    dbQR_other.append(replic(str(OPQR_other[i]))[1])
    ind_other.append(len(replic(str(OPQR_other[i]))[1]))
dQR = []
itd= []
dQR_init = []
itd_init= []
dQR_other = []
itd_other= []
axis0 = len(dbQR)

def fodb(var1,var2,var3):
    vqr =[]
    for j in range(var2):
        viv = int(var3[var1][j])
        vqr.append(viv)
    return (vqr)
    
for i in range(0,axis0):
    dQR.append(fodb(i,int(ind[i]),dbQR))
    dQR_init.append(fodb(i,int(ind_init[i]),dbQR_init))
    dQR_other.append(fodb(i,int(ind_other[i]),dbQR_other))

    itd.append(fodb(i,int(ind[i]),dbQR)[0])
    itd_init.append(fodb(i,int(ind_init[i]),dbQR_init)[0])
    itd_other.append(fodb(i,int(ind_other[i]),dbQR_other)[0])
    
    
    
locations= []
location =[]
numbers = []
numbers_init = []
numbers_other =[]
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
numbers_init.append(number)
numbers_other.append(number) 


for i in range(1,12):
    inps = str("compressedEntriesp.png")
    sign = str('es')
    img2 = cv2.imread(Heist(inps,sign,i,0))
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img2)
    img2i = cv2.imread(Heist(inps,sign,i,1))
    data2, bbox2, straight_qrcode2 = detector.detectAndDecode(img2i)
    im0g2i = cv2.imread(Heist(inps,sign,i,2))
    data3, bbox3, straight_qrcode3 = detector.detectAndDecode(im0g2i)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        numbers.append(QRminator(data,bbox))
        numbers_init.append(QRminator(data2,bbox2))
        numbers_other.append(QRminator(data3,bbox3))
numbers[10]='0113355'

pages = []
pages_init = []
pages_other =[]
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
pages_init.append(page)
pages_other.append(page)


for i in range(1,12):
    inps =str('Entitiesp.png')
    sign = str('es')
    img3 = cv2.imread(Heist(inps,sign,i,0))
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img3)
    img3i = cv2.imread(Heist(inps,sign,i,1))
    data2, bbox2, straight_qrcode2 = detector.detectAndDecode(img3i)
    im0g3i = cv2.imread(Heist(inps,sign,i,2))
    data3, bbox3, straight_qrcode3 = detector.detectAndDecode(im0g3i)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        pages.append(QRminator(data,bbox))
        pages_init.append(QRminator(data2,bbox2))
        pages_other.append(QRminator(data3,bbox3))
            
sortcode = []
AmiQR = []
ggQR = []
sortcode_init = []
AmiQR_init = []
ggQR_init = []
sortcode_other = []
AmiQR_other = []
ggQR_other = []

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
wtj_init = []
tCt_init = []
wtj_other = []
tCt_other = []

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
    AmiQR_init.append(Sor_tr(i,len(pages_init[i]),pages_init))
    AmiQR_other.append(Sor_tr(i,len(pages_other[i]),pages_other))
    
    ggQR.append(Srt_tr(i,ind[i],numbers,dQR))
    ggQR_init.append(Srt_tr(i,ind_init[i],numbers_init,dQR_init))
    ggQR_other.append(Srt_tr(i,ind_other[i],numbers_other,dQR_other))
    
    QRlist.append(Unhc(i,ind[i],ggQR))   
    QRlist_init.append(Unhc(i,ind_init[i],ggQR_init))
    QRlist_other.append(Unhc(i,ind_other[i],ggQR_other))
    
    wtj.append(twwt(i,ind[i],ggQR,QRlist,itd[i])[0])
    wtj_init.append(twwt(i,ind_init[i],ggQR_init,QRlist_init,itd_init[i])[0])
    wtj_other.append(twwt(i,ind_other[i],ggQR_other,QRlist_other,itd_other[i])[0])
    tCt.append(twwt(i,ind[i],ggQR,QRlist,itd[i])[1])
    tCt_init.append(twwt(i,ind_init[i],ggQR_init,QRlist_init,itd_init[i])[1])
    tCt_other.append(twwt(i,ind_other[i],ggQR_other,QRlist_other,itd_other[i])[1])
    
    

file1 = open("ShipParts.txt","r") 
files = [file1]
files_init = [file1]
files_other = [file1]
for i in range (1,12):
    files.append(open('Instr'+str(i),"r"))
    files_init.append(open('Instr'+str(i)+'2',"r"))
    files_other.append(open(str('Sub')+str(i)+'.txt',"r"))
    
duuxx = []
duuxx_init = []
duuxx_other =[]

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
    dix_init= files_init[i].readlines()
    duuxx_init.append(DuuxX(dix_init))
    tCt_init[i].append(-1)
    dix_other= files_other[i].readlines()
    duuxx_other.append(DuuxX(dix_other))
    tCt_other[i].append(-1)
    files[i].close()
    files_init[i].close()
    files_other[i].close()
duuxx_other[0]=duuxx_init[0]= duuxx[0]

AmQR = []
AmQR_init = []
AmQR_other=[]

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
    AmQR_init.append(nom(z,len(pages_init[z])-1,tCt_init))
    AmQR_other.append(nom(z,len(pages_other[z])-1,tCt_other))
    
    
xy = []
for z in range(len(files)):
    j=0
    i = 1
    xy0=[]
    while i & j < np.size(AmQR_other[z])-1:
    
        x=AmQR_other[z][j]
        #print (x)
       # qr = qrcode.make(x)
       # qr.save('entrypoints.png')
    #    img1 = cv2.imread("entrypoints.png")
        aa = AmiQR_other[z][j]
        i += 1
        bb = AmiQR_other[z][i-1]
        j +=1
        yy = x [0:aa]
        yy = int(yy)
        xx = x [aa:aa+bb]
        xx= int(xx)
       #### xy = (str(yy)+str(xx))
        xxyy =[(xx,yy)]
        xy0.append(xxyy)  
    xy.append(xy0)
for i in range(len(tCt_other)):
    j=1
    if i == 0 :
        while j <np.size(tCt_other[i])-3:
            aa= xy[i][j]
            a = str(aa)
            a = str(a)
            a = a.replace('[','').replace('(','').replace(']','').replace(')','')
            ab = a.split(',')
            aaa = int(ab[0])
            aab = int(ab[1])####
         
            if j != np.size(tCt_other[i])-3:
                print (duuxx_other[i][aab:aaa-4])
            elif j == np.size(tCt_other[i])-3:
                print(duuxx_other[i][aab:aaa-2])
            print(j,aab,aaa)
    
            qr = qrcode.make(duuxx_other[i][aab:aaa-4])
            qr.save('partEntities.png')
            img1 = cv2.imread("partEntities.png")
            greyy = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            data, bbox, straight_qrcode = detector.detectAndDecode(img1)
         #   plt.imshow(greyy)
         #   plt.show()
            j += 1
    elif i != 0:
        while j <np.size(tCt_other[i])-2:
            aa= xy[i][j]
            a = str(aa)
            a = str(a)
            a = a.replace('[','').replace('(','').replace(']','').replace(')','')
            ab = a.split(',')
            aaa = int(ab[0])
            aab = int(ab[1])####
         
            if j != np.size(tCt_other[i])-3:
                print (duuxx_other[i][aab:aaa-4])
            elif j == np.size(tCt_other[i])-3:
                print(duuxx_other[i][aab:aaa-2])
            print(j,aab,aaa)
    
            qr = qrcode.make(duuxx_other[i][aab:aaa-4])
            qr.save('partEntities.png')
            img1 = cv2.imread("partEntities.png")
            greyy = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            data, bbox, straight_qrcode = detector.detectAndDecode(img1)
         #   plt.imshow(greyy)
         #   plt.show()
            j += 1
            
dax =[]
dax_init = []
dax_other=[]

Subs_other=[]
Subs_init =[]
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
        dax_init.append(diXi(tCt_init[i][1],tCt_init[i][len(tCt_init[i])-2],duuxx_init[i])[0])
        dax_other.append(diXi(tCt_other[i][1],tCt_other[i][len(tCt_other[i])-2],duuxx_other[i])[0])
       
    elif i!=0:
        dax.append(diXi(tCt[i][1],tCt[i][len(tCt[i])-2],duuxx[i])[1])
        dax_init.append(diXi(tCt_init[i][1],tCt_init[i][len(tCt_init[i])-2],duuxx_init[i])[1])
        dax_other.append(diXi(tCt_other[i][1],tCt_other[i][len(tCt_other[i])-2],duuxx_other[i])[1])
  
    
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
        Subs_init.append(daXi(dax_init[0],dax_init[i])[0])
        Subs_other.append(daXi(dax_other[0],dax_other[i])[0])
    elif i==0:
        Subs.append(daXi(dax[0],dax[i])[1])
        Subs_init.append(daXi(dax_init[0],dax_init[i])[1])
        Subs_other.append(daXi(dax_other[0],dax_other[i])[1])

        


        
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
for i in range(len(Subassembly[1])):
    sub_lock[i]='Sub'+str(i+1)
sub_code = Subassembly[0]
Sub = {}
l = len(Subs)

Subx=list()
Suby= list()
Subz= list()
Subd= list()

def Customs(L,l1,l2,val):
    Subassembly={}        
    L= L+1               
    for i in range(1,L):
        Dict2 = {}
        k = len(l1[i])
        for j in range(0,k,2):
            Dict = {l1[i][j]:l2[i][j+val]}
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

Sub = Customs(11,Subs_init,Subs_other,0)
Sub2 = Customs(11,Subs_init,Subs_other,1)


def keywords(L,init):
    Termed = {}
    for i in range(1,l):
        k = len(init[i])
        for j in range(0,k,2):
            Dict = {init[i][j+1]:init[i][j+1]}
            Termed.update(Dict)
    return(Termed)

Terms= keywords(l,Subs)
Term = list(Terms)

Elements = []
Composition=[]
Dempt=[]
for i in range(1,l):
    k = len(Subs[i])
    Elem =[]
    Comp = []
    Demp = []
    for j in range(0,k,2):
        Elem.append(Subs_init[i][j+1])
        Comp.append(Subs_other[i][j])
        Demp.append(Subs_other[i][j])
    Elements.append(Elem)
    Composition.append(Comp)
    Dempt.append(Demp)

def SearchM(val2):
    val='PartL140'
    for i in range(1,12):
        k = len(Subs[i])
        for j in range(0,k-1):
            if val == Subs[i][j] and val2 == 'Sub'+str(i):
                Dicts= {Subs[i][j]:Subs[i][j]}
                Dicts2s= {Subs[i][int(j+1)]:Dicts}
                Dicts2s={val2:Dicts2s}
    return(Dicts2s.get(val2))    
    
def Search(val):
    for i in range(1,12):
        k = len(Subs[i])
        for j in range(0,k-1):
            if val == Subs[i][j]:
                Dicts= {Subs[i][j]:Subs[i][j]}
                Dicts2= {Subs[i][int(j+1)]:Dicts}
                
    return(Dicts2)


def NestSrc(val,val2,x):
    Dicts={}
    Dict=Partree.get(val)
    value = list(Dict.keys())
    for k in range(len(value)):
        if k == Relpos(partv[p][j-1],partv[p][j]):
            Dict={value[k]:val2}
            Dicts.update(Dict)
    return(Dicts)

def NestSrcp(val):
    
    Dict=Partree.get(val)
    value = list(Dict.keys())
    val3= value
    return(val3)   

def Relpos(pos,rel):
    nlp = int()
    for i in range(0,11):
        ik = len(Subx[i])
        for j in range(ik):
            if Subx[i][j]==pos and 'Sub'+str(i+1)==rel:
                nlp = int(j)
    return(nlp)

def Searchs(val,val3):
    for i in range(len(val)):
        art= list(val.keys())
        bart= list(val.values())    
        for p in range(len(val3)):
            L140=list(val3.keys())
            if int(L140[p][3:])!=int(art[i][3:]):
                x = len(bart[i])
                dart= list(bart[i].keys())
         
                for j in range(x):
                    if dart[j]==L140[p]:
                        print(dart[j],val[art[i]])
                        key = NestSrcp(art[i],j)
                        Dict={dart[j]:val3[L140[p]]}
                        
                        Dict={key:Dict}
                        print(dart[j])
                        val[art[i]].update(Dict)
                val2=val
                
    return(val2)    

def Searchs2(val):
    val3=Arty[val]
    return(val3) 


def Interam(L,l2,l1):
    Assembly ={}        
    L=L+1
    for i in range(1,L):
        Dict4 = {}
        Dict2={}
        k = len(Subs[i])
        E = Elements[i-1]
        for j in range(0,k,2):
            ln = Subs[i][j+1]
            lp =Subs_init[i][j+1]
            Dict = {Subs[i][j+1]:lp} 
            for c in range (1,l):
                r = len(Subs[c])
                for y in range(0,r,2):
                    ln2 = Subs[c][y+1]
                    lp2 =Subs_init[c][y+1]
                    pd=l2[c][y]
                    pd2=l2[c][y+l1]
                    for o in range(len(Term)):
                        for s in range(len(E)):
                            if ln2 == Term[o] and lp2 == E[s] and Term[o] == ln:
                                if l1 == 1:
                                    Dict= {pd:pd}
                                    Dict = {pd2:Dict}
                                    Dict4.update(Dict)
                                    Dict = {Subs[i][j+1]:Dict4}
                                elif l1 == 0:
                                    Dict = {pd2:pd2}
                                    Dict4.update(Dict)
                                    Dict = {Subs[i][j+1]:Dict4}
                        Dict2.update(Dict)
                Dict4={}
            SubN = {'Sub'+str(i):Dict2}
            
            for t in range(L-1):
                if Subs[i][j]== sub_lock[t]:
                    Dict = {'Sub'+str(t+1):Assembly['Sub'+str(t+1)]}
                    Dict3 = {Subs[i][j+1]:Dict}
                    Dict2.update(Dict3)
                    SubN = {'Sub'+str(i):Dict2}
        
            Assembly.update(SubN)
    return(Assembly)

Partree = Interam(11,Subs_init,0)
Assembly_M = Interam(11,Subs_init,1)




Subz= sub_lock
Suby= Composition
Subx = Dempt
for i in range(0,l-1):
    gdw= len(Suby[i])
    for j in range(gdw):
        for k in range (0,l-1):
            z = str(Subz[k])
            z=z.replace('Sub','')
            z= int(z)
            if Suby[i][j]==Subz[k]:
                for ijk in range(gdw):
                    if j == ijk:
                        Suby[i][ijk]=Suby[z-1]
 
sublist=[]
Subz=[]
for i in range(0,l-1):
   parts =[]
   if Subx[i]==Suby[i]:
       for j in range(len(Subx[i])):
           parts.append(Suby[i][j])
   elif Subx[i]!=Suby[i]:
       sublist=list(deepflatten(Suby[i],ignore=str,depth=(4)))
       parts=(sublist)
   Subz.append(parts)
   
for p in range(len(Parts)):    
    part = list(Parts.keys())
    parts = list()
    for i in range(0,l-1):
        y= len(Subz[i])
        for z in range (y):
            if Subz[i][z]==part[p]:
                parts.append('Sub'+str(1+i))
            Dict={part[p]:parts}
    Parts.update(Dict)
    
    


Artdict={}   
for p in range(len(Parts)):    
    part = list(Parts.keys())
    partv = list(Parts.values())
    Dict2 = {}
    for i in range(0,l-1):
        y= len(Subz[i])
        for z in range (y):
            if Subz[i][z]==part[p]:
                x = len(partv[p])
                for j in range(x):
                    Dict={partv[p][j]:j+1}
                    Dict2.update(Dict)
                    Dict={part[p]:Dict2}
                    Artdict.update(Dict)
             
partt=[]
for i in partv: 
    if i not in partt: 
        partt.append(i)
        
partt.remove(partt[len(partt)-1])
partt.remove(partt[len(partt)-1])

PartL140={}
for i in range(len(partt)):
    Dict2={}
    for j in range(len(partt[i])):
        Dict={partt[i][j]:j}
        Dict2.update(Dict)
        Dict={partt[i][0]:Dict2}
        Dict={partt[i][0]:SearchM(partt[i][0])}
        PartL140.update(Dict)
        

Partdict1={}        
for p in range(len(PartL140)):    
    part = list(PartL140.keys())
    Dict2 = {}
    x= len(partt[p])
    j = 0
    point =SearchM(part[p])
    while j<x:
        if j == 0:
            Dict={partt[p][j]:point}
            Dict2.update(Dict)
            Dict={part[p]:Dict2}
            Partdict1.update(Dict)
            j+=1
        elif j!=0:
            if j == 1:
                Dictn={partt[p][0]:point}
                Dict= Dictn
                Dict={partv[p][j]:NestSrc(partv[p][j],Dict,Relpos(partv[p][j-1],partv[p][j]))}
                Dict1= Dict
                Dict2.update(Dict)
                Dict={part[p]:Dict2}
                Partdict1.update(Dict)
                j+=1
            elif j!=1:
                Dict= Dict1
                Dict={partv[p][j]:NestSrc(partv[p][j],Dict,Relpos(partv[p][j-1],partv[p][j]))}
                Dict1= Dict
                Dict2.update(Dict)
                Dict={part[p]:Dict2}
                Partdict1.update(Dict)
                j+=1

PL14={}
Arty = Artdict['PartL140']
for p in range(len(Partdict1)):
    part = list(PartL140.keys())
    Dict=Partdict1[partt[p][0]]
    PL14.update(Dict)
Arty.update(PartL140)


for i in range(0,l-1):
    Dict2={}
    x = len(Subx[i])
    for j in range(x):
        if Subx[i][j][0:3]=='Sub':
            for k in range(0,l-1):
                y = len(Subx[k])
                c= 0
                for ijk in range(y):
                    if Subx[k][ijk]==Subx[i][j]:
                        Dict={Subx[k][ijk]:Searchs2(Subx[i][j])}
                        key = NestSrcp('Sub'+str(i+1))
                        Dict = {key[c]:Dict}
                        Dict2.update(Dict)   
                    c += 1         
            Dict={'Sub'+str(i+1):Dict2} 
    Arty.update(Dict) 



Partdict={}   
for p in range(len(Parts)):    
    part = list(Parts.keys())
    partv = list(Parts.values())
    Dict2={}
    for i in range(0,l-1):
        y= len(Subz[i])
        for z in range (y):
            if Subz[i][z]==part[p] and part[p]!='PartL140':
                x = len(partv[p])
                j = 0
                point =Search(part[p])
                while j<x:
                   if j == 0:
                        Dict={partv[p][j]:point}
                        Dict2.update(Dict)
                        Dict={part[p]:Dict2}
                        Partdict.update(Dict)
                        j+=1
                   elif j!=0:
                        if j == 1:
                            Dictn={partv[p][0]:point}
                            Dict= Dictn
                            Dict={partv[p][j]:NestSrc(partv[p][j],Dict,Relpos(partv[p][j-1],partv[p][j]))}
                            Dict1= Dict
                            Dict2.update(Dict)
                            Dict={part[p]:Dict2}
                            Partdict.update(Dict)
                            j+=1
                        elif j!=1:
                            Dict= Dict1
                            Dict={partv[p][j]:NestSrc(partv[p][j],Dict,Relpos(partv[p][j-1],partv[p][j]))}
                            Dict1= Dict
                            Dict2.update(Dict)
                            Dict={part[p]:Dict2}
                            Partdict.update(Dict)
                            j+=1
            elif part[p]=='PartL140':
                Dict={'PartL140':Arty}
                Partdict.update(Dict)                
                    
def Interom(L,l2,l1):
    Assemblie ={}        
    L=L+1
    for i in range(1,L):
        Dict4 = {}
        Dict2={}
        k = len(Subs[i])
        E = Elements[i-1]
        for j in range(0,k,2):
            ln = Subs[i][j+1]
            lp =Subs_init[i][j+1]
            Dict = {Subs[i][j+1]:lp} 
            for c in range (1,l):
                r = len(Subs[c])
                for y in range(0,r,2):
                    ln2 = Subs[c][y+1]
                    lp2 =Subs_init[c][y+1]
                    pd=l2[c][y]
                    pd2=l2[c][y+l1]
                    for o in range(len(Term)):
                        for s in range(len(E)):
                            if ln2 == Term[o] and lp2 == E[s] and Term[o] == ln:
                                for p in range(len(Partdict)):
                                    part= list(Partdict.keys())
                                    if l1 == 1 and pd ==part[p]:
                                        Dict= {pd:Partdict.get(pd)}
                                        Dict = {pd2:Dict}
                                        Dict4.update(Dict)
                                        Dict = {Subs[i][j+1]:Dict4}
                                    elif l1 == 0 and pd2 ==part[p]:
                                        Dict = {pd2:Partdict.get(pd2)}
                                        Dict4.update(Dict)
                                        Dict = {Subs[i][j+1]:Dict4}
                        Dict2.update(Dict)
                Dict4={}
            SubN = {'Sub'+str(i):Dict2}
            
            for t in range(L-1):
                if Subs[i][j]== sub_lock[t]:
                    Dict = {'Sub'+str(t+1):Assemblie['Sub'+str(t+1)]}
                    Dict3 = {Subs[i][j+1]:Dict}
                    Dict2.update(Dict3)
                    SubN = {'Sub'+str(i):Dict2}
        
            Assemblie.update(SubN)
    return(Assemblie)
Assembly_L={'Sub11':Interom(11,Subs,0)['Sub11']}  
Assembly_Lf=Interom(11,Subs,0)  
               
TreeRev={}    
for p in range(len(Parts)):
    part = list(Parts.keys())
    partv=list(Parts.values())
    trap = list(Partdict.values())
    i = len(trap[p])
    Dict2={}
    Dict3={}
    Dict4={}
    Dict5={}
    Dict6={}
    for j in range(i):
        term = list((Partree[partv[p][j]].keys()))
        for s in range(len(term)):
            Dict={partv[p][j]:Partree[partv[p][j]]}
            Dict2.update(Dict)
            Dict={term[s]:Dict2}
            Dict3.update(Dict)
            Dict={part[p]:Dict3[term[s]]}
            Dict4.update(Dict)
            TreeRev.update(Dict4)
        
        

G = vd.KeysGraph(Partree)

G.draw('./test.png')
Image('./test.png')