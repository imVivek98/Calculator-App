
from tkinter import *
import parser

root = Tk()

root.title("Calculator")
display = Entry(root)
display.grid(row=1,columnspan=6, sticky=W+E)

#get the user input and place it in the text field:

i=0
def get_Var(num):
    global i
    display.insert(i,num)
    i+=1

def clrscr():
    display.delete(0,END)

def delone():
    entire_str = display.get()
    if len(entire_str):
        new_str = entire_str[:-1]
        clrscr()
        display.insert(0,new_str)
    else:
        clrscr()
        display.insert("ERROR")


def operations(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length


def calculator():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()   #
        result = eval(a)
        clrscr()
        display.insert(0,result)
    except Exception:
        clrscr()
        display.insert(0,"ERROR")


#Adding Buttons :
Button(text='1',command=lambda :get_Var(1)).grid(row=2,column=0)
Button(text='2',command=lambda : get_Var(2)).grid(row=2,column=1)
Button(text='3',command=lambda : get_Var(3)).grid(row=2,column=2)
Button(text='4',command=lambda :get_Var(4)).grid(row=3,column=0)
Button(text='5',command=lambda :get_Var(5)).grid(row=3,column=1)
Button(text='6',command=lambda :get_Var(6)).grid(row=3,column=2)
Button(text='7',command=lambda :get_Var(7)).grid(row=4,column=0)
Button(text='8',command=lambda :get_Var(8)).grid(row=4,column=1)
Button(text='9',command=lambda :get_Var(9)).grid(row=4,column=2)
Button(text='0',command=lambda :get_Var(0)).grid(row=5,column=1)
Button(text='AC',command=lambda : clrscr()).grid(row=5,column=0)
Button(text='=',command=lambda :calculator()).grid(row=5,column=2)
Button(text='+',command=lambda : operations('+')).grid(row=2,column=3)
Button(text='-',command=lambda : operations('-')).grid(row=3,column=3)
Button(text='*',command=lambda : operations('*')).grid(row=4,column=3)
Button(text='/',command=lambda : operations('/')).grid(row=5,column=3)
Button(text='pi',command=lambda : operations('*3.14')).grid(row=6,column=0)
Button(text='%',command=lambda : operations('%')).grid(row=6,column=1)
Button(text='(',command=lambda : operations('(')).grid(row=6,column=2)
Button(text=')',command=lambda : operations(')')).grid(row=6,column=3)
Button(text='exp',command=lambda : operations('exp')).grid(row=7,column=1)
Button(text='x!',command=lambda :operations('!')).grid(row=7,column=2)
Button(text='**',command=lambda : operations('**')).grid(row=7 , column=3)
Button(text='->',command=lambda: delone()).grid(row=7,column=0)


root.mainloop()
