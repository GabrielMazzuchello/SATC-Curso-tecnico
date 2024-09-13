#include <Ultrasonic.h>
#include <DHT.h>

#define DHTPIN 2;
#define DHTTYPE DHT11;

#define pin_Ve = 8;
#define pin_Vs = 9;
#define pin_Aque = 10;
#define pin_Led = 11;
#define pin_Alarm = 7;
DHT dht(DHTPIN, DHTTYPE);
Ultrasonic ultrasonic(12, 13);
int h;

void setup() {
  // put your setup code here, to run once:
  dht.begin()
  pinMode(pin_Ve, OUTPUT);
  pinMode(pin_Vs, OUTPUT);
  pinMode(pin_Aque, OUTPUT);
  pinMode(pin_Led, OUTPUT);
  pinMode(pin_Alarm, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  float t = dht.readTemerature();
  h = ultrasonic.read();

  if (h == 0) {
    digitalWrite(pin_Ve, LOW);
  }
  else {
    digitalWrite(pin_Ve, HIGH);
  }

  if ((h<20) && (t>24) && (t<26)) {
    digitalWrite(pin_Vs, HIGH);
  }
  else {
    digitalWrite(pin_Vs, LOW);
  }

  if ((t<24) && (h<45)) {
    digitalWrite(pin_Aque, HIGH);
  }
  else {
    digitalWrite(pin_Aque, LOW);
  }

  if (h > 40) {
    digitalWrite(pin_Led, HIGH);
  }
  else {
    digitalWrite(pin_Led, LOW);
  }
  
  if (h > 45) {
    digitalWrite(pin_Alarm, HIGH);
  }
  else {
    digitalWrite(pin_Alarm, LOW);
  }
}
