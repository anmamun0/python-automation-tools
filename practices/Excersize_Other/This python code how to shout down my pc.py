
from tkinter import *
import os


# user define function
def shutdown():
	return os.system("shutdown /s /t 1")

def restart():
  
	return os.system("shutdown /r /t 1")
def logout():
	return os.system("shutdown -l")

# tkinter object
root = Tk()
root.geometry("300x300")

# background set to grey
root.configure(bg='light grey')

# creating a button using the widget
# Buttons that will call the submit function
Button(root, text="Shutdown", command=shutdown).grid(row=0)
Button(root, text="Restart", command=restart).grid(row=1)
Button(root, text="Log out", command=logout).grid(row=2)

mainloop()
