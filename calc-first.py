from tkinter import *

window = Tk()
window.geometry("320x450")
window.title("My first calculator")

label1 = Label(text="",width=25,height=2,font=("Arial",25),bg="white")
label1.pack()

equation = ""

def show(x):
    global equation
    equation = equation + x
    label1.config(text=equation)

def clear():
    global equation
    equation = ""
    label1.config(text="")

def calculate():
    global equation
    equation = equation.replace('x','*')
    try:
        result = eval(equation)
        equation = str(result)
        label1.config(text=result)
    except:
        label1.config(text="ERROR")

def backspace():
    global equation
    equation = equation[:-1]
    label1.config(text=equation)

Button(window, text ="C",width=5,height=3,fg= "#fff", bg="grey",command= lambda:clear()).place(x=10,y=90)
Button(window, text ="◀",width=5,height=3,command= lambda:backspace()).place(x=90,y=90)
Button(window, text ="%",width=5,height=3, command= lambda:show("%")).place(x=170,y=90)
Button(window, text ="/",width=5,height=3, bg="#FFA500", command= lambda:show("/")).place(x=250,y=90)

Button(window, text ="7",width=5,height=3, command= lambda:show("7")).place(x=10,y=160)
Button(window, text ="8",width=5,height=3, command= lambda:show("8")).place(x=90,y=160)
Button(window, text ="9",width=5,height=3,command= lambda:show("9")).place(x=170,y=160)
Button(window, text ="x",width=5,height=3, bg="#FFA500",command= lambda:show("x")).place(x=250,y=160)

Button(window, text ="4",width=5,height=3, command= lambda:show("4")).place(x=10,y=230)
Button(window, text ="5",width=5,height=3, command= lambda:show("5")).place(x=90,y=230)
Button(window, text ="6",width=5,height=3, command= lambda:show("6")).place(x=170,y=230)
Button(window, text ="-",width=5,height=3,bg="#FFA500", command= lambda:show("-")).place(x=250,y=230)

Button(window, text ="1",width=5,height=3, command= lambda:show("1")).place(x=10,y=300)
Button(window, text ="2",width=5,height=3, command= lambda:show("2")).place(x=90,y=300)
Button(window, text ="3",width=5,height=3, command= lambda:show("3")).place(x=170,y=300)
Button(window, text ="+",width=5,height=3,bg="#FFA500", command= lambda:show("+")).place(x=250,y=300)

Button(window, text ="0",width=16,height=3, command= lambda:show("0")).place(x=10,y=370)
Button(window, text = ".",width=5,height=3, command= lambda:show(".")).place(x=170,y=370)
Button(window, text = "=",width=5,height=3,bg="#FFA500", command= lambda:calculate()).place(x=250,y=370)

window.mainloop()