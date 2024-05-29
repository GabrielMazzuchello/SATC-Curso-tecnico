                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        const int botao_i0 = 2;
const int botao_i1 = 3;
const int led_d0 = 8;
const int led_d1 = 9;
const int led_d2 = 10;
const int led_d3 = 11;
int conta = 0
int aux_up = 0
int aux_dw = 0

void setup() {
  // put your setup code here, to run once:
  pinMode(botao_i0, INPUT);
  pinMode(botao_i1, INPUT);
  pinMode(led_d0, OUTPUT);
  pinMode(led_d1, OUTPUT);
  pinMode(led_d2, OUTPUT);
  pinMode(led_d3, OUTPUT);
  Serial.begin(9600);

}
void loop() {
  bool i0 = digitalRead(botao_i0);
  bool i0 = digitalRead(botao_i1);   
  if (i0 == 1) {
    if (aux_up == 0) {
      aux_up == 1;
      conta++;
      Serial.println(conta);
    }
  }
  else {
    aux_up = 0;
  }
  if (i1 == 1) {
    if (aux_up == 0) {
      aux_up == 1;
      conta--;
      Serial.println(conta);
    }
  }
  else {
    aux_up = 0;
  }
  if (conta > 15) {
    conta = 0;
  }
  if (conta < 0) {
    conta = 15;
  }
  switch (conta) {
    case 0:
      digitalWeite(d0, 0); 
      digitalWeite(d0, 0);
      digitalWeite(d0, 0);
      digitalWeite(d0, 0);
      break;
    case 1:
      digitalWeite(d0, 1); 
      digitalWeite(d0, 0);
      digitalWeite(d0, 0);
      digitalWeite(d0, 0);
      break;
    case 2:
      digitalWeite(d0, 0); 
      digitalWeite(d0, 1);
      digitalWeite(d0, 0);
      digitalWeite(d0, 0);
      break;
    case 3:
      digitalWeite(d0, 1); 
      digitalWeite(d0, 1);
      digitalWeite(d0, 0);
      digitalWeite(d0, 0);
      break;
    case 4:
      digitalWeite(d0, 0); 
      digitalWeite(d0, 0);
      digitalWeite(d0, 1);
      digitalWeite(d0, 0);
      break;
    case 5:
      digitalWeite(d0, 1); 
      digitalWeite(d0, 0);
      digitalWeite(d0, 1);
      digitalWeite(d0, 0);
      break;
    case 6:
      digitalWeite(d0, 1); 
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      digitalWeite(d0, 0);
      break;
    case 7:
      digitalWeite(d0, 0); 
      digitalWeite(d0, 0);
      digitalWeite(d0, 0);
      digitalWeite(d0, 1);
      break;
    case 8:
      digitalWeite(d0, 1); 
      digitalWeite(d0, 0);
      digitalWeite(d0, 0);
      digitalWeite(d0, 1);
      break;
    case 9:
      digitalWeite(d0, 0); 
      digitalWeite(d0, 1);
      digitalWeite(d0, 0);
      digitalWeite(d0, 1);
      break;
    case 10:
      digitalWeite(d0, 1); 
      digitalWeite(d0, 1);
      digitalWeite(d0, 0);
      digitalWeite(d0, 1);
      break;
    case 11:
      digitalWeite(d0, 0); 
      digitalWeite(d0, 0);
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      break;
    case 12:
      digitalWeite(d0, 1); 
      digitalWeite(d0, 0);
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      break;
    case 13:
      digitalWeite(d0, 0); 
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      break;
    case 14:
      digitalWeite(d0, 1); 
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      break;
    case 15:
      digitalWeite(d0, 1; 
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      digitalWeite(d0, 1);
      break;
    
  }
  }
 }
}
