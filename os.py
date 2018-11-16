import numpy as np

######################################################
class proc(object):
    
    #avgTat 
    #avgWeightedTat 
    #N 
    def __init__(self, arr, bur, pri, n):
        self.arr = arr
        self.bur = bur
        self.pri = pri
        self.n = n
        wait = 0
        tat = 0 
        weighted =0
        start =0
        finish = 0
        served =0



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
    procList.append(proc(arr, bur, pri, i + 1))
    '''
    
procList.append(proc (2,3,5,1))   
procList.append(proc (4,5,5,2)) 
processes =2  
#####################################################
o = open('output.txt', 'w')
o.write(str(processes) + '\n')

for p in procList:
    o.write(str(p.n) + ' ' + str(p.arr) + ' ' + str(p.bur) + ' ' + str(p.pri) + '\n')

o.close()


#################FCFS##################################
context =1
arrSorted = sorted(procList, key=lambda x: x.arr, reverse=False)


for i in range(processes):
    if i>0:
        if arrSorted[i].arr <= arrSorted[i-1].finish:
            arrSorted[i].finish = arrSorted[i].bur+arrSorted[i-1].finish+context
        elif arrSorted[i].arr > arrSorted[i-1].finish:
            arrSorted[i].finish = arrSorted[i].bur+arrSorted[i].arr
    else:    
        arrSorted[i].finish =arrSorted[i].arr+arrSorted[i].bur
		
		
print('finish1 ' +str(arrSorted[1].finish))
print('arr ' +str(arrSorted[1].arr))
################################################	
avgTat =0
weightedAvg =0
		#calc
for i in range(processes):
    arrSorted[i].tat = arrSorted[i].finish - arrSorted[i].arr
    arrSorted[i].wait= arrSorted[i].tat - arrSorted[i].bur	
    avgTat+=arrSorted[i].tat;
    weightedAvg += arrSorted[i].tat/arrSorted[i].bur
    
    
    
print('tat1 ' +str(arrSorted[1].tat))    
avgTat = avgTat/processes
weightedAvg = weightedAvg/processes
print(avgTat)