from tkinter import *
root = Tk()
root.geometry("350x310")
root.title("Login Form")
root.configure(bg="pink")

label1=Label(root,text="username", font=("Arial", 14, "bold"),fg="blue")
label1.place(x="30", y="100", width="100", height="30",)

textbox1=Entry(root,font=("Arial", 14, "bold"),fg="blue")
textbox1.place(x="150", y="100", width="200", height="30")

label2=Label(root,text="password",font=("Arial", 14, "bold"),fg="blue")
label2.place(x="30", y="200", width="100", height="30")

textbox2=Entry(root, font=("Arial", 14, "bold"),fg="blue")
textbox2.place(x="150",y="200", width="200", height="30")

button1=Button(root,text="login", font=("Arial", 14, "bold"),fg="blue",command="login")
button1.place(x="150", y="270", width="100", height="30")

root.mainloop()