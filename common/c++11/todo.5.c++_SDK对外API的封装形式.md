

# C++SDK对外API的封装形式



## 1，目标

1. 接口与实现相分离
2. 不暴露具体实现细节

## 2，常见的实现方式

### 2.1 组合形式

分别定义API接口的 接口类和实现类，对外提供接口类作为API。接口类中通过组合方式调用实现类具体实现类的功能。



#### 优缺点



#### 常见示例

1. [OpenNi2](https://github.com/OpenNI/OpenNI2)



### 2.2 继承形式

使用pure virtual 函数实现接口类，并暴露给SDK之外，具体实现则通过继承此接口类实现，



#### 优缺点

#### 常见示例





## 参考链接

1. [C++封装SDK的一种方法(接口与实现分离)](https://blog.csdn.net/u011583798/article/details/79615756)
2. https://blog.csdn.net/u011583798/article/details/79696242

