import pygame
import time

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

