from tkinter import *

# Create the main window
root = Tk()
root.title("Label Font Example")
root.geometry("350x200")

# Create a Label with custom font
label = Label(root,
              text="Welcome to Tkinter",
              font=("Arial", 18, "bold"))

label.pack(pady=50)

# Run the application
root.mainloop()