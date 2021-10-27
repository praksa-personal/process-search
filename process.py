import psutil
import datetime


#pid_current = os.getpid()
#print(psutil.Process(pid_current))

def start_time(process):
    for proc in psutil.process_iter():   
        if(proc.name()==process):
            print(proc)  
            time = proc.create_time()
            formated = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")
            print(formated)


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


if __name__ == '__main__':
    start_time('test_process.exe')
    #info()

    #postman pid
    proc_name = 'Postman.exe'
    pid = get_pid(proc_name)
    if(psutil.pid_exists(pid)):
        procs_list = [psutil.Process(pid)]
        print("Waiting for process {} to be terminated".format(proc_name))
        # waits for multiple processes to terminate, 20 sec timeout
        gone, alive = psutil.wait_procs(procs_list, timeout=20, callback=on_terminate)
    else:
        print("No process named {}".format(proc_name))
