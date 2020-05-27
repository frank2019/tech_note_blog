mysql的安装



###1. mysql的基本安装

参考文章

[在windows10上安装mysql详细图文教程](http://www.jb51.net/article/92158.htm)



###2. 安装报错

在本地使用命令链接mysql的时候，有如下报错

```
mysql -u root -p
```



```
Access denied for user 'root'@'localhost' (using password:YES) 解决方案 
```

问题的解决





解决方案：

1、打开MySQL目录下的my.ini文件，在文件的最后添加一行“skip-grant-tables”，保存并关闭文件。

2、重启MySQL服务。

3、在命令行中输入“mysql -uroot -p”(不输入密码)，回车即可进入数据库。

4、执行，“use mysql;”使用mysql数据库。

5、执行，“update user set authentication_string=PASSWORD("youpasswd") where user='root';”（修改root的密码）

成功提示如下：

```
Query OK, 1 row affected, 1 warning (0.15 sec)
Rows matched: 1 Changed: 1 Warnings: 1
```

6、打开MySQL目录下的my.ini文件，删除最后一行的“skip-grant-tables”，保存并关闭文件。

7、重启MySQL服务。

8、在命令行中输入“mysql -u root -p ”，



在老版本中，更新密码使用的是如下的命令：

mysql数据库下已经没有password这个字段了，password字段改成了authentication_string。

```
update mysql.user set password=password('password') where user='root';
```



### 常用命令



项目的启动

mysql -u root -p