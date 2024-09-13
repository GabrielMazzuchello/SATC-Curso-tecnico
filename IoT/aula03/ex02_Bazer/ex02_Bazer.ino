const int pin_entrada = A0;
int valor;
float tensao;
const int buzer = 9;

void setup() {
  Serial.begin(9600);
  pinMode(pin_entrada, INPUT);
  pinMode(buzer, OUTPUT);
}

void loop() {
  valor = analogRead(pin_entrada);
  tensao = float(valor)*5/1023;
  Serial.print("Tensao = ");
  Serial.print(tensao);
  Serial.println(" V");

  if (tensao >= 4.0) {
    digitalWrite(buzer, HIGH);
  }
  else {
    digitalWrite(buzer, LOW);
  }
}