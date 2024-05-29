const int botao_i0 = 2;
const int botao_i1 = 3;
const int led_d0 = 8;
const int led_d1 = 9;
const int led_d2 = 10;
void setup() {
  // put your setup code here, to run once:
    // put your setup code here, to run once:
  pinMode(botao_i0, INPUT);
  pinMode(botao_i1, INPUT);
  pinMode(led_d0, OUTPUT);
  pinMode(led_d1, OUTPUT);
  pinMode(led_d2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  bool i0 = digitalRead(botao_i0);
  bool i1 = digitalRead(botao_i1);

  if (i0 ==1 && i1 == 1) {
    digitalWrite(led_d0, HIGH);
  }
  else {
    digitalWrite(led_d0, LOW);
  }
  if  (i0 ==1 || i1 == 1) {
    digitalWrite(led_d1, HIGH);
  }
  else {
    digitalWrite(led_d1, LOW);
  }
  if  (i0 ==1 ^ i1 == 1) {
    digitalWrite(led_d2, HIGH);
  }
  else {
    digitalWrite(led_d2, LOW);
  }



  if (i0 == 1 && i1 == 1) {
    digitalWrite(led_d0, HIGH);
    if (i0 == 1 && i1 == 1) {
      digitalWrite(led_d0, LOW);
    }
  }
  else if (i0 == 1 || i1 == 1) {
    digitalWrite(led_d1, HIGH);
    if (i0 == 1 || i1 == 1) {
      digitalWrite(led_d1, LOW);
    }
  }
    if (i0 == 1 ^ i1 == 1) {
    digitalWrite(led_d2, HIGH);
  }
  else {
    digitalWrite(led_d2, LOW);
  }
}
