const int botao_i0 = 2;
const int botao_i1 = 3;
const int led_d0 = 8;
void setup() {
  // put your setup code here, to run once:
  pinMode(botao_i0, INPUT);
  pinMode(botao_i1, INPUT);
  pinMode(led_d0, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  bool i0 = digitalRead(botao_i0);
  bool i1 = digitalRead(botao_i1);
  if (i0 == 1) {
    digitalWrite(led_d0, HIGH);
  }
  if (i1 == 1) {
    digitalWrite(led_d0, LOW);
  }


}
