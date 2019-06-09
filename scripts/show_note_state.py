import os
import re
import string

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
        return []
    result =  []
    if subject_name.find('todo.') == 0:
        type = 'todo'
        res = re.search('(?P<subject_type>\w*)\.(?P<prority>\w{1})\.(?P<category>\w*)_(?P<title>\w*)',subject_name)
        result =  res.groupdict()
        #print(res.groupdict())
        #priority = result.groupdict()['prority']
    else :
        ret =  re.match(r'^\d*\.',subject_name)
        if ret:
            # release file format: 1.python_字符串.md
            res = re.search('(?P<id>\w*)\.(?P<category>\w*)_(?P<title>\w*)\.md',subject_name)
            result =  res.groupdict()
            result['subject_type'] = 'release'
        else :
            # done file format : python_字符串.md
            res = re.search('(?P<category>\w*)_(?P<title>\w*)\.md',subject_name)
            result =  res.groupdict()
            result['subject_type'] = 'done'
    return result


def test_get_subject_info():
    list = ['1.opencv_字符串.md']
    for line in list:
        ret = get_subject_info(line)
        print(ret)



def getNotesDone(target_dir):
    listDone = []
    listTodo = []
    listRelease = []
    #D("this is test %s" %(target_dir))
    for dirpath,dirnames,filenames in os.walk(target_dir):
        topDirName =  os.path.basename(dirpath)
        if 'img' == topDirName :
            continue
        if 'camera_img' == topDirName :
            continue
        for file in filenames:
            fullpath=os.path.join(dirpath,file)
            #print (fullpath)
            
            ret = file.find('todo.')
            if 0 == ret:
                #print (file)
                listTodo.append(file)
            else :
                ret =  re.match(r'^\d*\.',file)
                if ret:
                    #print (file)
                    listRelease.append(file)
                else :
                    listDone.append(file)
    return (listTodo,listDone,listRelease)

if __name__ == '__main__':
    #getNotesDone("D:\\MoreBetter\\tech_note_blog\\common\\3DCamera")
    #todo,done,released = getNotesDone("F:\\workspace\\tech_note_blog\\common\\3DCamera")
    
    #todo,done,released = getNotesDone("F:\\workspace\\tech_note_blog\\common")
    
    #print(todo)
    #print(done)
    #print(released)

    #print('num of todo: %d ' %(len(todo)))
    #print('num of done: %d ' %(len(done)))
    #print('num of released: %d ' %(len(released)))
    #ret =  get_subject_info('1.opencv_字符串.md')
    #ret =  get_subject_info('todo.1.opencv_字符串.md')
    ret =  get_subject_info('opencv_字符串.md')
    print(ret)