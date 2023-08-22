import speech_recognition as sr
from playsound import playsound
import sys

def request():
    # 음성 인식기 생성
    r = sr.Recognizer()
    global audio

    # 마이크에서 음성 입력 받기
    with sr.Microphone() as source:
        print("Please tell me.")
        try:
            # 3초간 입력이 없다면 종료
            audio = r.listen(source, timeout=3)
        except sr.WaitTimeoutError:
            playsound("/home/jetson/Desktop/LangChain-StoryBot-main/mp3/try_recognition.mp3")
            # sys.exit(0)
            request()
    try:
        # 음성을 텍스트로 변환
        text = r.recognize_google(audio, language='ko-KR')
        print(f"request  : {text}")
        return text

    except sr.UnknownValueError:
        playsound("/home/jetson/Desktop/LangChain-StoryBot-main/mp3/recognition.mp3")
        request()

    except sr.RequestError as e:
        request()