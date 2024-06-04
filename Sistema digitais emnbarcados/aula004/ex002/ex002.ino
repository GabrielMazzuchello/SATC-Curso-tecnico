const int button1 = 2;
const int button2 = 3;
const int led1 = 8;
const int led2 = 9;
const int led3 = 10;
const int led4 = 11;

int estado = 0;
unsigned long tempo_ant = 0;


void setup() {
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);

}

void loop() {
  bool i0 = digitalRead(button1);
  bool i1 = digitalRead(button2);
  if (i0 == 1) {
    if (estado == 0) {
      tempo_ant = millis();
    }
    estado = 1;
  }
  if (i1 == 1) {
    estado = 0;
  }

  switch (estado) {
  case 0: 
    digitalWrite(led1, 0);
    digitalWrite(led2, 0);
    digitalWrite(led3, 0);
    digitalWrite(led4, 0);
    break;

  case 1:
    digitalWrite(led1, HIGH);
    if (millis() - tempo_ant >= 1000) {
      estado = 2;
      tempo_ant = millis();
    }
    break;
  case 2:
    digitalWrite(led2, HIGH);
    if (millis() - tempo_ant >= 1000) {
      estado = 3;
      tempo_ant = millis();
    }
    break;
  case 3:
    digitalWrite(led3, HIGH);
    if (millis() - tempo_ant >= 1000) {
      estado = 4;
      tempo_ant = millis();
    }
    break;
  case 4:
    digitalWrite(led4, HIGH);
    if (millis() - tempo_ant >= 1000) {
      estado = 5;
      tempo_ant = millis();
    }
    break;
  case 5:
    digitalWrite(led1, 0);
    digitalWrite(led2, 0);
    digitalWrite(led3, 0);
    digitalWrite(led4, 0);
    if (millis() - tempo_ant >= 1000){
      estado = 1;
      tempo_ant = millis();
    }
    break;
  }

}
