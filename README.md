# ChatGPT-LLM 

# 스토리봇 - 유아용 동화 스토리봇 (유아용 동화 읽기, 번역 도우미)

## 1.프로젝트 개요

스토리봇은 ChatGPT 기반의 유아용 동화 스토리봇입니다. 이 프로젝트는 다음과 같은 주요 기능을 제공합니다:

    - 동화 읽어주기: 사용자에게 선택된 동화를 읽어주는 기능
    - 질의응답하기: 사용자의 질문에 대답해주는 기능
    - 역할놀이: 사용자와 대화하며 역할놀이를 할 수 있는 기능
    - 요약: 동화를 요약하여 사용자에게 제공하는 기능
    - 번역: 동화를 다른 언어로 번역해주는 기능

또한, 이 모델은 PDF 문서를 학습시켜 콘텐츠를 이해하고 처리하는 기능을 갖추고 있습니다.

## 2. 목표
    - 유아들을 대상으로 한 유창한 동화 읽기 및 상호작용 서비스 개발
    - 상상력을 자극하고 언어 능력 향상을 도모하는 동화 스토리봇 구현
    - ChatGPT 모델에 PDF 학습을 통해 다양한 동화를 구현할 수 있는 환경 제공

## 3. 기능설명
    - 동화 읽어주기 기능: ChatGPT 모델을 활용하여 다양한 동화를 실시간으로 읽어주는 기능
    - 질의응답하기 기능: 유아들이 동화 내용에 대해 질문을 하고, ChatGPT 모델이 답변을 제공하는 기능
    - 역할놀이 기능: 유아들이 동화의 캐릭터 역할을 맡고, ChatGPT 모델이 상호작용하여 역할놀이를 도와주는 기능
    - 동화 요약 기능: ChatGPT 모델을 사용하여 동화의 주요 내용을 요약하여 제공하는 기능
    - 번역 기능: ChatGPT 모델을 활용하여 다양한 언어로 동화를 번역하는 기능

## 기술 스택

- 언어 모델: ChatGPT (langchain.chat_models.ChatOpenAI)
- 벡터 데이터베이스: ChromaDB (chromadb)
- 토큰 수 계산: TikToken (tiktoken)
- PDF 처리: PyPDF2 (pypdf2)
- 음성 처리: Google Text-to-Speech (gtts), PyAudio (pyaudio), SpeechRecognition (speech_recognition)
- **`chromadb`**: ChromaDB는 특정 도구와 연계하여 데이터베이스를 구축하고 쿼리하는 데 사용되었습니다.
- **`tiktoken`**: Tiktoken은 텍스트 데이터를 토큰화하는 데 사용되었습니다. ChatGPT 모델에 입력으로 사용되는 텍스트를 토큰 단위로 분할하여 처리하는 데 활용되었습니다.
- **`langchain.chat_models`**: langchain.chat_models는 ChatGPT 모델의 구현과 관련된 모듈로 사용되었습니다. 이 모듈은 채팅 기반 기계 학습 모델을 사용하여 대화를 생성하고 처리하는 기능을 제공합니다.
- **`langchain.chains`**: langchain.chains는 LangChain 프레임워크의 일부로 사용되었습니다. 이 프레임워크는 자연어 처리 및 기계 학습 작업을 지원하는 다양한 도구와 모델을 제공합니다. ChatGPT 모델과의 통합 및 데이터 처리에 활용되었습니다.
- **`pypdf2`**: PyPDF2는 PDF 파일을 읽고 작성하는 데 사용되었습니다. PDF 학습 환경에서 사용자가 제공한 PDF 파일을 처리하고 필요한 데이터를 추출하는 데 활용되었습니다.

## **Langchain을 쓰는 이유?**

하나의 prompt만 가지고 답을 구하는건 이미 기존 LLM에서도 충분히 좋은 성능을 낼 수 있었습니다. 예를 들면 문서를 “요약”한다던지, 유사한 문서를 “검색” 한다던지 이런 기능들은 이미 충분히 좋은 모델들이 많이 나와있습니다. 하지만 진짜 사람이 생각하는 것처럼 “추론”을 하는 관점에서는 약점이 많았습니다.

Langchain을 사용한다면, agent를 사용하여 “문제”를 “추론”하고 여러 개의 작은 sub-task로 분할하는게 가능합니다. 각 단계마다 context를 유지하기 위해 어떤 도구를 사용해야하는지 결정하고 memory, prompt 등 다양한 기능들을 사용하여 원하는 결과를 만들어내게 할 수 있습니다.

[https://jayhey.github.io/deep learning/2023/04/23/langchain/](https://jayhey.github.io/deep%20learning/2023/04/23/langchain/)

## 일정

1. 기획 및 환경 설정 :
    - 프로젝트 목표 및 요구사항 정의
    - 필요한 라이브러리 및 도구 설치
    - Jetson Nano 설정 및 연결
2. 데이터 수집 및 전처리 :
    - 유아용 동화 데이터 수집
    - 데이터 전처리 (텍스트 정제, 포맷 변환 등)
3. 언어 모델 학습 :
    - ChatGPT 모델 학습 데이터 준비
    - ChatGPT 모델 학습 및 튜닝
    - 학습된 모델 저장 및 테스트
4. PDF 문서 학습 :
    - PDF 문서를 텍스트로 변환하여 벡터 데이터베이스에 등록
    - 벡터 데이터베이스 구축 및 검색 기능 테스트
5. 음성 처리 기능 추가 :
    - 음성 인식 기능 구현
    - 음성을 텍스트로 변환하여 질의응답 기능에 통합
    - 음성 출력 기능 구현
6. 기능 통합 및 최적화 :
    - 각 기능을 통합하여

사용자 친화적인 인터페이스 제공

- 성능 향상을 위한 최적화 작업
- 테스트 및 버그 수정
1. 최종 배포 및 문서 작성 (1일):
    - 젯슨나노에 프로젝트 배포
    - 사용 설명서 및 기술 문서 작성

## 향후 계획

- 사용자 피드백을 수집하여 모델 개선 및 기능 확장
- 추가적인 언어 모델 학습 및 데이터 수집
- 기존 기능의 성능 향상 및 새로운 기능 추가

## 기대 효과

- 유아들의 상상력과 언어 능력 향상에 기여
- 다양한 동화를 제공하여 교육적 가치와 즐거움을 동시에 제공
- ChatGPT 모델에 PDF 학습을 통해 다양한 동화를 구현할 수 있는 환경 제공

1. 참고 자료:
    - OpenAI ChatGPT 모델 문서 : https://openai.com/models/chatgpt
    - PDF 학습 관련 라이브러리 및 도구 문서 : [pdfloader](https://js.langchain.com/docs/api/document_loaders_fs_pdf/classes/PDFLoader)
    - colab link : https://colab.research.google.com/drive/1TONWO7bAg8Lkn4jprdBf5D-Go7C1N1w1?usp=sharing


## Presentation

![슬라이드1](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/3eba63e9-e497-40c1-b411-29590ec10b25)
![슬라이드2](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/0667c880-b81b-40ed-8e78-b2e46a515e0e)
![슬라이드3](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/d4341bb0-b842-4290-b17f-c406dfe2ab3c)
![슬라이드4](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/061afe54-cdef-4d72-988f-83d8c202843f)
![슬라이드5](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/5c54be83-d646-47ed-9eab-22d818d6bc9d)
![슬라이드6](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/3be4b1ab-0e2b-4012-ace1-5fe2d7adc0d4)
![슬라이드7](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/6fc2a3ed-575d-427d-a5c8-11a0cf75ae60)
![슬라이드8](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/9538fb4a-e9db-471b-b0de-16b4683596fa)
![슬라이드9](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/c21b7501-7285-486d-a978-be1369695aa0)
![슬라이드10](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/22fcfc0b-05e0-40b9-b49b-493c050f28c7)
![슬라이드11](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/7c79797b-1eb6-476e-a676-481dbf001c22)
![슬라이드12](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/d984b0e4-3827-4b21-9aee-9800abd0a8fc)
![슬라이드13](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/688ca633-d94f-4034-88b8-c334afcfe06a)
![슬라이드14](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/6b836529-9dee-47c0-b03c-06668d0e5a96)
![슬라이드15](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/a8cc9892-8a13-4d94-8f12-baf12551c378)
![슬라이드16](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/0d1b4675-b93c-4b9f-afa4-ac5b15909be5)
![슬라이드17](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/791657dc-c4e0-4e1f-ad0e-9a5e7ec9cea5)
![슬라이드18](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/54d00a96-2626-4215-aab4-c6b20e26af19)

## 전시계획
![전시계획](https://github.com/whiteDwarff/LangChain_StoryBot_Tory/assets/115057117/fb73efc1-23ac-4c60-bfc9-e31c72229dd4)

## JetsonNano 케이스 도면
![아크릴도면](https://github.com/whiteDwarff/LangChain-StoryBot-main/assets/115057117/fbbc3c40-dec2-40b7-84f6-7060ced6623c)

