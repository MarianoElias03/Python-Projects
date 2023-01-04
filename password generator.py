from tkinter import *
import string
from secrets import choice
from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk
from tkinter.constants import END

def charLength(e):
   pasLength.delete(0,"end")

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = ['!', '@', "#", "$", "%", "^", "&", "*", "(", ")"]
characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*()')

def genRandPas():
        passwordGen.delete(0, END)
        global feedback
        try:
            passwordLength = int(pasLength.get())
            feedback.destroy()
            data = uppercase + lowercase + numbers + symbols
            password = ''.join(choice(data) for _ in range(passwordLength))
            passwordGen.insert(0, password)
        except ValueError:
            feedback = Label(root, fg="red", text='Please enter number of characters required')
            feedback.pack()
root = Tk()
root.geometry('500x150')
root.title("Password Generator")
 #-----------------------------------------------------------------------------------root
feedback = Label(root)
pasLength = Entry(root, font=('calibri 20'))
passwordGen = Entry(root, text='', width='30', font=('calibri 20'))
pasGenBtn = Button(root, width=20, height = 2, text = 'Generate Password', command=genRandPas)
#**************************************************
pasLength.insert(0, "how many characters?")
pasLength.bind("<FocusIn>", charLength)
#**************************************************
pasGenBtn.pack()
pasLength.pack()
passwordGen.pack()
root.mainloop()