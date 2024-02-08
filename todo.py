import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")


icon = Image.open("image/task.png")
icon = ImageTk.PhotoImage(icon)
root.iconphoto(True, icon)

# Main Frame
main_frame = ttk.Frame(root, padding=(20, 10), style="Main.TFrame")
main_frame.grid(row=0, column=0, sticky="nsew")

# Task List
listbox_tasks = tk.Listbox(main_frame, height=15, width=50, font=("Arial", 12, "bold"), bg="white", bd=0, highlightthickness=0, selectbackground="lightblue")
listbox_tasks.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

scrollbar_tasks = tk.Scrollbar(main_frame, command=listbox_tasks.yview)
scrollbar_tasks.grid(row=0, column=1, pady=10, sticky="nsew")
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

# Task Entry
entry_task = ttk.Entry(main_frame, width=50, font=("Arial", 12, "bold"))
entry_task.grid(row=1, column=0, padx=(0, 10), pady=(0, 10), sticky="ew")
entry_task.focus()

# Add Task 
add_img = Image.open("image/add.png")
add_img.thumbnail((16, 16))
add_img = ImageTk.PhotoImage(add_img)
button_add_task = ttk.Button(main_frame, text="Add Task", width=20, image=add_img, compound="left", command=add_task, style="Add.TButton")
button_add_task.grid(row=1, column=1, pady=(0, 10), sticky="ew")

# Remove Task 
remove_img = Image.open("image/delete.png")
remove_img.thumbnail((16, 16))
remove_img = ImageTk.PhotoImage(remove_img)
button_remove_task = ttk.Button(main_frame, text="Remove Task", width=20, image=remove_img, compound="left", command=remove_task, style="Remove.TButton")
button_remove_task.grid(row=2, column=0, padx=(0, 10), sticky="ew")

# Clear All Tasks
clear_img = Image.open("image/broom.png")
clear_img.thumbnail((16, 16))
clear_img = ImageTk.PhotoImage(clear_img)
button_clear_tasks = ttk.Button(main_frame, text="Clear All Tasks", width=20, image=clear_img, compound="left", command=clear_tasks, style="Clear.TButton")
button_clear_tasks.grid(row=2, column=1, sticky="ew")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Styling
style = ttk.Style()

style.configure("Main.TFrame", background="#f0f0f0")

style.configure("Add.TButton", background="black", foreground="white", font=("Arial", 10, "bold"))
style.map("Add.TButton", background=[("active", "#4cae4c")])

style.configure("Remove.TButton", background="black", foreground="white", font=("Arial", 10, "bold"))
style.map("Remove.TButton", background=[("active", "#c9302c")])

style.configure("Clear.TButton", background="black", foreground="white", font=("Arial", 10, "bold"))
style.map("Clear.TButton", background=[("active", "#46b8da")])

root.mainloop()
