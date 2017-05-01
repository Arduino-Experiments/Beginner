auto ledPin=5;
int val;
void setup() {
 pinMode(ledPin,OUTPUT);
 Serial.begin(9600);
}

void loop() {
  val = Serial.read();
  if(-1 != val){
    if('H' == val){
      digitalWrite(ledPin,HIGH);
      delay(1000);
      digitalWrite(ledPin,LOW);
       Serial.println(char(val));
      Serial.print("Available:");
      Serial.println(Serial.available(),DEC);
    }
  }
}
