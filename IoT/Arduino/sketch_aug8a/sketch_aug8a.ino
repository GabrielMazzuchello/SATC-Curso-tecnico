int saida = 11;
int entrada = A5;
int pontos = 500;
int tempo = 1;
const int pin_led = 8;
int valor, k;
float tensao;

void setup() {
  pinMode(pin_led, OUTPUT);
  pinMode(saida, OUTPUT);
  pinMode(entrada, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(saida, LOW);
  for (k=1; k<=pontos; k++) {
    valor = analogRead(entrada);
    tensao = float(valor)*5/1023;
    Serial.println(tensao);
    delay(tempo);
    
    if (tensao < 4.0) {
      digitalWrite(pin_led, LOW);
    }
  }
  
  digitalWrite(saida, HIGH);
  for (k=1; k<=pontos; k++) {
    valor = analogRead(entrada);
    tensao = float(valor)*5/1023;
    Serial.println(tensao);
    delay(tempo);

    if (tensao >= 4.0) {
      digitalWrite(pin_led, HIGH);
      }
  }
}
