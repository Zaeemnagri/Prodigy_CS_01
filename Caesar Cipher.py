import tkinter as tk
from tkinter import ttk, messagebox



def encrypt_text():
    try:
        text = message_entry.get()
        shift = int(shift_entry.get())
        result = ""

        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char

        output_var.set(result)

    except:
        messagebox.showerror("Error", "Please enter a valid shift value")


def decrypt_text():
    try:
        text = message_entry.get()
        shift = int(shift_entry.get())
        result = ""

        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += char

        output_var.set(result)

    except:
        messagebox.showerror("Error", "Please enter a valid shift value")


def clear_all():
    message_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    output_var.set("")



root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("420x350")
root.configure(bg="#2c3e50")


style = ttk.Style()
style.theme_use("default")

style.configure("TLabel",
                background="#2c3e50",
                foreground="white",
                font=("Segoe UI", 11))

style.configure("TButton",
                font=("Segoe UI", 10, "bold"),
                padding=6)

style.configure("TEntry",
                padding=5)


title = tk.Label(root,
                 text="Caesar Cipher Encryption",
                 font=("Segoe UI", 16, "bold"),
                 bg="#2c3e50",
                 fg="#ecf0f1")
title.pack(pady=15)

ttk.Label(root, text="Enter Message").pack(anchor="w", padx=40)
message_entry = ttk.Entry(root, width=40)
message_entry.pack(pady=5)


ttk.Label(root, text="Shift Value").pack(anchor="w", padx=40)
shift_entry = ttk.Entry(root, width=10)
shift_entry.pack(pady=5)


btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(btn_frame, text="Encrypt",
                        bg="#27ae60", fg="white",
                        width=10, command=encrypt_text)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(btn_frame, text="Decrypt",
                        bg="#2980b9", fg="white",
                        width=10, command=decrypt_text)
decrypt_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear",
                      bg="#c0392b", fg="white",
                      width=10, command=clear_all)
clear_btn.grid(row=0, column=2, padx=5)


ttk.Label(root, text="Result").pack(anchor="w", padx=40)

output_var = tk.StringVar()
output_box = ttk.Entry(root, textvariable=output_var,
                       width=40, font=("Segoe UI", 11, "bold"))
output_box.pack(pady=10)


root.mainloop()