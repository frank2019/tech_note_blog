





在python3的标准库中，已经移除了md5，而关于hash加密算法都放在hashlib这个标准库中，如SHA1、SHA224、SHA256、SHA384、SHA512和MD5算法等。

以下为官方文档的介绍：

https://docs.python.org/3/library/hashlib.html?highlight=hashlib#credits

### md5()方法使用

update(arg)传入arg对象来更新hash的对象。必须注意的是，该方法只接受byte类型，否则会报错。这就是要在参数前添加b来转换类型的原因。
同时要注意，重复调用update(arg)方法，是会将传入的arg参数进行拼接，而不是覆盖。也就是说，m.update(a); m.update(b) 等价于m.update(a+b)。
hexdigest()在英语中hex有十六进制的意思，因此该方法是将hash中的数据转换成数据，其中只包含十六进制的数字。

```
`>>> ``import` `hashlib``>>> m ``=` `hashlib.md5()``>>> m.update(b``'123'``)``>>> m.hexdigest()``'202cb962ac59075b964b07152d234b70'` `# 或者可以这样（最常见的写法，常用于图片的命名）``>>> hashlib.md5(b``'123'``).hexdigest()``'202cb962ac59075b964b07152d234b70'` `# 也可以使用hash.new()这个一般方法，hashlib.new(name[, data])，name传入的是哈希加密算法的名称，如md5``>>> hashlib.new(``'md5'``, b``'123'``).hexdigest()``'202cb962ac59075b964b07152d234b70'`
```

以上是对于英文进行md5加密的，如果要对中文进行加密，发现按照上面来写会报错，原因在于字符转码问题，要如下写：

```
`>>> ``import` `hashlib``>>> data ``=` `'你好'``>>> hashlib.md5(data.encode(encoding``=``'UTF-8'``)).hexdigest()``'7eca689f0d3389d9dea66ae112e5cfd7'`
```

此处先将数据转换成UTF-8格式的，使用网上工具对比下加密的结果，发现有的md5加密工具并不是使用UTF-8格式加密的。 
经测试目前发现可以转为UTF-8、GBK、GB2312、GB18030，不分大小写(因为GBK/GB2312/GB18030均是针对汉字的编码，所以md5加密后结果一样)。 

例如：

```
`>>> hashlib.md5(``'你好'``.encode(encoding``=``'UTF-8'``)).hexdigest()``'7eca689f0d3389d9dea66ae112e5cfd7'` `>>> hashlib.md5(``'你好'``.encode(encoding``=``'GBK'``)).hexdigest()``'b94ae3c6d892b29cf48d9bea819b27b9'` `>>> hashlib.md5(``'你好'``.encode(encoding``=``'GB2312'``)).hexdigest()``'b94ae3c6d892b29cf48d9bea819b27b9'` `>>> hashlib.md5(``'你好'``.encode(encoding``=``'GB18030'``)).hexdigest()``'b94ae3c6d892b29cf48d9bea819b27b9'`
```