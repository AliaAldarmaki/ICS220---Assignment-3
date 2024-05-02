# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import pickle

# Define a class to represent a supplier
class Supplier:
    # Initialize supplier attributes
    def __init__(self, supplier_id, name, address, contact_number, service_provided, min_guests, max_guests):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.service_provided = service_provided
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Convert supplier information to a dictionary
    def to_dict(self):
        return {
            'supplier_id': self.supplier_id,
            'name': self.name,
            'address': self.address,
            'contact_number': self.contact_number,
            'service_provided': self.service_provided,
            'min_guests': self.min_guests,
            'max_guests': self.max_guests
        }

# Define a class to manage supplier
class SupplierManager:
    # Initialize the supplier list
    def __init__(self):
        self.supplier_list = []

    # Open a window to add a new supplier
    def add_supplier_window(self):
        # Create a new window
        add_window = tk.Toplevel()
        add_window.title("Add Supplier")
        add_window.geometry("300x300")
        add_window.configure(bg="light green")

        # Labels for supplier information
        tk.Label(add_window, text="Supplier ID:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Name:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Address:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Contact Number:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Service Provided:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Min Guests:").grid(row=5, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Max Guests:").grid(row=6, column=0, padx=10, pady=10)

        # Entry fields for supplier information
        self.supplier_id_entry = tk.Entry(add_window)
        self.supplier_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_entry = tk.Entry(add_window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.address_entry = tk.Entry(add_window)
        self.address_entry.grid(row=2, column=1, padx=10, pady=10)
        self.contact_entry = tk.Entry(add_window)
        self.contact_entry.grid(row=3, column=1, padx=10, pady=10)
        self.service_entry = tk.Entry(add_window)
        self.service_entry.grid(row=4, column=1, padx=10, pady=10)
        self.min_guests_entry = tk.Entry(add_window)
        self.min_guests_entry.grid(row=5, column=1, padx=10, pady=10)
        self.max_guests_entry = tk.Entry(add_window)
        self.max_guests_entry.grid(row=6, column=1, padx=10, pady=10)

        # Button to add supplier
        add_button = tk.Button(add_window, text="Add Supplier", command=self.add_supplier)
        add_button.grid(row=7, column=0, columnspan=2, pady=10)

    # Method to add a new supplier
    def add_supplier(self):
        # Get supplier information from entry fields
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_number = self.contact_entry.get()
        service_provided = self.service_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        # Define validation functions
        def is_valid_supplier_id(supplier_id):
            return supplier_id.isdigit()

        def is_valid_name(name):
            return name.replace(" ", "").isalpha()

        # Validate input
        if not supplier_id or not is_valid_supplier_id(supplier_id):
            messagebox.showerror("Error", "Please enter a valid supplier ID (integer).")
            return
        if not name or not is_valid_name(name):
            messagebox.showerror("Error", "Please enter a valid name (alphabetical characters only).")
            return

        # Create supplier object
        supplier = Supplier(supplier_id, name, address, contact_number, service_provided, min_guests, max_guests)
        self.supplier_list.append(supplier.to_dict()) # Convert to dictionary and append

        try:
            with open("supplier_pkl_file.pkl", "wb") as file:
                 # Save supplier data to a pickle file
                pickle.dump(self.supplier_list, file)
            messagebox.showinfo("Success", "Supplier added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add supplier: {e}")

        # Clear entry fields
        self.clear_entries()

    # Method to open a window for editing a supplier
    def edit_supplier_window(self):
        # Create a new window for editing supplier
        edit_window = tk.Toplevel()
        edit_window.title("Edit Supplier")
        edit_window.geometry("300x300")
        edit_window.configure(bg="light green")

        # Label
        tk.Label(edit_window, text="Enter Supplier ID:").grid(row=0, column=0, padx=10, pady=10)

        # Entry field for supplier ID
        self.edit_id_entry = tk.Entry(edit_window)
        self.edit_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Search Button
        search_button = tk.Button(edit_window, text="Search", command=self.search_supplier)
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to search for a supplier by ID
    def search_supplier(self):
        supplier_id = self.edit_id_entry.get()
        found = False
        try:
            with open("supplier_pkl_file.pkl", "rb") as file:
                self.supplier_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Supplier data file not found")
            return

        # Search for supplier in the supplier list
        for supplier in self.supplier_list:
            if supplier['supplier_id'] == supplier_id:
                found = True
                self.show_edit_supplier_window(supplier)
                break

        if not found:
            messagebox.showerror("Error", "Supplier ID not found")

    # Method to display window for editing supplier details
    def show_edit_supplier_window(self, supplier, edit_window):
        edit_window.destroy()  # Close the previous edit window
        # Open new window for supplier details
        edit_window = tk.Toplevel()
        edit_window.title("Edit Supplier")
        edit_window.geometry("300x300")
        edit_window.configure(bg="light green")

        # Labels
        tk.Label(edit_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Address:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Contact Number:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Service Provided:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Min Guests:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Max Guests:").grid(row=5, column=0, padx=10, pady=10)

        self.name_var = tk.StringVar()
        self.name_var.set(supplier['name'])
        self.address_var = tk.StringVar()
        self.address_var.set(supplier['address'])
        self.contact_var = tk.StringVar()
        self.contact_var.set(supplier['contact_number'])
        self.service_var = tk.StringVar()
        self.service_var.set(supplier['service_provided'])
        self.min_guests_var = tk.StringVar()
        self.min_guests_var.set(supplier['min_guests'])
        self.max_guests_var = tk.StringVar()
        self.max_guests_var.set(supplier['max_guests'])

        # Entry fields with existing supplier data
        name_entry = tk.Entry(edit_window, textvariable=self.name_var)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        address_entry = tk.Entry(edit_window, textvariable=self.address_var)
        address_entry.grid(row=1, column=1, padx=10, pady=10)
        contact_entry = tk.Entry(edit_window, textvariable=self.contact_var)
        contact_entry.grid(row=2, column=1, padx=10, pady=10)
        service_entry = tk.Entry(edit_window, textvariable=self.service_var)
        service_entry.grid(row=3, column=1, padx=10, pady=10)
        min_guests_entry = tk.Entry(edit_window, textvariable=self.min_guests_var)
        min_guests_entry.grid(row=4, column=1, padx=10, pady=10)
        max_guests_entry = tk.Entry(edit_window, textvariable=self.max_guests_var)
        max_guests_entry.grid(row=5, column=1, padx=10, pady=10)

        # Update Button
        save_button = tk.Button(edit_window, text="Save Changes", command=lambda: self.save_supplier(supplier))
        save_button.grid(row=6, column=0, columnspan=2, pady=10)

    def save_supplier(self, old_supplier):
        new_supplier = Supplier(old_supplier['supplier_id'], self.name_var.get(), self.address_var.get(),
                                self.contact_var.get(), self.service_var.get(), self.min_guests_var.get(),
                                self.max_guests_var.get())

        self.supplier_list.remove(old_supplier)
        self.supplier_list.append(new_supplier.to_dict())

        try:
            with open("supplier_pkl_file.pkl", "wb") as file:
                pickle.dump(self.supplier_list, file)
            messagebox.showinfo("Success", "Supplier details updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update supplier: {e}")

    # Method to open window for deleting a supplier
    def delete_supplier_window(self):
        delete_window = tk.Toplevel()
        delete_window.title("Delete Supplier")
        delete_window.geometry("250x150")
        delete_window.configure(bg="light green")

        # Label
        # Entry field for supplier ID
        tk.Label(delete_window, text="Enter Supplier ID:").grid(row=0, column=0, padx=10, pady=10)
        self.delete_id_entry = tk.Entry(delete_window)
        self.delete_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Delete Button
        delete_button = tk.Button(delete_window, text="Delete", command=self.delete_supplier)
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to delete a supplier
    def delete_supplier(self):
        supplier_id = self.delete_id_entry.get()
        found = False
        try:
            with open("supplier_pkl_file.pkl", "rb") as file:
                self.supplier_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Supplier data file not found")
            return

        # Search for supplier in the list
        for supplier in self.supplier_list:
            if supplier['supplier_id'] == supplier_id:
                found = True
                # Remove supplier from list
                self.supplier_list.remove(supplier)
                try:
                    # Save updated list to pickle file
                    with open("supplier_pkl_file.pkl", "wb") as file:
                        pickle.dump(self.supplier_list, file)
                    messagebox.showinfo("Success", "Supplier deleted successfully!")
                    return
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete supplier: {e}")

        # Display message if supplier not found
        if not found:
            messagebox.showerror("Error", "Supplier ID not found")

    # Method to open window for displaying all supplier
    def display_supplier_window(self):
        display_window = tk.Toplevel()
        display_window.title("Display Suppliers")
        display_window.geometry("500x300")
        display_window.configure(bg="light blue")

        # Create a text widget to display supplier information
        text_widget = tk.Text(display_window, bg="light yellow", fg="black", font=("Arial", 12), wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        try:
            # Load supplier data from pickle file
            with open("supplier_pkl_file.pkl", "rb") as file:
                self.supplier_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Supplier data file not found")

        # Display each supplier's information
        for supplier in self.supplier_list:
            text_widget.insert(tk.END, f"Supplier ID: {supplier['supplier_id']}\n")
            text_widget.insert(tk.END, f"Name: {supplier['name']}\n")
            text_widget.insert(tk.END, f"Address: {supplier['address']}\n")
            text_widget.insert(tk.END, f"Contact Number: {supplier['contact_number']}\n")
            text_widget.insert(tk.END, f"Service Provided: {supplier['service_provided']}\n")
            text_widget.insert(tk.END, f"Min Guests: {supplier['min_guests']}\n")
            text_widget.insert(tk.END, f"Max Guests: {supplier['max_guests']}\n\n")

        # Disable text widget to make it read-only
        text_widget.config(state=tk.DISABLED)