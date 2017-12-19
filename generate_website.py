# button_callback.py
from Tkinter import Tk, Button

root = Tk()


# Create a button with a custom callback
def my_callback():
    print("The button was clicked!")  # Prints to console not the GUI


print_button = Button(root, text='Click me!', command=my_callback)
print_button.pack()

root.mainloop()
