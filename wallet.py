from tkinter import *
from tkinter.ttk import Combobox

def wallet_page():
    #starts creating main window 
    window = Tk()
    window.title("Wallet") #Sets the title for the window
    window.geometry("925x500+300+200") #it sets the window size and position
    window.configure(bg="#fff") #Sets background colour for the window
    window.resizable(False,False) #Disables the resizing of the window

# This fuction enables or disables the card number selection based on the card type selection
    def enable_cardno(event):
        selected_card_type = cardtype.get()
        if selected_card_type == "Debit Card":
            cardno['values'] = ("Debit Card Number 1", "Debit Card Number 2", "Debit Card Number 3")
            cardno.config(state='normal')
        elif selected_card_type == "Credit Card":
            cardno['values'] = ("Credit Card Number 1", "Credit Card Number 2", "Credit Card Number 3")
            cardno.config(state='normal')
        else:
            cardno.config(state='disabled')

    #This function makes the AMOUNT entry field invisible when focused        
    def enter_amt(event):
        if amt.get() == 'Amount':
            amt.delete(0, "end")

    #This function restores the AMOUNT entry field when lost focous
    def leave_amt(event):
        if amt.get() == '':
            amt.insert(0, "Amount")

    #This function makes the CVV entry field invisible when focused
    def enter_cvv(event):
        if cvv.get() == 'CVV':
            cvv.delete(0, "end")

    # This fuction restores the CVV entry field when lost focous
    def leave_cvv(event):
        if cvv.get() == '':
            cvv.insert(0, "CVV") 

     # It manages the amount added to the wallet       
    def addamt():
        card_type = cardtype.get()
        card_no = cardno.get()
        cv = cvv.get()
        amount = amt.get()
        
    #Creats a frame inside the window
    frame = Frame(window, height=410,width=830, bg="white")
    frame.place(x=50, y=40)

    #Adds headline to the frame
    heading = Label(frame, text="Add Amount", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(relx=0.5, rely=0.05, anchor=CENTER)

    #Widget to enter amount
    amt = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    amt.place(x=30, y=100)  
    amt.insert(0,"Amount")
    amt.bind("<FocusIn>", enter_amt)
    amt.bind("<FocusOut>", leave_amt)
    Frame(frame, width=295, height=1, bg="black").place(x=25,y=125)

    #Combobox for selecting card type
    cardtype = Combobox(frame, width=35, state="readonly", font=("Microsoft YaHei UI Light", 11))
    cardtype['values'] = ("Select Card Type", "Debit Card", "Credit Card")
    cardtype.current(0)
    cardtype.place(x=22, y=170)

    #combobox for selecting card number
    cardno = Combobox(frame, width=35, state="readonly", font=("Microsoft YaHei UI Light", 11))
    cardno['values'] = ("Select Card Number","Card Number 1", "Card Number 2", "Card Number 3")
    cardno.current(0)
    cardno.config(state='disabled')
    cardno.place(x=490, y=100) 

    cardtype.bind("<<ComboboxSelected>>", enable_cardno)
 

   #Widget for entering cvv
    cvv = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    cvv.place(x=495, y=170)  
    cvv.insert(0,"CVV")
    cvv.bind("<FocusIn>", enter_cvv)
    cvv.bind("<FocusOut>", leave_cvv)
    Frame(frame,width=295,height=1,bg="black").place(x=490,y=195)
    
    #Button to submit the form
    Button(frame,width=39,pady=7,text="Submit", bg="#57a1f8",fg="white",border=0).place(x=280,y=280)
    
    #Binding event for card type selection
    cardtype.bind("<<ComboboxSelected>>", enable_cardno)

    # starting GUI loop
    window.mainloop()

wallet_page()