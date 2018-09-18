#coding=utf-8
from DbHelper import * 

def testDBHelper():
    dbhelper =  MysqlHelper(host='localhost',
        port = 3306,
        user='root',
        passwd='test1234',
        db ='fl_good',)
    
    version=dbhelper.getDBVersion()
    print("version=%s" %(version))

    data=dbhelper.descTable()
    print("data=%r" %(type(data)))



if __name__  == '__main__':
    testDBHelper()
