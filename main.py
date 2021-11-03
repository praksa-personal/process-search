import os
import paho.mqtt.client as paho
import psutil
import datetime
from test_results import running_time, simulate_results
from proc import on_test_start, on_terminate
from mqtt import on_publish

 
if __name__ == '__main__':
    client = paho.Client(client_id="Tester-1", clean_session=True, userdata=None, protocol=paho.MQTTv31)
    client.on_publish = on_publish
    client.connect(host="localhost", port=1883)
    
    test_pid=-1
    flag = 0
    
    print("Start test? [y/n]")
    x = input()
    #start dummy test.exe
    
    if(x == 'y'):
        os.startfile("C:/Users/puntaric/Projekti/process-search/exe/dist/test.exe")

        try:
            test_start, test_pid, test_name = on_test_start('test.exe')
            flag = 1
        except:
            ()

        if(flag == 1):
            procs_list = [psutil.Process(test_pid)]
            #print("Waiting for process {} to be terminated".format(test_name))
            # waits for process to terminate, 20 sec timeout
            gone, alive = psutil.wait_procs(procs_list, timeout=30, callback=on_terminate)
            x = 'n'
            test_end = datetime.datetime.now()
            test_end = test_end.strftime("%H:%M:%S")

            #test terminated, get running time, random status, post over mqtt
            dtime = running_time(test_start,test_end)
            topic, res_str = simulate_results()
            
            msg = "Test id XX " + res_str + ", total running time:\n" + str(dtime) 
            (rc, mid) = client.publish(topic, str(msg), qos=1)
             
        else:
            print("No running test process")

    