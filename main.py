import os
import random
import paho.mqtt.client as paho
import psutil
import datetime
import test_results
import proc
import mqtt
 
if __name__ == '__main__':
    client = paho.Client(client_id="Tester-1", clean_session=True, userdata=None, protocol=paho.MQTTv31)
    client.on_publish = mqtt.on_publish
    client.connect(host="localhost", port=1883)
    
    #print("Start test? [y/n]")
    #x = input()
    x = 'y'
    run_time = 20 #random.randint(10,60)

    if(x == 'y'):
        #start dummy test.exe process
        print("Test started")
        os.startfile("C:/Users/puntaric/Projekti/process-search/exe/dist/test.exe")

        test_start, test_pid, test_name = proc.on_test_start('test.exe')

        procs_list = [psutil.Process(test_pid)]
        #print("Waiting for process {} to be terminated".format(test_name))
        # waits for process to terminate, 20 sec timeout
        gone, alive = psutil.wait_procs(procs_list, timeout=run_time, callback=proc.on_terminate)
        x = 'n'
        print("Test finished")
        test_end = datetime.datetime.now()
        test_end = test_end.strftime("%H:%M:%S")

        #test terminated, get running time, random status, topic, post over mqtt
        dtime = test_results.running_time(test_start,test_end)
        res_str = test_results.simulate_results()
        topic = mqtt.set_topic(res_str)

        msg = "Test id XX " + res_str + ", total running time:\n" + str(dtime) 
        (rc, mid) = client.publish(topic, str(msg), qos=1)
             
    else:
        print("No running test process")

    