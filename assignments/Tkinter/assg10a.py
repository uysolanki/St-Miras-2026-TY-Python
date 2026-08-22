from tkinter import *

# Create main window
root = Tk()
root.title("Text Box Example")
root.geometry("300x200")
root.configure(bg="red")
label1=Label(root, text="Name")
label1.grid(row=0, column=0, padx=10, pady=5)

entry1=Entry(root)
entry1.grid(row=0, column=1)

label2=Label(root, text="Age")
label2.grid(row=1, column=0, padx=10, pady=5)
entry2=Entry(root)
entry2.grid(row=1, column=1)

label3=Label(root, text="City")
label3.grid(row=2, column=0, padx=10, pady=5)
entry3=Entry(root)
entry3.grid(row=2, column=1)

root.mainloop()