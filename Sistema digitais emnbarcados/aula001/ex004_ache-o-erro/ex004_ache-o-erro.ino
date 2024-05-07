void setup() {
  Serial.begin(9600); // define a velocidade de transmição
}

void loop() {
  Serial.println("Digite um numero: ");
  while (!Serial.available()) {}
  int valor = Serial.parseInt();
  Serial.print("O numero digitado foi ");
  Serial.println(valor);
  delay(2000);
}
