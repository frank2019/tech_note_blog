



安装SpeechRecognition模块
使用recognize_sphinx()，



安装PocketSphinx

```
pip  install  PocketSphinx
```



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