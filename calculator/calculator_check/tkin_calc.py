from _ast import Lambda
from tkinter import *

root=Tk()
root.title("Image Insertion")
root.iconbitmap('calc.ico')
root.title("Calculator By Niraj")
root.geometry("361x381+500+200")

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math="add"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math="mul"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math="div"
    f_num = int(first_number)
    e.delete(0, END)

def button_Equals():
    second_number = e.get()
    e.delete(0, END)
    if math=="add":
       e.insert(0, f_num + int(second_number))
    if math == "sub":
        e.insert(0, f_num - int(second_number))
    if math == "mul":
        e.insert(0, f_num * int(second_number))
    if math == "div":
        e.insert(0, f_num / int(second_number))


data=StringVar()
e=Entry(root, justify="right", bd=29, bg="light green", font=("ariel", 20))
e.grid(row=0, columnspan=4)
button7=Button(root, text="7",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(7))
button7.grid(row=1, column=0)
button8=Button(root, text="8",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(8))
button8.grid(row=1, column=1)
button9=Button(root, text="9",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(9))
button9.grid(row=1, column=2)
button_clear=Button(root, text="clear",font=("Ariel",12,"bold"), bd=12, bg="brown", height=2, width=6,command=lambda:button_clear)
button_clear.grid(row=1, column=3)

button4=Button(root, text="4",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(4))
button4.grid(row=2, column=0)
button5=Button(root, text="5",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(5))
button5.grid(row=2, column=1)
button6=Button(root, text="6",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(6))
button6.grid(row=2, column=2)
button_add=Button(root, text="+",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick("+"))
button_add.grid(row=2, column=3)

button1=Button(root, text="1",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(1))
button1.grid(row=3, column=0)
button2=Button(root, text="2",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(2))
button2.grid(row=3, column=1)
button3=Button(root, text="3",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(3))
button3.grid(row=3, column=2)
button_sub=Button(root, text="-",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick("-"))
button_sub.grid(row=3, column=3)

button_0=Button(root, text="0",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick(0))
button_0.grid(row=4, column=0)
button_mul=Button(root, text="*",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick("*"))
button_mul.grid(row=4, column=1)
button_div=Button(root, text="/",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=lambda:buttonClick("/"))
button_div.grid(row=4, column=2)
button_Equals=Button(root, text="=",font=("Ariel",12,"bold"), bd=12, height=2, width=6,command=button_Equals)
button_Equals.grid(row=4, column=3)




root.mainloop()

