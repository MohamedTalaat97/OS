
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



########################################################

################################################

#procList.append(proc (1,2,5,1))   
#procList.append(proc (9,1,5,2)) 
#procList.append(proc (3,2,5,2)) 
#procList.append(proc (7,2,5,3)) 
#procList.append(proc (7,4,5,2)) 


#####################################################


#################FCFS##################################

context =0 

procList = []
procList.append(proc (5,3,5,1))   
procList.append(proc (7,1,5,2)) 
procList.append(proc (6,2,5,3)) 
procList.append(proc (1,1,5,4))
procList.append(proc (1,2,5,5))
procList.append(proc (8,3,5,6))
   
arrSorted = sorted(procList, key=lambda x: x.arr, reverse=False)
time =arrSorted[0].arr   
arrReady=[]
st=[]
fn=[]
n=[] 
timestep=1
c=0
while c < len(arrSorted):
    if (arrSorted[c].arr<=time):
        arrReady.append(arrSorted[c])  # get the ready ones out of the arrival into the queue
        arrSorted.pop(c)
        c=c-1
    c = c+1
while (len(arrSorted)>0 or len(arrReady)>0):
    #main loop       
    arrReady.sort(key=lambda x: x.arr, reverse=False)  # sort according to arrival
    
    if len(arrReady)>0:
        time+=context
        st.append(time)
        n.append(arrReady[0].n)         #serve 
        time+=arrReady[0].bur
        fn.append(time)
        for j in range(len(procList)):
                    if arrReady[0].n ==procList[j].n :
                        procList[j].finish= time
                        procList[j].start= time-procList[j].bur
                        arrReady.pop(0)
                        break
        
    else:
        time+= timestep
         
    c=0
    while c < len(arrSorted):
        if (arrSorted[c].arr<=time):
            arrReady.append(arrSorted[c])        # check new arriving
            arrSorted.pop(c)
            c=c-1
        c=c+1

diff =[]      
for i in range(len(st)):
      diff.append(fn[i]-st[i])  
      
plt.bar(st, n, width = diff ,align='edge', color = ('blue'))
plt.show()
    
	
######################################################################
###########################SRTN#######################################

#######################################################
###############calc#################################	

