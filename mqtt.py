

def on_publish(client, userdata, mid):
    #print("mid: "+str(mid))
    ()

def set_topic(res_str):
    if(res_str == "passed"):
        return "testing/passed"
    elif(res_str == "failed"):
        return "testing/failed"
    else:
        return "testing/other"