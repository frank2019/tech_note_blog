



### 0x01 ，ubuntu 上Access denied for user 'root'@'localhost' (using password:YES) 

我的环境ubuntu 16.04  亲测可行。

解决步骤：

1、打开MySQL目录下的配置文件(我的目录是/etc/mysql/mysql.conf.d/mysqld.cnf, 可能有的系统是my.ini)，在文件的最后添加一行“skip-grant-tables”，保存并关闭文件。

2、重启MySQL服务(我用命令 service mysql restart)。

3、在命令行中输入“mysql -uroot -p”(不输入密码)，回车即可进入数据库。

4、执行，“use mysql;”使用mysql数据库。

5、执行，“update user set authentication_string=PASSWORD("rootadmin") where user='root';”（修改root的密码, 有的mysql表列名可能是password, 需要是命令:"update user set password=PASSWORD("rootadmin") where user='root';"）



6、打开MySQL目录下的my.ini文件，删除最后一行的“skip-grant-tables”，保存并关闭文件。

7、重启MySQL服务。( service mysql restart)

8、在命令行中输入“mysql -uroot -prootadmin”，问题搞定！

