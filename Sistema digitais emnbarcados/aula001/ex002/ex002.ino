void setup() {
  pinMode(5, OUTPUT);
}
void loop() {
  digitalWrite(12, HIGH);
  delay(500);

  digitalWrite(9, HIGH);
  delay(500);
  
  digitalWrite(5, HIGH);
  delay(500);
  
  digitalWrite(12, LOW);
  digitalWrite(9, LOW);
  digitalWrite(5, LOW);
  
}
