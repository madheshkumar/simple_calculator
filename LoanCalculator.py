from tkinter import *

class LoanCalculator:
    def __init__(self):    
        window = Tk()
        window.title("Loan Calculator")
        window.configure(bgcolor="blue")
        
        Label(window,font="Helvetica 12 bold",bg="blue",text="Annual Interest Rate").grid(row=1,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="blue",text="Number of Years").grid(row=2,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="blue",text="Loan Amount").grid(row=3,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="blue",text="Monthly Payment").grid(row=4,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="blue",text="Total Payment").grid(row=5,column=1,sticky=W)

        self.AnnualInterestRateVar = StringVar()
        Entry(window, textvariable= self.AnnualInterestRateVar,justify=RIGHT).grid(row=1,coloumn=2)
        self.NumberofYearsVar = StringVar()
        Entry(window, textvariable= self.NumberofYearsVar,justify=RIGHT).grid(row=2,column=2)
        self.LoanAmountVar = StringVar()
        Entry(window, textvariable= self.LoanAmountVar,justify=RIGHT).grid(row=3,column=2)
        self.MonthlyPaymentVar = StringVar()
        lblMonthlyPayment =Label(window,font="Helvetica 12 bold",bg="blue",textvariable=self.MonthlyPaymentVar).grid(row=4,column=2,sticky=E)
        self.TotalPaymentVar = StringVar()
        lblTotalPayment =Label(window,font="Helvetica 12 bold",bg="blue",textvariable=self.TotalPaymentVar).grid(row=5,column=2,sticky=E)

        