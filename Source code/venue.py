# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import pickle

# Define a class to represent a venue
class Venue:
    # Initialize venue attributes
    def __init__(self, venue_id, name, address, contact_details, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Convert venue information to a dictionary
    def to_dict(self):
        return {
            'venue_id': self.venue_id,
            'name': self.name,
            'address': self.address,
            'contact_details': self.contact_details,
            'min_guests': self.min_guests,
            'max_guests': self.max_guests
        }

# Define a class to manage venue
class VenueManager:
    # Initialize the venue list
    def __init__(self):
        self.venue_list = []

    # Open a window to add a new venue
    def add_venue_window(self):
        # Create a new window
        add_window = tk.Toplevel()
        add_window.title("Add Venue")
        add_window.geometry("400x300")
        add_window.configure(bg="light green")

        # Labels for venue information
        tk.Label(add_window, text="Venue ID:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Name:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Address:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Contact Details:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Min Guests:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(add_window, text="Max Guests:").grid(row=5, column=0, padx=10, pady=10)

        # Entry fields for venue information
        self.venue_id_entry = tk.Entry(add_window)
        self.venue_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_entry = tk.Entry(add_window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.address_entry = tk.Entry(add_window)
        self.address_entry.grid(row=2, column=1, padx=10, pady=10)
        self.contact_entry = tk.Entry(add_window)
        self.contact_entry.grid(row=3, column=1, padx=10, pady=10)
        self.min_guests_entry = tk.Entry(add_window)
        self.min_guests_entry.grid(row=4, column=1, padx=10, pady=10)
        self.max_guests_entry = tk.Entry(add_window)
        self.max_guests_entry.grid(row=5, column=1, padx=10, pady=10)

         # Button to add venue
        add_button = tk.Button(add_window, text="Add Venue", command=self.add_venue)
        add_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Method to add a new venue
    def add_venue(self):
        # Get venue information from entry fields
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        # Define validation functions
        def is_valid_venue_id(venue_id):
            return venue_id.isdigit()

        def is_valid_name(name):
            return name.replace(" ", "").isalpha()

        # Validate input
        if not venue_id or not is_valid_venue_id(venue_id):
            messagebox.showerror("Error", "Please enter a valid venue ID (integer).")
            return
        if not name or not is_valid_name(name):
            messagebox.showerror("Error", "Please enter a valid name (alphabetical characters only).")
            return
        
        # Create venue object
        venue = Venue(venue_id, name, address, contact_details, min_guests, max_guests)
        self.venue_list.append(venue.to_dict()) # Convert to dictionary and append

        try:
            with open("venue_pkl_file.pkl", "wb") as file:
                # Save venue data to a pickle file
                pickle.dump(self.venue_list, file)
            messagebox.showinfo("Success", "Venue added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add venue: {e}")

    # Method to open a window for editing a venue
    def edit_venue_window(self):
        edit_window = tk.Toplevel()
        edit_window.title("Edit Venue")
        edit_window.geometry("400x300")
        edit_window.configure(bg="light green")

        # Label
        tk.Label(edit_window, text="Enter Venue ID:").grid(row=0, column=0, padx=10, pady=10)

        # Entry Fields
        self.edit_id_entry = tk.Entry(edit_window)
        self.edit_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Search Button
        search_button = tk.Button(edit_window, text="Search", command=self.search_venue)
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to search for a venue by ID
    def search_venue(self):
        venue_id = self.edit_id_entry.get()
        found = False
        try:
            with open("venue_pkl_file.pkl", "rb") as file:
                self.venue_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Venue data file not found")
            return

        # Search for venue in the venue list
        for venue in self.venue_list:
            if venue['venue_id'] == venue_id:
                found = True
                self.show_edit_venue_window(venue)
                break

        if not found:
            messagebox.showerror("Error", "Venue ID not found")

    # Method to display window for editing venue details
    def show_edit_venue_window(self, venue):
        # Open new window for venue details
        edit_window = tk.Toplevel()
        edit_window.title("Edit Venue")
        edit_window.geometry("300x300")
        edit_window.configure(bg="light green")

        # Labels
        tk.Label(edit_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Address:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Contact Number:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Min Guests:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(edit_window, text="Max Guests:").grid(row=4, column=0, padx=10, pady=10)

        self.name_var = tk.StringVar()
        self.name_var.set(venue['name'])
        self.address_var = tk.StringVar()
        self.address_var.set(venue['address'])
        self.contact_var = tk.StringVar()
        self.contact_var.set(venue['contact_details'])
        self.min_guests_var = tk.StringVar()
        self.min_guests_var.set(venue['min_guests'])
        self.max_guests_var = tk.StringVar()
        self.max_guests_var.set(venue['max_guests'])

        # Entry fields with existing venue data
        name_entry = tk.Entry(edit_window, textvariable=self.name_var)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        address_entry = tk.Entry(edit_window, textvariable=self.address_var)
        address_entry.grid(row=1, column=1, padx=10, pady=10)
        contact_entry = tk.Entry(edit_window, textvariable=self.contact_var)
        contact_entry.grid(row=2, column=1, padx=10, pady=10)
        min_guests_entry = tk.Entry(edit_window, textvariable=self.min_guests_var)
        min_guests_entry.grid(row=3, column=1, padx=10, pady=10)
        max_guests_entry = tk.Entry(edit_window, textvariable=self.max_guests_var)
        max_guests_entry.grid(row=4, column=1, padx=10, pady=10)

        # Save Button
        save_button = tk.Button(edit_window, text="Save Changes", command=lambda: self.save_venue(venue))
        save_button.grid(row=5, column=0, columnspan=2, pady=10)

    def save_venue(self, old_venue):
        new_venue = Venue(old_venue['venue_id'], self.name_var.get(), self.address_var.get(),
                                self.contact_var.get(), self.min_guests_var.get(),
                                self.max_guests_var.get())

        self.venue_list.remove(old_venue)
        self.venue_list.append(new_venue.to_dict())

        try:
            with open("venue_pkl_file.pkl", "wb") as file:
                pickle.dump(self.venue_list, file)
            messagebox.showinfo("Success", "Venue details updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update Venue: {e}")

    # Method to open window for deleting a venue
    def delete_venue_window(self):
        delete_window = tk.Toplevel()
        delete_window.title("Delete Venue")
        delete_window.geometry("250x150")
        delete_window.configure(bg="light green")

        # Label
        # Entry field for venue ID
        tk.Label(delete_window, text="Enter Venue ID:").grid(row=0, column=0, padx=10, pady=10)
        self.delete_id_entry = tk.Entry(delete_window)
        self.delete_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Delete Button
        delete_button = tk.Button(delete_window, text="Delete", command=self.delete_venue)
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to delete a venue
    def delete_venue(self):
        venue_id = self.delete_id_entry.get()
        found = False
        try:
            with open("venue_pkl_file.pkl", "rb") as file:
                self.venue_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Venue data file not found")
            return

        # Search for venue in the list
        for venue in self.venue_list:
            if venue['venue_id'] == venue_id:
                found = True
                # Remove venue from list
                self.venue_list.remove(venue)
                try:
                    # Save updated list to pickle file
                    with open("venue_pkl_file.pkl", "wb") as file:
                        pickle.dump(self.venue_list, file)
                    messagebox.showinfo("Success", "Venue deleted successfully!")
                    return
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete venue: {e}")

        # Display message if venue not found
        if not found:
            messagebox.showerror("Error", "Venue ID not found")

    # Method to open window for displaying all venue
    def display_venue_window(self):
        display_window = tk.Toplevel()
        display_window.title("Display Venues")
        display_window.geometry("500x300")
        display_window.configure(bg="light blue")

        # Create a text widget to display venue information
        text_widget = tk.Text(display_window, bg="light yellow", fg="black", font=("Arial", 12), wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        try:
            # Load venue data from pickle file
            with open("venue_pkl_file.pkl", "rb") as file:
                self.venue_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Venue data file not found")

        # Display each venue's information
        for venue in self.venue_list:
            text_widget.insert(tk.END, f"Venue ID: {venue['venue_id']}\n")
            text_widget.insert(tk.END, f"Name: {venue['name']}\n")
            text_widget.insert(tk.END, f"Address: {venue['address']}\n")
            text_widget.insert(tk.END, f"Contact Details: {venue['contact_details']}\n")
            text_widget.insert(tk.END, f"Min Guests: {venue['min_guests']}\n")
            text_widget.insert(tk.END, f"Max Guests: {venue['max_guests']}\n\n")

        # Disable text widget to make it read-only
        text_widget.config(state=tk.DISABLED)
