from tkinter import * #importing module

class CurrencyConvertor:   #Creating Class
    def __init__(self):
        window = Tk()   #Creating app window
        window.title("Currency Convertor") #Adding title
        window.configure(bg="yellow")#Adding Background Color

        # Adding labels
        Label(window,font="Helvetica 16 bold",bg="yellow",text="Amount to Convert",border="10px").grid(row=1,column=1,sticky=W)
        Label(window,font="Helvetica 16 bold",bg="yellow",text="Conversion Rate",border="10px").grid(row=2,column=1,sticky=W)
        Label(window,font="Helvetica 16 bold",bg="yellow",text="Converted Amount",border="10px").grid(row=3,column=1,sticky=W)

        # Creating objects and Entry functions
        self.amounttoConvertVar=StringVar()
        Entry(window, textvariable=self.amounttoConvertVar,foreground="red",font="Helvetica 16 bold",justify = RIGHT).grid(row=1,column=2,ipadx="7px",ipady="7px")
        self.conversionRateVar=StringVar()
        Entry(window, textvariable=self.conversionRateVar,foreground="red",font="Helvetica 16 bold",justify = RIGHT).grid(row=2,column=2,ipadx="7px",ipady="7px")
        self.convertedAmountVar=StringVar()
        lblConvertedAmount= Label(window,font="Helvetica 16 bold",foreground="blue",bg="yellow",textvariable=self.convertedAmountVar).grid(row=3,column=2,sticky=E)

        #Creating Convert and clear buttons ,when clicked they will call the respective functions
        btConvertedAmount= Button(window,text="Convert" ,font="Helveltica 12 bold",bg="blue",fg="white",command=self.ConvertedAmount).grid(row=4,column=2,sticky=E)
        btdelete_all= Button(window,text="Clear" ,font="Helveltica 12 bold",bg="red",fg="white",command=self.delete_all).grid(row=4,column=6,padx=25,pady=25,sticky=E)

        window.mainloop()

        #Functions to do convertion
    def ConvertedAmount(self):   
        amt=float(self.conversionRateVar.get())
        convertedAmountVar=float(self.amounttoConvertVar.get())*amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))

        #function to clear all
    def delete_all(self):   
        self.amounttoConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")
    
CurrencyConvertor()