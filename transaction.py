import tkinter as tk
from tkinter import *
from tkinter import ttk

def transaction_page():
    # Function to go back to the home screen
    def back():
        root.destroy()  # Close the current window

    # Create main window
    root = tk.Tk()
    root.title("Transaction History")  # Set window title
    root.geometry("925x500+300+200")  # Set window size and position
    root.configure(bg="#fff")  # Set window background color
    root.resizable(False, False)  # Disable window resizing

    # Create Treeview widget
    tree = ttk.Treeview(root, columns=("Date", "Phone Number", "Type", "Amount"), show="headings")

    # Define column headings
    tree.heading("Date", text="Date")
    tree.heading("Phone Number", text="Phone Number")
    tree.heading("Type", text="Type")
    tree.heading("Amount", text="Amount")

    # Set column widths
    tree.column("Date", width=100)
    tree.column("Phone Number", width=150)
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

    # Pack the Treeview
    tree.pack(fill="both", expand=True)

    # Create a button to go back
    Button(width=15, pady=7, text="Back", bg="#57a1f8", fg="white", border=0, command=back).place(x=800, y=450)

    
    # Run the application
    root.mainloop()

transaction_page()
