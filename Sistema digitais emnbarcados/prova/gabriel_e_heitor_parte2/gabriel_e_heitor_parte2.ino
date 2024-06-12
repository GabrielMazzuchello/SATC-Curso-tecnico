const int NA = 2;
const int NB = 3;
const int TA = 4;
const int TB = 5;

const int VE = 8;
const int VS = 9;
const int AQC = 10;
const int ALA = 11;

void setup() {
  pinMode(NA, INPUT);
  pinMode(NB, INPUT);
  pinMode(TA, INPUT);
  pinMode(TB, INPUT);
  pinMode(VE, OUTPUT);
  pinMode(VS, OUTPUT); 
  pinMode(AQC, OUTPUT);
  pinMode(ALA, OUTPUT); 
}

void loop() {
  bool i0 = digitalRead(NA);
  bool i1 = digitalRead(NB);
  bool i2 = digitalRead(TA);
  bool i3 = digitalRead(TB);

  if ((i0 == 0) && (i1 == 0) && (i2 == 0) && (i3 == 0)) {
    digitalWrite(VE, 1);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 0);
  }
  else if ((i0 == 0) && (i1 == 0) && (i2 == 0) && (i3 == 1)) {
    digitalWrite(VE, 1);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 1);
    digitalWrite(ALA, 0);
  }
  else if ((i0 == 0) && (i1 == 0) && (i2 == 1) && (i3 == 0)) {
    digitalWrite(VE, 1);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 0) && (i1 == 0) && (i2 == 1) && (i3 == 1)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 0) && (i1 == 1) && (i2 == 0) && (i3 == 0)) {
    digitalWrite(VE, 1);
    digitalWrite(VS, 1);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 0);
  }
  else if ((i0 == 0) && (i1 == 1) && (i2 == 0) && (i3 == 1)) {
    digitalWrite(VE, 1);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 1);
    digitalWrite(ALA, 0);
  }
  else if ((i0 == 0) && (i1 == 1) && (i2 == 1) && (i3 == 0)) {
    digitalWrite(VE, 1);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 0) && (i1 == 1) && (i2 == 1) && (i3 == 1)) {
    digitalWrite(VE, 1);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 1) && (i1 == 0) && (i2 == 0) && (i3 == 0)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 1) && (i1 == 0) && (i2 == 0) && (i3 == 1)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 1);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 1) && (i1 == 0) && (i2 == 1) && (i3 == 0)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 1) && (i1 == 0) && (i2 == 1) && (i3 == 1)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 1) && (i1 == 1) && (i2 == 0) && (i3 == 0)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 1);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 0);
  }
  else if ((i0 == 1) && (i1 == 1) && (i2 == 0) && (i3 == 1)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 1);
    digitalWrite(ALA, 0);
  }
  else if ((i0 == 1) && (i1 == 1) && (i2 == 1) && (i3 == 0)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else if ((i0 == 1) && (i1 == 1) && (i2 == 1) && (i3 == 1)) {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 1);
  }
  else {
    digitalWrite(VE, 0);
    digitalWrite(VS, 0);
    digitalWrite(AQC, 0);
    digitalWrite(ALA, 0);
  }



}
