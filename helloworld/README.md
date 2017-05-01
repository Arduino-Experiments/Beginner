# helloworld实验


最基本的小实验,实现通过串口和pc通信，本实验不需要其他器材


## 程序

本程序使用数字输入输出端口的5号口,程序如下:

```C++
void setup() {
    Serial.begin(9600);//open a serial ,set baud rate as 9600bps
}

void loop() {
    Serial.println("hello world");
    delay(1000);
}
```
