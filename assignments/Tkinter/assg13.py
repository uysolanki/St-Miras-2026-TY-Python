from tkinter import *
from tkinter import messagebox

# Function to display alert message
def show_alert():
    messagebox.showinfo("Alert", "Button Pressed!")

# Create the main window
root = Tk()
root.title("Alert Message Example")
root.geometry("300x150")

# Create Button
Button(root, text="Click Me", command=show_alert).pack(pady=30)

# Run the application
root.mainloop()