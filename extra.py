from tkinter import *
import pywhatkit

import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your perak os extra tenchnology will open sooner please wait ")

x.runAndWait()
import os
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
def graph():
    import os
    os.system("python core.py")
lbl=Button(root,text="PERAK OS EXPLORE ",command=graph)
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="KILL",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT,padx=10)

img=PhotoImage(file="extra.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()
lbl2=Label(root,text="SELECT YOUR EXPLORE")
lbl2.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl2.pack(padx=20,pady=20)
def display1():
    import os
    os.system("python metamask.py")
#1
btn1=Button(root,text="METAMASK",command=display1)
btn1.config(font=("callibri",24,"bold"),fg="black",bg="green")
btn1.pack(side=LEFT,padx=100,pady=20)
#2
def display2():
    import os
    os.system("python googlemap.py")
btn2=Button(root,text="  EARTH ",command=display2)
btn2.config(font=("callibri",24,"bold"),fg="black",bg="green")
btn2.pack(side=LEFT,padx=50,pady=20)
#3
def display3():
    import os
    os.system("python windows11.py")
btn3=Button(root,text="WINDOWS 11",command=display3)
btn3.config(font=("callibri",24,"bold"),fg="black",bg="green")
btn3.pack(side=LEFT,padx=50,pady=20)
#4
def display4():
    import os
    os.system("shutdown /s /t 1")
btn4=Button(root,text=" DESTROY ",command=display4)
btn4.config(font=("callibri",24,"bold"),fg="black",bg="green")
btn4.pack(side=LEFT,padx=50,pady=20)
root.mainloop()