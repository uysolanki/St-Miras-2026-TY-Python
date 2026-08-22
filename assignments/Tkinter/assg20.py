from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("Sentence Alteration")


def alter_sentence():
    sentence = textbox.get()

    result = ""

    for ch in sentence:
        if ch == " ":
            result = result + "*"
        elif ch.isalpha():
            result = result + ch.swapcase()
        elif ch.isdigit():
            result = result + "?"
        else:
            result = result + ch

    label3.configure(text=result)


label1 = Label(root, text="Enter Sentence")
label1.pack(pady=10)

textbox = Entry(root, width=50)
textbox.pack()

button = Button(
    root,
    text="Alter Sentence",
    command=alter_sentence
)
button.pack(pady=15)

label2 = Label(root, text="Result:")
label2.pack()

label3 = Label(root, text="")
label3.pack(pady=10)

root.mainloop()