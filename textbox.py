from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win = Tk()
win.geometry("750x250")
def get_value():
    e_text = entry.get()
    messagebox.showinfo('You Typed',e_text)

label1 = ttk.Label(win, text="Textbox example", font = ('Century 35 bold'))
label1.pack(pady=30)
entry = ttk.Entry(win,font=('Century 12 bold'),width=40)
entry.pack(pady=30)
button = ttk.Button(win,text="Submit",command = get_value)
button.pack()
win.mainloop()