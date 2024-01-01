import tkinter as tk
from tkinter import messagebox

def press_key(event):
    """Function to handle keyboard presses"""
    key = event.char
    if key in '0123456789':
        number_pressed(key)
    elif key in ['+', '-', '*', '/']:
        operation_pressed(key)
    elif key == '\r':
        calculate()
    elif key == '\x08':
        clear_entry()

def number_pressed(number):
    current_text = entry_display.get()
    if current_text == "0":
        entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, number)

def operation_pressed(operator):
    entry_display.insert(tk.END, operator)

def clear_entry():
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, "0")

def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")

root = tk.Tk()
root.title("System-like Calculator")

root.bind('<Key>', press_key)

entry_display = tk.Entry(root, font=('Arial', 18), justify=tk.RIGHT)
entry_display.insert(tk.END, "0")
entry_display.grid(row=0, column=0, columnspan=4, sticky="nsew")

button_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in button_list:
    if button != '=':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14),
                  command=lambda button=button: number_pressed(button) if button.isdigit() or button == '.' else operation_pressed(button)).grid(row=row_val, column=col_val, sticky="nsew")
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 14),
                  command=calculate).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
