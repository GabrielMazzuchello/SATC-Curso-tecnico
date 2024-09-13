const int pin_entrada = A0;
const int pin_led = 9;
int valor;

void setup() {
  pinMode(pin_entrada, INPUT);
  pinMode(pin_led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  valor = analogRead(pin_entrada);

  analogWrite(pin_led, valor/4);
   Serial.println(valor/4);
  // valor = map(valor, 0, 1023, 0, 255);
  // serve para converter 1023 para 255 funciona o mesmo q divivido por 4
}
