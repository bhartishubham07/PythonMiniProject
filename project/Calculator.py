import tkinter
def add():
    e3.delete(0, 'end')
    x = int(e1.get())
    y = int(e2.get())
    z = x+y
    e3.insert(0, str(z))

def sub():
    e3.delete(0, 'end')
    x = int(e1.get())
    y = int(e2.get())
    z = x-y
    e3.insert(0, str(z))

def mul():
    e3.delete(0, 'end')
    x = int(e1.get())
    y = int(e2.get())
    z = x*y
    e3.insert(0, str(z))

def div():
    e3.delete(0, 'end')
    x = int(e1.get())
    y = int(e2.get())
    z = x/y
    e3.insert(0, str(z))

def reset():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')

window = tkinter.Tk()
window.geometry("600x450")
window.title("Calculator")

l1 = tkinter.Label(text = "Enter First Number : ")
l2 = tkinter.Label(text = "Enter Second Number : ")
l3 = tkinter.Label(text = "Result : ")

e1 = tkinter.Entry()
e2 = tkinter.Entry()
e3 = tkinter.Entry()

b1 = tkinter.Button(text = "Addition", command=add)
b2 = tkinter.Button(text = "Substraction", command=sub)
b3 = tkinter.Button(text = "Multiplication", command=mul)
b4 = tkinter.Button(text = "Division", command=div)
b5 = tkinter.Button(text = "Reset", command=reset )

l1.place(x=100, y=100)
e1.place(x=230, y=100)

l2.place(x=100, y=150)
e2.place(x=230, y=150)

l3.place(x=100, y=200)
e3.place(x=230, y=200)

b1.place(x=100, y=300)
b2.place(x=180, y=300)
b3.place(x=280, y=300)
b4.place(x=390, y=300)
b5.place(x=245, y=370)

window.mainloop()