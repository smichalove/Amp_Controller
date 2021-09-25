# Plulse conversion from constant 12V input
#This assumes your Mark Levinson APM is on Standby as start state
#Your input to the Mark Levinson Should connect to GPIO21 for + and a GRND
#The control Signal from constant high or low should connect to a 12 V relay
#the switch signals from the relay to toggle on/off should be connected to GPIO twenty six and GRND
import signal                   
import sys
from time import sleep 
import RPi.GPIO as GPIO
from gpiozero import LED, Button
from gpiozero.tools import booleanized, all_values
GPIO.setmode(GPIO.BCM)
AMP=21 #Control Signal to amp
GPIO.setup(AMP, GPIO.OUT)
Button.was_held = False

def held(btn): #when siglnal is high and stays high
    btn.was_held = True
    print("button was held ")
    GPIO.output(AMP, 1) 
    sleep(.3) 
    GPIO.output(AMP, 0)

def released(btn): #when signal is low and stays low
    if not btn.was_held:
        print("Release1")         
        pressed()
    else:       
        print("Release2")
        GPIO.output(AMP, 1) 
        sleep(.3) 
        GPIO.output(AMP, 0) 
   
    btn.was_held = False

def pressed():
    print("button was pressed not held")


btn = Button(26,bounce_time = .001) # relay is on pin GPIO2  and GRND

if __name__ == '__main__':

    while True:
        btn.when_held = held
        btn.when_released = released
        sleep(1)
        
    GPIO.cleanup() 
