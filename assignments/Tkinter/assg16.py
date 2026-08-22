from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Text Widget Demo")

text = Text(root, width=50, height=8)
text.pack(pady=20)

def insert_beginning():
    text.insert("1.0", "Hello ")

def insert_current():
    text.insert(INSERT, "Python ")

def delete_first_last():
    # Delete first character
    text.delete("1.0", "1.1")

    # Delete last character
    text.delete("end-2c", "end-1c")


Button(root, text="Insert at Beginning",
       command=insert_beginning).pack(pady=5)

Button(root, text="Insert at Current Position",
       command=insert_current).pack(pady=5)

Button(root, text="Delete First & Last Character",
       command=delete_first_last).pack(pady=5)

root.mainloop()