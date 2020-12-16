from tkinter import *
from tkinter import messagebox
import math
screen = Tk()
screen.title("My Calculator")
screen.configure(bg='blue')
screen.iconbitmap('cal.ico')
#screen.geometry("365x490")
screen.geometry('362x490')
screen.maxsize(width=453,height=490)
screen.minsize(width=362,height=490)

tex = StringVar()
operator = ''

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)    
    except:
        messagebox.showinfo('Notification','Try again something wents wrong...',parent=screen)

def cm_sin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)   
    except:
            messagebox.showinfo('Notification','Try again something wents wrong...',parent=screen)   

def cm_cos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)   
    except:
            messagebox.showinfo('Notification','Try again something wents wrong...',parent=screen)            

def cm_tan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)   
    except:
            messagebox.showinfo('Notification','Try again something wents wrong...',parent=screen)

def cm_sqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)   
    except:
            messagebox.showinfo('Notification','Try again something wents wrong...',parent=screen)

def cm_log():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)   
    except:
            messagebox.showinfo('Notification','Try again something wents wrong...',parent=screen)                        
########------->Binding Function<--------########

def on_enter7(e):
    btn7.configure(bg='red')
def on_leave7(e):
    btn7.configure(bg='powder blue')

def on_enter8(e):
    btn8.configure(bg='red')
def on_leave8(e):
    btn8.configure(bg='powder blue')

def on_enter9(e):
    btn9.configure(bg='red')
def on_leave9(e):
    btn9.configure(bg='powder blue')

def on_enter_add(e):
    btnadd.configure(bg='red')
def on_leave_add(e):
    btnadd.configure(bg='powder blue')

def on_enter4(e):
    btn4.configure(bg='red')
def on_leave4(e):
    btn4.configure(bg='powder blue')

def on_enter5(e):
    btn5.configure(bg='red')
def on_leave5(e):
    btn5.configure(bg='powder blue')    

def on_enter6(e):
    btn6.configure(bg='red')
def on_leave6(e):
    btn6.configure(bg='powder blue')    

def on_enter_sub(e):
    btnsub.configure(bg='red')
def on_leave_sub(e):
    btnsub.configure(bg='powder blue')

def on_enter1(e):
    btn1.configure(bg='red')
def on_leave1(e):
    btn1.configure(bg='powder blue')

def on_enter2(e):
    btn2.configure(bg='red')
def on_leave2(e):
    btn2.configure(bg='powder blue')

def on_enter3(e):
    btn3.configure(bg='red')
def on_leave3(e):
    btn3.configure(bg='powder blue')    

def on_enter_div(e):
    btndiv.configure(bg='red')
def on_leave_div(e):
    btndiv.configure(bg='powder blue')

def on_enter_mul(e):
    btnmul.configure(bg='red')
def on_leave_mul(e):
    btnmul.configure(bg='powder blue')

def on_enter_clear(e):
    btnclear.configure(bg='red')
def on_leave_clear(e):
    btnclear.configure(bg='powder blue')    

def on_enter_equal(e):
    btnequal.configure(bg='red')
def on_leave_equal(e):
    btnequal.configure(bg='powder blue')   

def on_enter0(e):
    btn0.configure(bg='red')
def on_leave0(e):
    btn0.configure(bg='powder blue') 

def on_enter_entery(e):
    enter1.configure(bg='red',fg='white')
def on_leave_entery(e):
    enter1.configure(bg='orange',fg='black')  

def on_enter_sin(e):
    btnsin.configure(bg='red')
def on_leave_sin(e):
    btnsin.configure(bg='powder blue')
      
def on_enter_cos(e):
    btncos.configure(bg='red')
def on_leave_cos(e):
    btncos.configure(bg='powder blue')  

def on_enter_tan(e):
    btntan.configure(bg='red')
def on_leave_tan(e):
    btntan.configure(bg='powder blue')   

def on_enter_sqrt(e):
    btnsquare.configure(bg='red')
def on_leave_sqrt(e):
    btnsquare.configure(bg='powder blue')  

def on_enter_log(e):
    btnlog.configure(bg='red')
def on_leave_log(e):
    btnlog.configure(bg='powder blue')             

enter1 = Entry(screen,bg="orange",font=('arial',20,'italic bold'), bd='30',justify='right',textvariable=tex)
enter1.grid(row=0,columnspan=4)

btn7 = Button(screen,text="7",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(7)
                                    ,activebackground='green',activeforeground='white',bg='powder blue')
btn7.grid(row=1,column=0)


btn8 = Button(screen,text="8",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(8)
                                    ,activebackground='green',activeforeground='white',bg='powder blue')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text="9",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(9)
                        ,activebackground='green',activeforeground='white',bg='powder blue')
btn9.grid(row=1,column=2)

btnadd = Button(screen,text="+",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click('+')
,activebackground='green',activeforeground='white',bg='powder blue')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text="4",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(4)
,activebackground='green',activeforeground='white',bg='powder blue')
btn4.grid(row=2,column=0)

btn5 = Button(screen,text="5",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(5)
,activebackground='green',activeforeground='white',bg='powder blue')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text="6",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(6)
,activebackground='green',activeforeground='white',bg='powder blue')
btn6.grid(row=2,column=2)

btnsub = Button(screen,text="-",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click('-')
,activebackground='green',activeforeground='white',bg='powder blue')
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text="1",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(1)
,activebackground='green',activeforeground='white',bg='powder blue')
btn1.grid(row=3,column=0)

btn2 = Button(screen,text="2",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(2)
,activebackground='green',activeforeground='white',bg='powder blue')
btn2.grid(row=3,column=1)

btn3 = Button(screen,text="3",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(3)
,activebackground='green',activeforeground='white',bg='powder blue')
btn3.grid(row=3,column=2)

btnmul = Button(screen,text="*",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click('*')
,activebackground='green',activeforeground='white',bg='powder blue')
btnmul.grid(row=3,column=3)


btn0 = Button(screen,text="0",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click(0)
,activebackground='green',activeforeground='white',bg='powder blue')
btn0.grid(row=4,column=0)

btnclear = Button(screen,text="C",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=clear
,activebackground='green',activeforeground='white',bg='powder blue')
btnclear.grid(row=4,column=1)

btnequal = Button(screen,text="=",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=equal
,activebackground='green',activeforeground='white',bg='powder blue')
btnequal.grid(row=4,column=2)

btndiv = Button(screen,text="/",font=('arial',20,'italic bold'), bd='8',padx=16,pady=16,command=lambda: click('/')
,activebackground='green',activeforeground='white',bg='powder blue')
btndiv.grid(row=4,column=3)

btnsin = Button(screen,text="Sin",font=('arial',15,'italic bold'), bd='8',padx=14,pady=19,command=cm_sin
,activebackground='green',activeforeground='white',bg='powder blue')
btnsin.grid(row=0,column=4)

btncos = Button(screen,text="Cos",font=('arial',15,'italic bold'), bd='8',padx=14,pady=19,command=cm_cos
,activebackground='green',activeforeground='white',bg='powder blue')
btncos.grid(row=1,column=4)

btntan = Button(screen,text="Tan",font=('arial',15,'italic bold'), bd='8',padx=14,pady=19,command=cm_tan
,activebackground='green',activeforeground='white',bg='powder blue')
btntan.grid(row=2,column=4)

btnsquare = Button(screen,text="Sqrt",font=('arial',15,'italic bold'), bd='8',padx=14,pady=19,command=cm_sqrt
,activebackground='green',activeforeground='white',bg='powder blue')
btnsquare.grid(row=3,column=4)

btnlog = Button(screen,text="Log",font=('arial',15,'italic bold'), bd='8',padx=14,pady=19,command=cm_log
,activebackground='green',activeforeground='white',bg='powder blue')
btnlog.grid(row=4,column=4)
########------->Binding<--------########
enter1.bind('<Enter>',on_enter_entery)
enter1.bind('<Leave>',on_leave_entery)

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd.bind('<Enter>',on_enter_add)
btnadd.bind('<Leave>',on_leave_add)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnsub.bind('<Enter>',on_enter_sub)
btnsub.bind('<Leave>',on_leave_sub)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btnmul.bind('<Enter>',on_enter_mul)
btnmul.bind('<Leave>',on_leave_mul)

btndiv.bind('<Enter>',on_enter_div)
btndiv.bind('<Leave>',on_leave_div)

btnequal.bind('<Enter>',on_enter_equal)
btnequal.bind('<Leave>',on_leave_equal)

btnclear.bind('<Enter>',on_enter_clear)
btnclear.bind('<Leave>',on_leave_clear)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnsin.bind('<Enter>',on_enter_sin)
btnsin.bind('<Leave>',on_leave_sin)

btncos.bind('<Enter>',on_enter_cos)
btncos.bind('<Leave>',on_leave_cos)

btntan.bind('<Enter>',on_enter_tan)
btntan.bind('<Leave>',on_leave_tan)

btnsquare.bind('<Enter>',on_enter_sqrt)
btnsquare.bind('<Leave>',on_leave_sqrt)

btnlog.bind('<Enter>',on_enter_log)
btnlog.bind('<Leave>',on_leave_log)
screen.mainloop()
