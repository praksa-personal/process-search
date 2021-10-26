import psutil

data = psutil.pids()

##print process names
for i in data:
    try:        
        temp = psutil.Process(i)
        print(temp.name())
    except:
        continue
