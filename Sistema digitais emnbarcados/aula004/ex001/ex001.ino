const int button1 = 2;
const int button2 = 3;
const int led1 = 8;
const int led2 = 9;
const int led3 = 10;
const int led4 = 11;

bool estado = 0;
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
    digitalWrite(led1, 1);
    if (estado == 0) {
      tempo_ant = millis();
  }
  estado = 1;

  }
  if (estado == 1) {
   if (millis() - tempo_ant >= 1000) {
      digitalWrite(led2, 1);
      estado = 0;
   }
  }  
  if (i1 == 1) {
    digitalWrite(led1, 0);
    digitalWrite(led2, 0);
  }
}


