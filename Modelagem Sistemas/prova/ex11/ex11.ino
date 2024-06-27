const int pin_INI = 2;
const int pin_CONT = 3;
const int pin_FIM = 4;

const int pin_LEDMOT = 8;
const int pin_LEDVER = 9;
int espiras = 0;

int aux_up = 0;
unsigned long tempo_ant = 0;
unsigned long tempo_atual = 0;

void setup() {
  pinMode(pin_INI, INPUT);
  pinMode(pin_CONT, INPUT);
  pinMode(pin_FIM, INPUT);
  pinMode(pin_LEDMOT, OUTPUT);
  pinMode(pin_LEDVER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  bool INI = digitalRead(pin_INI);
  bool CONT = digitalRead(pin_CONT);
  bool FIM = digitalRead(pin_FIM);

  if (FIM == 1) {
    espiras = 0;
    digitalWrite(pin_LEDVER, LOW);
    Serial.println(espiras);
  }

  if (INI == 1) {
    digitalWrite(pin_LEDMOT, HIGH);
  }

  if (CONT == 1){
    espiras = espiras + 1;
    Serial.println(espiras);
  }

  if (espiras >= 60) {
    digitalWrite(pin_LEDMOT, LOW);
    tempo_atual = millis();
    if (tempo_atual - tempo_ant >= 600) {
      digitalWrite(pin_LEDVER, HIGH);
      tempo_ant = tempo_atual;
    }
    else {
      digitalWrite(pin_LEDVER, LOW);
    }
  }
}




