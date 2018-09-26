#coding=utf-8
from DbHelper import * 

def testDBHelper():
    dbhelper =  MysqlHelper(host='localhost',
        port = 3306,
        user='root',
        passwd='test1234',
        db ='fl_good',)
    
    version=dbhelper.getDBVersion()
    print("version=%s" %(version))

    data=dbhelper.descTable()
    print("data=%r" %(type(data)))
    for item in data:
        print("item=%r,%r" %(item[0],item[1]))


def createMapper(filename,data):
    filename = filename + ".java"
    with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        f.write("\n")
        f.write("\n")

def  test2():
    ss="titleCn,  titleEn,  img,  rating,  scoreCount,  year,  content,  tags,  url,  standard_definition_url,  high_definition_url,  wapUrl,  isEggHunt,  commonSpecial,  hotRanking,  directorId,  isTicket,  showCinemaCount,  showtimeCount,  showDay,  is3D,  isMAX,  isDMAX,  totalWinAward,  totalNominateAward,  directors,  actors,  imageCount,  images,  video,  videoId,  videoCount,  videos,  personCount"

    mm = ss.split(',')

    out=""
    for i in mm:
        m = i.strip()
        out =  out + '#{bean.'+m+'},'
    print(out)


if __name__  == '__main__':
    #testDBHelper()
    test2()
