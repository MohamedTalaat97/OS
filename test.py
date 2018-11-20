from tkinter import *
import tkinter.ttk as ttk
import numpy as np 
import matplotlib.pyplot as plt

class proc(object):

    def __init__(self, arr, bur, pri, n):
        self.arr = arr
        self.bur = bur
        self.pri = pri
        self.n = n
        self.wait = 0
        self.tat = 0 
        self.weighted =0
        self.start =0
        self.finish = 0
        self.served =0
        self.time = bur

context =1

procList = []
procList.append(proc (1,2,5,1))   
procList.append(proc (1,0.3,5,2)) 
st=[]
fn=[]
n=[] 
servedProc=-1    #no process
timestep = 0.1
arrSorted = sorted(procList, key=lambda x: x.arr, reverse=False) #sort according to arrival
time =arrSorted[0].arr
       #start of timeline
arrReady=[]
c=0
while c < len(arrSorted):
    if (arrSorted[c].arr<=time):
        arrReady.append(arrSorted[c])  # get the ready ones out of the arrival into the queue
        arrSorted.pop(c)
        c=c-1
    c = c+1
 
    
while (len(arrSorted)>0 or len(arrReady)>0): #main loop
       
    if servedProc != -1:
        m = arrReady[0].time
        for i in range(len(arrReady)):
            if (arrReady[i].time+context) < m:
                m = arrReady[i].time
                temp = arrReady[i]
                arrReady[i]=arrReady[0]
                arrReady[0]=temp
                
    else:
        arrReady.sort(key=lambda x: x.time, reverse=False)     # sort according to remaining time   
                
    if len(arrReady)>0:
        if servedProc!=-1 and servedProc != arrReady[0].n:
            fn.append(time)
            time += float(context)
            st.append(time)
            n.append(arrReady[0].n)
        if (servedProc==-1):
            time += float(context)
            st.append(time)
            n.append(arrReady[0].n)
                 
        servedProc = arrReady[0].n       #serving
        arrReady[0].time -= timestep                    
        time+= timestep
    else:   
        time+= timestep
        servedProc=-1                               #no serving  ->advance time    
        #new processes arriving
    c=0
    while c < len(arrSorted):
        if (arrSorted[c].arr<=time):
            arrReady.append(arrSorted[c])        # check new arriving
            arrSorted.pop(c)
            c=c-1
        c=c+1
        #finished proceses    
    c=0
    while c < len(arrReady):
        if arrReady[c].time <=0:
            for j in range(len(procList)):
                if arrReady[c].n ==procList[j].n :
                    fn.append(time+procList[j].time)        # remove finished proc from ready and set finish time in original list
                    procList[j].finish= time+procList[j].time
                    arrReady.pop(c)
                    servedProc=-1
                    c=c-1
                    break
        c=c+1
            
diff =[]   
    
for i in range(len(st)):
    diff.append(fn[i]-st[i])
                
print(st,n,fn)    
plt.bar(st, n, width = diff ,align='edge', color = ('blue'))
plt.show()