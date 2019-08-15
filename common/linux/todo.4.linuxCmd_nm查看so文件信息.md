

 nm不是ni ma的缩写， 当然， 也不是ni mei的缩写， 而是names的缩写， nm命令主要是用来列出某些文件中的符号



###  			Linux 查看.so中导出函数]



**方法一**

nm -D  **.so

但这样能看到所有的导出，乱七八糟的很多，筛选用：

nm **.so | grep XX

 

**方法二**
objdump -tT **.so

