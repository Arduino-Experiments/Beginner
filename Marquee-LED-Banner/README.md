# 跑马灯

blink的延伸，跑马灯小实验

## 器材

1. led小灯x6
2. 1000欧姆稳流电阻
3. 面包板

## 电路图

![banner](source/banner.png)

## 程序

本程序使用数字输入输出端口的5号口,程序如下:

```C++
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

```
