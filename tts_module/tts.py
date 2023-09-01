import os
from google.cloud import texttospeech

# Google Cloud 서비스 계정 키 파일 경로
key_file_path = '/home/jetson/Desktop/LangChain-StoryBot-main/tts_module/ai-tory-d429a82ee164.json'

# 텍스트를 음성으로 변환할 텍스트
text = """hello"""

def gtts(str, fileName):
    # Google Cloud Text-to-Speech API 클라이언트 초기화
    client = texttospeech.TextToSpeechClient.from_service_account_json(key_file_path)

    # 음성 합성 매개변수 설정 (WaveNet 사용)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", name="ko-KR-Neural2-A", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
            speaking_rate=0.8,  # speaking_rate를 조절하여 음성을 느리게 만듭니다.
            pitch= -0.4
    )
    # 텍스트를 음성으로 변환
    input_text = texttospeech.SynthesisInput(text=str)
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    # WaveNet으로 생성된 음성을 파일로 저장
    with open(f"/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/{fileName}.wav", "wb") as out_file:
        out_file.write(response.audio_content)

    # 음성 파일 재생 (예: macOS)
    os.system(f"aplay /home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/{fileName}.wav")

#gtts('메뉴가 선택되지 않았습니다. 다시 선택해주세요.', 'retry')