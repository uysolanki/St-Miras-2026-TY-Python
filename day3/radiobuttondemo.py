from tkinter import *
root = Tk()
root.geometry("400x350")
root.title("Post Graduation Form")
root.configure(bg="pink")

def pg():
    label2.configure(text=postGrad.get())
    
postGrad = StringVar(value="MCA SPPU")

label1=Label(root,text="masters",font=("Arial", 14, "bold"),fg="blue")
label1.place(x="90", y="30", width="150", height="30")

radio1 = Radiobutton(
    root,
    text="MCA",         #end user see beside the radio button
    variable=postGrad,
    value="MCA SPPU"    #programmer see beside the radio button
)

radio1.place(x="90", y="90", width="150", height="30")

radio2 = Radiobutton(
    root,
    text="MCS",         #end user see beside the radio button
    variable=postGrad,
    value="MCS SPPU"
)

radio2.place(x="90", y="140", width="150", height="30")

radio3 = Radiobutton(
    root,
    text="MBA",         #end user see beside the radio button
    variable=postGrad,
    value="MBA SPPU"
)

radio3.place(x="90", y="190", width="150", height="30")

button1=Button(root,text="Submit", font=("Arial", 14, "bold"),fg="blue",command=pg)
button1.place(x="90", y="240", width="100", height="30")

label2=Label(root,text="",font=("Arial", 14, "bold"),fg="blue")
label2.place(x="50", y="290", width="150", height="30")


root.mainloop()