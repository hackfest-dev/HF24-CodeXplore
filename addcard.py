from tkinter import * #tkinter module
from tkinter import messagebox #messagebox from tkinter
from tkinter.ttk import Combobox #themed tk for dropdowm list

#func to craete add card page
def addcard_page():
    window = Tk()  #creating tk window
    window.title("Cards") #title
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

#func for entering card number
    def enter_cardno():
        if cardno.get() == 'Card Number':#default text
            cardno.delete(0, "end") #clr def text

 #func to leave card no. when clicked for next, eg expiry no           
    def leave_cardno():
        if cardno.get() == '':
            cardno.insert(0, "Card Number") 

 #func for entering expiry date           
    def enter_expdt():
        if expdt.get() == 'Expiry Date':
            expdt.delete(0, "end")

#func to leave card no. when clicked for next
    def leave_expdt():
        if expdt.get() == '':
            expdt.insert(0, "Expiry Date") 

#func for entering cvv
    def enter_cvv():
        if cvv.get() == 'CVV':
            cvv.delete(0, "end")

#func to leave card no. when clicked for next
    def leave_cvv():
        if cvv.get() == '':
            cvv.insert(0, "CVV") 

# Func to add card details
    def addcard():
        card = cardtype.get() #gets entry card type from combobox widget,dropdown list
        num = cardno.get()
        dt = expdt.get()
        cv = cvv.get()
        if (card != "Select Card Type") and (num != "Card Number") and (dt != "Expiry Date") and (cv != "CVV"):
            messagebox.showinfo("Success", "Card Added Successfully!")
            window.destroy()
            #shows pop up as success
            # user input correct thn window gets destroyed

            #home(login, loggedin_user)
        else:
            messagebox.showerror("Invalid", "Please fill up all the fields")
            #shows pop up as invalid
            #not entered the req
   #frame for ui
    frame = Frame(window, height=410, width=830, bg="white")
    frame.place(x=50, y=40)# placeed in men x axis and y axis
    
    
#HEADING INSIDE PARENT WIDGET
    heading = Label(frame, text="ADD CARD", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(relx=0.5, rely=0.05, anchor=CENTER)
    #centre of parent widget,down from top parent,coincide
    
#CHOOSING CARTYPE    
    cardtype = Combobox(frame, width=35, state="readonly", font=("Microsoft YaHei UI Light", 11))
    #cant edit readonly
    cardtype['values'] = ("Select Card Type", "Debit Card", "Credit Card")
    cardtype.current(0)  # Select the default option
    cardtype.place(x=25, y=100)

#CARDNO ENTRY
    cardno = Entry(frame, width=35, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    cardno.place(x=30, y=170)
    cardno.insert(0, "Card Number")

    cardno.bind("<FocusIn>", enter_cardno)
    cardno.bind("<FocusOut>", leave_cardno)#binds cardno entry and leave
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=198)#line under placeholder(SEPARATOR LINE)

#EXPIRY DATE ENTRY
    expdt = Entry(frame, width=35, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    expdt.place(x=495, y=100)
    expdt.insert(0, "Expiry Date")

    expdt.bind("<FocusIn>", enter_expdt)
    expdt.bind("<FocusOut>", leave_expdt)
    Frame(frame, width=295, height=2, bg="black").place(x=490, y=127)

#CVV ENTRY
    cvv = Entry(frame, width=35, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    cvv.place(x=495, y=170)
    cvv.insert(0, "CVV")

    cvv.bind("<FocusIn>", enter_cvv)
    cvv.bind("<FocusOut>", leave_cvv)
    Frame(frame, width=295, height=2, bg="black").place(x=490, y=198)


#BUTTON TO SUBMIT
    Button(frame, width=39, pady=7, text="SUBMIT", bg="#57a1f8", fg="white", border=7, command=addcard).place(x=280, y=280)

    window.mainloop()
    #window resizing or closing

addcard_page()