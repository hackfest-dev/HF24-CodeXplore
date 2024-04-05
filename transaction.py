import tkinter as tk
from tkinter import *
from tkinter import ttk
#from database import transaction  # Assuming transaction function is defined in database module

def transaction_page():
    # Function to go back to the home screen
    def back():
        root.destroy()  # Close the current window
        #home(login, loggedin_user)  # Call the home function to return to the home screen

    # Function to load transaction data into the Treeview
    # def load_data():
    #     # Retrieve transaction data for the logged-in user
    #     transactions = transaction(loggedin_user)
    #     # Insert data into the Treeview
    #     for data in transactions:
    #         tree.insert("", tk.END, values=data)

    # Create main window
    root = tk.Tk()
    root.title("Transaction History")  # Set window title
    root.geometry("925x500+300+200")  # Set window size and position
    root.configure(bg="#fff")  # Set window background color
    root.resizable(False, False)  # Disable window resizing

    # Create Treeview widget
    tree = ttk.Treeview(root, columns=("Date", "Phone", "Type", "Amount"), show="headings")

    # Define column headings
    tree.heading("Date", text="Date")
    tree.heading("Phone", text="Phone")
    tree.heading("Type", text="Type")
    tree.heading("Amount", text="Amount")

    # Set column widths
    tree.column("Date", width=100)
    tree.column("Phone", width=150)
    tree.column("Type", width=100)
    tree.column("Amount", width=100)

    # Set style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#f0f0f0", foreground="black")
    style.map("Treeview", background=[('selected', '#0078d7')])

    # Add a vertical scrollbar
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Load data into the Treeview
    #load_data()

    # Pack the Treeview
    tree.pack(fill="both", expand=True)

    # Create a button to go back
    Button(width=15, pady=7, text="Submit", bg="#57a1f8", fg="white", border=0, command=back).place(x=800, y=450)

    

    # Run the application
    root.mainloop()

transaction_page()