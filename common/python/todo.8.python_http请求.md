-*3

## 目标

使用requests库实现 http请求的 GET，POST，PUT DELETE



## 安装

```bash
pip install requests
```



## 使用



### GET

```
import requests
import json


url = 'http://localhost:8888/mattos?author=me'

def  test_main_entry():
    r = requests.get(url)
    body =  r.content.decode('utf-8')
    #print(body)
    text  =  json.loads(body)
    #print(text)
    for item in text:
        assert item['author'] != None


if __name__ == '__main__':
    test_main_entry()
```





http://2.python-requests.org/zh_CN/latest/user/quickstart.html