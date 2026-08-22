from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Simple Calculator")


def calculate():
    number1 = float(textbox1.get())
    number2 = float(textbox2.get())

    operation = choice.get()

    if operation == 1:
        result = number1 + number2

    elif operation == 2:
        result = number1 - number2

    elif operation == 3:
        result = number1 * number2

    elif operation == 4:
        if number2 == 0:
            result = "Cannot divide by zero"
        else:
            result = number1 / number2

    label4.configure(text="Result = " + str(result))


# Number 1
label1 = Label(root, text="Enter Number 1")
label1.grid(row=0, column=0, padx=10, pady=15)

textbox1 = Entry(root)
textbox1.grid(row=0, column=1)


# Number 2
label2 = Label(root, text="Enter Number 2")
label2.grid(row=1, column=0, padx=10, pady=15)

textbox2 = Entry(root)
textbox2.grid(row=1, column=1)


# Radio buttons
choice = IntVar()

radio1 = Radiobutton(
    root,
    text="Addition",
    variable=choice,
    value=1
)
radio1.grid(row=2, column=0)

radio2 = Radiobutton(
    root,
    text="Subtraction",
    variable=choice,
    value=2
)
radio2.grid(row=2, column=1)

radio3 = Radiobutton(
    root,
    text="Multiplication",
    variable=choice,
    value=3
)
radio3.grid(row=3, column=0)

radio4 = Radiobutton(
    root,
    text="Division",
    variable=choice,
    value=4
)
radio4.grid(row=3, column=1)


# Calculate button
button = Button(
    root,
    text="Calculate",
    command=calculate
)
button.grid(row=4, column=1, pady=20)


# Result
label4 = Label(root, text="")
label4.grid(row=5, column=1)


root.mainloop()