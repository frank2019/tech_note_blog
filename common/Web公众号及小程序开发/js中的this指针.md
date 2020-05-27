javascript  中的this指针



## 前言

this 指针代码所属类，实例化的对象。  由于javascript是动态绑定语言，所有应用场景的变化形式会比较多，我们看看常用的一些场景   ---->



## 常见的应用场景

常见的场景

1、作为普通函数使用

2、作为对象方法来使用

3、call和apply

4、作为构造函数来使用



### 场景1 普通方法的使用

```javascript
function funcA() {
    this.name = "hello";
    console.log(this.name);
    this.show = function() {
        console.log(this.name);
    }
}
funcA();// 1、hello
```

这个代码很简单，但也隐藏了一个坑，就是这个时候的this 代表的是window的指针，所以当这段代码运行完之后，你再输出 console.log(window.name)时候，你会发现输出为”hello”,在使用中尽量避免。

再游离的非类中的成员函数中使用的this指针，默认指代的是window对象。



### 2 在类的成员函数中使用this

示例代码说话：

```
var obj={name:"hello",show:function(){

console.log(this.name);

}};

obj.show();
```

这个很简单，this指向自己,所以this.name就用hello;

实例2

```
var obj={name:"hello",show:function(){
    console.log(this.name);
}};
obj.show();

var objA={name:"world"}
objA.show=obj.show;
objA.show()
```

这个结果又是什么呢？答案是”world”,

因为在js中对象都是引用类型，当objA.show=obj.show这句代码把objA.show也指向的show方法，所以在调用的时候会把this，指向objA而不是obj.（方法和数据是独立的，二者之间没有耦合关系）

### 场景3  在构造函数中的使用



代码说话:





### 参考链接

1. [Javascript中call和apply的区别与详解](http://blog.csdn.net/chelen_jak/article/details/21021101)

