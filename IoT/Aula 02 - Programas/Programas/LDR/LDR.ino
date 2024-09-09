int porta = A0;
const int pin_led = 8;
int valor;

void setup() {
  pinMode(pin_led, OUTPUT);
  Serial.begin(9600);
  pinMode(porta, INPUT);
}

void loop() {
  valor = analogRead(porta);
  Serial.println(valor);
  if (valor > 100) {
    digitalWrite(pin_led, LOW);
  }
  else {
    digitalWrite(pin_led, HIGH);
  }
}
