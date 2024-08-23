from tkinter import *

def click(event):
    global scvalue
    text=event.wedget.cget("text")
    print(text)

    if text=="=":
        pass
    if text=="c":
        pass
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root= Tk()
root.title("calculator")
root.geometry("300x350")
root.configure(bg="black")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=10,ipady=10)
var=IntVar
label=Label(root,text="",width=38,height=3,border=5).place(x=10,y=3)


button1=Button(root,text="c",width=8,height=2).place(x=10,y=70)
button2=Button(root,text="%",width=8,height=2).place(x=80,y=70)
button3=Button(root,text="/",width=8,height=2).place(x=150,y=70)
button4=Button(root,text="*",width=8,height=2).place(x=220,y=70)

button5=Button(root,text="9",width=8,height=2).place(x=10,y=120)
button6=Button(root,text="8",width=8,height=2).place(x=80,y=120)
button7=Button(root,text="7",width=8,height=2).place(x=150,y=120)
button8=Button(root,text="-",width=8,height=2).place(x=220,y=120)

button9=Button(root,text="6",width=8,height=2).place(x=10,y=170)
button10=Button(root,text="5",width=8,height=2).place(x=80,y=170)
button11=Button(root,text="4",width=8,height=2).place(x=150,y=170)
button12=Button(root,text="+",width=8,height=2).place(x=220,y=170)

button13=Button(root,text="3",width=8,height=2).place(x=10,y=220)
button14=Button(root,text="2",width=8,height=2).place(x=80,y=220)
button15=Button(root,text="1",width=8,height=2).place(x=150,y=220)
button16=Button(root,text="X",width=8,height=2).place(x=220,y=220)

button17=Button(root,text="0",width=8,height=2).place(x=10,y=270)
button18=Button(root,text=".",width=8,height=2).place(x=80,y=270)
button19=Button(root,text="00",width=8,height=2).place(x=150,y=270)
button20=Button(root,text="=",width=8,height=2).place(x=220,y=270)


root.mainloop()
