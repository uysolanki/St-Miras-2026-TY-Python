from tkinter import *
root = Tk()
root.geometry("500x200")
root.title("Login Form")
root.configure(bg="pink")

def square():
    number=int(textbox1.get())
    #print(data)
    ans=number*number
    label2.configure(text=ans)

label1=Label(root,text="Enter a Number")
label1.grid(row=1, column=1)
textbox1=Entry(root)
textbox1.grid(row=1, column=2, padx=15, columnspan=2)
button1=Button(root,text="Calculate Square",command=square)
button1.grid(row=2, column=1, columnspan=3)
label2=Label(root,text="",font=("Arial", 18, "bold"),fg="blue")
label2.grid(row=3, column=1, columnspan=3)

root.mainloop()


