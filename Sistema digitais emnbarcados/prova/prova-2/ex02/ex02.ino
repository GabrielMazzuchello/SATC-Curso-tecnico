const int pin_SEV = 2;
const int pin_SSV = 3;
const int pin_BOT = 4;
const int pin_VER = 8;
const int pin_LIB = 9;
const int pin_LOT = 10;

long unsigned int vagas = 0;
unsigned long tempo_ant = 0;
unsigned long tempo_ant2 = 0;

void setup() {
  pinMode(pin_SEV, INPUT);
  pinMode(pin_SSV, INPUT);
  pinMode(pin_BOT, INPUT);
  pinMode(pin_VER, OUTPUT);
  pinMode(pin_LIB, OUTPUT);
  pinMode(pin_LOT, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  bool SEV = digitalRead(pin_SEV);
  bool SSV = digitalRead(pin_SSV);
  bool BOT = digitalRead(pin_BOT);

  if (BOT == 1) {
    vagas = 0;
    Serial.println(vagas);
  }

  if (SEV == 1) {
    vagas = vagas + 1;
    Serial.println(vagas);
  }

  if (SSV == 1) {
    vagas = vagas - 1;
    Serial.println(vagas);
    
  }
  if (vagas <= 50) {
    digitalWrite(pin_LIB, HIGH);
  }
  else {
    digitalWrite(pin_LIB, LOW);
  }

  if (vagas >= 50) {
    digitalWrite(pin_LOT, HIGH);
  }
  else {
    digitalWrite(pin_LOT, LOW);
  }



if (vagas == 0) {
      millis();
      if (millis() - tempo_ant >= 500) {
        digitalWrite(pin_VER, HIGH);
        tempo_ant = millis();
        if (millis() - tempo_ant2 >= 500){
          digitalWrite(pin_VER, LOW);
          tempo_ant2 = millis();
        }
      }
    }
}
