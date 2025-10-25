#AN.Mamun-> Project Name: Password Generator
import random
from tkinter import *
import string

def generate_password():
    n = int(type.get())
    password = password_gen(n)
    display.config(text=password)

def copy_to_clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(display.cget("text"))
    root.update()  # required for clipboard changes to be noticed

def window():
    global root
    root = Tk()
    root.geometry("500x200")
    root.maxsize(600,200) 
    root.title("Make Password With ANMamun")
 
    global type
    type = Entry(root,width=20, font=('Helvetica', 12),relief=FLAT,borderwidth=3, 
                 highlightbackground="black",background='#c2f1ff') 
    type.grid(row=0, column=0, pady=20, padx=30, sticky=W) 

    btn = Button(root, text="Generate", command=generate_password, bg='#4CAF50', fg='white',
                 activebackground='#68cc6c', font=('Helvetica', 12, 'bold'), relief=RAISED) 
    btn.place(x=250,y=15)
    Label(root, text="Password ",font=('Helvetica', 12, 'bold'), fg='#1E90FF').place(x=30,y=80)

    global display
    display = Label(root,  text="", justify=CENTER, font=('Helvetica', 13, 'bold'),
                    cursor="hand2", bg='#f0f0f0',wraplength=300)
    
    display.place(x=150,y=80) 
    display.bind("<Button-1>", copy_to_clipboard)
    root.mainloop()
    return

def password_gen(n):
    sequence =  "#$%&0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy"
    password = ""
    for _ in range(n): password += random.choice(sequence)
    return password
window()
