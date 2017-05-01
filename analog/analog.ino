auto analogPin = A5;
auto ledPin = 3;
auto val = 0;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
}

void loop() {
  val=analogRead(analogPin);
  Serial.println(val);
  analogWrite(ledPin,val/4);
  delay(1000);
}
