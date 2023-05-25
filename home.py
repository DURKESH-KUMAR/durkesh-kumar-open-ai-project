from tkinter import *
import pywhatkit

import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your perak os home will open sooner please wait ")

x.runAndWait()
import os
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
def graph():
    import os
    os.system("python core.py")
lbl=Button(root,text="PERAK OS HOME",command=graph)
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="KILL",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT,padx=10)
def display():
    import os
    os.system("python time_1.py")

btns=Button(root,text="DATE",command=display)
btns.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btns.pack(side=LEFT,padx=10)

img=PhotoImage(file="home.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()
lbl2=Label(root,text="SELECT YOUR PASSION")
lbl2.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl2.pack(padx=20,pady=20)
#1
def display1():
    import os
    os.system("python chatgpt.py")
btn1=Button(root,text="GPT",command=display1)
btn1.config(font=("callibri",20,"bold"),fg="black",bg="yellow")
btn1.pack(side=LEFT,padx=10,pady=10)
#2
def display2():
    import os
    os.system("python wiki.py")
btn2=Button(root,text="WIKI",command=display2)
btn2.config(font=("callibri",20,"bold"),fg="black",bg="green")
btn2.pack(side=LEFT,padx=10,pady=10)
#3
def display3():
    import os
    os.system("python sos.py")
btn3=Button(root,text="SOS",command=display3)
btn3.config(font=("callibri",20,"bold"),fg="black",bg="green")
btn3.pack(side=LEFT,padx=10,pady=10)
#4
def display4():
    import os
    os.system("python searchai.py")
btn4=Button(root,text="SEARCH",command=display4)
btn4.config(font=("callibri",20,"bold"),fg="black",bg="green")
btn4.pack(side=LEFT,padx=10,pady=10)
#5
def display5():
    import os
    os.system("python skynet.py")
btn4=Button(root,text="SKYNET",command=display5)
btn4.config(font=("callibri",20,"bold"),fg="black",bg="yellow")
btn4.pack(side=LEFT,padx=10,pady=10)
#6
def display6():
    import os
    os.system("python imagesearchengine.py")
btn4=Button(root,text="IMAGE",command=display6)
btn4.config(font=("callibri",20,"bold"),fg="black",bg="green")
btn4.pack(side=LEFT,padx=10,pady=10)
#7
def display7():
    import os
    os.system("python bmi.py")
btn4=Button(root,text="BMI",command=display7)
btn4.config(font=("callibri",20,"bold"),fg="black",bg="green")
btn4.pack(side=LEFT,padx=10,pady=10)
#8
def display8():
    import os
    os.system("python calculator.py")
btn4=Button(root,text="MATH",command=display8)
btn4.config(font=("callibri",20,"bold"),fg="black",bg="green")
btn4.pack(side=LEFT,padx=10,pady=10)
#9
def display9():
    import os
    os.system("python bard.py")
btn4=Button(root,text="BARD",command=display9)
btn4.config(font=("callibri",20,"bold"),fg="black",bg="yellow")
btn4.pack(side=LEFT,padx=10,pady=10)
root.mainloop()