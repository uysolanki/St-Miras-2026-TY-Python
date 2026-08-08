from tkinter import *
root = Tk()
root.geometry("500x200")
root.title("Login Form")
root.configure(bg="pink")

def show():
    data=textbox1.get()
    #print(data)
    label2.configure(text=data)

label1=Label(root,text="Username")
label1.pack()
textbox1=Entry(root)
textbox1.pack()
button1=Button(root,text="Display",command=show)
button1.pack()
label2=Label(root,text="",font=("Arial", 18, "bold"),fg="blue")
label2.pack()

root.mainloop()


