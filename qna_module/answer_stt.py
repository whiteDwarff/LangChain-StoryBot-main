from gtts import gTTS
import json
import os
import playsound

class Text2Speech:
    def __init__(self):
        # 음성 스펙 가져오기
        with open('/home/jetson/Desktop/LangChain-StoryBot-main/assist/voice.json', 'r') as fp:
            info = json.load(fp)

        # 언어 및 기타 옵션 설정
        self.language = info['language']
        self.rate = info['rate']
        self.should_stop = False

    def speak(self, text):
        tts = gTTS(text=text, lang=self.language)
        tts.save('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3')

        # playsound를 사용하여 오디오 재생
        playsound.playsound('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3', True)
        # 재생 후 오디오 파일 삭제
        os.remove('/home/jetson/Desktop/LangChain-StoryBot-main/mp3/output.mp3') 

def result(text):
    text = str(text)
    # tts 인스턴스 생성
    tts = Text2Speech()
    # 텍스트를 mp3 파일로 변환하여 출력
    tts.speak(text)