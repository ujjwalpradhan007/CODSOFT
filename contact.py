import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        else:
            return False

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]['phone_number'] = phone_number
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            return True
        else:
            return False

    def search_contact(self, keyword):
        search_results = []
        for name, contact_info in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in contact_info['phone_number']:
                search_results.append((name, contact_info['phone_number'], contact_info['email'], contact_info['address']))
        return search_results

    def view_contacts(self):
        return list(self.contacts.keys())

def add_contact_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Contact")

    tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    tk.Label(add_window, text="Phone Number:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    tk.Label(add_window, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    tk.Label(add_window, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="e")

    name_entry = tk.Entry(add_window, width=30)
    phone_entry = tk.Entry(add_window, width=30)
    email_entry = tk.Entry(add_window, width=30)
    address_entry = tk.Entry(add_window, width=30)

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)
    email_entry.grid(row=2, column=1, padx=5, pady=5)
    address_entry.grid(row=3, column=1, padx=5, pady=5)

    def add_contact():
        name = name_entry.get()
        phone_number = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone_number:
            contact_book.add_contact(name, phone_number, email, address)
            messagebox.showinfo("Success", "Contact added successfully!")
            add_window.destroy()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required!")

    tk.Button(add_window, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, pady=10)

def view_contacts_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Contacts")

    contacts_list = tk.Listbox(view_window, width=60)
    contacts_list.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    for contact in contact_book.view_contacts():
        contacts_list.insert(tk.END, contact)

    def delete_contact():
        selected_contact = contacts_list.curselection()
        if selected_contact:
            contact_name = contacts_list.get(selected_contact)
            confirmed = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {contact_name}?")
            if confirmed:
                contact_book.delete_contact(contact_name)
                contacts_list.delete(selected_contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    delete_button = ttk.Button(view_window, text="Delete Contact", command=delete_contact)
    delete_button.grid(row=1, column=0, pady=10, sticky="w")

def search_contacts_window():
    search_window = tk.Toplevel(root)
    search_window.title("Search Contacts")

    tk.Label(search_window, text="Search by Name or Phone Number:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    search_entry = tk.Entry(search_window, width=30)
    search_entry.grid(row=0, column=1, padx=5, pady=5)

    def search_contacts():
        keyword = search_entry.get()
        search_results = contact_book.search_contact(keyword)
        search_result_text = ""
        for result in search_results:
            search_result_text += f"Name: {result[0]}\nPhone Number: {result[1]}\nEmail: {result[2]}\nAddress: {result[3]}\n\n"
        messagebox.showinfo("Search Results", search_result_text.strip())

    search_button = ttk.Button(search_window, text="Search", command=search_contacts)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

root = tk.Tk()
root.title("Contact Book")
icon = Image.open("image/contacts.png")
icon = ImageTk.PhotoImage(icon)
root.iconphoto(True, icon)

contact_book = ContactBook()

add_button = ttk.Button(root, text="Add Contact", command=add_contact_window)
add_button.pack(pady=5)

view_button = ttk.Button(root, text="View Contacts", command=view_contacts_window)
view_button.pack(pady=5)

search_button = ttk.Button(root, text="Search Contacts", command=search_contacts_window)
search_button.pack(pady=5)

root.mainloop()
