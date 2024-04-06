from tkinter import *

def register_page():
    #creates a tkinter window
    window = Tk()
    window.title("Register") 
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False) #makes window non resiable 
    
    #first name field
    #entry field gains focus
    def enter_fn(event):
        if first_name_entry.get() == 'First Name':
            first_name_entry.delete(0, "end")
    #entry field loses focus   
    def leave_fn(event):
        if first_name_entry.get() == '':
            first_name_entry.insert(0, "First Name") 

    #last name field
    def enter_ln(event):
        if last_name_entry.get() == 'Last Name' :
            last_name_entry.delete(0, "end")
    def leave_ln(event):
        if last_name_entry.get() == '':
            last_name_entry.insert(0, "Last Name")
    
    #email field       
    def enter_email(event):
        if useremail.get() == 'Email':
            useremail.delete(0, "end")
    def leave_email(event):
        if useremail.get() == '':
            useremail.insert(0, "Email")        

    #country field       
    def enter_country(event):
        if usercountry.get() == 'Country':
            usercountry.delete(0, "end")
    def leave_country(event):
        if usercountry.get() == '':
            usercountry.insert(0, "Country") 
    
    #phone number
    def enter_phn(event):
        if userphone.get() == 'Phone Number':
            userphone.delete(0, "end")
    def leave_phn(event):
        if userphone.get() == '':
            userphone.insert(0, "Phone Number")   

    #date of birth       
    def enter_dob(event):
        if userdob.get() == 'Date of Birth':
            userdob.delete(0, "end")
    def leave_dob(event):
        if userdob.get() == '':
            userdob.insert(0, "Date of Birth")                                  
    
    #creates the frame within the window
    frame = Frame(window, height=410, width=830, bg='white')
    frame.place(x=50, y=40)
    
    #creates heading of name register
    heading = Label(frame, text="Register", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(relx=0.5, rely=0.05, anchor=CENTER)
    
     # Create entry field for first name
    first_name_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    first_name_entry.place(x=30, y=80) 
    first_name_entry.insert(0, "First Name")#inserts default text
    first_name_entry.bind("<FocusIn>", enter_fn)#function will be called when the entry field gains focus
    first_name_entry.bind("<FocusOut>", leave_fn)# function will be called when the entry field loses focus
    Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)
    

    # Create entry field for last name
    last_name_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    last_name_entry.place(x=30, y=150)
    last_name_entry.insert(0, "Last Name")
    last_name_entry.bind("<FocusIn>", enter_ln)
    last_name_entry.bind("<FocusOut>", leave_ln)
    Frame(frame, width=295, height=2, bg="black").place(x=25,y=178)
    
    #create entr field for email
    useremail = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
    useremail.place(x=30, y=220)  
    useremail.insert(0,"Email")
    useremail.bind("<FocusIn>", enter_email)
    useremail.bind("<FocusOut>", leave_email)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)
    
    #create entry field for date of birth 
    userdob = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    userdob.place(x=495, y=80)  
    userdob.insert(0, "Date of Birth")
    userdob.bind("<FocusIn>", enter_dob)
    userdob.bind("<FocusOut>", leave_dob)
    Frame(frame, width=295, height=2, bg="black").place(x=490,y=107)
    
    #create entry field for country
    usercountry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    usercountry.place(x=495, y=150)  
    usercountry.insert(0, "Country")
    usercountry.bind("<FocusIn>", enter_country)
    usercountry.bind("<FocusOut>", leave_country)
    Frame(frame, width=295, height=2, bg="black").place(x=490,y=178)
    
    #create entry field for phone number
    userphone = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    userphone.place(x=495, y=220)  
    userphone.insert(0, "Phone Number")
    userphone.bind("<FocusIn>", enter_phn)
    userphone.bind("<FocusOut>", leave_phn)
    Frame(frame,width=295,height=2,bg="black").place(x=490,y=247)
    
    #create signup button
    Button(frame,width=39,pady=7,text="Sign up", bg="#57a1f8",fg="white",border=0).place(x=280,y=280)
    Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=350, y=340)
    #create signin button
    Button(frame,width=6,text="Sign in",border=0,bg="white",cursor="hand2",fg="#57a1f8").place(x=460, y=340)
    
    window.mainloop()

# Call the function to run the UI
register_page()
