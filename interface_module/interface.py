from playsound import playsound
from stt import request
from qna_module import answer
from tts_module import story
from role_module import role
from tts_module import tts
from assist.gpio import led_gpio
import sys



def handle_command(question, documents):

    if question is not None:
        if "동화" in question or "읽기" in question or "읽어" in question:
            led_gpio.RedLed()
            playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/ready.wav") 

            #
            # tts = gTTS(f"{a_documents}", lang='ko')
            # tts.save("/home/jetson/Desktop/LangChain-StoryBot-main/mp3/story.mp3")
            #
            # speak 함수의 return값이 False일 경우 if문을 빠져나옴
            if story.speak() is False:
                return False
        ##############################################################
        elif "질문" in question or "큐앤" in question:
            qna_state = False
            # return 값이 True일 경우에 while문 반복
            while True:
                # 두번째 질문부터 효과음 재생
                if qna_state:
                    playsound('/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/answer.mp3')
                # 질문을 처음 시작할 경우 '질문을 시작해주세요' 재생
                else:
                    led_gpio.RedLed()
                    playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/question.wav")
                ###########################################################################
                led_gpio.GreenLed()
                # 사용자의 음성을 인식받는 새로운 tts 객체 생성
                user_question = request()
                qna_state = True
                # ask 함수의 return값이 False일 경우 while문 elif문을 빠져나옴
                if answer.ask(documents, user_question) is False:
                    qna_state = False
                    return False
        ##############################################################
        elif "역할" in question or "놀이" in question:
            role_state = False

            led_gpio.RedLed()
            playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/user_role.wav")

            # 사용자의 역할을 선택
            led_gpio.GreenLed()
            user = request()

            # 사용자의 역할이 None이나 공백이 아닐경우 GPT의 역할을 선택 
            if user is not None and user != "":
                led_gpio.RedLed()
                playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/ai_role.wav")
                led_gpio.GreenLed()
                ai = request()
                # GPT의 역할이 None이나 공백이 아닐경우 역할놀이를 시작
                if ai is not None and ai != "":
                    led_gpio.RedLed()
                    str = f"친구의 역할은 {user}이고 토리의 역할은 {ai}입니다. {user}역할을 시작해주세요"
                    tts.gtts(str, 'role_guide')
            while True:
                if role_state:
                    led_gpio.RedLed()
                    playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/answer.mp3")
                ############################################################################
                led_gpio.GreenLed()
                ###########################################################################
                user_question = request()
                role_state = True
                # return 값이 False인 경우 elif문을 빠져나옴 
                if role.role_playing(user, ai, user_question) is False:
                    return False
        ##############################################################
        elif "종료" in question or "끝내" in question:
            led_gpio.RedLed()
            playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/end.wav")
            led_gpio.Red_outLed()
            led_gpio.Green_outLed()
            sys.exit(0)
      
        # question이 None이 아니고 모든 조건이 충족되지 못할 경우
        else:
            playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/recognition.wav")
            question = request()
            handle_command(question, documents) 
    # question이 None인 경우
    else:
        playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/retry.wav")
        question = request()
        handle_command(question, documents) 


    handle_command(question, documents)