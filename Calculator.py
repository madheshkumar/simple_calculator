from tkinter import *
from tkinter.font import Font

class Calculator:


    def __init__(self):
        #display
        window = Tk()
        window.title("Calculator")
        window.configure(bg="#c0d6fa")

        #variables
        value1=""
        value2=""
        operation=""
        user_input=StringVar()

        #result display
        resultDisplay=Entry(window,font="Helvetica 25 bold",bg="#befaf0",foreground="#6c02b8",textvariable=user_input,border=0,insertwidth="4",justify="right").grid(columnspan="4",ipadx="15px",ipady="20px")

        #buttons
        button7= Button(window,font="Helvetica 25 bold",text="7",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(7)).grid(row=1,column=0,ipadx="20px",ipady="15px")
        button8= Button(window,font="Helvetica 25 bold",text="8",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(8)).grid(row=1,column=1,ipadx="20px",ipady="15px")
        button9= Button(window,font="Helvetica 25 bold",text="9",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(9)).grid(row=1,column=2,ipadx="20px",ipady="15px")

        Addition=Button(window,font="Helvetica 25 bold",text="+",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : add()).grid(row=1,column=3,ipadx="18px",ipady="15px")

        button4= Button(window,font="Helvetica 25 bold",text="4",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(4)).grid(row=2,column=0,ipadx="20px",ipady="15px")
        button5= Button(window,font="Helvetica 25 bold",text="5",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(5)).grid(row=2,column=1,ipadx="20px",ipady="15px")
        button6= Button(window,font="Helvetica 25 bold",text="6",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(6)).grid(row=2,column=2,ipadx="20px",ipady="15px")

        Subtraction=Button(window,font="Helvetica 25 bold",text="-",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : sub()).grid(row=2,column=3,ipadx="21px",ipady="15px")

        button1= Button(window,font="Helvetica 25 bold",text="1",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(1)).grid(row=3,column=0,ipadx="20px",ipady="15px")
        button2= Button(window,font="Helvetica 25 bold",text="2",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(2)).grid(row=3,column=1,ipadx="20px",ipady="15px")
        button3= Button(window,font="Helvetica 25 bold",text="3",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(3)).grid(row=3,column=2,ipadx="20px",ipady="15px")

        Multiply=Button(window,font="Helvetica 25 bold",text="x",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : mul()).grid(row=3,column=3,ipadx="19px",ipady="15px")

        button0= Button(window,font="Helvetica 25 bold",text="0",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : click(0)).grid(row=4,column=0,ipadx="20px",ipady="15px")
        clear= Button(window,font="Helvetica 25 bold",text="C",background="#d4f1fa",foreground="#004d99",border=0,command= lambda : clearDisplay()).grid(row=4,column=1,ipadx="18px",ipady="15px")
        equalto= Button(window,font="Helvetica 25 bold",text="=",background="#d4f1fa",foreground="#004d99",border=0,command= lambda : Calculate()).grid(row=4,column=2,ipadx="20px",ipady="15px")
        Division=Button(window,font="Helvetica 25 bold",text="/",background="#d4f1fa",foreground="#56abe3",border=0,command= lambda : div()).grid(row=4,column=3,ipadx="22px",ipady="15px")

        def click(number):
            nonlocal value2
            value2 = value2 + str(number)
            user_input.set(value2)

        #to clear display
        def clearDisplay():
            nonlocal value2,value1
            value1 = ""
            value2 = ""
            user_input.set(value2)
        
        def Calculate():

            nonlocal value1,value2,operation

            if operation == "+":
                #adding
                a=int(value1)
                b=int(value2)
                cal=str(a+b)
                user_input.set(cal)
                value1=str(cal)
                value2=""

            if operation == "-":
                #subtracting
                a=int(value1)
                b=int(value2)
                cal=str(a-b)
                user_input.set(cal)
                value1=str(cal)
                value2=""


            if operation == "x":
                #multipling
                a=int(value1)
                b=int(value2)
                cal=str(a*b)
                user_input.set(cal)
                value1=str(cal)
                value2=""

            if operation == "/":
                #dividing
                a=int(value1)
                b=int(value2)
                try:
                    cal=str(a/b)
                except ZeroDivisionError:
                    cal="Math Error"
                user_input.set(cal)
                value1=str(cal)
                value2=""


        def add():
            nonlocal value1,value2,operation
            if value1 == '':
                value1=value2
            value2=""
            operation="+"

        def sub():
            nonlocal value1,value2,operation
            if value1 == '':
                value1=value2
            value2=""
            operation="-"

        def mul():
            nonlocal value1,value2,operation
            if value1 == '':
                value1=value2
            value2=""
            operation="x"

        def div():
            nonlocal value1,value2,operation
            if value1 == '':
                value1=value2
            value2=""
            operation="/"

        window.mainloop()
           
Calculator()