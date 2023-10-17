#!/usr/bin/env python3

from utils import sound
from utils.brick import wait_ready_sensors, EV3GyroSensor, TouchSensor, reset_brick
import time

gYRO_SENSOR = EV3GyroSensor(4)
EXIT_SENSOR = TouchSensor(1)
tOUCH_SENSOR = TouchSensor(2)
SOUNDS = [sound.Sound(duration=1.2, pitch="C5", volume=60), #pitch = 0 
          sound.Sound(duration=1.2, pitch="D5", volume=60), #pitch = 1
          sound.Sound(duration=1.2, pitch="E5", volume=60), #pitch = 2
          sound.Sound(duration=1.2, pitch="F5", volume=60), #pitch = 3
          sound.Sound(duration=1.2, pitch="G5", volume=60), #pitch = 4 (ORIGIN NOTE)
          sound.Sound(duration=1.2, pitch="A5", volume=60), #pitch = 5
          sound.Sound(duration=1.2, pitch="B5", volume=60), #pitch = 6
          sound.Sound(duration=1.2, pitch="C6", volume=60)] #pitch = 7 

wait_ready_sensors()

def executeSoundSystem(TOUCH_SENSOR, GYRO_SENSOR):
        
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
            
            if(pitch >= 0 and pitch < len(SOUNDS)):
                SOUNDS[pitch].play()
                SOUNDS[pitch].wait_done()
    
if __name__=='__main__':
    
    print("started")
    
    while(not EXIT_SENSOR.is_pressed()):
        executeSoundSystem(TOUCH_SENSOR, GYRO_SENSOR)
    
    reset_brick()
    exit()
    