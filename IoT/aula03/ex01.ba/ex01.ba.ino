int porta = A0;
const int pin_led1 = 9;
const int pin_led2 = 10;
const int pin_led3 = 11;
int valor;

void setup() {
  pinMode(pin_led1, OUTPUT);
  pinMode(pin_led2, OUTPUT);
  pinMode(pin_led3, OUTPUT);
  Serial.begin(9600);
  pinMode(porta, INPUT);
}

void loop() {
  valor = analogRead(porta);
  Serial.println(valor/5);
  analogWrite(pin_led1, valor/5);
  analogWrite(pin_led2, valor/5);
  analogWrite(pin_led3, valor/5);
}
