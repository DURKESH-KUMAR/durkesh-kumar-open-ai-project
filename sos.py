from tkinter import *
import pywhatkit

import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your save my soal will open sooner please wait ")

x.runAndWait()
import os
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
lbl=Label(root,text="PERAK OS DISTRIBUTION SOS")
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT)
img=PhotoImage(file="sos.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()
lbl1=Label(root,text="ENTER THE TIMING:")
lbl1.config(font=("callibri",24,"bold"),fg="green",bg="black")
lbl1.pack(padx=20,pady=20)

entry=Entry(root)
entry.config(font=("callibri",10,"bold"))
entry.pack(padx=10,pady=10)
entry1=Entry(root)
entry1.config(font=("callibri",10,"bold"))
entry1.pack(padx=10,pady=10)
def sample():
    x=entry.get()
    a=entry1.get()
    y=int(x)
    z=int(a)
    pywhatkit.sendwhatmsg("+919442326609","their is an emergency",y,z)
    
    

btn=Button(root,text="SAVE ME",command=sample)
btn.config(font=("callibri",20,"bold"),bg="green",fg="black")
btn.pack(padx=100,pady=20)
root.mainloop()