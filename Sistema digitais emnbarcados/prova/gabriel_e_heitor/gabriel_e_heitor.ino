const int SNA = 2;
const int SNB = 3;
const int STP = 4;
const int IR = 8;
const int BP = 9;
const int BR = 10;

void setup() {
  pinMode(SNA, INPUT);
  pinMode(SNB, INPUT);
  pinMode(STP, INPUT);
  pinMode(IR, OUTPUT);
  pinMode(BP, OUTPUT);
  pinMode(BR, OUTPUT); 
}

void loop() {
  bool i0 = digitalRead(SNA);
  bool i1 = digitalRead(SNB);
  bool i2 = digitalRead(STP);

  if ((i1 == 1) && (i0 == 1)) {
    digitalWrite(IR, 0);
    digitalWrite(BR, 0);
    digitalWrite(BP, 0);
  }

    else if (i2 == 1) {
    digitalWrite(BP, 1);
    digitalWrite(IR, 0);
    digitalWrite(BR, 0);
  }

  else if ((i1 == 0) && (i0 == 0) && (i2 == 0)){
    digitalWrite(BR, 1);
    digitalWrite(IR, 1);
    digitalWrite(BP, 0);
  }
  else if ((i1 == 0) && (i0 == 1)){
    digitalWrite(BR, 0);
    digitalWrite(IR, 0);
    digitalWrite(BP, 0);
  }
  else if ((i1 == 1) && (i0 == 0) && (i2 == 1)){
    digitalWrite(BR, 0);
    digitalWrite(IR, 0);
    digitalWrite(BP, 0);
  }

  else if ((i1 == 1) && (i0 == 1) && (i2 == 0)){
    digitalWrite(BR, 1);
    digitalWrite(IR, 1);
    digitalWrite(BP, 0);
  }

  else if ((i1 == 1) && (i0 == 0)) {
    if (STP == 1){
      digitalWrite(BP, 1);
      digitalWrite(BR, 0);
      digitalWrite(IR, 0);
    }
  }
}
