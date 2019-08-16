

在Python中获取系统信息的另一个好办法是使用`psutil`这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。



## 安装

```bash
pip install psutils
```

or

```bash
easy_install psutils
```



```python

# -*- coding: utf-8-*-
import psutil

def get_proc_by_id(pid):
    return psutil.Process(pid)
def get_process_info(pid):
	proc = psutil.Process(pid)

	total = psutil.virtual_memory().total
	used = psutil.virtual_memory().used
	available = psutil.virtual_memory().available
	#rss, vss = proc.memory_info()
	rssinfo = proc.memory_info()
	percent = proc.memory_percent()

	print(rssinfo)
	#print("rss: %s Byte, vss: %s Byte" % (rss, vss))
	print("total: %.2f(M)" % (float(total)/1024/1024/1024))
	print("used: %.2f(M)" % (float(used)/1024/1024/1024))
	#print("percent: %.2f%%, calc: %.2f%%" % (percent, 100*float(rss)/total))

def get_proc_by_name(pname):
    """ get process by name
    
    return the first process if there are more than one
    """
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == pname.lower():
                return proc  # return if found one
        except psutil.AccessDenied:
            pass
        except psutil.NoSuchProcess:
            pass
    return None


if '__main__' == __name__:
    myprocess=get_proc_by_name("test.exe")
    #print(get_proc_by_id(25436))
    if myprocess is None:
        print("None process exist")
    else : 
        print(get_process_info(myprocess.pid))
	

```



# 参考链接

1. [win/linux 下使用 psutil 获取进程 CPU / memory / IO 占用信息](https://www.cnblogs.com/misspy/p/3851327.html)
2. [psutils官方API文档](https://psutil.readthedocs.io/en/latest/)

