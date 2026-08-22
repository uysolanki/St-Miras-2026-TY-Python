from tkinter import *
from datetime import date

root = Tk()
root.geometry("400x250")
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


label1 = Label(root, text="Enter Date of Birth")
label1.pack(pady=10)

label2 = Label(root, text="Day")
label2.pack()

day = Entry(root, width=10)
day.pack()

label3 = Label(root, text="Month")
label3.pack()

month = Entry(root, width=10)
month.pack()

label4 = Label(root, text="")
label4.pack(pady=10)

label5 = Label(root, text="Year")
label5.pack()

year = Entry(root, width=10)
year.pack()

button = Button(root, text="Calculate Age", command=calculate_age)
button.pack(pady=10)

root.mainloop()