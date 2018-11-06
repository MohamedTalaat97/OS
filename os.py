import numpy as np


######################################################
class proc(object):
    
    avgTat 
    avgWeightedTat 
    N 
    def __init__(self, arr, bur, pri, n):
        self.arr = arr
        self.bur = bur
        self.pri = pri
        self.n = n
        wait = 0
        tat = 0 
        weighted =0
        


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

f.close()
################################################
procList = []

for i in range(processes):
    arr = (np.random.normal(loc=arrivalMu, scale=arrivalSigma))
    bur = (np.random.normal(loc=arrivalMu, scale=arrivalSigma))
    pri = int(np.random.poisson(lam=priorityLamda))
    procList.append(proc(arr, bur, pri, i + 1))
#####################################################
o = open('output.txt', 'w')
o.write(str(processes) + '\n')

for p in procList:
    o.write(str(p.n) + ' ' + str(p.arr) + ' ' + str(p.bur) + ' ' + str(p.pri) + '\n')

o.close()


#########################################################
time =0
#FCFS
'''
arrSorted = sorted(procList, key=lambda x: x.arr, reverse=True)
for i in range(processes):
    time+= 
    arrSorted[i].wait = a
'''
