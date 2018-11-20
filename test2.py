
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
        
f=open("output.txt","r")
lines=f.readlines()
no = lines[0]
no =no.replace('\n','')
processes = int (no)
lines.remove(lines[0])
procList=[]
print(processes)
for i in range(processes):
    priority=lines[i].split(' ')[3]
    print(priority)
    priority=priority.replace('\n','')
    procList.append(proc(float(lines[i].split(' ')[1]),float(lines[i].split(' ')[2]),int(priority),int(lines[i].split(' ')[0])))
f.close()


