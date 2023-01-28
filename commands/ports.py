
import json;
import time;

jsonFile = 'ports.json'

def printPorts():
    checkForDelayedOnPorts()
    with open('/usr/local/bin/ports.json') as user_file:
        file_contents = user_file.read()
        ports = json.loads(file_contents)
        for port in ports: 
            portIndex = int(port)
            print(port + ": Outlet " + port + " : " + ports[port]["status"]) 
 

def getPorts(): 
    with open('/usr/local/bin/ports.json','r') as user_file:
        file_contents = user_file.read()
        ports = json.loads(file_contents)
        return ports
    
def setPortDelay(changePort : int, changDelay : int): 
    
    ports = getPorts()

    for port in ports: 
        if (port == str(changePort)): 
            ports[port]["delay"] = changDelay 
        
    with open('/usr/local/bin/ports.json','w') as user_file: 
        user_file.truncate()
        user_file.write(json.dumps(ports))
        
def setPortOff(changePort : int):  
    ports = getPorts() 
    for port in ports: 
        if (port == str(changePort)): 
            ports[port]["status"] = "Off" 
        
    with open('/usr/local/bin/ports.json','w') as user_file: 
        user_file.truncate()
        user_file.write(json.dumps(ports))

def setPortDelayOn(changePort : int):
    ports = getPorts() 
    for port in ports: 
        if (port == str(changePort)): 
            ports[port]["turn_on_timestamp"] = time.time()
        
    with open('/usr/local/bin/ports.json','w') as user_file: 
        user_file.truncate()
        user_file.write(json.dumps(ports))

def checkForDelayedOnPorts():
    
    ports = getPorts() 
    for port in ports: 
        if (ports[port]["status"] == "Off"): 
            
            #ignore devices that havent been turned on
            if ((ports[port]["turn_on_timestamp"]) == 0):
                continue
            
            if (( time.time() - ports[port]["turn_on_timestamp"]) > float(ports[port]["delay"])):
                ports[port]["turn_on_timestamp"] = 0
                ports[port]["status"] = "On"
        
    with open('/usr/local/bin/ports.json','w') as user_file: 
        user_file.truncate()
        user_file.write(json.dumps(ports))