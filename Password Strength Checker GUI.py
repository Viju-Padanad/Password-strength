# Password Strength Checker GUI

import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()
    if len(password) < 8:
        messagebox.showwarning("Weak Password", "Password must be at least 8 characters long.")
    elif not re.search("[a-z]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one lowercase letter.")
    elif not re.search("[A-Z]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one uppercase letter.")
    elif not re.search("[0-9]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one digit.")
    elif not re.search("[@#$%^&+=]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one special character.")
    else:
        messagebox.showinfo("Strong Password", "Your password is strong!")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create a label
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, show='*', width=30)
entry.pack(pady=10)

# Create a button to check password strength
button = tk.Button(root, text="Check Strength", command=check_password_strength)
button.pack(pady=20)

# Run the application
root.mainloop()
