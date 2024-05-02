# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import pickle

# Define a class to represent a guest
class Guest:
    # Initialize guest attributes
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Convert guest information to a dictionary
    def to_dict(self):
        return {
            'guest_id': self.guest_id,
            'name': self.name,
            'address': self.address,
            'contact_details': self.contact_details
        }
    
# Define a class to manage guest  
class GuestManager:
    # Initialize the guest list
    def __init__(self):
        self.guest_list = []

    # Open a window to add a new guest
    def add_guest_window(self):
        # Create a new window
        self.add_window = tk.Toplevel()
        self.add_window.title("Add Guest")
        self.add_window.geometry("400x300")
        self.add_window.configure(bg="light green")

        # Labels for guest information
        tk.Label(self.add_window, text="Guest ID:", bg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_window, text="Name:", bg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_window, text="Address:", bg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_window, text="Contact Details:", bg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="e")

        # Entry fields for guest information
        self.guest_id_entry = tk.Entry(self.add_window)
        self.guest_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_entry = tk.Entry(self.add_window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.address_entry = tk.Entry(self.add_window)
        self.address_entry.grid(row=2, column=1, padx=10, pady=10)
        self.contact_details_entry = tk.Entry(self.add_window)
        self.contact_details_entry.grid(row=3, column=1, padx=10, pady=10)

        # Button to add guest
        add_button = tk.Button(self.add_window, text="Add Guest", bg="blue", fg="black", font=("Arial", 12, "bold"), command=self.add_guest)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Method to add a new guest
    def add_guest(self):
        # Get guest information from entry fields
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()

        # Define validation functions
        def is_valid_guest_id(guest_id):
            return guest_id.isdigit()

        def is_valid_name(name):
            return name.replace(" ", "").isalpha()

        # Validate input
        if not guest_id or not is_valid_guest_id(guest_id):
            messagebox.showerror("Error", "Please enter a valid guest ID (integer).")
            return
        if not name or not is_valid_name(name) or not address:
            messagebox.showerror("Error", "Please fill in all required fields with valid input.")
            return

        # Create guest object
        guest = Guest(guest_id, name, address, contact_details)
        self.guest_list.append(guest.to_dict())  # Convert to dictionary and append

        # Save guest data to a pickle file
        try:
            with open("guest_pkl_file.pkl", "wb") as file:
                pickle.dump(self.guest_list, file)
            messagebox.showinfo("Success", "Guest added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add guest: {e}")

        # Clear entry fields
        self.guest_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_details_entry.delete(0, tk.END)

    # Method to open a window for editing a guest
    def edit_guest_window(self):
        # Create a new window for editing guest
        edit_window = tk.Toplevel()
        edit_window.title("Edit Guest")
        edit_window.geometry("280x300")
        edit_window.configure(bg="light green")

        # Label
        tk.Label(edit_window, text="Enter Guest ID:", bg="light green").grid(row=0, column=0, padx=10, pady=10)

        # Entry field for Guest ID
        guest_id_entry = tk.Entry(edit_window)
        guest_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Search Button
        search_button = tk.Button(edit_window, text="Search", bg="green", fg="black", font=("Arial", 12, "bold"),
                                  command=lambda: self.search_guest(guest_id_entry.get(), edit_window))
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to search for a guest by ID
    def search_guest(self, guest_id, edit_window):
        found = False
        try:
            with open("guest_pkl_file.pkl", "rb") as file:
                self.guest_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Guest data file not found")
            return

        # Search for guest in the guest list
        for guest in self.guest_list:
            if guest['guest_id'] == guest_id:
                found = True
                self.show_edit_guest_window(guest, edit_window)
                break

        if not found:
            messagebox.showerror("Error", "Guest ID not found")    

    # Method to display window for editing guest details
    def show_edit_guest_window(self, guest, edit_window):
        edit_window.destroy()  # Close the previous edit window
        # Open new window for guest details
        edit_window = tk.Toplevel()
        edit_window.title("Edit Guest")
        edit_window.geometry("300x250")
        edit_window.configure(bg="light green")

        # Labels
        tk.Label(edit_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Address:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Contact Details:").grid(row=2, column=0, padx=10, pady=10)

        self.name_var = tk.StringVar()
        self.name_var.set(guest['name'])
        self.address_var = tk.StringVar()
        self.address_var.set(guest['address'])
        self.contact_var = tk.StringVar()
        self.contact_var.set(guest['contact_details'])

        # Entry fields with existing guest data
        name_entry = tk.Entry(edit_window, textvariable=self.name_var)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        address_entry = tk.Entry(edit_window, textvariable=self.address_var)
        address_entry.grid(row=1, column=1, padx=10, pady=10)
        contact_entry = tk.Entry(edit_window, textvariable=self.contact_var)
        contact_entry.grid(row=2, column=1, padx=10, pady=10)

         # Update Button
        update_button = tk.Button(edit_window, text="Update", command=lambda: self.update_guest(guest))
        update_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Method to update guest details
    def update_guest(self, old_guest):
        new_name = self.name_var.get()
        new_address = self.address_var.get()
        new_contact = self.contact_var.get()

        updated_guest = Guest(old_guest['guest_id'], new_name, new_address, new_contact)

        self.guest_list.remove(old_guest)
        self.guest_list.append(updated_guest.to_dict())
        # Save to pickle file
        try:
            with open("guest_pkl_file.pkl", "wb") as file:
                pickle.dump(self.guest_list, file)
            messagebox.showinfo("Success", "Guest updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update guest: {e}")

     # Method to open window for deleting a guest
    def delete_guest_window(self):
        delete_window = tk.Toplevel()
        delete_window.title("Delete Guest")
        delete_window.geometry("250x100")
        delete_window.configure(bg="light green")

        # Label
        # Entry field for guest ID
        tk.Label(delete_window, text="Enter Guest ID:").grid(row=0, column=0, padx=10, pady=10)
        self.delete_id_entry = tk.Entry(delete_window)
        self.delete_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Delete Button
        delete_button = tk.Button(delete_window, text="Delete", command=self.delete_guest)
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to delete a guest
    def delete_guest(self):
        guest_id = self.delete_id_entry.get()
        found = False
        try:
            with open("guest_pkl_file.pkl", "rb") as file:
                self.guest_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Guest data file not found")
            return

        # Search for guest in the list
        for guest in self.guest_list:
            if guest['guest_id'] == guest_id:
                found = True
                # Remove guest from list
                self.guest_list.remove(guest)
                try:
                    # Save updated list to pickle file
                    with open("guest_pkl_file.pkl", "wb") as file:
                        pickle.dump(self.guest_list, file)
                    messagebox.showinfo("Success", "Guest deleted successfully!")
                    return
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete guest: {e}")

        # Display message if guest not found
        if not found:
            messagebox.showerror("Error", "Guest ID not found")

    # Method to open window for displaying all guest
    def display_guest_window(self):
        display_window = tk.Toplevel()
        display_window.title("Guest List")
        display_window.geometry("400x300")
        display_window.configure(bg="light blue")

        # Create a text widget to display guest information
        text_widget = tk.Text(display_window)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Load guest data from pickle file
        try:
            with open("guest_pkl_file.pkl", "rb") as file:
                self.guest_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Guest data file not found")
            return

        # Display each guest's information
        for guest in self.guest_list:
            text_widget.insert(tk.END, f"Guest ID: {guest['guest_id']}\n")
            text_widget.insert(tk.END, f"Name: {guest['name']}\n")
            text_widget.insert(tk.END, f"Address: {guest['address']}\n")
            text_widget.insert(tk.END, f"Contact Details: {guest['contact_details']}\n\n")

        # Disable text widget to make it read-only
        text_widget.config(state=tk.DISABLED)