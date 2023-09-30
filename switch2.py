import Jetson.GPIO as GPIO
import time

# GPIO 핀 번호 설정 (Jetson Nano 핀 번호 사용)
BUTTON_PIN = 33  # 예시로 33번 핀 사용, 원하는 핀 번호로 변경 가능

# GPIO 설정
GPIO.setmode(GPIO.BOARD)  # Jetson Nano 핀 번호 사용
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # PUD_DOWN으로 풀다운 설정

def btnOn(channel):
    print("Button Pressed!")

# 이벤트 핸들러 등록
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=btnOn, bouncetime=200)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

