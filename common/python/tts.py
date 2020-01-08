import win32com.client as wincl
from tkinter import *
def text2Speech(): 
	text = e.get() 
	speak = wincl.Dispatch("SAPI.SpVoice") 
	speak.Speak(text)
#window configs
tts = Tk()
tts.wm_title("Text to Speech")
tts.geometry("600x400")
tts.config(background="#708090")

f=Frame(tts,height=600,width=800,bg="#bebebe")
f.grid(row=0,column=0,padx=10,pady=5)
lbl=Label(f,text="输入需要转换的文本 : ")
lbl.grid(row=1,column=0,padx=10,pady=2)
e=Entry(f,width=80)
e.grid(row=2,column=0,padx=10,pady=2)
btn=Button(f,text="语音输出",command=text2Speech)
btn.grid(row=3,column=0,padx=20,pady=10)
tts.mainloop()

