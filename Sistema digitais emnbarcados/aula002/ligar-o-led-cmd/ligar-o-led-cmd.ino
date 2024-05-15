const int led_vermelho = 8;
const int led_verde = 9;
const int led_azul = 10;
char led;

void setup() {
  pinMode(led_vermelho, OUTPUT);
  pinMode(led_verde, OUTPUT);
  pinMode(led_azul, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    led = Serial.read();
    switch (led) {
      case 'R': digitalWrite(led_vermelho, HIGH);
        break;
      case 'r': digitalWrite(led_vermelho, LOW);
        break;
      case 'G': digitalWrite(led_verde, HIGH);
        break;
      case 'g': digitalWrite(led_verde, LOW);
        break;
      case 'B': digitalWrite(led_azul, HIGH);
        break;
      case 'b': digitalWrite(led_azul, LOW);
        break;
    }

  }
}
