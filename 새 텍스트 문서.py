import serial
import pyautogui
import time

# --- 설정 영역 ---
PORT = 'COM3'
BAUD_RATE = 9600
SECRET_SEQUENCE = ["Button A Pressed", "Button B Pressed", "Button C Pressed"]
current_input = []

def unhide_icons_shortcut():
    """
    Shift + F10 -> V -> D 단축키를 실행하여 바탕화면 아이콘을 토글합니다.
    """
    print("[!] 단축키 매크로를 실행합니다...")
    
    try:
        # 1. 먼저 모든 창을 최소화하고 바탕화면을 포커스 (Win + D)
        # 바탕화면이 선택되어 있어야 단축키가 먹힙니다.
        pyautogui.hotkey('win', 'd')
        time.sleep(0.5)

        # 2. 우클릭 메뉴 열기 (Shift + F10)
        pyautogui.hotkey('shift', 'f10')
        time.sleep(0.5)

        # 3. '보기(V)' 메뉴 선택
        pyautogui.press('v')
        time.sleep(0.5)

        # 4. '바탕 화면 아이콘 표시(D)' 선택
        pyautogui.press('d')
        
        print("[+] 바탕화면 아이콘 표시 설정이 변경되었습니다.")
    except Exception as e:
        print(f"[-] 단축키 실행 실패: {e}")

# --- 메인 루프 ---
try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"아두이노 연결됨 ({PORT}). 버튼을 누르세요.")

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"입력됨: {line}")
                current_input.append(line)

                if len(current_input) == len(SECRET_SEQUENCE):
                    if current_input == SECRET_SEQUENCE:
                        print("\n[***] 비밀번호 일치! 매크로 작동 [***]")
                        unhide_icons_shortcut()
                        current_input = []
                    else:
                        print("[-] 틀렸습니다.")
                        current_input = []
except Exception as e:
    print(f"오류: {e}")