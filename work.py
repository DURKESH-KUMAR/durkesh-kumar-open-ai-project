from tkinter import *
import pywhatkit

import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your perak os work profile will open sooner please wait ")

x.runAndWait()
import os
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
def graph():
    import os
    os.system("python core.py")
lbl=Button(root,text="PERAK OS WORK PROFILE",command=graph)
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="KILL",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT,padx=10)

img=PhotoImage(file="work.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()
lbl2=Label(root,text="SELECT YOUR EXPLORE")
lbl2.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl2.pack(padx=20,pady=20)
def display1():
    import os
    os.system("python linkedin.py")
#1
btn1=Button(root,text="LINKED IN",command=display1)
btn1.config(font=("callibri",24,"bold"),fg="black",bg="green")
btn1.pack(side=LEFT,padx=100,pady=20)
#2
def display2():
    import webbrowser
    webbrowser.open("https://www.github.com")
btn2=Button(root,text="GITHUB",command=display2)
btn2.config(font=("callibri",24,"bold"),fg="black",bg="green")
btn2.pack(side=LEFT,padx=50,pady=20)
#3
def display3():
    import os
    os.system("python twitter.py")
btn3=Button(root,text="TWITTER",command=display3)
btn3.config(font=("callibri",24,"bold"),fg="black",bg="green")
btn3.pack(side=LEFT,padx=50,pady=20)
#4
def display4():
    import os
    os.system("python gmail.py")
btn4=Button(root,text="GMAIL",command=display4)
btn4.config(font=("callibri",24,"bold"),fg="black",bg="green")
btn4.pack(side=LEFT,padx=50,pady=20)
root.mainloop()