#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:07:21 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 05:47:37 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:03:14 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:54:20 2020

@author: fadewell
"""

import qrcode
#import pyqrcode
import numpy as np
#from pandas import D
import matplotlib.pyplot as plt
#import pprint
import visualisedictionary as vd
from IPython.display import Image
#from sets import Set

OPQR = list()
db = list()
ind = list()
location = []

import cv2
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
    for i in range (n_lines):
        #draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
       # cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
        OPQR.append( f"{data}" )

for i in range(1,12):
   # import cv2
# read the QRCODE image
    rep = str('7p')+'0'+str(i)
    QRin77pp = str("QRin77pp.png").replace('7pp',rep)
    img = cv2.imread(QRin77pp)
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
          #  cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
            OPQR.append( f"{data}" )
    
dbQR = []
for i in range(0,len(OPQR)):
    c = str(OPQR[i])
    c= c.replace('[','').replace(']', '').replace(' ', '').replace("''", "")
    db.append([c])
    pars=c.split(',')
    dbQR.append(pars)
    ind.append(len(pars))
    #ind 
dQR = []
itd= []
axis0 = len(dbQR)
for i in range(0,axis0):
    axis1 = int(ind[i])
    dQR0= []
    for j in range(axis1):
      #  print(i,j)
        par = int(dbQR[i][j])
        print(par)
        dQR0.append(par)
    dQR.append(dQR0)
    ist = dQR0[0]
    itd.append(ist)
    
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
    #    cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
number =  f"{data}"
number = number.replace('-1','')
numbers.append(number)


for i in range(1,12):
   # import cv2
# read the QRCODE image
    rep = str('es')+'0'+str(i)
    print(rep)
    compressedEntriesp = str("compressedEntriesp.png").replace('esp',rep)
    print(compressedEntriesp)
    img2 = cv2.imread(compressedEntriesp)
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
        #    cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
            number =  f"{data}"
            print(number)
    number = number.replace('-1','')
    numbers.append(number)
   
numbers[10]='0113355'

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
      #  cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
page = f"{data}"
pages.append(page)

for i in range(1,12):
    rep = str('es')+'0'+str(i)
    Entitiesp = str('Entitiesp.png').replace('esp',rep)
    img3 = cv2.imread(Entitiesp)
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
          #  cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
        page = f"{data}"
    pages.append(page)
    
    
sortcode = []
AmiQR = []
ggQR = []
for i in range(len(pages)):
    axis2= len(pages[i])
    AmiQR0 = []
    for j in range(axis2):
        a = j+1
        b = j
        c = pages[i]
        d = c[b:a]
        d = int(d)
        AmiQR0.append(d)
    AmiQR.append(AmiQR0)

for i in range(len(ind)):    
    axis3 = ind[i]
    ggQR0=[0]
    for j in range (1,axis3):
        d2 = numbers[i]
        d3 = d2[dQR[i][j-1]:dQR[i][j]]
        d3= int(d3)
        ggQR0.append(d3)
    ggQR.append(ggQR0)

QRlist = []
for i in range(len(ind)):    
    axis3 = ind[i]
    QRlist0=[0]
    for j in range (1,axis3):
        e = str(ggQR[i][j])
        f = len(e)/(j+1)
        f = int(f)
        QRlist0.append(f)
    QRlist.append(QRlist0)
    
wtj = []
tCt = []
k = 1
for y in range(len(ind)):
    k = 1
    axis3 = ind[y]
    wtj0=[]
    while k < axis3:
        i=0
        istr = str(ggQR[y][k])
        j = (k+1)* QRlist[y][k]
        wtj0.append(j)
        k += 1
      #  ij = istr[i:i+k]
    wtj.append(wtj0)
    i1 = k
    tCt0= [0]
    L= ind[y] - 2
    if itd[y] != 1:
        x = 1
        while itd[y] > x:
            tCt0.append(int(numbers[y][x]))
            x+=1
    for i in range(i1-L,axis3+1):
        h = wtj0[i-2]
        for k in range (0,wtj0[i-2],i):
            istr = str(ggQR[y][i-1])
            j= istr[k:k+i]
            j = int(j)
            tCt0.append(j)
    tCt.append(tCt0)
    
files = []
file1 = open("ShipParts.txt","r") 
files.append(file1)
for i in range (1,12):
    rep = str('Instr')+str(i)
    subtxt = str(rep)
    file1 = open(subtxt,"r") 
    files.append(file1)
    
duuxx = []
dix = []

for i in range(0,len(files)):
    dix0= files[i].readlines()
    z = np.size(dix0)
    ion = []
    files[i].close()
    for x in range(z):
        ion.append(dix0)
    dix0 = str(dix0)
    duuxx0=dix0#.replace(", \' \',", "")#.replace(", \'" , "")#.replace("[","")#.replace("]","")#.replace("'","")#.replace("\\n", "  ")#.replace(","," ")
    duuxx0=dix0.replace("[","").replace("]","").replace(","," ").replace("\'  \'"," ").replace("\'" , "").replace("\\n", "  ").replace("     ", 'rQr')
    tCt[i].append(-1)
    duuxx.append(duuxx0)

AmQR = []
for z in range (len(pages)):
    axis4= len(pages[z])-1
    AmQR0=[]
    for i in range (axis4):
        a = tCt[z][i]
        b = tCt[z][i+1]
        c = (str(a)+str(b))
       # c = int(c)
      #  print(c)
        AmQR0.append(c)
    AmQR.append(AmQR0)
OPQR_init = list()
db_init = list()
ind_init = list()
location_init = []

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
    #    cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
OPQR_init.append( f"{data}" )

for i in range(1,12):
   # import cv2
# read the QRCODE image
    rep = str('7p')+'0'+str(i)
    QRin77pp = str("QRin77pp.png").replace('7pp',rep)
    img = cv2.imread(QRin77pp)
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
       #     cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
            OPQR_init.append( f"{data}" )
    
dbQR_init = []
for i in range(0,len(OPQR)):
    c = str(OPQR_init[i])
    c= c.replace('[','').replace(']', '').replace(' ', '').replace("''", "")
    db.append([c])
    pars=c.split(',')
    dbQR_init.append(pars)
    ind_init.append(len(pars))
    #ind 
dQR_init = []
itd_init= []
axis0 = len(dbQR_init)
for i in range(0,axis0):
    axis1 = int(ind_init[i])
    dQR0= []
    for j in range(axis1):
      #  print(i,j)
        par = int(dbQR_init[i][j])
        print(par)
        dQR0.append(par)
    dQR_init.append(dQR0)
    ist = dQR0[0]
    itd_init.append(ist)
    
locations_init= []
location_init =[]
numbers_init = []

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
       # cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
number =  f"{data}"
number = number.replace('-1','')
numbers_init.append(number)

for i in range(1,12):
   # import cv2
# read the QRCODE image
    rep = str('es')+'0'+str(i)
    print(rep)
    compressedEntriesp = str("compressedEntriesp.png").replace('esp',rep)
    print(compressedEntriesp)
    img2 = cv2.imread(compressedEntriesp)
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
       #     cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
            number =  f"{data}"
            print(number)
    number = number.replace('-1','')
    numbers_init.append(number)
   


pages_init = []

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
       # cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
page = f"{data}"
pages_init.append(page)

for i in range(1,12):
    rep = str('es')+'0'+str(i)
    Entitiesp = str('Entitiesp.png').replace('esp',rep)
    img3 = cv2.imread(Entitiesp)
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
           # cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
        page = f"{data}"
    pages_init.append(page)
    
    
sortcode_init = []
AmiQR_init = []
ggQR_init = []
for i in range(len(pages_init)):
    axis2= len(pages_init[i])
    AmiQR0 = []
    for j in range(axis2):
        a = j+1
        b = j
        c = pages_init[i]
        d = c[b:a]
        d = int(d)
        AmiQR0.append(d)
    AmiQR_init.append(AmiQR0)

for i in range(len(ind)):    
    axis3 = ind_init[i]
    ggQR0=[0]
    for j in range (1,axis3):
        d2 = numbers_init[i]
        d3 = d2[dQR_init[i][j-1]:dQR_init[i][j]]
        d3= int(d3)
        ggQR0.append(d3)
    ggQR_init.append(ggQR0)

QRlist_init = []
for i in range(len(ind)):    
    axis3 = ind_init[i]
    QRlist0=[0]
    for j in range (1,axis3):
        e = str(ggQR_init[i][j])
        f = len(e)/(j+1)
        f = int(f)
        QRlist0.append(f)
    QRlist_init.append(QRlist0)
    
wtj_init = []
tCt_init = []
k = 1
for y in range(len(ind_init)):
    k = 1
    axis3 = ind_init[y]
    wtj0=[]
    while k < axis3:
        i=0
        istr = str(ggQR_init[y][k])
        j = (k+1)* QRlist_init[y][k]
        wtj0.append(j)
        k += 1
      #  ij = istr[i:i+k]
    wtj_init.append(wtj0)
    i1 = k
    tCt0= [0]
    L= ind_init[y] - 2
    if itd_init[y] != 1:
        x = 1
        while itd[y] > x:
            tCt0.append(int(numbers_init[y][x]))
            x+=1
    for i in range(i1-L,axis3+1):
        h = wtj0[i-2]
        for k in range (0,wtj0[i-2],i):
            istr = str(ggQR_init[y][i-1])
            j= istr[k:k+i]
            j = int(j)
            tCt0.append(j)
    tCt_init.append(tCt0)
    
files_init = []
file1 = open("ShipParts.txt","r") 
files_init.append(file1)
for i in range (1,12):
    rep = str('Instr')+str(i)+'2'
    subtxt = str(rep)
    file1 = open(subtxt,"r") 
    files_init.append(file1)
    
duuxx_init = []
dix_init = []

for i in range(0,len(files_init)):
    dix0= files_init[i].readlines()
    z = np.size(dix0)
    ion = []
    files[i].close()
    for x in range(z):
        ion.append(dix0)
    dix0 = str(dix0)
    duuxx0=dix0#.replace(", \' \',", "")#.replace(", \'" , "")#.replace("[","")#.replace("]","")#.replace("'","")#.replace("\\n", "  ")#.replace(","," ")
    duuxx0=dix0.replace("[","").replace("]","").replace(","," ").replace("\'  \'"," ").replace("\'" , "").replace("\\n", "  ").replace("     ", 'rQr')
    tCt_init[i].append(-1)
    duuxx_init.append(duuxx0)

AmQR_init = []
for z in range (len(pages)):
    axis4= len(pages[z])-1
    AmQR0=[]
    for i in range (axis4):
        a = tCt[z][i]
        b = tCt[z][i+1]
        c = (str(a)+str(b))
       # c = int(c)
      #  print(c)
        AmQR0.append(c)
    AmQR_init.append(AmQR0)        
xy = []
for z in range(len(files)):
    j=0
    i = 1
    xy0=[]
    #while i or j < np.size(tCt) or np.size(AmQR):
    while i & j < np.size(AmQR[z])-1:
    
        x=AmQR[z][j]
        #print (x)
       # qr = qrcode.make(x)
       # qr.save('entrypoints.png')
    #    img1 = cv2.imread("entrypoints.png")
        aa = AmiQR[z][j]
        i += 1
        bb = AmiQR[z][i-1]
        j +=1
        yy = x [0:aa]
        yy = int(yy)
        xx = x [aa:aa+bb]
        xx= int(xx)
       #### xy = (str(yy)+str(xx))
        xxyy =[(xx,yy)]
        xy0.append(xxyy)  
    xy.append(xy0)
for i in range(len(tCt)):
    j=1
    if i == 0 :
        while j <np.size(tCt[i])-3:
            aa= xy[i][j]
            a = str(aa)
            a = str(a)
            a = a.replace('[','').replace('(','').replace(']','').replace(')','')
            ab = a.split(',')
            aaa = int(ab[0])
            aab = int(ab[1])####
         
            if j != np.size(tCt[i])-3:
                print (duuxx[i][aab:aaa-4])
            elif j == np.size(tCt[i])-3:
                print(duuxx[i][aab:aaa-2])
            print(j,aab,aaa)
    
            qr = qrcode.make(duuxx[i][aab:aaa-4])
            qr.save('partEntities.png')
            img1 = cv2.imread("partEntities.png")
            greyy = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            data, bbox, straight_qrcode = detector.detectAndDecode(img1)
         #   plt.imshow(greyy)
         #   plt.show()
            j += 1
    elif i != 0:
        while j <np.size(tCt[i])-2:
            aa= xy[i][j]
            a = str(aa)
            a = str(a)
            a = a.replace('[','').replace('(','').replace(']','').replace(')','')
            ab = a.split(',')
            aaa = int(ab[0])
            aab = int(ab[1])####
         
            if j != np.size(tCt[i])-3:
                print (duuxx[i][aab:aaa-4])
            elif j == np.size(tCt[i])-3:
                print(duuxx[i][aab:aaa-2])
            print(j,aab,aaa)
    
            qr = qrcode.make(duuxx[i][aab:aaa-4])
            qr.save('partEntities.png')
            img1 = cv2.imread("partEntities.png")
            greyy = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            data, bbox, straight_qrcode = detector.detectAndDecode(img1)
         #   plt.imshow(greyy)
         #   plt.show()
            j += 1
            
dax = dax_init = []
p2 = p2_init=[]
p1=p1_init=[]
Subs_init =[]

for i in range(len(duuxx)):
    if i == 0 :
        p01 = tCt[i][1]
        p02 = tCt[i][len(tCt[i])-2]
        dax0= duuxx[i][p01:p02]
        dax0 = dax0.replace('   ',',').replace('rQr ', '.')#.replace(' ','')
        dax0 = dax0[:len(dax0)-3]
        dax.append(dax0)
    else:
        p01 = tCt[i][1]
        p02 = tCt[i][len(tCt[i])-2]
        dax0= duuxx[i][p01:p02]
        dax0 = dax0.replace('   ',',').replace('rQr ', '.')#.replace(' ','')
        dax0 = dax0[:len(dax0)]
        dax.append(dax0)
    p1.append(p01)
    p2.append(p02)
        
 
Subs = []  
for i in range(0,len(dax)):
    blanks= []
    if i != 0 :
        dax0= dax[i][p1[i]:p2[i]]
        dax0 = dax[i].replace('rQr',',').replace(', ',',').replace('   ',',').replace('.',',')
        dax0 = dax0[:len(dax0)-2]
        sub = dax0.split(',')
        Subs.append(sub)
    else:
        dax0= dax[0]
        dax0 = dax0.replace('.',',')#.replace(' ','')
        dax0 = dax0[:len(dax[0])]
        sub = dax0.split(',')
        Subs.append(sub)
        print(Subs)







for i in range(len(duuxx_init)):
    if i == 0 :
        p01_init = tCt_init[i][1]
        p02_init = tCt_init[i][len(tCt_init[i])-2]
        dax0_init= duuxx_init[i][p01_init:p02_init]
        dax0_init = dax0_init.replace('   ',',').replace('rQr ', '.')#.replace(' ','')
        dax0_init = dax0_init[:len(dax0_init)-3]
        dax_init.append(dax0_init)
    else:
        p01_init = tCt_init[i][1]
        p02_init = tCt_init[i][len(tCt_init[i])-2]
        dax0_init= duuxx_init[i][p01_init:p02_init]
        dax0_init = dax0_init.replace('   ',',').replace('rQr ', '.')#.replace(' ','')
        dax0_init = dax0_init[:len(dax0_init)]
        dax.append(dax0_init)
    p1_init.append(p01_init)
    p2_init.append(p02_init)
        
 
for i in range(0,len(dax_init)):
    blanks_init= []
    if i != 0 :
        dax0_init= dax_init[i][p1_init[i]:p2_init[i]]
        dax0_init = dax_init[i].replace('rQr',',').replace(', ',',').replace('   ',',').replace('.',',')
        dax0_init = dax0_init[:len(dax0_init)-2]
        sub_init = dax0_init.split(',')
        Subs_init.append(sub_init)
    else:
        dax0_init= dax_init[0]
        dax0_init = dax0_init.replace('.',',')#.replace(' ','')
        dax0_init = dax0_init[:len(dax_init[0])]
        sub_init = dax0_init.split(',')
        Subs_init.append(sub_init)
Subs_in = []
for i in range (12,len(Subs_init)):
    Subs_in.append(Subs_init[i])
Parts ={}
Keys={}
Assembly={}
Sub1 = {}
Sub2={}
Sub3={}
QRcodes ={}
Values={}
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
    elif int(tCt[0][i-1])>= Sub1st:
       # locations=(tCt[0][i-1],duuxx[0][b:a-4])
    #    location.append(locations)
        Subassemblies=(str(tCt[0][i-1]),duuxx[0][b:a-4])
        Subassembly.append(Subassemblies)
    #print(duuxx[b:a-4])
    Dict={duuxx[0][b:a-4]:str(tCt[0][i-1])}
    Parts.update(Dict)
 
    i += 1
Subassembly= np.array(Subassembly)
Subassembly = np.transpose(Subassembly)
location= np.array(location)
location = np.transpose(location)
partlock = list(location[1])
partcode = location[0]
sub_lock = list(Subassembly[1])
sub_code = Subassembly[0]
plus = str('+')
minus = str('-')
Sub = {}
Dict2 ={}
subcode = []
sortcode = []
partsubs=[]
l = len(Subs)
Subs_in = Subs

for i in range(1,l):
    Dict2 = {}
    assem = str('PartS')
    k = len(Subs_in[i])
    assem = assem + str(i)
    for j in range(0,k,2):
        val = str(int(j/2+1))
        Dict = {Subs_in[i][j+1]:Subs_in[i][j]}
        Dict2.update(Dict)
        SubN = {'Sub'+str(i):Dict2}
        
        for t in range(l-1):
            if Subs_in[i][j]== sub_lock[t]:
               # print('i','j',i,j,t+1,)
                Dict = {'Sub'+str(t+1):Sub['Sub'+str(t+1)]}
               # print(Sub[t+1],Dict)
                Dict3 = {Subs_in[i][j+1]:Dict}
                Dict2.update(Dict3)
                SubN = {'Sub'+str(i):Dict2}
               # Sub.update(SubN)
    
        Sub.update(SubN)
        
Term = {}
for i in range(1,l):
    assem = str('PartS')
    k = len(Subs[i])
    assem = assem + str(i)
    for j in range(0,k,2):
        val = int(j/2+1)
        Dict = {Subs[i][j+1]:Subs[i][j+1]}
        
        #print(Dict)
        
       # Dict = {}
        Term.update(Dict)
Term = list(Term)
iAssembly ={}        
Elements = []
for i in range(1,l):
    Dict2 = {}
    Dict4={}
    assem = str('PartS')
    k = len(Subs[i])
    Elem =[]
    assem = assem + str(i)
    for j in range(0,k,2):
        val = int(j/2+1)
        Dict = {Subs_in[i][j+1]:Subs[i][j+1]}
        
     #   print(Dict)
        Elem.append(Subs_in[i][j+1])
       # Dict = {}
        Dict2.update(Dict)
       
                
    #    Dict= Dict2.setdefault(Subs[i][j+1])
        
        SubN = {'Sub'+str(i):Dict2}
        
        for t in range(l-1):
            if Subs_in[i][j]== sub_lock[t]:
               # print('i','j',i,j,t+1,)
                Dict = {'Sub'+str(t+1):iAssembly['Sub'+str(t+1)]}
               # print(Sub[t+1],Dict)
                Dict3 = {Subs_in[i][j+1]:Dict}
                Dict2.update(Dict3)
                SubN = {'Sub'+str(i):Dict2}
               # Sub.update(SubN)
        
        iAssembly.update(SubN)  
    Elements.append(Elem)
Assembly ={}        
Term

for i in range(1,l):
    Dict4 = {}
    Dict2={}
    assem = str('PartS')
    k = len(Subs[i])
    E = Elements[i-1]
    assem = assem + str(i)
   # val = 0 
    for j in range(0,k,2):
        
        val = int(j/2+1)
        EL = E[val-1]
        print(EL)
        ln = Subs[i][j+1]
        lp =Subs_in[i][j+1]
        Dict = {Subs[i][j+1]:lp} 
        for c in range (1,l):
            r = len(Subs[c])
            
            for y in range(0,r,2):
                ln2 = Subs[c][y+1]
                lp2 =Subs_in[c][y+1]
                for o in range(len(Term)):
                    for s in range(len(E)):
                        if ln2 == Term[o] and lp2 == E[s] and Term[o] == ln:
                            Dict = {lp2:s+1}
                            Dict4.update(Dict)
                           # print(ln2,lp2,s+1,EL)
                          #  print(Dict4,lp2,Dict2)
                            Dict = {Subs[i][j+1]:Dict4}
                    Dict2.update(Dict)
            Dict4={}
        
        
       # Dict = {}
        
     #   Dict = {Subs_in[i][j+1]:Subs[i][j+1]}
       # Dict4.append(Subs_in[i][j+1])
           # print(Dict4)
       # while z <= count:
       #     z+=1
                    
            
         
           # print(z+1,val,Dict,ln2)
              
           # Dict = {str(val):Dict}
        #Dict2.update(Dict)
           
        SubN = {'Sub'+str(i):Dict2}
        
        for t in range(l-1):
            if Subs[i][j]== sub_lock[t]:
               # print('i','j',i,j,t+1,)
                Dict = {'Sub'+str(t+1):Assembly['Sub'+str(t+1)]}
               # print(Sub[t+1],Dict)
                Dict3 = {Subs[i][j+1]:Dict}
                Dict2.update(Dict3)
                SubN = {'Sub'+str(i):Dict2}
               # Sub.update(SubN)
    
        Assembly.update(SubN) 
#Assembly = {'Sub11':Assembly['Sub11']}

#vd.pprint(Assembly)
Assembly ={}
Subone = [0,1,2,3,4,5,6,7,8,9,10,11]
Subway =[0,1,2,3,4,5,6,7,8,9,10,11]
Subwas =[0,1,2,3,4,5,6,7,8,9,10,11]
for i in range(1,12):
    #print(i,'doux',len(Subs[i]))
    k = len(Subs[i])
    elp = []
    hel = []
    for j in range(0,k,2):
        print(Subs[i][j])
        elp.append(Subs[i][j])        
        hel.append(Subs[i][j+1])
    Subone[i] = elp
    Subway[i]= hel
    Subwas[i] = hel
Subone.pop(0)
Subway.pop(0)   
Subwas.pop(0)

for i in range(1,12):
    mylist = set(Subway[i-1])
    Subway[i-1]=list(mylist)

Assembly ={}

for i in range (1,12):
    Subj = {}
    for j in Subway[i-1]: 
        Dic = {}
        k = len(Subwas[i-1])
       # print(k,j)
        for kij in range(0,k):
           # print(j,Subwas[i-1][kij],kij)
            if j == Subwas[i-1][kij]:
                print(kij,'here',Subone[i-1][kij][0:4])
                if Subone[i-1][kij][0:5] != 'PartS' :
                    Dic.update({Subone[i-1][kij]:kij})
                    Subj.update({j:Dic})
                elif Subone[i-1][kij][0:5] == 'PartS' :
                    ijk = int(Subone[i-1][kij][5:])
                    print(Subone[ijk],'THAt') 
                    Dic.update(Assembly['PartS'+str(Subone[i-1][kij][5:])])
                    Subj.update({j:Dic})
                print(Subj)
        Assembly.update({'PartS'+str(i):Subj})
                
##### no sub count


Assembly ={}

for i in range (1,12):
    Subj = {}
    for j in Subway[i-1]: 
        Dic = {}
        k = len(Subwas[i-1])
       # print(k,j)
        for kij in range(0,k):
           # print(j,Subwas[i-1][kij],kij)
            if j == Subwas[i-1][kij]:
                print(kij,'here',Subone[i-1][kij][0:4])
                if Subone[i-1][kij][0:5] != 'PartS' :
                    Dic.update({Subone[i-1][kij]:kij})
                    Subj.update({j:Dic})
                elif Subone[i-1][kij][0:5] == 'PartS' :
                    ijk = int(Subone[i-1][kij][5:])
                    print(Subone[ijk],'THAt') 
                    Dic.update({'PartS'+str(Subone[i-1][kij][5:]):Assembly['PartS'+str(Subone[i-1][kij][5:])]})
                    Subj.update({j:Dic})
                print(Subj)
            Assembly.update({'PartS'+str(i):Subj})

for i in range (1,12):
    Subf=Subs[i]
    k = 0
    procs = {}
    for j in Subf:
        proc = j
        k+=1
        if k/2 != int(k/2):
           # print(j,i,k)
            for ijk in range (1,12):
                if j == 'PartS'+str(ijk):
                   # print(j,i,'t!t',ijk)
                    
                    Subs[i][k-1]= Subs[ijk]

     
                    
for i in range (1,12):
    Subf=Subs[i]
    k = 0
    procs = {}
    for j in Subf:
        proc = j
        k+=1
                    
        if k/2 == int(k/2):
            kij = 0
            for jik in Subf:
                
                if jik == j:
                    kij +=1
#3                    print(j,i,'t!t',jik,kij,int(k/2))
                    procs.update({jik:kij})
 #         3#        3  print(procs, jik)
                 #   print()
#            pass
          #  print('else')
 #   print(Aset)

G = vd.KeysGraph(Assembly)

G.draw('./test.png')
Image('./test.png')