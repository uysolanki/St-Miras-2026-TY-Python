from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Uppercase Converter")

def convert_upper():
    data = textbox.get()
    result = data.upper()
    label2.configure(text=result)

label1 = Label(root, text="Enter String")
label1.pack(pady=10)

textbox = Entry(root, width=30)
textbox.pack()

button = Button(root, text="Convert to Uppercase", command=convert_upper)
button.pack(pady=10)

label2 = Label(root, text="")
label2.pack(pady=10)

root.mainloop()