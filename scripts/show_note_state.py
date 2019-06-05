import os

def D(*kwargs):
    print(*kwargs)


def getNotesDone(target_dir):
    #D("this is test %s" %(target_dir))
    for dirpath,dirnames,filenames in os.walk(target_dir):
        for file in filenames:
            fullpath=os.path.join(dirpath,file)
            #print (fullpath)
            print (file)

if __name__ == '__main__':
    getNotesDone("D:\\MoreBetter\\tech_note_blog\\common\\3DCamera")