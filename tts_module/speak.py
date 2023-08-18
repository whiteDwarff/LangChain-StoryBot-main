from gtts import gTTS
from playsound import playsound

def tts(text, name):
    tts = gTTS(text, lang='ko')
    tts.save(f"/home/jetson/Desktop/LangChain-StoryBot-main/mp3/{name}.mp3")
    return playsound(f"/home/jetson/Desktop/LangChain-StoryBot-main/mp3/{name}.mp3")


# role_response