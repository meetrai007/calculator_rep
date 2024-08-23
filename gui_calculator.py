from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(scvalue.get()))
            scvalue.set(result)
        except Exception as e:
            scvalue.set("Error")
    elif text == "c":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.title("Calculator")
root.geometry("350x400")
root.configure(bg="black")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8, padx=10, pady=10)

b = Button(root, text="9", width=8, height=2)
b.grid(row=1, column=1, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="8", width=8, height=2)
b.grid(row=1, column=2, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="7", width=8, height=2)
b.grid(row=1, column=3, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="/", width=8, height=2)
b.grid(row=1, column=4, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="6", width=8, height=2)
b.grid(row=2, column=1, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="5", width=8, height=2)
b.grid(row=2, column=2, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="4", width=8, height=2)
b.grid(row=2, column=3, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="*", width=8, height=2)
b.grid(row=2, column=4, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="3", width=8, height=2)
b.grid(row=3, column=1, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="2", width=8, height=2)
b.grid(row=3, column=2, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="1", width=8, height=2)
b.grid(row=3, column=3, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="+", width=8, height=2)
b.grid(row=3, column=4, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text=".", width=8, height=2)
b.grid(row=4, column=1, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="0", width=8, height=2)
b.grid(row=4, column=2, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="%", width=8, height=2)
b.grid(row=4, column=3, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="-", width=8, height=2)
b.grid(row=4, column=4, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="00", width=8, height=2)
b.grid(row=5, column=1, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="c", width=8, height=2)
b.grid(row=5, column=2, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(root, text="=", width=20, height=2)
b.grid(row=5, column=3,columnspan=2, padx=10, pady=10)
b.bind("<Button-1>", click)

root.mainloop()
