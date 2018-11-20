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



########################################################
f = open('input.txt', 'r')
processes = int(float(f.readline()))  # no of processes

arrival = f.readline()
k = arrival.split(' ')
arrivalMu = float(k[0])
arrivalSigma = float(k[1])

burst = f.readline()
k = burst.split(' ')
burstMu = float(k[0])
burstSigma = float(k[1])

priorityLamda = float(f.readline())
b = proc(4,5,6,7)

f.close()
################################################
procList = []
'''
for i in range(processes):
    arr = (np.random.normal(loc=arrivalMu, scale=arrivalSigma))
    bur = (np.random.normal(loc=arrivalMu, scale=arrivalSigma))
    pri = int(np.random.poisson(lam=priorityLamda))
    procList.append(proc(arr, bur, pri, i ))                          
    '''
procList.append(proc (1,2,5,1))   
procList.append(proc (9,1,5,2)) 
#procList.append(proc (3,2,5,2)) 
#procList.append(proc (7,2,5,3)) 
#procList.append(proc (7,4,5,2)) 
processes =2

#####################################################
o = open('output.txt', 'w')
o.write(str(processes) + '\n')

for p in procList:
    o.write(str(p.n) + ' ' + str(p.arr) + ' ' + str(p.bur) + ' ' + str(p.pri) + '\n')

o.close()


#################FCFS##################################

context =1 
procList = []
procList.append(proc (1,2,5,1))   
procList.append(proc (9,1,5,2)) 
    
arrSorted = sorted(procList, key=lambda x: x.arr, reverse=False)
    
    
for i in range(len(procList)):
    if i>0:
        if arrSorted[i].arr <= arrSorted[i-1].finish:
            arrSorted[i].start = arrSorted[i-1].finish+context
            arrSorted[i].finish = arrSorted[i].bur+arrSorted[i].start
        elif arrSorted[i].arr > arrSorted[i-1].finish:
            arrSorted[i].start =arrSorted[i].arr
            arrSorted[i].finish = arrSorted[i].bur+arrSorted[i].arr
    else:
        arrSorted[i].start =arrSorted[i].arr    
        arrSorted[i].finish =arrSorted[i].arr+arrSorted[i].bur
    
st =[]  
n =[]      
diff =[]
for i in range(len(procList)):
    st.append(procList[i].start)
    n.append(procList[i].n)
    diff.append(procList[i].finish - procList[i].arr )
        
print(st,n,diff)    
plt.bar(st, n, width = diff ,align='edge', color = ('blue'))
    
		
######################################################################
###########################SRTN#######################################
def SRTN(file,context):
    
    procList = []
    procList.append(proc (1,2,5,1))   
    procList.append(proc (9,1,5,2)) 
    st=[]
    fn=[]
    n=[]
    
    
    servedProc=-1    #no process
    timestep = 0.3
    arrSorted = sorted(procList, key=lambda x: x.arr, reverse=False) #sort according to arrival
    time =arrSorted[0].arr+float(context) 
    st.append(time)
    n.append(arrSorted[0].n)
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
                n.append(arrSorted[0].n)
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
                        c=c-1
                        break
            c=c+1
            
        
            
    print(st,n,diff)    
    plt.bar(st, n, width = diff ,align='edge', color = ('blue'))
    plt.show()

#######################################################
###############calc#################################	
'''
avgTat =0
weightedAvg =0
		
for i in range(len(procList)):
    arrSorted[i].tat = arrSorted[i].finish - arrSorted[i].arr
    arrSorted[i].wait= arrSorted[i].tat - arrSorted[i].bur	 # calc finish
    avgTat+=arrSorted[i].tat;
    weightedAvg += arrSorted[i].tat/arrSorted[i].bur
        
avgTat = avgTat/processes
weightedAvg = weightedAvg/processes
'''
'''
gui -> get data from text boxes and connect the button and get data form combo box 
code to read new input file 
'''
