#🔥 Final Tuple Challenge: Sensor Alert System (Real-world Simulation)
#You're developing a sensor alert system. Each sensor logs data as a

#tuple:(sensor_id, location, temperature, is_critical)


#✅ Your Task (Do all of these in one program):
#Print all logs where is_critical == True
#Count how many times each (sensor_id, location) combo appears in the log.
#Find the sensor (ID & location) with the highest temperature.
#Track only unique sensors (by sensor_id), and print their latest (last seen) reading.

sensor_logs = [
    ("S-101", "ServerRoom-1", 48.5, True),
    ("S-102", "ServerRoom-2", 35.0, False),
    ("S-101", "ServerRoom-1", 49.0, True),
    ("S-103", "ServerRoom-3", 32.0, False),
    ("S-101", "ServerRoom-1", 45.5, True),
    ("S-102", "ServerRoom-2", 42.0, True),
    ("S-103", "ServerRoom-3", 30.5, False),
    ("S-103", "ServerRoom-1", 49.0, True),
]

chack=[]
chack2=[]

#print(sensor_logs[0])
#print(sensor_logs[0][3])
#print([ is_critical for sensor_id, location, temperature, is_critical in sensor_logs if is_critical==True])

def countSensor_id():
    key=-1
    sensor_ids = [s[0] for s in sensor_logs]
    for sensor_id, location, temperature, is_critical in sensor_logs:
        key+=1
    
        if sensor_id not in chack2: #to print count of each sensor_id
            c = sensor_ids.count(sensor_id)
            #c = [s[0] for s in sensor_logs].count(sensor_id) #we get list of only sensor id then count each sencer id 
            print(f"Count of {sensor_id} is {c}")
            chack2.append(sensor_id)

def printCritical():
    key=-1    
    for sensor_id, location, temperature, is_critical in sensor_logs:
        key+=1    

        if sensor_id not in chack: #to print True values tuple
            if is_critical==True:
                print(sensor_logs[key])
                chack.append(sensor_id)


def findIdHighstTmp():
    Hitmp=[]
    Htmp=0 #hihg tmp
    key=-1 #location of tuple of high tmp
    for sensor_id, location, temperature, is_critical in sensor_logs:
        key+=1
        if temperature>Htmp:
            if Hitmp:
                Hitmp.clear()
                Htmp=temperature
                Hitmp.append((sensor_id,location,temperature))

            else:

                Htmp=temperature
                Hitmp.append((sensor_id,location,temperature))

        elif temperature==Htmp:
            Hitmp.append((sensor_id,location,temperature))


            
            
            
    for i in Hitmp:
        print(f"We Found hihst tmp:{i}")
    
            

    #for sensor_id, location, temperature, is_critical in sensor_logs:
        #key+=1
        #if temperature==Htmp:
            #print(f"The senser {sensor_id} in {location} have highst temperature {Htmp}")
 

def latestReading(): #not a good option (use disnary wich is nest topic)

    for sensor_id, location, temperature, is_critical in sensor_logs:

        if sensor_id=="S-101":
            ltmp1=temperature

        elif sensor_id=="S-102":
            ltmp2=temperature

        elif sensor_id=="S-103":
            ltmp3=temperature 

    print(f"Latest Tmp\nS-101:   {ltmp1}\nS-102:   {ltmp2}\nS-103:   {ltmp3}")               


printCritical()
countSensor_id()
findIdHighstTmp()
latestReading()




              




              
              
              
    









