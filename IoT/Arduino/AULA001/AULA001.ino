const int pin_entrada = A0;
const int pin_led1 = 8;
int valor;
float tensao;

void setup() {
  pinMode(pin_led1, OUTPUT);
  Serial.begin(9600);
  pinMode(pin_entrada, INPUT);
}

void loop() {
  valor = analogRead(pin_entrada);
  tensao = float(valor)*5/1023;
  Serial.print("Tensao = ");
  Serial.print(tensao);
  Serial.println(" V");
  if (tensao < 2.5) {
    digitalWrite(pin_led1, HIGH);
  }
  else {
    digitalWrite(pin_led1, LOW);
  }
}
