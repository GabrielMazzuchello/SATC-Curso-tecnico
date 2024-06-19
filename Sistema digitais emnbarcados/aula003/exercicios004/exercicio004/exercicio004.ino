const int botao_io = 2;
const int led_d0 == 8;

bool aux = 0
bool estado = 0

void setup() {
  pinMode(botao_i0, INPUT);
  pinMode(led_d0, OUTPUT);
}

void loop() {
  bool i0 = digitalRead(botao_i0);
  if (i0 == 1) {
    if (aux == 0) {
      aux = 1;
      estado = !estado;
    }
  }
  else {
    aux = 0
  }
  digitalWrite(led_d0, estado);
}
