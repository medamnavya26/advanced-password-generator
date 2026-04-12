import random
import string
import tkinter as tk

# ---------------- PASSWORD STRENGTH ----------------
def check_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*" for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 8 and score >= 3:
        return "Strong 💪"
    elif length >= 6:
        return "Medium 🙂"
    else:
        return "Weak 😐"

# ---------------- GENERATE PASSWORD ----------------
def generate_password():
    try:
        length = int(length_entry.get())
    except:
        result_label.config(text="Enter valid number!")
        return

    website = website_entry.get()

    letters = string.ascii_letters
    chars = letters

    if number_var.get():
        chars += string.digits

    if symbol_var.get():
        chars += string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(chars)

    result_label.config(text=password)

    # Strength
    strength = check_strength(password)
    strength_label.config(text="Strength: " + strength)

    # Save
    if website != "":
        with open("passwords.txt", "a") as file:
            file.write(website + ": " + password + "\n")

# ---------------- COPY ----------------
def copy_password():
    password = result_label.cget("text")
    if password != "":
        root.clipboard_clear()
        root.clipboard_append(password)
        status_label.config(text="Copied! ✅")

# ---------------- CLEAR ----------------
def clear_all():
    website_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    result_label.config(text="")
    strength_label.config(text="")
    status_label.config(text="")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.configure(bg="#e6f2ff")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#e6f2ff").pack(pady=10)

# Website
tk.Label(root, text="Website", bg="#e6f2ff").pack()
website_entry = tk.Entry(root)
website_entry.pack(pady=5)

# Length
tk.Label(root, text="Password Length", bg="#e6f2ff").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkboxes
number_var = tk.IntVar()
symbol_var = tk.IntVar()

tk.Checkbutton(root, text="Include Numbers", variable=number_var, bg="#e6f2ff").pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var, bg="#e6f2ff").pack()

# Buttons
tk.Button(root, text="Generate", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Copy", command=copy_password, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(root, text="Clear", command=clear_all, bg="#f44336", fg="white").pack(pady=5)

# Output
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e6f2ff")
result_label.pack(pady=10)

strength_label = tk.Label(root, text="", bg="#e6f2ff")
strength_label.pack()

status_label = tk.Label(root, text="", bg="#e6f2ff")
status_label.pack()

# Run
root.mainloop()
    