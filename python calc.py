from tkinter import *
import tkinter as tk

expression = ""

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def num(event):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equals():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

        expression = ""
    except:

        equation.set(" error ")
        expression = ""

def returnEquals(Event):
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def clearKey(event):
    global expression
    expression = ""
    equation.set("")    

root = Tk()
root.geometry("320x350")
root.resizable(width=False, height=False)
# set the title for GUI interface
root.title("Python Calculator")
#StringVar is variable class and instance is being made
equation = StringVar()
 #entry box
expression_field = Entry(root, textvariable=equation, font=('calibri 20'), state='disabled')

expression_field.grid(columnspan=8, column=1, ipady=20, ipadx=17.5)
#calculator buttons
#numbers    
button1 = Button(root, text=' 1 ', fg='black', bg='white',
                command=lambda: press(1), height=3, width=10).grid(row=3, column=1)
button2 = Button(root, text=' 2 ', fg='black', bg='white',
                command=lambda: press(2), height=3, width=10).grid(row=3, column=2)
button3 = Button(root, text=' 3 ', fg='black', bg='white',
                command=lambda: press(3), height=3, width=10).grid(row=3, column=3)
button4 = Button(root, text=' 4 ', fg='black', bg='white',
                command=lambda: press(4), height=3, width=10).grid(row=4, column=1)
button5 = Button(root, text=' 5 ', fg='black', bg='white',
                command=lambda: press(5), height=3, width=10).grid(row=4, column=2)
button6 = Button(root, text=' 6 ', fg='black', bg='white',
                command=lambda: press(6), height=3, width=10).grid(row=4, column=3)
button7 = Button(root, text=' 7 ', fg='black', bg='white',
                command=lambda: press(7), height=3, width=10).grid(row=5, column=1)
button8 = Button(root, text=' 8 ', fg='black', bg='white',
                command=lambda: press(8), height=3, width=10).grid(row=5, column=2)
button9 = Button(root, text=' 9 ', fg='black', bg='white',
                command=lambda: press(9), height=3, width=10).grid(row=5, column=3)
button0 = Button(root, text=' 0 ', fg='black', bg='white',
                command=lambda: press(0), height=3, width=10).grid(row=6, column=2)

#Operations
buttonDiv = Button(root, text=' / ', fg='black', bg='white',
                command=lambda: press("/"), height=3, width=10).grid(row=3, column=4)
buttonMin = Button(root, text=' - ', fg='black', bg='white',
                command=lambda: press("-"), height=3, width=10).grid(row=4, column=4)
buttonPlus = Button(root, text=' + ', fg='black', bg='white',
                command=lambda: press("+"), height=3, width=10).grid(row=5, column=4, columnspan=1, rowspan=1)
buttonEquals = Button(root, text=" = ", fg = 'black', bg='white',
                command=equals, height=3, width=10).grid(row=6, column=4)
buttonMul = Button(root, text="*", fg='black', bg='white',
                command=lambda: press("*"), height=3, width=10).grid(column=4, row=1)
clear = Button(root, text='All Clear', fg='black', bg='white',
                command=clear, height=3, width=10).grid(row=6, column='1')
Decimal= Button(root, text='.', fg='black', bg='white',
                command=lambda: press('.'), height=3, width=10).grid(row=6, column=3)
buttonOpenBracket= Button(root, text='(', fg='black', bg='white',
                command=lambda: press('('), height=3, width=10).grid(row=1, column=1)
buttonClosedBracket= Button(root, text=')', fg='black', bg='white',
                command=lambda: press(')'), height=3, width=10).grid(row=1, column=2)
buttonExponent= Button(root, text='^', fg='black', bg='white',
                command=lambda: press('**'), height=3, width=10).grid(row=1, column=3)

#Key Binds
enterKey = root.bind('<Return>', returnEquals)
keyOne = root.bind('1', lambda event: press('1'))
keyTwo = root.bind('2', lambda event: press('2'))
keyThree = root.bind('3', lambda event: press('3'))
keyFour = root.bind('4', lambda event: press('4'))
keyFive = root.bind('5', lambda event: press('5'))
keySix = root.bind('6', lambda event: press('6'))
keySeven = root.bind('7', lambda event: press('7'))
keyEight = root.bind('8', lambda event: press('8'))
keyNin = root.bind('9', lambda event: press('9'))
keyZer = root.bind('0', lambda event: press('0'))
keyPlus = root.bind('+', lambda event: press('+'))
keySub = root.bind('-', lambda event: press('-'))
keyDiv = root.bind('/', lambda event: press('/'))
keyDec = root.bind('.', lambda event: press('.'))
keyMul = root.bind('*', lambda event: press('*'))
keyOpenBracket = root.bind('(', lambda event: press('('))
keyCloseBrack = root.bind(')', lambda event: press(')'))
keyIndex = root.bind('^', lambda event: press('**'))
keyClear = root.bind('<Escape>', clearKey)
root.mainloop()