from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import time
import urllib
import re
from urllib.parse import quote
name_lt=pd.read_excel('名单.xlsx')
name_lt=list(name_lt['名单'])
 
final_result=[]
 
url='https://baike.baidu.com/item/'+name_lt[204]
 
url=quote(url, safe='/:?=')
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
soup=BeautifulSoup(data,"lxml")
soup_pr=soup.prettify()
 
fig_cv=soup.find_all("div",class_="lemma-summary")
fig_summary=fig_cv[0].text.strip('\n')
fig_info={}
fig_info['姓名']=fig_summary.split('，')[0].replace('[1]','')
fig_info['性别']=fig_summary.split('，')[1]
fig_info['民族']=fig_summary.split('，')[2]
fig_info['出生年份']=fig_summary.split('，')[3][0:4]
fig_info['出生月份']=fig_summary.split('，')[3].split('年')[1].strip('月生')
fig_info['出生省份']=fig_summary.split('，')[4][0:2]
fig_info['出生城市']=fig_summary.split('，')[4].rstrip('人')[-2:]
fig_info['其他']=fig_summary.split('，',5)[5]
 
for fig_exp in soup.find_all("div",class_="para-title level-2"):
    result=[]
    tmp=fig_exp
    #tmp=tmp.span.clear()
    key=tmp.text.replace(fig_info['姓名'],'')
    fig_start=fig_exp.next_sibling
    result=[]
    for sibling in fig_start.next_siblings:
        if sibling!='\n':
            if sibling.has_attr('class'):
                if sibling['class'][0]!='para':
                    break
                else:
                    result.append(sibling.text)
    fig_info[key]=result
 
final_result.append(fig_info)