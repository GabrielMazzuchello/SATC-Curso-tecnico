const int pin_STP =2;
const int pin_STA =3;
const int pin_STB =4;
const int pin_IR =8;
const int pin_M1 =9;
const int pin_M2 =10;

void setup() {
  pinMode(pin_STP, INPUT);
  pinMode(pin_STA, INPUT);
  pinMode(pin_STB, INPUT);
  pinMode(pin_IR, OUTPUT);
  pinMode(pin_M1, OUTPUT);
  pinMode(pin_M2, OUTPUT);
}

void loop() {
  bool STP = digitalRead(pin_STP);
  bool STA = digitalRead(pin_STA);
  bool STB = digitalRead(pin_STB); 

  if (STP == 0) {
    digitalWrite(pin_IR, HIGH);
  }
  else {
    digitalWrite(pin_IR, LOW);
  }
    if ((STP == 1) && (STA == 0)) {
    digitalWrite(pin_M1, HIGH);
  }
  else {
    digitalWrite(pin_M1, LOW);
  }
    if ((STP == 0) && (STA == 0)) {
    digitalWrite(pin_M2, HIGH);
  }
  else {
    digitalWrite(pin_M2, LOW);
  }
}
