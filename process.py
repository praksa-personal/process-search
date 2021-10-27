import psutil
import os
import datetime


#pid_current = os.getpid()
#print(psutil.Process(pid_current))

def start_time(process):
    data = psutil.pids()
    for i in data:
        try:        
            temp = psutil.Process(i)
            #if(temp.name()=='Code.exe' and temp.status()=='running'):
                #print(temp.children(recursive=True),"\n")
                #print(temp.started()) #should be time, ali ne zeli
            if(temp.name()==process):
                print(temp)  
                time = temp.create_time()
                formated = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")
                print(formated)
                
        except:
            continue


if __name__ == '__main__':
    name = 'test_process.exe'
    start_time(name)