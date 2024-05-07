void setup() {
  Serial.begin(9600); // define a velocidade de transmição
}

void loop() {
  Serial.println("Digite um numero: ");
  int valor = Serial.();
  Serial.print("O numero digitado foi ");
  Serial.write(valor);
  Serial.println();


}
