const int botao_i0 = 2;
const int botao_i1 = 3;
bool botao = false;
int count = 0;


void setup() {
  pinMode(botao_i0, INPUT);
  pinMode(botao_i1, INPUT);
  Serial.begin(9600);
  
}
void loop() {
  // put your main code here, to run repeatedly:
  bool i0 = digitalRead(botao_i0);
  bool i1 = digitalRead(botao_i1);
  botao = digitalRead(botao_i0);
  if (botao == true) {
    count = count + 1;
    Serial.println(count);
  }
  botao = digitalRead(botao_i1);
  if (botao == true) {
    count = count - 1;
    Serial.println(count);
  }
}
