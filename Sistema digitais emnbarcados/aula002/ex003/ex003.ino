  const int pin_botao = 2;
  const int pin_led = 8;
  bool botao = false;

void setup() {
  pinMode(pin_botao, INPUT);
  pinMode(pin_led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  botao = digitalRead(pin_botao);
  if (botao == true) {
    Serial.println("Botão pressionado!!!");
    digitalWrite(pin_led, HIGH);
  }
  else {
    digitalWrite(pin_led, LOW);
    }
  }

