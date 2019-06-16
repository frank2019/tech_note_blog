import os
import re
import string
import sys
import pytest

def D(*kwargs):
    print(*kwargs)

def get_subject_info(subject_name):
    """
    获取给定题目的信息
    Args: 
        subject_name: 题目文件名
    Returns:
        type:  type of subject like  done,todo,release
        title: subject titled
        priority: subject priority (0-9)  default is 6,if not set
        category: category of subject
    """
    if subject_name is None:
        return None
    result =  {}
    result['subject_type'] = 'unknow'
    if subject_name.find('todo.') == 0:
        type = 'todo'
        res = re.search('(?P<subject_type>\w*)\.(?P<prority>\w{1})\.(?P<category>\w*)_(?P<title>\w*)',subject_name)
        if res is None:
            return result
        result =  res.groupdict()
        #print(res.groupdict())
        #priority = result.groupdict()['prority']
    else :
        ret =  re.match(r'^\d*\.',subject_name)
        if ret:
            # release file format: 1.python_字符串.md
            res = re.search('(?P<id>\w*)\.(?P<category>\w*)_(?P<title>\w*)\.md',subject_name)
            if res is None:
                return result
            result =  res.groupdict()
            result['subject_type'] = 'release'
        else :
            # done file format : python_字符串.md
            res = re.search('(?P<category>\w*)_(?P<title>\w*)\.md',subject_name)
            if res is None:
                return result
            result =  res.groupdict()
            result['subject_type'] = 'done'
    return result



def get_notes(target_dir):
    list_done = []
    list_todo = []
    list_release = []
    list_unknow = []
    #D("this is test %s" %(target_dir))
    for dirpath,dirnames,filenames in os.walk(target_dir):
        topDirName =  os.path.basename(dirpath)
        if 'img' == topDirName or 'asset' == topDirName:
            continue
        if 'camera_img' == topDirName :
            continue
        for file in filenames:
            fullpath=os.path.join(dirpath,file)
            #print (fullpath)
            result = get_subject_info(file)
            if result is None :
                continue
            if result['subject_type'] == 'done':
                list_done.append(fullpath)
            elif result['subject_type'] == 'release':
                list_release.append(fullpath)
            elif result['subject_type'] == 'todo':
                list_todo.append(fullpath)
            else :
                list_unknow.append(fullpath)
    return (list_todo,list_done,list_release,list_unknow)

def get_max_prority(list_todo):
    if list_todo is None:
        return '0'
    max_property = '0'
    for fullname in list_todo:
        name =  os.path.basename(fullname)
        subject = get_subject_info(name)
        if max_property < subject['prority']:
            max_property = subject['prority']
    return max_property

def get_max_prority_subject(list_todo):
    if list_todo is None:
        return  None
    max_property =  get_max_prority(list_todo)
    list_result = []
    for fullname in list_todo:
        name =  os.path.basename(fullname)
        subject = get_subject_info(name)
        if subject['prority'] == max_property:
            list_result.append(fullname)
    return list_result

if __name__ == '__main__':
    #todo,done,released,unknow = get_notes("F:\\workspace\\tech_note_blog\\common\\opencv")
    todo,done,released,unknow = get_notes("F:\\workspace\\tech_note_blog\\common")
    
    #print(todo)
    #print(done)
    #print(released)
    #print(unknow)

    #max_prority = get_max_prority(todo)
    #print(max_prority)
    print('num of todo: %d ' %(len(todo)))
    print('num of done: %d ' %(len(done)))
    print('num of released: %d ' %(len(released)))
    #pytest.main()

    list_sth =  get_max_prority_subject(todo)
    print(list_sth)


