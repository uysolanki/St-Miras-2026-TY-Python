from tkinter import *
root = Tk()
root.geometry("400x350")
root.title("Post Graduation Form")
root.configure(bg="pink")

def skill():
    result=""
    if cProg.get():
        result=result+" C "
    if javaProg.get():
            result=result+" Java "
    if pythonProg.get():
            result=result+" Python "
    label2.configure(text=result)
    
cProg = BooleanVar()
javaProg =BooleanVar()
pythonProg =BooleanVar()

label1=Label(root,text="masters",font=("Arial", 14, "bold"),fg="blue")
label1.place(x="90", y="30", width="150", height="30")

check1 = Checkbutton(
    root,
    text="C",           #end user see beside the radio button
    variable=cProg
               #programmer see beside the radio button
)

check1.place(x="90", y="90", width="150", height="30")

check2 = Checkbutton(
    root,
    text="Java",         #end user see beside the radio button
    variable=javaProg
)

check2.place(x="90", y="140", width="150", height="30")

check3 = Checkbutton(
    root,
    text="Python",         #end user see beside the radio button
    variable=pythonProg
)

check3.place(x="90", y="190", width="150", height="30")

button1=Button(root,text="Submit", font=("Arial", 14, "bold"),fg="blue",command=skill)
button1.place(x="90", y="240", width="100", height="30")

label2=Label(root,text="",font=("Arial", 14, "bold"),fg="blue")
label2.place(x="50", y="290", width="150", height="30")


root.mainloop()