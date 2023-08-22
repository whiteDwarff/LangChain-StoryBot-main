import pygame
import time
import playsound
import os

def speak():
  pygame.init()
  pygame.mixer.music.load('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/story.mp3')
  pygame.mixer.music.play()

  running = True

  while running:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        running = False
        pygame.quit()
        time.sleep(1)
        return False
      
"""
def speak(self, text):
        tts = gTTS(text=text, lang=self.language)
        tts.save('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3')

        # playsound를 사용하여 오디오 재생
        playsound.playsound('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3', True)
        # 재생 후 오디오 파일 삭제
        os.remove('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3') 

"""