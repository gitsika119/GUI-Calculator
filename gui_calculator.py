'''
GUI Calculator
Basic 4 ops
'''

import tkinter
from tkinter import *
root=Tk()
root.title("GUI Calculator")
root.geometry("550x600")
root.resizable(False,False)
root.configure(bg="Black")

equation=""
def show(val):
    global equation
    equation+=val
    label_res.config(text=equation)
def clear():
    global equation
    equation=""
    label_res.config(text=equation)
label_res=Label(root,width=32,height=2,text="",font=("Cambria",24))
label_res.pack()
def answer():
    global equation 
    result=""
    if (equation != ""):
        try:
            result=eval(equation)
        except:
            result="ERROR"
            equation=""
    label_res.config(text=result)        
#r1
Button(root,text="C",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=15,y=100)
Button(root,text="/",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=100)
#r2
Button(root,text="7",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=15,y=200)
Button(root,text="8",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=200)
Button(root,text="+",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=430,y=200)
#r3
Button(root,text="4",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=15,y=300)
Button(root,text="5",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="-",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=430,y=300)
#bottom2
Button(root,text="1",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=15,y=400)
Button(root,text="2",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0",width=12,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=15,y=500)
Button(root,text=".",width=5,height=1,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3,font=("Cambria",24,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: answer()).place(x=430,y=415)

root.mainloop()
