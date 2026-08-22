from tkinter import *
from tkinter import ttk
from datetime import date

root = Tk()
root.geometry("450x250")
root.title("Age Calculator")


def calculate_age():
    dob = date(
        int(year.get()),
        int(month.get()),
        int(day.get())
    )

    today = date.today()

    age = today.year - dob.year

    label4.configure(text="Your Age is: " + str(age))


# Day
label1 = Label(root, text="Day")
label1.grid(row=0, column=0, padx=10, pady=20)

day = ttk.Combobox(root, values=list(range(1, 32)), width=10)
day.grid(row=0, column=1)
day.set("Select Day")


# Month
label2 = Label(root, text="Month")
label2.grid(row=0, column=2, padx=10)

month = ttk.Combobox(root, values=list(range(1, 13)), width=10)
month.grid(row=0, column=3)
month.set("Select Month")


# Year
label3 = Label(root, text="Year")
label3.grid(row=1, column=0, padx=10, pady=20)

year = ttk.Combobox(
    root,
    values=list(range(1950, date.today().year + 1)),
    width=10
)
year.grid(row=1, column=1)
year.set("Select Year")


# Button
button = Button(
    root,
    text="Calculate Age",
    command=calculate_age
)
button.grid(row=2, column=1, pady=20)


# Result
label4 = Label(root, text="")
label4.grid(row=3, column=1)


root.mainloop()