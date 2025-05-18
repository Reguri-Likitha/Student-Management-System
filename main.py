import tkinter as tk
from tkinter import ttk, messagebox
import database  # your database.py file

# Connect to DB and create table if not exists
database.connect_db()

# Create the main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("900x500")
root.configure(bg="#f0f0f0")

# Labels and entry fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Contact").grid(row=2, column=0, padx=10, pady=10)
contact_entry = tk.Entry(root)
contact_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Department").grid(row=3, column=0, padx=10, pady=10)
department_entry = tk.Entry(root)
department_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Semester").grid(row=4, column=0, padx=10, pady=10)
semester_entry = tk.Entry(root)
semester_entry.grid(row=4, column=1, padx=10, pady=10)

# Functions ----------------------------------------

def add_student():
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    department = department_entry.get()
    semester = semester_entry.get()

    if name == "" or email == "":
        messagebox.showerror("Error", "Name and Email are required!")
        return

    database.insert(name, email, contact, department, semester)
    messagebox.showinfo("Success", "Student added successfully!")
    clear_fields()
    view_students()

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)

def view_students():
    for row in tree.get_children():
        tree.delete(row)
    for row in database.view():
        tree.insert("", tk.END, values=row)

def delete_student():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "Please select a student to delete")
        return
    values = tree.item(selected, 'values')
    student_id = values[0]
    database.delete(student_id)
    messagebox.showinfo("Success", "Student deleted successfully!")
    view_students()
    clear_fields()

def update_student():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "Please select a student to update")
        return

    values = tree.item(selected, 'values')
    student_id = values[0]

    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    department = department_entry.get()
    semester = semester_entry.get()

    if name == "" or email == "":
        messagebox.showerror("Error", "Name and Email are required!")
        return

    database.update(student_id, name, email, contact, department, semester)
    messagebox.showinfo("Success", "Student updated successfully!")
    clear_fields()
    view_students()

def on_tree_select(event):
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, 'values')
    # Populate the entries with selected row data
    name_entry.delete(0, tk.END)
    name_entry.insert(0, values[1])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, values[2])
    contact_entry.delete(0, tk.END)
    contact_entry.insert(0, values[3])
    department_entry.delete(0, tk.END)
    department_entry.insert(0, values[4])
    semester_entry.delete(0, tk.END)
    semester_entry.insert(0, values[5])

# Buttons ------------------------------------------

tk.Button(root, text="Add Student", command=add_student).grid(row=5, column=0, pady=20)
tk.Button(root, text="View All", command=view_students).grid(row=5, column=1, pady=20)
tk.Button(root, text="Update Selected", command=update_student).grid(row=5, column=2, padx=10, pady=20)
tk.Button(root, text="Delete Selected", command=delete_student).grid(row=5, column=3, padx=10, pady=20)

# Treeview widget ----------------------------------

tree = ttk.Treeview(root, columns=("ID", "Name", "Email", "Contact", "Department", "Semester"), show='headings')
tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Define headings and column widths
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=130)

# Bind row select event
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Load data on startup
view_students()

# Start the GUI event loop
root.mainloop()
