import os
import re

def D(*kwargs):
    print(*kwargs)


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
    
    todo,done,released = getNotesDone("F:\\workspace\\tech_note_blog\\common")
    
    #print(todo)
    print(done)
    #print(released)

    print('num of todo: %d ' %(len(todo)))
    print('num of done: %d ' %(len(done)))
    print('num of released: %d ' %(len(released)))