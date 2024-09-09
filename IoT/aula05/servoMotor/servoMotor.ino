#include <Servo.h>
#include <Ultrasonic.h>

int posic = 0;
int distancia = 0;

Ultrasonic ultrasonic(6, 7);
const int botaoPin = 2;
Servo myservo;


void setup() {
  Serial.begin(9600);
  pinMode(botaoPin, INPUT);
  pinMode(6, OUTPUT);
  pinMode(7, INPUT);
  myservo.attach(9);
  myservo.write(90);

}

void loop() {
  enum Estado {SEMCARRO, COMCARRO, ABRIRCANCELA, FECHARCANCELA};
  Estado estadoAtual = SEMCARRO;


  distancia = ultrasonic.read();
  if (distancia <= 10) {
    estadoAtual = COMCARRO;
    Serial.println("Pressione o botão ");
    Serial.println(distancia);
  }

  if ((distancia < 50) && (estadoAtual == COMCARRO) && (digitalRead(botaoPin) == HIGH)) {
    estadoAtual = ABRIRCANCELA;
    myservo.write(180);
  }

  if (estadoAtual == ABRIRCANCELA) {
    estadoAtual = FECHARCANCELA;
    myservo.write(90);
  }

  if (estadoAtual == FECHARCANCELA) {
    estadoAtual = SEMCARRO;
  }

  
}
