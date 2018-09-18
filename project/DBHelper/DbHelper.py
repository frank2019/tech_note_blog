#coding=utf-8
import MySQLdb

class MysqlHelper:
    def __init__(self,host,port,user,passwd,db):
        self.host =  host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbname = db
        self.connect()

        self.DBType = 'Mysql'
    
    def __del__(self):
        if self.db is not None:
            self.db.close()
    
    def connect(self):
        self.db = MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='test1234',
            db ='fl_good',
        )


    def getDBVersion(self):
        # 使用cursor()方法获取操作游标 
        cursor = self.db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchone()
        return data

    def showTables(self):
        cursor = self.db.cursor()
        cursor.execute('SHOW TABLES')
        data = cursor.fetchall()
        return data
    
    def descTable(self):
        cursor = self.db.cursor()
        #cursor.execute('desc tb_pagecontent')
        cursor.execute('show full fields from  tb_pagecontent')
        data = cursor.fetchall()
        return data





def test():
    #connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息。
    # #这只是连接到了数据库，要想操作数据库需要创建游标。
    db= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='test1234',
        db ='fl_good',
        )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()
    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()