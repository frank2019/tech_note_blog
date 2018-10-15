from tomd import Tomd

def htmlToMd(htmlFile,mdFile) :
    print(htmlFile)
    with open(htmlFile, 'r', encoding="utf-8") as f:
	    contents = f.read()
    f.close()

    #print(contents)
    md = Tomd(contents).markdown
    #print(md)

    with open(mdFile, 'w', encoding="utf-8") as f:
	    f.write(md)
    f.close()
    

    

if __name__ == '__main__':
    htmlToMd("22.html","nihao.md")