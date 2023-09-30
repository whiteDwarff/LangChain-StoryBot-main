

import pygame
import time
from assist.gpio import led_gpio

isSwitchValue = 0

def speak():
    pygame.init()
    pygame.mixer.music.load('/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/snow_white.wav')
    pygame.mixer.music.play()

    global isSwitchValue  # Make sure to handle global variables accordingly in your main script
    
    running = True
    while running:
        try:
          led_gpio.switch_event()
          while isSwitchValue == 0:
              print("스위치 눌림 이벤트를 감지 중... (Ctrl+C를 눌러 종료)")
              print("isSwitchValue =", isSwitchValue)
              time.sleep(1)

        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
            print("isSwitchValue =", isSwitchValue)
        '''
        finally:
            GPIO.cleanup()
        '''
        if isSwitchValue == 1:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            running = False
            pygame.quit()
            time.sleep(1)
            #GPIO.cleanup()
        return False
    return False

if __name__ == "__main__":
    speak()



def switch_handler(channel):
    global isSwitchValue  # Use the global variable from audio.py
    isSwitchValue = 1
    print('s', isSwitchValue)
    print('=====================switch======================')
    return False

