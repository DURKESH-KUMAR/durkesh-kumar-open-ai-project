from tkinter import *
import pywhatkit

import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your perak os distribution will open sooner please wait ")

x.runAndWait()
import os
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
def graph():
    import os
    os.system("python pymatrixrain.py")
lbl=Button(root,text="PERAK OS DISTRIBUTION ",command=graph)
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="KILL",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT,padx=10)
def display():
    import os
    os.system("python audio.py")

btns=Button(root,text="AUDIO",command=display)
btns.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btns.pack(side=LEFT,padx=10)
img=PhotoImage(file="TEAM.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()
lbl1=Label(root,text="ENTER PASSWORD:")
lbl1.config(font=("callibri",24,"bold"),fg="green",bg="black")
lbl1.pack(padx=20,pady=20)

entry=Entry(root)
entry.config(font=("callibri",20,"bold"))
entry.pack(padx=10,pady=20)
def sample():
    x=entry.get()
    y=str(x)
    if(y=="2023"):
        import os
        #call core
        os.system("python core.py")
    
    

btn=Button(root,text="LOGIN",command=sample)
btn.config(font=("callibri",20,"bold"),bg="green",fg="black")
btn.pack(padx=100,pady=20)
root.mainloop()