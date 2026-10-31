import tkinter as tk

def show_selection():
    selected = var.get()
    label_result.config(text=f"You selected: {selected}")

# Create main window
root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

# Variable to hold selected value
var = tk.StringVar(value="male")

# Create radio buttons
radio1 = tk.Radiobutton(root, text="male", variable=var, value="male")
radio2 = tk.Radiobutton(root, text="Female", variable=var, value="female")
radio3 = tk.Radiobutton(root, text="Others", variable=var, value="Others")

# Place radio buttons
radio1.pack(anchor="w")
radio2.pack(anchor="w")
radio3.pack(anchor="w")

# Button to show selection
btn_show = tk.Button(root, text="Show Selection", command=show_selection)
btn_show.pack(pady=10)

# Label to display result
label_result = tk.Label(root, text="You selected: ")
label_result.pack()

# Run the application
root.mainloop()