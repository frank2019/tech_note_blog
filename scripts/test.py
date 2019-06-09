import re
import pytest

s='130532198708XXXXXX'


#res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})(?P<mon>\d{2})',s)
#print(res.groupdict())



def  myfun():
    s='todo.4.opencv_123'
    res = re.search('(?P<subject_type>\w*)\.(?P<prority>\w{1})\.(?P<category>\w*)_(?P<title>\w*)',s)
    print(res.groupdict())
    priority = res.groupdict()['prority']
    print(priority)


def test_myfun():
    myfun()
