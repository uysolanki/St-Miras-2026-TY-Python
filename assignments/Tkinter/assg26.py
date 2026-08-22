from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Color Menu")


def change_color(color):
    root.configure(bg=color)


# Create Menu Bar
menubar = Menu(root)

# Create Color Menu
colormenu = Menu(menubar, tearoff=0)

colormenu.add_command(label="Red", command=lambda: change_color("red"))
colormenu.add_command(label="Green", command=lambda: change_color("green"))
colormenu.add_command(label="Blue", command=lambda: change_color("blue"))
colormenu.add_command(label="Yellow", command=lambda: change_color("yellow"))
colormenu.add_command(label="Pink", command=lambda: change_color("pink"))
colormenu.add_command(label="White", command=lambda: change_color("white"))

# Add Color menu to Menu Bar
menubar.add_cascade(label="Colors", menu=colormenu)

# Display Menu Bar
root.config(menu=menubar)

root.mainloop()