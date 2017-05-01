# Arduino Experiments

本项目为用arduino做的实验记录,这东西真好玩!意大利人干的好!

## 环境搭建

硬件:

1. 一块arduino uno
2. 一块面包板
3. 一些传感器,开关等作为输入
4. 一些led小灯,电机,小屏幕等作为输出

软件:

1. 一台装有操作系统的电脑,推荐台式机,这样有个桌子可以放板子.我的台式机是win10
2. 一个arduino的IDE(windows下不要装应用商店的哪个版本,那个版本无法上传)
3. 如果更有追求些,还需要一个画电路图的软件,身为一个pythoner,我用的[SchemDraw](https://cdelker.bitbucket.io/SchemDraw/SchemDraw.html)

除此之外你还得会一点C++

## 代码风格

arduino的代码看着比较像c++代码,但有几点有显著的特点

+ 使用预定义的函数作为钩子操作硬件

    这点有点像processin,我们并不能自己定义哪个函数是主函数,哪个函数来初始化,而是必须实现预定义好的函数.
    + setup()初始化函数,程序开始的时候会运行,一般用来初始化一些变量,接口模式,和启用库等

        接口模式:`pinMode(port:int ,OUTPUT/INPUT)`启用某一个数字输入输出端口,并设定它是输入还是输出.注意,OUTPUT/INPUT不是字符串而是预定义好的变量

    + loop()程序主循环,一般程序都是作为服务要长期运行的,loop定义主循环中的逻辑.

+ 使用预定义好的函数操作硬件

    常见的函数有:

+ `digitalRead(port:int)` 读出数字端口的值是高电平还是低电平
+ `digitalWrite(port:int, HIGH/LOW)` 数字端口写入高低电平
+ `analogWrite(port:int,value:float)`模拟端口写入
+ `analogRead(port:int,)`模拟端口读取
+ `delay(number:int)` 等待,参数单位为毫秒
+ `Serial.begin(baud_rate)`设置串行每秒传输数据的速率,同计算机通讯时,使用:300,1200,2400,4800,9600,14400,19200,28800,38400,57600,115200,这些数值;与0,1号插口通讯时会要求特殊的波特率,这个方法一般用在`setup()`函数里
+ `Serial.read()`读取持续输入的数据
+ `Serial.print(data[,system])`默认使用10进制,从串行端口输出数据
+ `Serial.println(data[,system])`默认使用10进制,从串行端口输出数据,会跟随一个回车和一个换行符

## I/O

与树莓派不同的是,arduino没有操作系统,更底层更注重硬件,它配置了14个数字I/O端口和6个模拟I/O端口.

### 数字I/O

数字I/O分为两段,即管脚0到管脚7和管脚8到管脚13,除了管脚13上接了1k的电阻外其他都只i金额连在ATmega上.
