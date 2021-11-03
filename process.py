import psutil
import datetime
import os
#pid_current = os.getpid()
#print(psutil.Process(pid_current))

def start_time(process):
    for proc in psutil.process_iter():   
        if(proc.name()==process):
            #print(proc)  
            time = proc.create_time()
            formated = datetime.datetime.fromtimestamp(time).strftime("%H:%M:%S")
            #print(formated)
            return (formated,proc.pid,proc.name)


def info():
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)

def on_terminate(proc):
    print("Process {} terminated".format(proc))

def get_pid(PROCNAME):
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
           return proc.pid
    return -1


def delta_time(t1,t2):
    print("\nStart time: ",t1)
    print("End time: ",t2)
            
    FMT = '%H:%M:%S'
    tdelta = datetime.datetime.strptime(t2, FMT) - datetime.datetime.strptime(t1, FMT)
    print("Time to complete test:",tdelta)

if __name__ == '__main__':
    test_pid=-1
    flag = 0
    
    print("Start test? [y/n]")

    x = input()
    os.startfile("C:/Users/puntaric/Projekti/process-search/exe/dist/test.exe")
  
        
    if(x == 'y'):
        try:
            test_start, test_pid, test_name = start_time('test.exe')
            flag = 1
        except:
            ()

        if(flag == 1):
            procs_list = [psutil.Process(test_pid)]
            print("Waiting for process {} to be terminated".format(test_name))
            # waits for process to terminate, 20 sec timeout
            gone, alive = psutil.wait_procs(procs_list, timeout=30, callback=on_terminate)
            x = 'n'
            test_end = datetime.datetime.now()
            test_end = test_end.strftime("%H:%M:%S")

            delta_time(test_start,test_end)

        else:
            print("No running test process")

    
    

