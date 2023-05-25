from tkinter import *

import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your metamask will open sooner please wait ")

x.runAndWait()
import os
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
lbl=Label(root,text="PERAK OS DISTRIBUTION METAMASK")
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT)
img=PhotoImage(file="metamask.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=500)
lbl1.pack()
def sample():
    import webbrowser
    webbrowser.open("https://portfolio.metamask.io")
    

btn=Button(root,text="START",command=sample)
btn.config(font=("callibri",20,"bold"),bg="green",fg="black")
btn.pack(padx=100,pady=40)
root.mainloop()