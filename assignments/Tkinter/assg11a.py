from tkinter import *

# Function to display selected option
def show():
    # print("Selected Option:", var.get())
    label.config(text=f"Selected Option: {var.get()}")

# Create main window
root = Tk()
root.title("Radio Button Example")
root.geometry("300x250")

# Variable to store selected value
var = StringVar()
var.set("Python")      # Default selection

# Create Radio Buttons
r1=Radiobutton(root, text="Python", variable=var,
            value="Python", command=show)
r1.place(x=50, y=50, width=100, height=30)


r2=Radiobutton(root, text="Java", variable=var,
            value="Java", command=show)
r2.place(x=50, y=100, width=100, height=30)

r3=Radiobutton(root, text="Cpp", variable=var,
            value="C++", command=show)
r3.place(x=50, y=150, width=100, height=30)

label=Label(root, text="")
label.place(x=50, y=200, width=150, height=30)

root.mainloop()