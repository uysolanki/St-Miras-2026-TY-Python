from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("400x200")
root.title("Digital Clock")


def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")

    label.configure(text=current_time)

    # Call show_time() again after 1000 milliseconds
    root.after(1000, show_time)


label = Label(
    root,
    font=("Arial", 40)
)

label.pack(pady=50)

show_time()

root.mainloop()