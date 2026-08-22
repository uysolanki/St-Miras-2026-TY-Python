from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Number Checking")


def check_number():
    n = int(textbox.get())

    if choice.get() == 1:
        # Prime Number
        if n < 2:
            result = "Not a Prime Number"
        else:
            flag = True

            for i in range(2, n):
                if n % i == 0:
                    flag = False
                    break

            if flag:
                result = "Prime Number"
            else:
                result = "Not a Prime Number"

    elif choice.get() == 2:
        # Perfect Number
        sum = 0

        for i in range(1, n):
            if n % i == 0:
                sum = sum + i

        if sum == n:
            result = "Perfect Number"
        else:
            result = "Not a Perfect Number"

    elif choice.get() == 3:
        # Armstrong Number
        temp = n
        sum = 0
        digits = len(str(n))

        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** digits
            temp = temp // 10

        if sum == n:
            result = "Armstrong Number"
        else:
            result = "Not an Armstrong Number"

    label4.configure(text=result)


label1 = Label(root, text="Enter Number")
label1.pack(pady=10)

textbox = Entry(root, width=20)
textbox.pack()


choice = IntVar()

radio1 = Radiobutton(
    root,
    text="Prime",
    variable=choice,
    value=1
)
radio1.pack()

radio2 = Radiobutton(
    root,
    text="Perfect",
    variable=choice,
    value=2
)
radio2.pack()

radio3 = Radiobutton(
    root,
    text="Armstrong",
    variable=choice,
    value=3
)
radio3.pack()


button = Button(
    root,
    text="Check",
    command=check_number
)
button.pack(pady=10)


label4 = Label(root, text="")
label4.pack()

root.mainloop()