# GPIO library
import Jetson.GPIO as GPIO
import threading

# Handles time
import time 
 
# Pin Definition
led_pin = 7

# Set GPIO mide
GPIO.setmode(GPIO.BOARD)
 
def outLed():
  # Blink the LED
  GPIO.output(led_pin, GPIO.LOW)

def fullLed():
  GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH) 
  GPIO.output(led_pin, GPIO.HIGH) 


def blinkLed(stop_event):
    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH)  
    outLed()
    while not stop_event.is_set():
        time.sleep(1)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_pin, GPIO.LOW)





