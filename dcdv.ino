void setup() {
  Serial.begin(9600); // 시리얼 모니터 시작
}


void loop() {
  int val = analogRead(A0); // A0 핀에서 값 읽기
 
  // 버튼을 누르지 않았을 때는 보통 1000 이상의 값이 나옵니다.
  if (val < 1000) {
    if (val < 20) {
      Serial.println("Button A Pressed");
    } else if (val < 80) {
      Serial.println("Button B Pressed");
    } else if (val < 100) {
      Serial.println("Button C Pressed");
    } else if (val < 150) {
      Serial.println("Button D Pressed");
    } else if (val < 600) {
      Serial.println("Button E Pressed");
    }
    delay(250); // 중복 입력 방지
  }
}
