from tkinter import *
root = Tk()
root.geometry("500x200")
root.title("Login Form")
root.configure(bg="red")
label1 = Label(root, text="Enter Name")
label1.pack()

label2 = Label(root, text="Enter Password", font=("Arial", 18, "bold"),fg="blue")
label2.pack(side="left",pady=10)
root.mainloop()


