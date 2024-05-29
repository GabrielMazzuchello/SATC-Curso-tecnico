const int botao_i0 = 2;
const int botao_i1 = 3;
const int led_d0 = 8;
const int led_d1 = 9;
const int led_d2 = 10;
const int led_d3 = 11;

void setup() {
  // put your setup code here, to run once:
  pinMode(botao_i0, INPUT);
  pinMode(botao_i1, INPUT);
  pinMode(led_d0, OUTPUT);
  pinMode(led_d1, OUTPUT);
  pinMode(led_d2, OUTPUT);
  pinMode(led_d3, OUTPUT);
}

void loop() {
  bool i0 = digitalRead(botao_i0);
  bool i1 = digitalRead(botao_i1);
  if (i0 == 1){
    digitalWrite(led_d0, HIGH);
    digitalWrite(led_d1, HIGH);
  }
  else {
    digitalWrite(led_d0, LOW);
    digitalWrite(led_d1, LOW);
  }
  if (i1 == 1) {
    digitalWrite(led_d2, HIGH);
  digitalWrite(led_d3, HIGH);
  }
  else {
    digitalWrite(led_d2, LOW);
    digitalWrite(led_d3, LOW);
  }
}