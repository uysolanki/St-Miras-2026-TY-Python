from tkinter import *

root = Tk()
root.geometry("400x250")
root.title("Checkbox Demo")


def show_selection():
    result = ""

    if java.get():
        result = result + "Java "

    if python.get():
        result = result + "Python "

    if javascript.get():
        result = result + "JavaScript "

    label4.configure(text="Selected: " + result)


java = BooleanVar()
python = BooleanVar()
javascript = BooleanVar()


label1 = Label(root, text="Select Your Skills")
label1.pack(pady=10)


check1 = Checkbutton(
    root,
    text="Java",
    variable=java
)
check1.pack()


check2 = Checkbutton(
    root,
    text="Python",
    variable=python
)
check2.pack()


check3 = Checkbutton(
    root,
    text="JavaScript",
    variable=javascript
)
check3.pack()


button = Button(
    root,
    text="Show Selection",
    command=show_selection
)
button.pack(pady=15)


label4 = Label(root, text="")
label4.pack()


root.mainloop()