import random
import re
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Requires Pillow library

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Medium"
    else:
        return "Weak"

def generate_strong_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    characters = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "!@#$%^&*()-_+=<>?"
    )
    
    password = [
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),  # At least one uppercase
        random.choice("abcdefghijklmnopqrstuvwxyz"),  # At least one lowercase
        random.choice("0123456789"),                    # At least one digit
        random.choice("!@#$%^&*()-_+=<>?")               # At least one special character
    ]
    
    password += random.choices(characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showerror("Error", "Password length should be at least 8 characters.")
            return
        strong_password = generate_strong_password(length)
        generated_password_label.config(text=f"Generated Password: {strong_password}", bg='lightblue')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def check_strength():
    password = password_entry.get()
    strength = check_password_strength(password)
    strength_label.config(text=f"Password Strength: {strength}", bg='lightgreen')

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker and Generator")

# Set the window size (width x height)
root.geometry("600x400")  # Set the window size

# Load and set the background image
bg_image = Image.open(r"V:\College topic\Python course\project-1(pass)\2.jpg")  # Use raw string
bg_image = bg_image.resize((600, 800), Image.LANCZOS)  # Resize to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Make background label fill the window

# Generate Password Section
length_label = tk.Label(root, text="Enter desired length for strong password (min 8):", bg='lightgray', font=("Arial", 12))
length_label.pack(pady=10)

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='blue', fg='white', font=("Arial", 12))
generate_button.pack(pady=10)

generated_password_label = tk.Label(root, text="", bg='lightblue', font=("Arial", 16))
generated_password_label.pack(pady=10)

# Check Password Strength Section
password_label = tk.Label(root, text="Enter a password to check its strength:", bg='lightgray', font=("Arial", 12))
password_label.pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 12))
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_strength, bg='green', fg='white', font=("Arial", 12))
check_button.pack(pady=10)

strength_label = tk.Label(root, text="", bg='lightgreen', font=("Arial", 12))
strength_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
