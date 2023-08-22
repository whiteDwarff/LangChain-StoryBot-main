import Jetson.GPIO as GPIO
import time

# GPIO 핀 번호 설정 (Jetson Nano 핀 번호 사용)
BUTTON_PIN = 33  # 예시로 18번 핀 사용, 원하는 핀 번호로 변경 가능
PIN = 29

# GPIO 설정
GPIO.setmode(GPIO.BOARD)  # Jetson Nano 핀 번호 사용
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.HIGH) 

def button_pressed(channel):
        print("스위치가 눌렸습니다!")

try:
    # 이벤트 핸들러 등록
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed, bouncetime=200)
    
    print("스위치 눌림 이벤트를 감지 중... (Ctrl+C를 눌러 종료)")

    # 프로그램이 계속 실행되도록 대기
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
finally:
    GPIO.cleanup()


# # 스위치 핀 번호 설정
# switch_pin = 29

# # GPIO 모드 설정
# GPIO.setmode(GPIO.BOARD)

# # 스위치 핀 설정
# GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# try:
#     while True:
#         # 스위치 값 읽기
#         switch_value = GPIO.input(switch_pin)
#         print(switch_value)

#         # 스위치 값에 따라 출력
#         if switch_value == GPIO.LOW:
#             print("스위치 안눌림 (0)")
#         else:
#             print("스위치 눌림 (1)")

#         time.sleep(0.1)  # 잠시 대기
# except KeyboardInterrupt:

#     GPIO.cleanup()

