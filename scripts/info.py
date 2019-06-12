import datetime
import os

def get_day_info():
    weekth = datetime.datetime.now().isocalendar()
    print(weekth)
    #str = input("Press any key to quit: ");
    #print ("%s", str)

def execCmd(cmd):  
    r = os.popen(cmd)  
    text = r.read()  
    r.close()  
    return text  


def do_git_pull():
    repo_dir_home = 'F:\\workspace\\tech_note_blog'
    repo_dir_work = 'D:\\MoreBetter\\tech_note_blog'

    if os.path.exists(repo_dir_home):
        repo_dir =  repo_dir_home
    elif os.path.exists(repo_dir_work):
        repo_dir = repo_dir_work
    else :
        print('repo dir do net exist')
        return 

    
    cmd_git_status='git -C ' + repo_dir + ' status'
    cmd_git_pull = 'git -C ' + repo_dir + ' pull'
    #os.system("git  -C F:\\workspace\\tech_note_blog status")
    print(cmd_git_pull)
    ret = execCmd(cmd_git_pull)
    print(ret)

if __name__ == '__main__':
    get_day_info()
    do_git_pull()