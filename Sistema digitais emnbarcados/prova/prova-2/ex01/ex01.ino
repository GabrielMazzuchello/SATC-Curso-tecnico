const int pin_BOTAO1 = 2;
const int pin_BOTAO2 = 3;
const int pin_BOTAO3 = 4;
const int pin_LED1 = 8;
const int pin_LED2 = 9;
const int pin_LED3 = 10;
// declaração de todos os pinos dos botões e dos leds

void setup() {
  // define o se o terminal é de entrada ou saida
  pinMode(pin_BOTAO1, INPUT);
  pinMode(pin_BOTAO2, INPUT);
  pinMode(pin_BOTAO3, INPUT);
  pinMode(pin_LED1, OUTPUT);
  pinMode(pin_LED2, OUTPUT);
  pinMode(pin_LED3, OUTPUT);
}

void loop() {
  // salva o estado dos botões em uma variavel 
  bool BOTAO1 = digitalRead(pin_BOTAO1);
  bool BOTAO2 = digitalRead(pin_BOTAO2);
  bool BOTAO3 = digitalRead(pin_BOTAO3); 

  // com o estado dos botões salvos nas variaveis a cima verifica os seus valores e liga ou desliga o led correspondente
  if (BOTAO1 == 1) {
    digitalWrite(pin_LED1, HIGH);
  }
  else {
    digitalWrite(pin_LED1, LOW);
  }
    if (BOTAO2 == 1) {
    digitalWrite(pin_LED2, HIGH);
  }
  else {
    digitalWrite(pin_LED2, LOW);
  }

  if (BOTAO3 == 1) {
    digitalWrite(pin_LED3, HIGH);
  }
  else {
    digitalWrite(pin_LED3, LOW);
  }
}
