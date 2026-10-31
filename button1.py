from tkinter import *
top = Tk()
top.geometry('600x400')
top.title('First Window')

b = Button(top,text = "My buttom")
b.place(relx=0.60,rely=0.50)
top.mainloop()