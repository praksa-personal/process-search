import psutil

data = psutil.pids()

##print process names
for i in data:
    try:        
        temp = psutil.Process(i)
        if(temp.name()=='Code.exe' and temp.status()=='running'):
            print(temp.name())
    except:
        continue
