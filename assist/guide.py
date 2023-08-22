from gtts import gTTS
from playsound import playsound

# ???documents
def make_story():
    tts = gTTS("백설공주 동화의 등장인물을 선택해주세요.", lang='ko')
    tts.save("/home/jetson/Desktop/LangChain-StoryBot-main/mp3/user_role.mp3")

make_story()