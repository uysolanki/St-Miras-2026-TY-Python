from tkinter import *
root = Tk()
root.geometry("500x200")
root.title("My Calculator")
root.configure(bg="pink")

def addition():
    number1=int(textbox1.get())
    number2=int(textbox2.get())
    number3=int(textbox3.get())
    #print(data)
    ans=number1+number2+number3
    label4.configure(text=ans)



label1=Label(root, text="Enter Number 1").grid(row=0, column=0)
textbox1=Entry(root)
textbox1.grid(row=0, column=1,padx=15)

label2=Label(root, text="Enter Number 2").grid(row=1, column=0, pady=15)
textbox2=Entry(root)
textbox2.grid(row=1, column=1,padx=15)

label3=Label(root, text="Enter Number 3").grid(row=2, column=0, pady=15)
textbox3=Entry(root)
textbox3.grid(row=2, column=1,padx=15)

button1=Button(root,text="Addition",command=addition).grid(row=3, column=1)
label4=Label(root, text="")
label4.grid(row=4, column=1, pady=15)

root.mainloop()


