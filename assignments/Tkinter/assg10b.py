from tkinter import *

# Create main window
root = Tk()
root.title("Text Box Example")
root.geometry("400x300")
root.configure(bg="red")
label1=Label(root, text="Name")
label1.place(x=50, y=50, width=100, height=30)

entry1=Entry(root)
entry1.place(x=200, y=50, width=100, height=30)

label2=Label(root, text="Age")
label2.place(x=50, y=100, width=100, height=30)
entry2=Entry(root)
entry2.place(x=200, y=100, width=100, height=30)

label3=Label(root, text="City")
label3.place(x=50, y=150, width=100, height=30)
entry3=Entry(root)
entry3.place(x=200, y=150, width=100, height=30)

root.mainloop()