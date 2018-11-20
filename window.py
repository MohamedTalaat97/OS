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
        elif (not str.isdigit(self.combo.get())) and self.combo.get() == 'RR':
            self.ErrorLabel['text'] = 'please enter a valid Quantum '    
            
        else:
             if self.combo.get() == 'FCFS':
                 FCFS(self.FileEntry.get(),self.ContextEntry.get())
             elif self.combo.get() == 'STRN':
                STRN(self.FileEntry.get(),self.ContextEntry.get())
########################################################

def FCFS(file , context ):

    procList = []
    procList.append(proc (1,2,5,1))   
    procList.append(proc (2,0.2,5,2)) 
    
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
    
    procList = []
    procList.append(proc (1,2,5,1))   
    procList.append(proc (2,0.3,5,2)) 
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

 

root = Tk()
w=Window(root)
root.mainloop()



