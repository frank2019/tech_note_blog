from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import time
import urllib
import re
from urllib.parse import quote
import pymysql
import traceback




def getInfo(url):
    url=quote(url, safe='/:?=')
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    soup=BeautifulSoup(data,"lxml")
    soup_pr=soup.prettify()

    fig_info={}

    fig_cv=soup.find_all("div",class_="summary-pic")
    
    if fig_cv is not None and len(fig_cv)>0:
        for n in fig_cv[0].descendants:
            #print(n.name)
            if n.name == 'img':
                #print(n['src'])
                fig_info['icon_url']=n['src']
                break
    
    
    fig_name=soup.find_all("dt",class_="basicInfo-item name")
    #name=fig_name[0].text.strip('\n')

    fig_cv=soup.find_all("dd",class_="basicInfo-item value")
  

    for i  in range(len(fig_name)):
        name=fig_name[i].text.strip('\n')
        value=fig_cv[i].text.strip('\n')
        fig_info[convertName(name)]=value

    print(fig_info)
    return fig_info


def convertName(name):
    if name == '中文名':
        return 'name'
    if name == '外文名':
        return 'english_name'
    if name == '星\xa0\xa0\xa0\xa0座':
        return 'constellation'
    if name == '代表作品':
        return 'movienames'
    if name == '主要成就':
        return 'description'
    return name


def testMysql():
    db = pymysql.connect("192.168.1.70","root","root1230ROOT!@#","mx_video" )
    cursor = db.cursor()
    sql = "SELECT * FROM tb_persons"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id=row[0]
            name = row[1]
            englist_name = row[2]
            icon_url = row[11]
            # 打印结果
            print ("id=%d,name=%s,englist_name=%s,icon_url=%s" % \
                (id, name, englist_name, icon_url ))
    except:
        print ("Error: unable to fetch data")
 
    # 关闭数据库连接
    db.close()


def insert(name,englist_name,constellation,description,movienames,icon_url):
    db = pymysql.connect("192.168.1.70","root","root1230ROOT!@#","mx_video" )
    cursor = db.cursor()
    sql = "INSERT INTO  tb_persons(name,english_name,constellation,description,movienames,icon_url) VALUES ('%s','%s','%s','%s','%s','%s')" %(name,englist_name,constellation,description,movienames,icon_url)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
    except Exception:
        print ("Error: unable to fetch data")
        traceback.print_exc()
        db.rollback()

 
    # 关闭数据库连接
    db.close()



def refresh():
    #'刘德华','周笔畅','陈伟霆','鹿晗','黄子韬','乔振宇','宋茜','蔡徐坤','李敏镐'
    #names=['苍井空','杨颖','赵丽颖','迪丽热巴','周杰伦','霍建华','胡歌','郑爽','韩雪','唐嫣','戚薇','王俊凯']
    #names=['范冰冰','刘亦菲','张国荣','杨子','韩雨芹','冯提莫','陶辰宇','华晨宇','易烊千玺','菜花甜妈']
    #names=['全智贤','欧阳娜娜','佟丽娅','杨洋','李易峰','邓紫棋','孙艺珍','陈赫','郑恺','王源','邓超']
    #names=['柳岩','张翰','关晓彤','林允儿','张杰','道恩·强森','李晨','杨子姗','吴亦凡','黄圣依','林志颖']
    #names=['林心如','钟汉良','杨紫','泰勒·斯威夫特','奥黛丽·赫本','贾斯汀·比伯','白百何','高圆圆','张馨予','陈乔恩','何超琼']
    #names=['李小璐','黄晓明','古力娜扎','刘恺威','吴奇隆','孙俪','景甜','何炅','杰森·斯坦森','黄景瑜','文章','金·卡戴珊']
    names=['朴信惠','谢娜','黄渤','阿米尔·汗','莱昂纳多·迪卡普里奥','谢霆锋','陈晓','周冬雨','马天宇','吴京','郑秀妍','霍思燕']
    
    for name in names:
        url='https://baike.baidu.com/item/' +  name
        #print(url)
        info=getInfo(url)
        if info is None:
            continue
        if not 'name' in info:
            print("%s is  not get" %(name))
            continue
        name=info['name']
        englist_name=None
        constellation=None
        movienames=None
        try:
            englist_name=info['english_name']
        except Exception:
            #traceback.print_exc() 
            print("")
        if 'constellation' in info:
            constellation=info['constellation']
        if 'description' in info:
            description=info['description']
        if 'movienames' in info:
            movienames=info['movienames']
        
        icon_url=""
        try:
            icon_url=info['icon_url']
        except Exception:
            #traceback.print_exc() 
            print("")
        insert(name,englist_name,constellation,description,movienames,icon_url)



if  __name__=='__main__' :
    
    refresh()

    #print("Hello world")
    #urlStr='https://baike.baidu.com/item/舒畅'
    #urlStr='https://baike.baidu.com/item/刘德华'
    #urlStr='https://baike.baidu.com/item/成龙'
    #getInfo(urlStr)
    #testMysql()
    #insert('舒畅','Jennifer','射手座','','单亲之家、孝庄秘史、宝莲灯、魔幻手机、连城诀、天龙八部、宫锁珠帘、烽火佳人','https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign=76046f018b0a19d8df0e8c575293e9ee/cc11728b4710b9127247c04ec8fdfc03934522ff.jpg')