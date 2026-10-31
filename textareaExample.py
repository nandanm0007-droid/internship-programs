from tkinter import *
import tkinter as tk

root = Tk()

# specify size of window.
root.geometry("750x570")

# Create text widget and specify size.
T = Text(root, height=15, width=52)

# Create Label
l = Label(root, text="Textarea Example")
l.config(font=("Courier", 14))

Fact = """hi good evening
may i help. this is nandan"""

def nextfunction():
    nexttext = """hi good morning
the is my next text."""
    T.delete("1.0", tk.END)
    T.insert(tk.END, nexttext)

# Create button for next text.
b1 = Button(root, text="Next", command=nextfunction)

# Create an Exit button.
b2 = Button(root, text="Exit", command=root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()