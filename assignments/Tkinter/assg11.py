from tkinter import *

# Function to display selected option
def show():
    print("Selected Option:", var.get())

# Create main window
root = Tk()
root.title("Radio Button Example")
root.geometry("300x200")

# Variable to store selected value
var = StringVar()
var.set("Python")      # Default selection

# Create Radio Buttons
Radiobutton(root, text="Python", variable=var,
            value="Python", command=show).pack(anchor=W)

Radiobutton(root, text="Java", variable=var,
            value="Java", command=show).pack(anchor=W)

Radiobutton(root, text="Cpp", variable=var,
            value="C++", command=show).pack(anchor=W)

root.mainloop()