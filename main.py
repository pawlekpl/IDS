#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED, Button
import gpiozero
from timeit import default_timer as timer
#GPIO SETmode
GPIO.setmode(GPIO.BCM)
#Sound detector setup
channel = 3
GPIO.setup(channel, GPIO.IN)
#led setup
ledred = LED(17)
ledblue = LED(18)
ledgreen = LED(2)
ledred.off()
ledblue.off()
ledgreen.off()

#Buttons setup
button = 8                                                                                                                                                    
GPIO.setup(button, GPIO.IN)

#Buzzer setup
Buzzer = 26
GPIO.setup(Buzzer, GPIO.OUT) 
global Buzz 
Buzz = GPIO.PWM(Buzzer, 440) 
GPIO.output(Buzzer,GPIO.LOW)
#pir setup
pir = 21 #Associate pin 26 to pir
GPIO.setup(pir, GPIO.IN) #Set pin as GPIO in
#kontaktron setup
contact=3
GPIO.setup(contact, GPIO.IN)
def alarm(ledred,ledblue):
    while True:
        ledred.on()
        sleep(0.1)
        ledblue.on()
        sleep(0.1)
        ledred.off()
        sleep(0.1)
        ledblue.off()
        sleep(0.1)
        Buzz.start(31) 
        if GPIO.input(button)==False:
            print("Alarm is now off")
            Buzz.stop()
            sleep(0.5)
            break
#funkcja detekcji dzwieku
#def callback(channel):
        #if GPIO.input(channel):
                #print ("Sound Detected!")
                #time.sleep(0.5)
        #else:
                #print ("Sound Not Detected!")
#Main loop
   
while True:
    print("Waiting for turning alarm on")
    #ledgreen.on()
    GPIO.output(Buzzer,GPIO.LOW)
    while True:
        if GPIO.input(button)==False:
            ledgreen.off()
            ledblue.on()
            print("Uzbrojono")
            print('Waiting for sensor to settle')
            sleep(2) #Waiting 2 seconds for the sensor to initiate
            print('Detecting motion')
            break
    while True:
        if GPIO.input(contact):
            ledgreen.off()
            sleep(1.0)
            print("Door is open")
            start=timer()
            end=timer()
            while (end - start <10.0):
                ledgreen.on()
                end=timer()
                if GPIO.input(pir): #Check whether pir is HIGH
                    print('Motion Detected!')
                    #wlaczenie alarmu
                    alarm(ledred,ledblue)
                    break
                    
                
                
                
        
        
        #if GPIO.input(pir): #Check whether pir is HIGH
            #print('Motion Detected!')
            #wlaczenie alarmu
            #alarm(ledred,ledblue)
            #break
        
    
#small sound 
#GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change


