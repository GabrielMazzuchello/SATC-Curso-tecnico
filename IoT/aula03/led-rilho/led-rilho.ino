const int pin_led1 = 9;
const int pin_led2 = 10;
const int pin_led3 = 11;

int valor = 0;
int brilho = 0;

int aux = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pin_led1, OUTPUT);
  pinMode(pin_led2, OUTPUT);
  pinMode(pin_led3, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    valor = Serial.parseInt();
    if (aux == 0) {
      Serial.println("Digite um valor de 0 a 255. (azul)");
      brilho = valor*2.55;
      analogWrite(pin_led1, brilho);
      aux = 1;
    }

    if (aux == 1) {
      // Serial.println("Digite um valor de 0 a 255. (verde)");
      brilho = valor*2.55;
      analogWrite(pin_led2, brilho);
      aux = 2;
    }

    if (aux == 2) {
      // Serial.println("Digite um valor de 0 a 255. (vermelho)");
      brilho = valor*2.55;
      analogWrite(pin_led3, brilho);
      aux = 0;
    }
  }
}
