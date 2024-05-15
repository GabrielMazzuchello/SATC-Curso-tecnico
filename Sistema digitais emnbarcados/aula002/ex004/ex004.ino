const int buttonPin = 2; // Pino onde está conectado o botão
const int ledPin1 = 3;   // Pino onde está conectado o primeiro LED
const int ledPin2 = 4;   // Pino onde está conectado o segundo LED
const int ledPin3 = 5;   // Pino onde está conectado o terceiro LED

int buttonState = 0;     // Variável para armazenar o estado do botão
int buttonCounter = 0;   // Contador de cliques no botão

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    delay(50); // Debounce

    if (buttonState == HIGH) {
      buttonCounter++;

      if (buttonCounter == 10) {
        digitalWrite(ledPin1, HIGH);
      } else if (buttonCounter == 100) {
        digitalWrite(ledPin2, HIGH);
      } else if (buttonCounter == -127) {
        digitalWrite(ledPin3, HIGH);
      }
    }

    while (digitalRead(buttonPin) == HIGH) {} // Aguarda até que o botão seja solto
  }

  if (buttonCounter >= 100) {
    buttonCounter = 0; // Reinicia o contador para evitar overflow
  }
}