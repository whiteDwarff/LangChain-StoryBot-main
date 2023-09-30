"""
# GPIO library
import Jetson.GPIO as GPIO
import pygame
import threading

# Handles time
import time 
GPIO.cleanup()
# Pin Definition
red_pin = 38
green_pin = 40

button_pin = 33
button_gnd = 29


GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(green_pin, GPIO.OUT, initial=GPIO.LOW)  
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_gnd, GPIO.OUT, initial=GPIO.HIGH)
# Set GPIO mode


def Red_outLed():
  # led off
  try:
    GPIO.output(red_pin, GPIO.LOW)
  except KeyboardInterrupt:
    GPIO.cleanup()

def Green_outLed():
  # led off
  try:
    GPIO.output(green_pin, GPIO.LOW)
  except KeyboardInterrupt:
    GPIO.cleanup()
def RedLed():
  try:
    Green_outLed()
    GPIO.output(red_pin, GPIO.HIGH) 
  except KeyboardInterrupt:
    GPIO.cleanup()

def GreenLed():
  try:
    Red_outLed()
    GPIO.output(green_pin, GPIO.HIGH) 
  except KeyboardInterrupt:
    GPIO.cleanup()

##############################################
isSwitchValue = 0
def switch_handler(channel):
  global isSwitchValue
  isSwitchValue = 1
  print('s', isSwitchValue)
  print('=====================switch======================')
  return False


def switch_event():
  GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=switch_handler, bouncetime=200)
  print('e ', isSwitchValue)
# def blinkLed(stop_event):
#     GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH)  
#     outLed()
#     while not stop_event.is_set():
#         time.sleep(1)
#         GPIO.output(led_pin, GPIO.HIGH)
#         time.sleep(1)
#         GPIO.output(led_pin, GPIO.LOW)
"""





import Jetson.GPIO as GPIO
import pygame
from tts_module import story

# GPIO library
red_pin = 38
green_pin = 40
button_pin = 33
button_gnd = 29

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(green_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_gnd, GPIO.OUT, initial=GPIO.HIGH)

def Red_outLed():
    # LED off
    try:
        GPIO.output(red_pin, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.cleanup()

def Green_outLed():
    # LED off
    try:
        GPIO.output(green_pin, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.cleanup()

def RedLed():
    try:
        Green_outLed()
        GPIO.output(red_pin, GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()

def GreenLed():
    try:
        Red_outLed()
        GPIO.output(green_pin, GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()

# Global variable
# isSwitchValue = 0  # Remove this line to avoid redefining the variable
isSwitchValue = 0


def switch_handler(channel):
    global isSwitchValue  # Use the global variable from audio.py
    isSwitchValue = 1
    print('s', isSwitchValue)
    print('=====================switch======================')
    return False

def switch_event():
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=story.switch_handler, bouncetime=200)
    print('switch event enabled')

if __name__ == "__main__":
    switch_event()

# Call the speak() function or other relevant functions to trigger audio playback
# Be sure to handle isSwitchValue appropriately when using it in your GPIO-related functions.