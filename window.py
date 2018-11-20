from tkinter import *
import tkinter.ttk as ttk
import numpy as np 
import matplotlib.pyplot as plt

######################################################
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
        self.beenReady=0
##########################################################
class Window:
    def __init__(self,r):
        self.AlgoLabel=Label(r, text='Choose Algo')
        self.FileLabel = Label(r, text='File Name')
        self.ErrorLabel = Label(r, text='')
        self.FileEntry = Entry(r)
        self.ContextLabel = Label(r, text='context')
        self.ContextEntry = Entry(r)
        self.QuantumLabel = Label(r, text='RR quantum')
        self.QuantumEntry = Entry(r)
        self.combo =  ttk.Combobox(root, values=("FCFS", "HPF", "RR", "STRN"))
        self.combo.bind('<<ComboboxSelected>>', self.callback)
        self.bt = Button(r, text='ok')
        self.AlgoLabel.grid(row=2)
        self.combo.grid(row=2,column=1)
        self.FileLabel.grid(row=3)
        self.FileEntry.grid(row=3, column=1)
        self.ContextLabel.grid(row=4)
        self.ContextEntry.grid(row=4, column=1)
        self.bt.grid(row=6)
        self.ErrorLabel.grid(row=6,column=1)
        self.bt.bind("<Button-1>", self.done)
        self.data=[]
    
    def callback(self,event):
        if self.combo.get() == 'RR':
            self.QuantumLabel.grid(row=5)
            self.QuantumEntry.grid(row=5, column=1)
        else:
            self.QuantumLabel.grid_forget()
            self.QuantumEntry.grid_forget()
        
    def done(self, event):
        if self.FileEntry.get() == '' or self.ContextEntry.get() == '' or self.combo.get() == '' :
           self.ErrorLabel['text'] = 'please enter all fileds '
        elif not str.isdigit(self.ContextEntry.get()):
            self.ErrorLabel['text'] = 'please enter a valid context '
        elif ( str.isdigit(self.combo.get())) and self.combo.get() == 'RR':
            self.ErrorLabel['text'] = 'please enter a valid Quantum '    
            
        else:
             if self.combo.get() == 'FCFS':
                 FCFS(self.FileEntry.get(),self.ContextEntry.get())
             elif self.combo.get() == 'STRN':
                STRN(self.FileEntry.get(),self.ContextEntry.get())
             elif self.combo.get() == 'RR':
                RR(self.FileEntry.get(),self.ContextEntry.get(),self.QuantumEntry.get())
             elif self.combo.get() == 'HPF':
                HPF(self.FileEntry.get(),self.ContextEntry.get())
########################################################
def FCFS(file , context ):

   f=open(file,"r")
   lines=f.readlines()
   no = lines[0]
   no =no.replace('\n','')
   processes = int (no)
   lines.remove(lines[0])
   procList=[]
   for i in range(processes):
       priority=lines[i].split(' ')[3]
       priority=priority.replace('\n','')
       procList.append(proc(float(lines[i].split(' ')[1]),float(lines[i].split(' ')[2]),int(priority),int(lines[i].split(' ')[0])))
   f.close() 
    
   arrSorted = sorted(procList, key=lambda x: x.arr, reverse=False)   
   for i in range(len(procList)):
       if i>0:
           if arrSorted[i].arr <= arrSorted[i-1].finish:
               arrSorted[i].start = arrSorted[i-1].finish+float(context) 
               arrSorted[i].finish = arrSorted[i].bur+arrSorted[i].start
           elif arrSorted[i].arr > arrSorted[i-1].finish:
               arrSorted[i].start =arrSorted[i].arr+float(context) 
               arrSorted[i].finish = arrSorted[i].bur+arrSorted[i].start
       else:
            print(arrSorted[i].arr)
            arrSorted[i].start =arrSorted[i].arr+float(context)    
            arrSorted[i].finish =arrSorted[i].start+arrSorted[i].bur
 
   st =[]  
   n =[]      
   diff =[]
   for i in range(len(procList)):
        st.append(procList[i].start)
        n.append(procList[i].n)
        diff.append(procList[i].finish - procList[i].start )
            
   print(st,n,diff)    
   plt.bar(st, n, width = diff ,align='edge', color = ('blue'))
   plt.show()

##############################################################################    
def STRN(file,context):
    
    f=open(file,"r")
    lines=f.readlines()
    no = lines[0]
    no =no.replace('\n','')
    processes = int (no)
    lines.remove(lines[0])
    procList=[]
    for i in range(processes):
        priority=lines[i].split(' ')[3]
        priority=priority.replace('\n','')
        procList.append(proc(float(lines[i].split(' ')[1]),float(lines[i].split(' ')[2]),int(priority),int(lines[i].split(' ')[0])))
    f.close() 
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
                        servedProc=-1
                        arrReady.pop(c)
                        c=c-1
                        break
            c=c+1           
    diff =[]      
    for i in range(len(st)):
        diff.append(fn[i]-st[i])               
    print(st,n,fn)    
    plt.bar(st, n, width = diff ,align='edge', color = ('blue'))
    plt.show()   
###############################################################################
def RR(file ,context ,quantum):
    
    f=open(file,"r")
    lines=f.readlines()
    no = lines[0]
    no =no.replace('\n','')
    processes = int (no)
    lines.remove(lines[0])
    procList=[]
    cpyProcList=[]
    for i in range(processes):
        priority=lines[i].split(' ')[3]
        priority=priority.replace('\n','')
        procList.append(proc(float(lines[i].split(' ')[1]),float(lines[i].split(' ')[2]),int(priority),int(lines[i].split(' ')[0])))
        cpyProcList.append(proc(float(lines[i].split(' ')[1]),float(lines[i].split(' ')[2]),int(priority),int(lines[i].split(' ')[0])))
    f.close() 
    cpyProcList.sort(key=lambda x: x.arr, reverse=False)
    readyQueue=[]
    t=cpyProcList[0].arr+float(context) #initial time 
    readyQueue.append(cpyProcList[0])
    cpyProcList[0].beenReady=1
    ################# Arrays for Graph####################
    procStarts=[]
    procEnds=[]
    procDiff=[]
    procIDs=[]
    flag=0
    lastProcess=cpyProcList[0]
    while True:
        if len (readyQueue) !=0:
            if readyQueue[0].bur > float(quantum):
                if lastProcess.n!=readyQueue[0].n:
                    t+=float(context)
                procStarts.append(t)
                t+= float(quantum)
                procEnds.append(t)
                readyQueue[0].bur-= float(quantum)
                for u in range (len(cpyProcList)):
                    if readyQueue[0].n == cpyProcList[u].n:
                        cpyProcList[u].bur=readyQueue[0].bur
                readyQueue[0].arr+=float(quantum)
                procIDs.append(readyQueue[0].n)
                
            else:
                if lastProcess.n!=readyQueue[0].n:
                    t+=float(context)
                procStarts.append(t)
                t+=readyQueue[0].bur
                procEnds.append(t)
                readyQueue[0].arr+=readyQueue[0].bur
                for j in range(len(procList)):
                    if readyQueue[0].n == procList[j].n:
                        procList[j].finish=t
                        procIDs.append(readyQueue[0].n)
                readyQueue[0].bur=0
                for u in range (len(cpyProcList)):
                    if readyQueue[0].n == cpyProcList[u].n:
                        cpyProcList[u].bur=readyQueue[0].bur

            for index in range (len(cpyProcList)):
                if cpyProcList[index].arr<=readyQueue[0].arr:
                    if cpyProcList[index].beenReady==0:
                        readyQueue.append(cpyProcList[index])
                        cpyProcList[index].beenReady=1
                        
            if readyQueue[0].bur!=0:
                for index in range (len(cpyProcList)):
                    if cpyProcList[index].arr<=t:
                        if cpyProcList[index].beenReady==0:
                            readyQueue.append(cpyProcList[index])
                            cpyProcList[index].beenReady=1
                readyQueue.append(readyQueue[0])
                readyQueue.remove(readyQueue[0])
            else:
                readyQueue.remove(readyQueue[0])           
        else:
            t+=1
            for index in range (len(cpyProcList)):
                    if cpyProcList[index].arr<=t:
                        if cpyProcList[index].beenReady==0:
                            readyQueue.append(cpyProcList[index])
                            cpyProcList[index].beenReady=1
        for index in range (len(cpyProcList)):
             if cpyProcList[index].bur==0:
                 flag+=1
        if flag == len(cpyProcList):
            break
        else:
            flag=0       
    for index in range (len(procEnds)):
        procDiff.append(procEnds[index]-procStarts[index])
        
    for index in range (len(procList)):
        procList[index].tat=procList[index].finish-procList[index].arr
        procList[index].wait=procList[index].tat-procList[index].bur
        procList[index].weighted=float(procList[index].tat)/float(procList[index].bur)
        
    plt.bar(procStarts, procIDs, width = procDiff ,align='edge', color = ('blue'))
    print(len(procIDs))
    plt.show()

###############################################################################
def HPF(file,c):
    context = float(c)
    f=open(file,"r")
    lines=f.readlines()
    no = lines[0]
    no =no.replace('\n','')
    processes = int (no)
    lines.remove(lines[0])
    procList=[]
    cpyProcList=[]
    for i in range(processes):
        priority=lines[i].split(' ')[3]
        priority=priority.replace('\n','')
        procList.append(proc(float(lines[i].split(' ')[1]),float(lines[i].split(' ')[2]),int(priority),int(lines[i].split(' ')[0])))
        cpyProcList.append(proc(float(lines[i].split(' ')[1]),float(lines[i].split(' ')[2]),int(priority),int(lines[i].split(' ')[0])))
    f.close() 
    servedProcList = []
    procList.sort(key=lambda x: x.arr, reverse=False)   
    #handeling first process
    tmparr=[]
    for i in range (len(procList)):
        if procList[0].arr==procList[i].arr:
            tmparr.append(procList[i])
    tmparr.sort(key=lambda x: x.pri, reverse=True)
    for index in range(len(procList)):
        if tmparr[0].n == procList[index].n:
            procList[index].start=procList[index].arr+context
            procList[index].finish=procList[index].start+procList[index].bur
            procList[index].served=1
            servedProcList.append(procList[index])
    tmparr=[]
    ######################################################
    allProcessesAreDone=False
    while allProcessesAreDone!=True:
        for i in range (len(procList)):
            temparr=[]
            #first case if the arrival time of [i] is less than the finish time [i-1]
            if True:
                if procList[i].served!=1:
                    for index in range(len(procList)):
                        if procList[index].served!=1 and procList[index].arr<=servedProcList[-1].finish:
                            temparr.append(procList[index])
                    if len(temparr)>0:
                        temparr.sort(key=lambda x: x.pri, reverse=True)
                        for index in range(len(temparr)):
                            if temparr[index].arr == temparr[0].arr and temparr[index].pri==temparr[0].pri and temparr[index].n<temparr[0].n:
                                temparr[0]=temparr[index]
                    for index in range(len(procList)):
                        if len(temparr)>0 and temparr[0].n == procList[index].n:
                            if len(servedProcList)>0:
                                procList[index].start=servedProcList[-1].finish+context
                                procList[index].finish=procList[index].start+procList[index].bur
                            else:
                                procList[index].start=procList[index].arr+context
                                procList[index].finish=procList[index].start+procList[index].bur
                            procList[index].served=1
                            servedProcList.append(procList[index])
    #################################################################################################################################
                    #second case if the arrival time of [i] is greater than the finish time [i-1]
                    if len(temparr)==0:
                        for index in range(len(procList)):
                            if procList[index].served!=1 and procList[index].arr>servedProcList[-1].finish:
                                temparr.append(procList[index])
                        temparr.sort(key=lambda x: x.arr, reverse=False)
                        for index in range(len(temparr)):
                            #check if there is more than on e process have > arr but diff priorities
                            if temparr[index].arr == temparr[0].arr and temparr[index].pri>temparr[0].pri:
                                temparr[0]=temparr[index]
                            elif temparr[index].arr == temparr[0].arr and temparr[index].pri==temparr[0].pri and temparr[index].n<temparr[0].n:
                                temparr[0]=temparr[index]
                        #marking process as served and put it in the served list
                        for index in range(len(procList)):
                            if temparr[0].n == procList[index].n:
                                if len(servedProcList)>0:
                                    procList[index].start=procList[index].arr+context
                                    procList[index].finish=procList[index].start+procList[index].bur
                                procList[index].served=1
                                servedProcList.append(procList[index])
    #####################################################################################################################################
        #check if all processes are served to exit the while loop
        for i in range (len(procList)):
            if procList[i].served!=1:
                allProcessesAreDone=False
                break
            else:allProcessesAreDone=True
      
    for i in range (len(servedProcList)):
        servedProcList[i].tat=servedProcList[i].finish-servedProcList[i].arr
        servedProcList[i].wait=servedProcList[i].tat-servedProcList[i].bur
        servedProcList[i].weighted=float(servedProcList[i].tat)/float(servedProcList[i].bur)
        print(servedProcList[i].finish)
        print(servedProcList[i].n)
    ################################ HPF Graph ####################################   
    procStarts=[]
    procEnds=[]
    procDiff=[]
    procIDs=[]
    for i in range (len(servedProcList)):
        procIDs.append(servedProcList[i].n)
        procStarts.append(servedProcList[i].start)
        procEnds.append(servedProcList[i].finish)
        procDiff.append(procEnds[i]-procStarts[i])
        print( procIDs[i],procStarts[i], procEnds[i],procDiff[i])
        
    plt.bar(procStarts, procIDs, width = procDiff ,align='edge', color = ('blue'))
    plt.show()        
###############################################################################
root = Tk()
w=Window(root)
root.mainloop()



