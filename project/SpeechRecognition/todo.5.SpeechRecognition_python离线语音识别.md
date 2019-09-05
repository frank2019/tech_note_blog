



安装SpeechRecognition模块
使用recognize_sphinx()，



安装PocketSphinx

```
pip  install  PocketSphinx
```



报错

```ini
Failed to build PocketSphinx
Installing collected packages: PocketSphinx
  Running setup.py install for PocketSphinx ... error
    Complete output from command "D:\Program Files (x86)\anaconda3\python.exe" -u -c "import setuptools, tokenize;__file__='C:\\Users\\XIAXUE~1\\AppData\\Local\\Temp\\pip-install-f_ed7kqi\\PocketSphinx\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\XIAXUE~1\AppData\Local\Temp\pip-record-ddrvvanu\install-record.txt --single-version-externally-managed --compile:
    running install
    running build_ext
    building 'sphinxbase._sphinxbase' extension
    swigging deps/sphinxbase/swig/sphinxbase.i to deps/sphinxbase/swig/sphinxbase_wrap.c
    swig.exe -python -modern -threads -Ideps/sphinxbase/include -Ideps/sphinxbase/include/sphinxbase -Ideps/sphinxbase/include/win32 -Ideps/sphinxbase/swig -outdir sphinxbase -o deps/sphinxbase/swig/sphinxbase_wrap.c deps/sphinxbase/swig/sphinxbase.i
    error: command 'swig.exe' failed: No such file or directory
```

解决



需要安装swig

1.下载Swig for Windows：http://www.swig.org/download.html
2 解压 .zip 文件到目录，比如：D:\backupsoftware

3 添加环境变量到path， 比如： D:\backupsoftware\swigwin-2.0.9
4. Python
PYTHON_INCLUDE : Set this to the directory that contains Python.h
PYTHON_LIB : Set this to the python library including path for linking

Example using Python 2.1.1:
PYTHON_INCLUDE: D:\python21\include
PYTHON_LIB: D:\python21\libs\python21.lib
http://www.swig.org/download.html

备注

`C` 和 `C++` 被公认为（理当如此）创建高性能代码的首选平台。对开发人员的一个常见要求是向脚本语言接口公开 `C/C++` 代码，这正是 Simplified Wrapper and Interface Generator (SWIG) 的用武之地。SWIG 允许您向广泛的脚本语言公开 `C/C++` 代码，包括 Ruby、Perl、Tcl 和 Python等。







```python
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
print(r)
harvard = sr.AudioFile('input.wav')
print(harvard)
with harvard as source:
    audio = r.record(source)
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
```



## 参考链接

1. [win+python实现离线语音识别](https://blog.csdn.net/weixin_40490238/article/details/84841825)

1.https://github.com/Uberi/speech_recognition 
2.https://realpython.com/python-speech-recognition/ 
3.http://www.mamicode.com/info-detail-93746.html 
4,https://blog.csdn.net/qiaocuiyu/article/details/52093509 
5.http://blog.itpub.net/16582684/viewspace-1243341/