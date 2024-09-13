const int pin_led = 9;
int caunt = 0;
int i = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(pin_led, OUTPUT);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  for (i <= 255; i += 1) {
    analogWrite(pin_led, i);
    delay(50);

  };

  for (i >= 255; i -=1) {
    analogWrite(pin_led, i);
    delay(50);

  };







}
