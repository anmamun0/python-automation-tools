import datetime
from tkinter import *

def isLeapYear(year):
    if year % 400 == 0: return True
    if year % 100 == 0: return False
    if year % 4 == 0: return True
    return False

def days_in_year(year):
    return 366 if isLeapYear(year) else 365

def days_in_month(year, month):
    if month == 2:  return 29 if isLeapYear(year) else 28
    else:
        mnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return mnt[month - 1]

def BirdhDay_Calculation(day, m, y):
    now = datetime.datetime.now()
    cY, cM, cD = now.year, now.month, now.day

    fast = days_in_month(y, m) - day
    for i in range(m, 12):  fast += days_in_month(y, i + 1)

    last = cD
    for i in range(1, cM): last += days_in_month(cY, i)

    total = 0
    for year in range(y + 1, cY):  total += days_in_year(year)
    
    total += fast + last 
    return total

def gen():
    try:
        a = int(da.get())
        b = int(mon.get())
        c = int(yr.get())
        total = BirdhDay_Calculation(a, b, c)
        s = f"Your Total Day = {total}\nYour Year = {total//365} Year {total%365} Days" 
        display.config(text=s)
        
    except ValueError:
        display.config(text="Please enter valid integers for day, month, and year")
    
    da.delete(0, 'end')
    mon.delete(0, 'end')
    yr.delete(0, 'end')

def copy_to_clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(display.cget("text"))

def window():
    global root, da, mon, yr, display
    root = Tk()
    root.geometry("500x300")
    root.resizable(False, False)
    root.title("Birthday Generator With ANMamun")

    Label(root, text="Day            Month         Year", font=('Arial', 10)).place(x=97, y=18)
    da = Entry(root, width=4, font=('Helvetica', 12), relief=FLAT, borderwidth=8,
               highlightbackground="black", bg="#1c175c", foreground="white", insertbackground="white")
    da.place(x=100, y=40)

    mon = Entry(root, width=4, font=('Helvetica', 12), relief=FLAT, borderwidth=8,
                highlightbackground="black", bg="#1c175c", foreground="white", insertbackground="white")
    mon.place(x=170, y=40)

    yr = Entry(root, width=4, font=('Helvetica', 12), relief=FLAT, borderwidth=8,
               highlightbackground="black", bg="#1c175c", foreground="white", insertbackground="white")
    yr.place(x=240, y=40)

    btn = Button(root, text="Calculate", command=gen, bg='#4CAF50', fg='white',
                 activebackground='#68cc6c', font=('Helvetica', 12, 'bold'), relief=FLAT, borderwidth=3.4)
    btn.place(x=350, y=40)

    Label(root, text="Your Information ->", justify=CENTER, font=('Helvetica', 13),
          cursor="hand2", bg='#f0f0f0', wraplength=300).place(x=30, y=120)

    display = Label(root, text="", justify=LEFT, anchor="w", font=('Helvetica', 13),
                    cursor="hand2", bg='#f0f0f0', wraplength=300,)
    display.place(x=30, y=150)

    display.bind("<Button-1>", copy_to_clipboard)

    root.mainloop()

window()
