const int pin_botao1 = 2;
const int pin_botao2 = 3;
const int pin_botao3 = 4;
const int pin_led1 = 8;
const int pin_led2 = 9;
const int pin_led3 = 10;

int aux_up1 = 0;;

bool aux_led2 = 0;
bool aux_led3 = 0;

void setup() {
  pinMode(pin_botao1, INPUT);
  pinMode(pin_botao2, INPUT);
  pinMode(pin_botao3, INPUT);
  pinMode(pin_led1, OUTPUT);
  pinMode(pin_led2, OUTPUT);
  pinMode(pin_led3, OUTPUT);

}

void loop() {
  bool bot1 = digitalRead(pin_botao1);
  bool bot2 = digitalRead(pin_botao2);
  bool bot3 = digitalRead(pin_botao3);
  

  if ((bot1 == 1) && (aux_up1 == 0)){
    digitalWrite(pin_led1, HIGH);
    aux_up1 = 1;
  }
  else if ((bot1 == 1) && (aux_up1 == 1)) {
    digitalWrite(pin_led1, LOW);
    aux_up1 = 0;
  }

  if (bot2 == 1) {
    digitalWrite(pin_led2, HIGH);
    aux_led2 = 1;
    if (aux_led3 == 1) {
      digitalWrite(pin_led3, LOW);
    }
  }
  if (bot3 == 1) {
    digitalWrite(pin_led3, HIGH);
    aux_led3 = 1;
    if (aux_led2 == 1) {
      digitalWrite(pin_led2, LOW);
    }
  }
}
