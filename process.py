import psutil
import os
import datetime

data = psutil.pids()
pid_current = os.getpid()

#print(psutil.Process(pid_current))

##print process names
for i in data:
    try:        
        temp = psutil.Process(i)
        #if(temp.name()=='Code.exe' and temp.status()=='running'):
            #print(temp.children(recursive=True),"\n")
            #print(temp.started()) #should be time, ali ne zeli
        if(temp.name()=='test_process.exe'):
            print(temp.name())  
            time = temp.create_time()
            formated = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")
            print(formated)
            
    except:
        continue


