from tkinter import *

# Create main window
root = Tk()
root.title("Text Box Example")
root.geometry("300x200")
root.configure(bg="red")
Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
Entry(root).grid(row=0, column=1)

Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5)
Entry(root).grid(row=1, column=1)

Label(root, text="City").grid(row=2, column=0, padx=10, pady=5)
Entry(root).grid(row=2, column=1)

root.mainloop()