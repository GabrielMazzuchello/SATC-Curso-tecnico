int num1 = 0;
int num2 = 0;


int multi(int a, int b) {
  int z = 0;
  for (int i = 0; i < b; i++) {
    z += a;
  }
  return z;
}

void imprime(int resultado) {
  Serial.print("O resultado é: ")
  Serial.println(resultado);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myservo.attach(4);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Informe um nuumero: ");
  while (1) { 
    if (Serial.available() > 0 ) {  
      break;
    }
  }
  num1 = Serial.parseInt();

  Serial.println("Informe outro nuumero: ");
  while (1) {
    if (Serial.available() > 0 ) {  
      break;
    }
  }
  num2 = Serial.parseInt();
  int resultado = multi(num1, num2);
  imprime();





}