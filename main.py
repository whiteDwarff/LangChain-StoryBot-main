# Lib import
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from playsound import playsound
# Module import
from stt import request
from interface_module import interface
from API_KEY import pwd
import subprocess

###################################################################################
###########   깃 커밋할 때 [main], [role]의 API KEY는 공란으로 입력해주세요    #############
##################################################################################

# OpenAI KEY
os.environ["OPENAI_API_KEY"] = pwd.key

loader = PyPDFLoader("/home/jetson/Desktop/LangChain-StoryBot-main/assist/story/snow_white.pdf")
documents = loader.load()
a_documents = []

for doc in documents:
    content = doc.page_content.replace("\n", " ").replace("  ", " ").strip() 
    a_documents.append(content)
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap = 0)
a_documents = text_splitter.split_documents(documents)    

# PDF 로더 초기화
loader = PyPDFLoader("/home/jetson/Desktop/LangChain-StoryBot-main/assist/story/snow_white.pdf")
documents = loader.load()
# chunk : text를 자르는 단위, 1000글자당 1chunk
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap = 0)
a_documents = text_splitter.split_documents(documents)

def run():
    playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/start.wav")
    menu_state = False 
    fan = "sudo sh -c 'echo 100 > /sys/devices/pwm-fan/target_pwm'"
    subprocess.run(fan, shell=True)
    
    while True:
        # 사용자의 두번째 메뉴 선택부터 음성을 출력  
        if menu_state:
            playsound("/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/select_menu.wav")

        command = request() 
        
        if not command:
            run()
        
        interface.handle_command(command, a_documents, documents)
        menu_state = True

if __name__ == "__main__":
    run()
