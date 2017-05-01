auto startPin=2;
auto endPin=7;
auto index=0;

void setup() {
  for(auto i = startPin;i<=endPin;i++){
    pinMode(i,OUTPUT);
  }
}

void loop() {
  for(auto i = startPin;i<=endPin;i++){
    digitalWrite(i,LOW);
    }
    digitalWrite(startPin+index,HIGH);
    index = (index+1)%(endPin-startPin+1);
    delay(100);
}
