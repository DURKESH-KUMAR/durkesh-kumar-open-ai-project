from tkinter import *
import pywhatkit

import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your wiki ai will open sooner please wait ")

x.runAndWait()
import os
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
lbl=Label(root,text="PERAK OS DISTRIBUTION WIKI AI")
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT)
img=PhotoImage(file="wiki.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()
lbl1=Label(root,text="SEARCH ANYTHING:")
lbl1.config(font=("callibri",24,"bold"),fg="green",bg="black")
lbl1.pack(padx=20,pady=20)

entry=Entry(root)
entry.config(font=("callibri",20,"bold"))
entry.pack(padx=10,pady=20)
def sample():
    import wikipedia
    y=entry.get()
    z=wikipedia.summary(str(y),sentences=2)
    x=pyttsx3.init()
    x.setProperty("rate",125)
    x.say("you entered"+y+"hence the answer is"+z)
    
    x.runAndWait()

    
    

btn=Button(root,text="START",command=sample)
btn.config(font=("callibri",20,"bold"),bg="green",fg="black")
btn.pack(padx=100,pady=20)
root.mainloop()