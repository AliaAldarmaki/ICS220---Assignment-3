# Import necessary modules
import tkinter as tk              
from tkinter import messagebox  
import pickle                 

# Define a class to represent a Client
class Client:
    # Initialize client attributes
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    # Convert client information to a dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'client_id': self.client_id,
            'address': self.address,
            'contact_details': self.contact_details,
            'budget': self.budget
        }

# Define a class to manage clients
class ClientManager:
    # Initialize the client list
    def __init__(self):
        self.client_list = []

    # Open a window to add a new client
    def add_client_window(self):
        # Create a new window
        self.add_client_window = tk.Toplevel()
        self.add_client_window.title("Add Client")
        self.add_client_window.geometry("280x400")
        self.add_client_window.configure(bg="light blue")

        # Labels for client information
        tk.Label(self.add_client_window, text="Client ID:", bg="light blue").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_client_window, text="Name:", bg="light blue").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_client_window, text="Address:", bg="light blue").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_client_window, text="Contact Details:", bg="light blue").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_client_window, text="Budget:", bg="light blue").grid(row=4, column=0, padx=10, pady=10, sticky="e")

        # Entry fields for client information
        self.client_id_entry = tk.Entry(self.add_client_window)
        self.client_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_entry = tk.Entry(self.add_client_window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.address_entry = tk.Entry(self.add_client_window)
        self.address_entry.grid(row=2, column=1, padx=10, pady=10)
        self.contact_details_entry = tk.Entry(self.add_client_window)
        self.contact_details_entry.grid(row=3, column=1, padx=10, pady=10)
        self.budget_entry = tk.Entry(self.add_client_window)
        self.budget_entry.grid(row=4, column=1, padx=10, pady=10)

        # Button to add client
        add_button = tk.Button(self.add_client_window, text="Add Client", bg="green", fg="black", font=("Arial", 12, "bold"), command=self.add_client)
        add_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Method to add a new client
    def add_client(self):
        # Get client information from entry fields
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()

        # Validate client ID and name
        def is_valid_client_id(client_id):
            return client_id.isdigit()

        def is_valid_name(name):
            return name.replace(" ", "").isalpha()

        # Validate input fields
        if not client_id or not is_valid_client_id(client_id):
            messagebox.showerror("Error", "Please enter a valid client ID (integer).")
            return
        if not name or not is_valid_name(name):
            messagebox.showerror("Error", "Please enter a valid name (alphabetical characters only).")
            return
        if not address or not contact_details or not budget:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        # Create a new client object
        client = Client(client_id, name, address, contact_details, budget)
        self.client_list.append(client.to_dict())  # Convert to dictionary and append to client list

        # Save client data to a pickle file
        try:
            with open("client_pkl_file.pkl", "wb") as file:
                pickle.dump(self.client_list, file)
            messagebox.showinfo("Success", "Client added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add client: {e}")

        # Clear entry fields after adding client
        self.client_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_details_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)

    # Method to open a window for editing a client
    def edit_client_window(self):
        # Create a new window for editing client
        edit_window = tk.Toplevel()
        edit_window.title("Edit Client")
        edit_window.geometry("280x400")
        edit_window.configure(bg="light blue")

        # Label for entering client ID
        tk.Label(edit_window, text="Enter Client ID:", bg="light blue").grid(row=0, column=0, padx=10, pady=10)

        # Entry field for entering client ID
        client_id_entry = tk.Entry(edit_window)
        client_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to search for client
        search_button = tk.Button(edit_window, text="Search", bg="green", fg="black", font=("Arial", 12, "bold"),
                                command=lambda: self.search_client(client_id_entry.get(), edit_window))
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to search for a client by ID
    def search_client(self, client_id, edit_window):
        found = False
        try:
            with open("client_pkl_file.pkl", "rb") as file:
                self.client_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Client data file not found")
            return

        # Search for client in the client list
        for client in self.client_list:
            if client['client_id'] == client_id:
                found = True
                self.show_edit_client_window(client, edit_window)
                break

        # Display appropriate message if client not found
        if not found:
            messagebox.showerror("Error", "Client ID not found")

    # Method to display window for editing client details
    def show_edit_client_window(self, client, edit_window):
        # Close previous edit window
        edit_window.destroy()

        # Create new window to display client details
        details_window = tk.Toplevel()
        details_window.title("Edit Client")
        details_window.geometry("280x400")
        details_window.configure(bg="light blue")

        # Labels for client details
        tk.Label(details_window, text="Client ID:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Name:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Address:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Contact Details:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Budget:").grid(row=4, column=0, padx=10, pady=10, sticky="e")

        # Entry fields with existing client data
        client_id_entry = tk.Entry(details_window)
        client_id_entry.insert(tk.END, client['client_id'])
        client_id_entry.config(state=tk.DISABLED)  # Disable editing of Client ID
        client_id_entry.grid(row=0, column=1, padx=10, pady=10)
        name_entry = tk.Entry(details_window)
        name_entry.insert(tk.END, client['name'])
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        address_entry = tk.Entry(details_window)
        address_entry.insert(tk.END, client['address'])
        address_entry.grid(row=2, column=1, padx=10, pady=10)
        contact_details_entry = tk.Entry(details_window)
        contact_details_entry.insert(tk.END, client['contact_details'])
        contact_details_entry.grid(row=3, column=1, padx=10, pady=10)
        budget_entry = tk.Entry(details_window)
        budget_entry.insert(tk.END, client['budget'])
        budget_entry.grid(row=4, column=1, padx=10, pady=10)

        # Button to update client details
        update_button = tk.Button(details_window, text="Update Client", bg="blue", fg="black", font=("Arial", 12, "bold"),
                                command=lambda: self.update_client(client, name_entry.get(), address_entry.get(),
                                                                    contact_details_entry.get(), budget_entry.get(), details_window))
        update_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Method to update client details
    def update_client(self, old_client, name, address, contact_details, budget, details_window):
        # Remove old client from list
        self.client_list.remove(old_client)
        # Create updated client object
        updated_client = Client(old_client['client_id'], name, address, contact_details, budget)
        # Add updated client to list
        self.client_list.append(updated_client.to_dict())
        # Save updated list to pickle file
        try:
            with open("client_pkl_file.pkl", "wb") as file:
                pickle.dump(self.client_list, file)
            messagebox.showinfo("Success", "Client updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update client: {e}")
        # Close edit window after updating client
        details_window.destroy()

    # Method to open window for deleting a client
    def delete_client_window(self):
        # Create new window for deleting client
        delete_window = tk.Toplevel()
        delete_window.title("Delete Client")
        delete_window.geometry("280x400")
        delete_window.configure(bg="light blue")

        # Label for entering client ID
        tk.Label(delete_window, text="Enter Client ID:", bg="light blue").grid(row=0, column=0, padx=10, pady=10)

        # Entry field for entering client ID
        client_id_entry = tk.Entry(delete_window)
        client_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to delete client
        delete_button = tk.Button(delete_window, text="Delete", bg="red", fg="black", font=("Arial", 12, "bold"),
                                command=lambda: self.delete_client(client_id_entry.get(), delete_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to delete a client
    def delete_client(self, client_id, delete_window):
        found = False
        try:
            with open("client_pkl_file.pkl", "rb") as file:
                self.client_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Client data file not found")
            return

        # Search for client in the list
        for client in self.client_list:
            if client['client_id'] == client_id:
                found = True
                # Remove client from list
                self.client_list.remove(client)
                try:
                    # Save updated list to pickle file
                    with open("client_pkl_file.pkl", "wb") as file:
                        pickle.dump(self.client_list, file)
                    messagebox.showinfo("Success", "Client deleted successfully!")
                    delete_window.destroy()  # Close delete window after successful deletion
                    return
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete client: {e}")

        # Display message if client not found
        if not found:
            messagebox.showerror("Error", "Client ID not found")

    # Method to open window for displaying all clients
    def display_client_window(self):
        # Create new window for displaying clients
        display_window = tk.Toplevel()
        display_window.title("Display Clients")
        display_window.geometry("500x300")
        display_window.configure(bg="light blue")

        # Text widget to display client information
        text_widget = tk.Text(display_window, bg="light yellow", fg="black", font=("Arial", 12), wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Load client data from pickle file
        try:
            with open("client_pkl_file.pkl", "rb") as file:
                self.client_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Client data file not found")

        # Display information for each client
        for client in self.client_list:
            text_widget.insert(tk.END, f"Client ID: {client['client_id']}\n")
            text_widget.insert(tk.END, f"Name: {client['name']}\n")
            text_widget.insert(tk.END, f"Address: {client['address']}\n")
            text_widget.insert(tk.END, f"Contact Details: {client['contact_details']}\n")
            text_widget.insert(tk.END, f"Budget: {client['budget']}\n\n")

        # Disable text widget to make it read-only
        text_widget.config(state=tk.DISABLED)
