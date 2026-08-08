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
label1.pack()
textbox1=Entry(root)
textbox1.pack()
button1=Button(root,text="Calculate Square",command=square)
button1.pack()
label2=Label(root,text="",font=("Arial", 18, "bold"),fg="blue")
label2.pack()

root.mainloop()


