import tkinter as tk
from tkinter import font

def add_task(event=None):
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        listbox.delete(listbox.curselection())
    except:
        pass

#main window
root = tk.Tk()
root.title("To-Do List App")

#window size and background color
root.geometry("400x402")
root.configure(bg="#1e1e1e")  # Dark background

# Fonts and styles
heading_font = font.Font(family="Helvetica", size=16, weight="bold")
button_font = font.Font(family="Helvetica", size=10, weight="bold")
listbox_font = font.Font(family="Helvetica", size=12)

# widget for typing tasks
entry = tk.Entry(root, width=30, font=listbox_font, bg="#333333", fg="#f5f5f5", insertbackground="white")
entry.pack(pady=10)
entry.bind("<Return>", add_task)

# Heading for the app
heading_label = tk.Label(root, text="To-Do List", font=heading_font, bg="#1e1e1e", fg="#f5f5f5")
heading_label.pack(pady=10)

# Button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task, font=button_font, bg="#4CAF50", fg="white", padx=10, pady=5)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=35, height=10, bg="#333333", fg="#f5f5f5", font=listbox_font, selectbackground="#4CAF50")
listbox.pack(pady=10)

# Button to delete tasks
delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=button_font, bg="#f44336", fg="white", padx=10, pady=5)
delete_button.pack(pady=5)

root.mainloop()
