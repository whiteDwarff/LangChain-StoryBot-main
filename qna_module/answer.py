from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from playsound import playsound
from qna_module import answer_stt
import sys
import os
from langchain.prompts.chat import(
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
# gpio import 
from assist.gpio import led_gpio
# thread import
from assist.thread import led_thread

def ask(story, question):

    embeddings = OpenAIEmbeddings()
    #vector_store에 stroy를 저장
    vector_store = Chroma.from_documents(story, embeddings)
    # 2개의 chunk로 나누어진 stroy 중 2개의 값을 넘김
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    # ------------------------------------------------
    # prompt 설정
    # ------------------------------------------------
    system_template ="""
    [예시 문장]
    - 저는 '백설공주'라는 동화를 학습했어요. 이 동화에 대한 정보를 알려드릴게요!
    - 안녕하세요, 저는 AI Tory에요. 나랑 같이 놀자!
    - 무엇이 궁금하니? 나한테 물어봐!
    - 학습된 동화의 제목입니다: 백설공주
    - 백설공주가 쓰러진 이유는 사악한 마녀의 독사과를 먹었기 때문이에요.
    - 저는 '백설공주'라는 동화를 학습했어요. (사용자의 질문)은 모르겠어요..

    -----

    [예외]
    - 저는 '백설공주'라는 동화를 학습했어요. (사용자의 질문)은 모르겠어요..

    -----

    [학습 정보]
    - {summaries}

    -----

    [규칙]
    - [학습 정보]에 없는 질문인 경우 [예외]로 대답한다.
    - '백설공주'를 학습했습니다.
    - 오직 [학습 정보]에서 배운 내용만 답하세요. 
    - 마치 어린 아이와 대화하는 것처럼 친절한 어조와 간단한 단어로 작성
    - (사용자의 질문)에는 사용자의 질문을 넣어

    -----

    위 정보는 모두 백설공주 동화에 관련된 내용입니다. [예시 문장]은 AI Tory가 학습된 동화를 읽어주고 정보를 가지고 만든 답변입니다.
    당신은 오직 학습된 내용만 알려주며 [규칙]을 무조건 따르는 AI Tory입니다. 질문하는 사용자에게 [학습 정보]로 학습된 내용을 기반으로 답변해야합니다. 
    [예시 문장]과 [학습 정보]를 참고하여 다음 조건을 만족하면서 [학습 정보]에 있는 정보 메시지를 생성해주세요.
"""

    # ------------------------------------------------
    # 대화모델 생성
    # ------------------------------------------------
    messages = [
        # 시스템 메시지 템플릿을 생성
        SystemMessagePromptTemplate.from_template(system_template),
        # 유저 메시지 생성
        HumanMessagePromptTemplate.from_template("{question}")
    ]
    # ------------------------------------------------
    # 채팅 형식의 프롬프트 생성
    # ------------------------------------------------
    # 채팅 프롬프트 템플릿 생성
    prompt =ChatPromptTemplate.from_messages(messages)
    # 딕셔너리 변수를 생성하여 prmpt key 값에 value를 prompt를 할당
    chain_type_kwargs = {"prompt": prompt}
    # ------------------------------------------------
    # 기계 학습 모델과 검색기능을 활용하여 질문-답변 형태의 대화를 수행
    # ------------------------------------------------
    # 모델을 초기화하여 llm 변수에 할당
    llm = ChatOpenAI(model_name ="gpt-3.5-turbo-16k", temperature=0)

    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        # 채팅 프롬프트를 사용하여 대화하는 체인을 설정
        chain_type="stuff",
        # 검색기능을 제공하는 객체 
        retriever = retriever,
        # 검색에 사용된 관련 지문들을 함께 반환
        return_source_documents=True,
        # chain_type_kwargs 딕셔너리를 체인에 전달, 입력 형식과 추가 매개변수를 설정할 수 있음
        chain_type_kwargs=chain_type_kwargs
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
        answer = chain(question)
        print(f"response : {answer['answer']}")
        #answer_stt.result(answer['answer'])

        led_thread.thread(led_gpio.blinkLed, answer_stt.result, answer['answer'], led_gpio.outLed)

        return True
    # 모든 조건이 충족하지 못해도 새로운 질문을 시작
    else:
        return True
    
    #######################################################################
    # 질문이 없을 경우 예외처리 !!!!