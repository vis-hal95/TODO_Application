import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import ttk

# Function to add a new task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark the selected task as completed
def complete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, f"{task} ✓")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Create the main window
root = tk.Tk()
root.title("VISHAL To-Do List Application")
root.geometry("400x400")
root.resizable(False, False)  # Disable resizing for better layout control

# Apply a custom font for buttons and labels
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create a frame to hold the Listbox and Entry widgets for a more organized layout
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Create the Listbox widget to display tasks
listbox = tk.Listbox(frame, height=10, width=35, selectmode=tk.SINGLE, font=("Helvetica", 12), bd=0, highlightthickness=0)
listbox.pack(padx=10, pady=10)

# Create an Entry widget to input new tasks
entry = ttk.Entry(frame, width=35, font=("Helvetica", 12))
entry.pack(padx=10, pady=10)

# Create buttons with a modern look
add_button = ttk.Button(frame, text="Add Task", width=20, command=add_task, style="Accent.TButton")
add_button.pack(pady=5)

delete_button = ttk.Button(frame, text="Delete Task", width=20, command=delete_task, style="Danger.TButton")
delete_button.pack(pady=5)

complete_button = ttk.Button(frame, text="Mark as Completed", width=20, command=complete_task, style="Success.TButton")
complete_button.pack(pady=5)

# Style for themed buttons (Accent, Danger, Success)
style = ttk.Style()
style.configure("Accent.TButton", foreground="white", background="#4CAF50", font=custom_font)
style.configure("Danger.TButton", foreground="white", background="#f44336", font=custom_font)
style.configure("Success.TButton", foreground="white", background="#008CBA", font=custom_font)

# Run the main event loop
root.mainloop()


