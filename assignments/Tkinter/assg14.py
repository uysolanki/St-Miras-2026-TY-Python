from tkinter import *

# List of background colors
colors = ["red", "green", "blue", "yellow", "pink", "orange", "cyan"]

index = 0

# Function to change background color
def change_color():
    global index
    root.configure(bg=colors[index])
    index = (index + 1) % len(colors)   # Move to next color
    root.after(1000, change_color)      # Change color every 1 second

# Create the main window
root = Tk()
root.title("Changing Background Colors")
root.geometry("400x300")

# Start changing colors
change_color()

# Run the application
root.mainloop()