#28 NotePade with GUI

from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    root.title('New File')
    TextArea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(title="This is AskOpenFileName Doc",initialdir='/home/anmamun/Documents/Apple_Linux_B/Python/Python_Project/Python',defaultextension='.txt',filetypes=[('All File','*.*'),('Text Document','*.txt')])
    if file == '':
        file= None
    else:
        root.title(os.path.basename(file)+'  -  anmamun@anmamun')
        TextArea.delete(1.0, END)
        f = open(file,'r')
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file= asksaveasfilename(initialdir='/home/anmamun/Documents/Apple_Linux_B/Python/Python_Project/Python',initialfile='New-Untitled-File',filetypes=[('ALL FILES','*.*'),('Documents Files','.txt'),('All PIcture','.png')])
        if file == '':
            file = None
        else:
            f= open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ '  -  anmamun@anmamun')
    else:
        f = open(file,'r')
        f.write(TextArea.get(1.0,END))
        f.close()


def quitFile():
    root.destroy()

def cutFile():
    TextArea.event_generate(('<<cut>>'))
def copyFile():
    TextArea.event_generate(('<<Copy>>'))
def pasteFile():
    TextArea.event_generate(('<<Paste>>'))

def aboutFile():
    show = tmsg.showinfo('About','This a making a new DocumentsThis a making a new DocumentsThis a making a new DocumentsThis a making a new DocumentsThis a making a new Documents')
def updateFile():
    tmsg.showinfo('updateFile', 'Letest Updateed 9 March 2022 \n\n          Version 2.0')
def reviewFile():
    tmsg.showerror('Review','Get Review \n\n *****')




if __name__ == '__main__':
    root = Tk()
    root.title('New Python Documents')
    root.geometry('640x440')
    root.config(borderwidth=0)
    # root.wm_iconbitmap('@calculator-icon-1.xbm')

    # TextArea Section
    TextArea = Text(root,font=('Bitstream Charter', 13),borderwidth=0,wrap=NONE,bg='#070707',border=0,fg='#ffffff',padx=20,pady=20,selectforeground='#000000',selectbackground='#00FF00',selectborderwidth=0,insertbackground='#00FF00')

    TextArea.pack(fill=BOTH,expand=True)
    file = None

    # End TextArea


    # Adding VERTIVAL Scrallbar
    fast = Scrollbar(TextArea,cursor='hand1',background='#5D5D5D',activebackground='#444444')
    fast.pack(fill=Y,side=RIGHT)
    fast.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=fast.set)
    # End Scrall Bar
    

    # Adding HORISONTAL Scrallbar
    last = Scrollbar(TextArea,orient=HORIZONTAL,cursor='hand1',background='#5D5D5D',activebackground='#444444')
    last.pack(fill=X,side=BOTTOM)
    last.config(command=TextArea.xview)
    TextArea.config(xscrollcommand=last.set)
    # End Scrall Bar



    # Lets create MenueBar
    MenuBar = Menu(root,bg='#373737',borderwidth=0,activebackground='#5D5D5D',fg='#ffffff',activeforeground='#ffffff')
    FileMenu = Menu(MenuBar,tearoff=0,bg='#373737',activebackground='#1E59B8',fg='#ffffff',activeforeground='#ffffff')
    FileMenu.add_command(label='New',command=newFile)
    FileMenu.add_command(label='Open',command=openFile)
    FileMenu.add_command(label='Save',command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit',command=quitFile)
    MenuBar.add_cascade(label='File',menu= FileMenu)

    EditMenu = Menu(MenuBar,tearoff=0,bg='#373737',activebackground='#1E59B8',fg='#ffffff',activeforeground='#ffffff',borderwidth=0)
    EditMenu.add_command(label='Cut' ,command=cutFile)
    EditMenu.add_command(label='Copy' ,command=copyFile)
    EditMenu.add_command(label='Past' ,command=pasteFile)
    MenuBar.add_cascade(label='Edit',menu=EditMenu)


    HelpMenu = Menu(MenuBar,tearoff=0,bg='#373737',activebackground='#1E59B8',fg='#ffffff',activeforeground='#ffffff',borderwidth=0)
    HelpMenu.add_command(label='About Notpad' ,command=aboutFile)
    HelpMenu.add_command(label='Update Version' ,command=updateFile)
    HelpMenu.add_command(label='Get Review' ,command=reviewFile)
    MenuBar.add_cascade(label ='View', menu = HelpMenu)
    root.config(menu=MenuBar)

    root.mainloop()