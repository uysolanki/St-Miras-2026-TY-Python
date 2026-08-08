# from tkinter import *

# # Create the main window
# root = Tk()
# root.title("Listbox Example")
# root.geometry("300x200")

# # Create Listbox
# listbox = Listbox(root)

# # Add items to the Listbox
# listbox.insert(END, "Python")
# listbox.insert(END, "Java")
# listbox.insert(END, "C")
# listbox.insert(END, "C++")
# listbox.insert(END, "JavaScript")

# # Display the Listbox
# listbox.pack(pady=20)

# # Run the application
# root.mainloop()



#option 2

from tkinter import *

def show():
    print("Selected:", listbox.get(ACTIVE))

root = Tk()
root.title("Listbox Example")
root.geometry("300x250")

listbox = Listbox(root)

languages = ["Python", "Java", "C", "C++", "JavaScript"]

for lang in languages:
    listbox.insert(END, lang)

listbox.pack(pady=10)

Button(root, text="Show Selection", command=show).pack()

root.mainloop()