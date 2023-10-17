#!/usr/bin/env python3

from utils import sound
from utils.brick import wait_ready_sensors, EV3GyroSensor, TouchSensor, reset_brick
import time

GYRO_SENSOR_DATA_FILE = "../data_analysis/gyro_sensor.csv"

GYRO_SENSOR = EV3GyroSensor(4)
EXIT_SENSOR = TouchSensor(1)
TOUCH_SENSOR = TouchSensor(2)

wait_ready_sensors()

def printGyroDataForever():
    
    output_file = open(GYRO_SENSOR_DATA_FILE, "w")
    
    while(not EXIT_SENSOR.is_pressed()):
        
        mesure = GYRO_SENSOR.get_both_measure()
        
        if(TOUCH_SENSOR.is_pressed()):
            print(mesure) #debug purposes
            
            if(mesure != None):
                angle = mesure[0]
                
                #start your pitch after a revolution, so you can also go backwards.
                #pitch = 4 is your origin (w/o offset). the +45 is just an offset.
                #Max backward you can go is 1, which is turned the opposite way to
                #a full revolution. Just angle/90 is pitch = 0
                pitch = int((angle+360+45)/90) 
        
                print(pitch) #debug purposes
                
                output_file.write(f"{angle}\n")
                
                time.sleep(0.2)
    
    output_file.close()
    reset_brick()
    exit()
    
if __name__=='__main__':
    
    print("started")
    printGyroDataForever()