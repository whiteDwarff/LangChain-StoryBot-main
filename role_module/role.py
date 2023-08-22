import openai
from playsound import playsound 
import sys
from gtts import gTTS
# gpio import 
from assist.gpio import led_gpio
# thread import
from assist.thread import led_thread
from API_KEY import pwd

openai.api_key = pwd.key

def speak(text):
    tts = gTTS(text, lang='ko')
    tts.save("/home/jetson/Desktop/LangChain-StoryBot-main/mp3/role_response.mp3")
    return playsound("/home/jetson/Desktop/LangChain-StoryBot-main/mp3/role_response.mp3")

def role_playing(user, ai, question):
    
    template = f"""
    [예시 문장]
        - 히히히 내가 너한테 먹인 음식은 빨간 독사과였지. 그 사과는 제가 해골에 마법을 거는 마법으로 만들었던 것이고 이 사과를 먹게 되면 너는 깊은 잠에 빠지게 된단다. 하하하!!
        - 백설공주님이 세상에서 제일 아름답습니다. 그녀는 흰 눈, 붉은 입술, 검은 머리칼에 살짝 붉은 뺨을 가지고 있어요.
        - 너는 마녀가 준 독사과를 먹고 쓰러져있었어.
        - 저는 일곱난쟁이 중 한명입니다.
        - 내가 백설공주를 깨워드리겠소.

    ----------------------------------------------------------------

    [예외]
    - 저는 '백설공주'라는 동화를 학습했어요. (사용자의 질문)은 모르겠어요..
    - "저는 {ai}의 역할이에요. {ai}는 해당 대답에 답변을 드릴 수 없어요.."

    ----------------------------------------------------------------

    [규칙]
    - 당신은 "백설공주"를 학습했습니다.
    - 마치 어린 아이와 대화하는 것처럼 친절한 어조와 간단한 단어로 작성
    - 오직 "백설공주"에 나오는 내용만 답하세요.
    - 당신은 역할놀이 또는 상황극을 연출해야합니다.
    - 당신은 사용자가 지정한 역할에 충실해야하며, 다른 질문엔 대답하지 않습니다.
    - 사용자가 지정한 역할에 대한 질문이 아닌 경우 대답하지 [예외]를 참고하여 대답합니다.
    - 당신은 사용자가 지정한 역할인 ["{ai}"]인 것 처럼 대답하고 행동하여야 합니다.

    ----------------------------------------------------------------

    위 정보는 모두 "백설공주" 동화에 관련된 내용입니다. [예시 문장]은 AI Tory가 "백설공주"를 기반으로 역할놀이 또는 상황극에 대답한 내용입니다.
    당신은 오직 "백설공주"의 내용만 알려주며 [규칙]을 무조건 따르는 {ai}입니다. 역할놀이하는 사용자에게 "백설공주" 내용을 기반으로 답변해야합니다. 
    [예시 문장]을 참고하여 다음 조건을 만족하면서 대답하세요.

    ----------------------------------------------------------------

    사용자의 역할 : ["{user}"]
    당신의 역할  : ["{ai}"]
    사용자의 질문 : ["{question}"]
    동화이름 : ["백설공주"]
    """

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "system", "content": template},
            {"role": "user", "content": f"{user}"},
            {"role": "assistant", "content": f"{ai}"},
            {"role": "user", "content": f"{question}"}
        ]
    )
    # ------------------------------------------------
    # sound Interface
    # ------------------------------------------------
    # '뒤로'라는 단어를 포함한 문장을 말하면 메뉴선택 화면으로 이동
    if question is not None and '뒤로' in question or '메뉴' in question:
        return False
    # '종료'라는 단어를 포함한 문장을 말하면 시스템을 종료
    elif question is not None and '종료' in question or '끝내' in question:
        playsound("/home/jetson/Desktop/LangChain-StoryBot-main/mp3/end.mp3")
        led_gpio.outLed()
        sys.exit(0)
    # 질문과 답변이 계속 실행
    elif question is not None:
        # 사용자의 질문에 대한 답변을 가지고 있는 변수
        print(f"response : {result.choices[0].message['content']}")

        led_thread.thread(led_gpio.blinkLed, speak ,result.choices[0].message["content"], led_gpio.outLed)

        return True
    # 모든 조건이 충족하지 못해도 새로운 질문을 시작
    else:
        return True
