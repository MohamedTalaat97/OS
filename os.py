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
