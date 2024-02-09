import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 6:
        result_label.config(text="Password length must be at least 6 characters")
        return
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    result_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
