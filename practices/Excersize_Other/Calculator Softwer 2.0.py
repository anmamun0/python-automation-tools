from  tkinter import *

root = Tk()
root.geometry('380x380')
# root.wm_iconbitmap('@calculator-icon-2.xbm')
root.title('Calculator Project on Python')
root.config(background='#232323')


result = ''

# ver:- 2.1.0v
# New Function added By Jubayer -> called when "." is clicked
def click_on_dot(text):
    global result
    existed_text = result # gets the full existed text which is on the mainscreen

    # To get the index of the last operator in the existed_text
    # Example: if the existed text is "1.2+2.3-5.3"
    # Then this part with grab the last operator such as "-" in this example
    # the index of "-" in existed_text is "7"
    index = 0
    for n,x in enumerate(existed_text):
        if(x == "+" or x == "-" or x == "*" or x == "/"):
            index = n
    
    # this line of code gets a part of existed_text
    # Example: if the existed text is "1.2+2.3-5.3"
    # Then this line will grab "5.3"
    # partial_text = "5.3" then
    partial_text = existed_text[index:]

    # only works if "." does not exist in partial text
    # Example: If partial text is "5.0" then it will not work as there is already a "." between 5 and 0 in 5.0
    # Example: If partial text is "5" then it will work as there is no "." in "5"
    if(text not in partial_text):
        result += text
        Project_Screen.config(text=result)

def click(value):
    global result
    result +=value
    Project_Screen.config(text=result)
    
def final_result():
    global result
    show = ''
    if result != '':
        try:
            show = eval(result)
        except:
            show='!-error'
            result =''

    # Updated Line
    Result_Screen.config(text=f'{Project_Screen.cget("text")}={show}') # to get the string in Project_Screen Label used "<label name>.cget("text")"

def all_Clear():
    global result
    result =''
    Project_Screen.config(text=result)
def remove_click():
    global result
    result = result[:-1]
    Project_Screen.config(text=result)
    Project_Screen.update()

# Buttons
# Last Buttons  0 .  %  +  =
f1 = Frame(root,height=50,width=400,background='#333333',pady=9,padx=8)
btn = Button(f1,text='0',bg='#404040',borderwidth=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('0'))
btn.pack(side='left',padx=5)


btn = Button(f1,text='.',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click_on_dot('.'))
btn.pack(side='left',padx=5)


btn = Button(f1,text='%',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('/100'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='+',bg='#404040',cursor='plus',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('+'))
btn.pack(side='left',padx=5)


btn = Button(f1,text='=',bg='#2E7CF7',cursor='exchange',border=0,width=11,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#398AE3',command = lambda:final_result())
btn.pack(side='left',padx=5)
f1.pack(side =BOTTOM)

# 2 Buttons 1  2  3 -  x2 ^
f1 = Frame(root,height=50,width=400,background='#333333',pady=9,padx=20)
btn = Button(f1,text='1',bg='#404040',cursor='spider',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('1'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='2',bg='#404040',cursor='top_left_corner',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('2'))
btn.pack(side='left',padx=5)


btn = Button(f1,text='3',bg='#404040',cursor='target',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('3'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='-',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('-'))
btn.pack(side='left',padx=5)


btn = Button(f1,text='x2',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('**'))
btn.pack(side='left',padx=5)


btn = Button(f1,text='^',bg='#404040',cursor='mouse',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('^'))
btn.pack(side='left',padx=5)
f1.pack(side =BOTTOM)



# 3 Buttons 4 5 6 * {  }
f1 = Frame(root,height=50,width=400,background='#333333',pady=9,padx=20)
btn = Button(f1,text='4',bg='#404040',cursor='pencil',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('4'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='5',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('5'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='6',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('6'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='*',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('*'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='{',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('{'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='}',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('}'))
btn.pack(side='left',padx=5)
f1.pack(side =BOTTOM)


# 3 Buttons 7 8 9 / ! C
f1 = Frame(root,height=50,width=400,background='#333333',pady=9,padx=20)
btn = Button(f1,text='7',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('7'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='8',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('8'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='9',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('9'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='/',bg='#404040',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:click('/'))
btn.pack(side='left',padx=5)

btn = Button(f1,text='<<',bg='#404040',cursor='left_side',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:remove_click())
btn.pack(side='left',padx=5)

btn = Button(f1,text='C',bg='#333333',cursor='X_cursor',border=0,width=3,height=1,font ='Ubuntu 10  bold',fg='white',activebackground='#656565',activeforeground='white',command = lambda:all_Clear())
btn.pack(side='left',padx=5)
f1.pack(side =BOTTOM)



# Project Screen Display

Project_Screen = Label(root,text='',width=300,height=5,background='#232323',fg='white',anchor='w',padx=30)
Project_Screen.pack(pady=1,side=BOTTOM)

# Middle Line Canvas
line = Canvas(width=400,height=1,background='#333333',borderwidth=0,border=0)
line.pack(side=BOTTOM)
line.create_line(400,1,0,1)

# Result Screen Display

Result_Screen = Label(root,text='',width=300,height=5,background='#232323',fg='white',anchor='w',padx=30)
Result_Screen.pack(side=BOTTOM)

root.mainloop()