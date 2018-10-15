import requests,random,time
from bs4 import BeautifulSoup

#MySQLdb


def get_webdata(url): 
    headers = { 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' } 
    r = requests.get(url,headers=headers) 
    c = r.content 
    b = BeautifulSoup(c) 
    data_list = b.find('ul',{'class':'article-ul'}) 
    data_li = data_list.findAll('li') 
    for i in data_li: 
        # 替换标题中的英文双引号，防止插入数据库时出现错误 
        title = i.find('h4').find('a').get_text().replace('"','\'\'') 
        link = i.find('h4').find('a').attrs['href'] 
        source = i.find('span',{'class':'blue'}).get_text() 
        time = i.find('span',{'class':'blue'}).parent.next_sibling.next_sibling.get_text().replace('发布时间：'.decode('utf-8'),'') 
        readnum = int(i.find('i',{'class':'fa-book'}).next_sibling) 
        praisenum = int(i.find('i',{'class':'fa-thumbs-o-up'}).next_sibling) 
        #insert_content(title,readnum,praisenum,time,link,source)


if __name__ == "__main__" :
    print("Hello World!")

    get_webdata('https://mp.weixin.qq.com/s/G34zZ-Q2JCG1eY1QuUmKoQ')