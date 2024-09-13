  #include <Ultrasonic.h>
  #include "DHT.h"
  #define DHTPIN 2
  #define DHTTYPE DHT11
  DHT dht(DHTPIN, DHTTYPE);

  Ultrasonic ultrasonic(8, 9);
  int distance; 

  const int valvEntrada = 4;
  const int valvSaida = 3;


  const int botValvEntrada = 6;
  const int botvalvSaida = 7;
  const int aquecimento = 5;
  int buttonState1 = 0;
  int buttonState2 = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(valvEntrada, OUTPUT);
  pinMode(valvSaida, OUTPUT);
  pinMode(botValvEntrada, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState1 = digitalRead(botValvEntrada);
  buttonState2 = digitalRead(botvalvSaida);

  if (buttonState1 == HIGH) {
    digitalWrite(valvEntrada, HIGH);
  }
  else {
    digitalWrite(valvEntrada, LOW);
  }

  float t = dht.readTemperature();
  if (t < 24) {
    digitalWrite(aquecimento, HIGH);

  }



  

}
