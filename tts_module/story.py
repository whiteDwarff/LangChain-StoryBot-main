import pygame
import time
import playsound
import os
import Jetson.GPIO as GPIO
# from assist.gpio import event_detect



# GPIO 핀 번호 설정 (Jetson Nano 핀 번호 사용)
BUTTON_PIN = 33  
PIN = 29

# GPIO 설정
GPIO.setmode(GPIO.BOARD)  # Jetson Nano 핀 번호 사용
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.HIGH)

aaaa = 0

def button_pressed(channel):
    global aaaa  # aaaa 변수를 전역 변수로 사용
    print("스위치가 눌렸습니다!")
    aaaa = 1

# 이벤트 핸들러 등록
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed, bouncetime=200)


def speak():

    #event_detect()

    global aaaa 
    aaaa= 0  # aaaa 변수를 전역 변수로 사용
    pygame.init()
    pygame.mixer.music.load('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/story.mp3')
    pygame.mixer.music.play()

    running = True

    while running:
        try:
          while aaaa == 0:
              print("스위치 눌림 이벤트를 감지 중... (Ctrl+C를 눌러 종료)")
              print("aaaa =", aaaa)
              time.sleep(1)

        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
            print("aaaa =", aaaa)
        '''
        finally:
            GPIO.cleanup()
        '''
        if aaaa == 1:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            running = False
            pygame.quit()
            time.sleep(1)
            #GPIO.cleanup()
        return False
    return False






# ==================================
# import pygame
# import time
# import playsound
# import os

# def speak():
#   pygame.init()
#   pygame.mixer.music.load('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/story.mp3')
#   pygame.mixer.music.play()

#   running = True

#   while running:
#     for event in pygame.event.get():
#       if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#         pygame.mixer.music.stop()
#         pygame.mixer.music.unload()
#         running = False
#         pygame.quit()
#         time.sleep(1)
#         return False
      
"""
def speak(self, text):
        tts = gTTS(text=text, lang=self.language)
        tts.save('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3')

        # playsound를 사용하여 오디오 재생
        playsound.playsound('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3', True)
        # 재생 후 오디오 파일 삭제
        os.remove('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3') 

"""