import tkinter
from tkinter import *

def add_digit(digit):
    calc.insert(END, digit)

def clear_last():
    current_value = calc.get()[:-1]
    calc.delete(0, END)
    calc.insert(0, current_value)

def clear_all():
    calc.delete(0, END)

def evaluate_expression():
    try:
        result = eval(calc.get())
        calc.delete(0, END)
        calc.insert(0, str(result))
    except Exception as e:
        calc.delete(0, END)
        calc.insert(0, "Error")

root = Tk()

calc = Entry(root, justify=RIGHT)
calc.grid(row=0, column=0, columnspan=3)

root.config(bg="#86F4FF")
root.title("Calculator")
root.geometry("400x400")

btn1 = Button(root, text="1", command=lambda: add_digit('1'))
btn1.grid(row=1, column=0, sticky="wens", padx=5, pady=5)

btn2 = Button(root, text="2", command=lambda: add_digit('2'))
btn2.grid(row=1, column=1, sticky="wens", padx=5, pady=5)

btn3 = Button(root, text="3", command=lambda: add_digit('3'))
btn3.grid(row=1, column=2, sticky="wens", padx=5, pady=5)

btn4 = Button(root, text="4", command=lambda: add_digit('4'))
btn4.grid(row=2, column=0, sticky="wens", padx=5, pady=5)

btn5 = Button(root, text="5", command=lambda: add_digit('5'))
btn5.grid(row=2, column=1, sticky="wens", padx=5, pady=5)

btn6 = Button(root, text="6", command=lambda: add_digit('6'))
btn6.grid(row=2, column=2, sticky="wens", padx=5, pady=5)

btn7 = Button(root, text="7", command=lambda: add_digit('7'))
btn7.grid(row=3, column=0, sticky="wens", padx=5, pady=5)

btn8 = Button(root, text="8", command=lambda: add_digit('8'))
btn8.grid(row=3, column=1, sticky="wens", padx=5, pady=5)

btn9 = Button(root, text="9", command=lambda: add_digit('9'))
btn9.grid(row=3, column=2, sticky="wens", padx=5, pady=5)

btn0 = Button(root, text="0", command=lambda: add_digit('0'))
btn0.grid(row=4, column=0, sticky="wens", padx=5, pady=5)

btn_clear = Button(root, text="C", command=clear_last)
btn_clear.grid(row=4, column=1, sticky="wens", padx=5, pady=5)

btn_add = Button(root, text="+", command=lambda: add_digit('+'))
btn_add.grid(row=5, column=1, sticky="wens", padx=5, pady=5)

btn_subtract = Button(root, text="-", command=lambda: add_digit('-'))
btn_subtract.grid(row=5, column=0, sticky="wens", padx=5, pady=5)

btn_equals = Button(root, text="=", command=evaluate_expression)
btn_equals.grid(row=4, column=2, sticky="wens", padx=5, pady=5)

btn_multiply = Button(root, text="*", command=lambda: add_digit('*'))
btn_multiply.grid(row=5, column=2, sticky="wens", padx=5, pady=5)

btn_divide = Button(root, text="/", command=lambda: add_digit('/'))
btn_divide.grid(row=6, column=1, sticky="wens", padx=5, pady=5)

for i in range(3):
    root.grid_columnconfigure(i, minsize=60)
    root.grid_rowconfigure(i, minsize=60)

root.mainloop()

