import tkinter as tk
from tkinter import messagebox

def addition():
    a=int(entery.get())
    b=int(entery2.get())
    c=a+b
    print(c)
def sub():
    a=int(entery.get())
    b=int(entery2.get())
    c=a-b
    print(c)
def multiply():
    a=int(entery.get())
    b=int(entery2.get())
    c=a*b
    print(c)


root= tk.Tk()
root.title("calculator")
root.geometry("300x400")

var=tk.IntVar
entery=tk.Entry(root)
entery.pack()
entery2=tk.Entry(root)
entery2.pack()

button=tk.Button(root,text="add",command=addition)
button.pack()
button2=tk.Button(root,text="sub",command=sub)
button2.pack()
button3=tk.Button(root,text="mul",command=multiply)
button3.pack()

root.mainloop()
