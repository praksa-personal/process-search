import datetime
import random

def running_time(t1,t2):
    #print("\n"+t1)
    #print(t2)
    FMT = '%H:%M:%S'
    tdelta = datetime.datetime.strptime(t2, FMT) - datetime.datetime.strptime(t1, FMT)
    return tdelta


def simulate_results():
    x = random.randint(0, 1)
    if(x):
        topic = "testing/passed"
        res_str = "passed"
    else:
        topic = "testing/failed"
        res_str = "failed"
    return topic,res_str