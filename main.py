from tkinter import *

screen=Tk()
screen.title("Calculator")
screen.geometry('365x490')
screen.iconbitmap('cal.ico')


def put(number):
    global operator
    operator+= str(number)
    tex.set(operator)

def clear():
    global operator
    operator=''
    tex.set(operator)

def equal():
    global operator
    result=eval(operator)
    operator=str(result)
    tex.set(result)


tex=StringVar()
operator=''

entry1=Entry(screen,bg='yellow',font=('arial',20,'bold'),bd='30',justify='right',textvariable=tex)
entry1.grid(row='0',columnspan='4')

btn7=Button(screen,text='7',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(7))
btn7.grid(row=1,column=0)

btn8=Button(screen,text='8',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(8))
btn8.grid(row=1,column=1)

btn9=Button(screen,text='9',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(9))
btn9.grid(row=1,column=2)

btnadd=Button(screen,text='+',bg='aqua',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put('+'))
btnadd.grid(row=1,column=3)

btn4=Button(screen,text='4',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(4))
btn4.grid(row=2,column=0)

btn5=Button(screen,text='5',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(5))
btn5.grid(row=2,column=1)

btn6=Button(screen,text='6',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(6))
btn6.grid(row=2,column=2)

btnmulti=Button(screen,text='*',bg='aqua',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put('*'))
btnmulti.grid(row=2,column=3)

btn1=Button(screen,text='1',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(1))
btn1.grid(row=3,column=0)

btn2=Button(screen,text='2',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(2))
btn2.grid(row=3,column=1)

btn3=Button(screen,text='3',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(3))
btn3.grid(row=3,column=2)

btnsub=Button(screen,text='-',bg='aqua',font=('arial',20,' bold'),bd='8',padx=16,pady=16,command=lambda:put('-'))
btnsub.grid(row=3,column=3)

btn0=Button(screen,text='0',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put(0))
btn0.grid(row=4,column=0)

btnclear=Button(screen,text='C',bg='red',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=clear)
btnclear.grid(row=4,column=1)

btnequal=Button(screen,text='=',bg='white',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=equal)
btnequal.grid(row=4,column=2)

btndiv=Button(screen,text='/',bg='aqua',font=('arial',20,'bold'),bd='8',padx=16,pady=16,command=lambda:put('/'))
btndiv.grid(row=4,column=3)

screen.mainloop()

