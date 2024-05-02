# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import pickle

# Define a class to represent a event
class Event:
    # Initialize event attributes
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, company, invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.company = company
        self.invoice = invoice

    # Convert event information to a dictionary
    def to_dict(self):
        return {
            'event_id': self.event_id,
            'event_type': self.event_type,
            'theme': self.theme,
            'date': self.date,
            'time': self.time,
            'duration': self.duration,
            'venue_address': self.venue_address,
            'client_id': self.client_id,
            'guest_list': self.guest_list,
            'company': self.company,
            'invoice': self.invoice
        }
    
# Define a class to manage event
class Event_Manager:
    # Initialize the event list
    def __init__(self):
        self.event_list = []

    # Open a window to add a new event
    def add_event_window(self):
        # Create a new window
        self.add_event_window = tk.Toplevel()
        self.add_event_window.title("Add Event")
        self.add_event_window.geometry("400x500")
        self.add_event_window.configure(bg="light green")

        # Labels for event information
        tk.Label(self.add_event_window, text="Event ID:", bg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Event Type:", bg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Theme:", bg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Date:", bg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Time:", bg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Duration:", bg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Venue Address:", bg="light green").grid(row=6, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Client ID:", bg="light green").grid(row=7, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Guest List:", bg="light green").grid(row=8, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Company:", bg="light green").grid(row=9, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_event_window, text="Invoice:", bg="light green").grid(row=10, column=0, padx=10, pady=10, sticky="e")

        # Entry fields for event information
        self.event_id_entry = tk.Entry(self.add_event_window)
        self.event_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.event_type_entry = tk.Entry(self.add_event_window)
        self.event_type_entry.grid(row=1, column=1, padx=10, pady=10)
        self.theme_entry = tk.Entry(self.add_event_window)
        self.theme_entry.grid(row=2, column=1, padx=10, pady=10)
        self.date_entry = tk.Entry(self.add_event_window)
        self.date_entry.grid(row=3, column=1, padx=10, pady=10)
        self.time_entry = tk.Entry(self.add_event_window)
        self.time_entry.grid(row=4, column=1, padx=10, pady=10)
        self.duration_entry = tk.Entry(self.add_event_window)
        self.duration_entry.grid(row=5, column=1, padx=10, pady=10)
        self.venue_address_entry = tk.Entry(self.add_event_window)
        self.venue_address_entry.grid(row=6, column=1, padx=10, pady=10)
        self.client_id_entry = tk.Entry(self.add_event_window)
        self.client_id_entry.grid(row=7, column=1, padx=10, pady=10)
        self.guest_list_entry = tk.Entry(self.add_event_window)
        self.guest_list_entry.grid(row=8, column=1, padx=10, pady=10)
        self.company_entry = tk.Entry(self.add_event_window)
        self.company_entry.grid(row=9, column=1, padx=10, pady=10)
        self.invoice_entry = tk.Entry(self.add_event_window)
        self.invoice_entry.grid(row=10, column=1, padx=10, pady=10)

        # Button to add event
        add_button = tk.Button(self.add_event_window, text="Add Event", bg="blue", fg="black", font=("Arial", 12, "bold"), command=self.add_event)
        add_button.grid(row=11, column=0, columnspan=2, pady=10)

    # Method to add a new event
    def add_event(self):
        # Get event information from entry fields
        event_id = self.event_id_entry.get()
        event_type = self.event_type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_address_entry.get()
        client_id = self.client_id_entry.get()
        guest_list = self.guest_list_entry.get()
        company = self.company_entry.get()
        invoice = self.invoice_entry.get()

        # Validate event ID 
        def is_valid_event_id(event_id):
            return event_id.isdigit()

        # Validate input
        if not event_id or not is_valid_event_id(event_id):
            messagebox.showerror("Error", "Please enter a valid event ID (integer).")
            return
        if not event_type or not date or not time or not client_id:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        # Create event object
        event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, company, invoice)
        self.event_list.append(event.to_dict())  # Convert to dictionary and append

        # Save event data to a pickle file
        try:
            with open("event_pkl_file.pkl", "wb") as file:
                pickle.dump(self.event_list, file)
            messagebox.showinfo("Success", "Event added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add event: {e}")

        # Clear entry fields
        self.event_id_entry.delete(0, tk.END)
        self.event_type_entry.delete(0, tk.END)
        self.theme_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.venue_address_entry.delete(0, tk.END)
        self.client_id_entry.delete(0, tk.END)
        self.guest_list_entry.delete(0, tk.END)
        self.company_entry.delete(0, tk.END)
        self.invoice_entry.delete(0, tk.END)

    # Method to open a window for editing a event
    def edit_event_window(self):
        # Create a new window for editing event
        edit_window = tk.Toplevel()
        edit_window.title("Edit Event")
        edit_window.geometry("280x400")
        edit_window.configure(bg="light green")

        # Label
        tk.Label(edit_window, text="Enter Event ID:", bg="light green").grid(row=0, column=0, padx=10, pady=10)

        # Entry field for Event ID
        event_id_entry = tk.Entry(edit_window)
        event_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Search Button
        search_button = tk.Button(edit_window, text="Search", bg="green", fg="black", font=("Arial", 12, "bold"),
                                  command=lambda: self.search_event(event_id_entry.get(), edit_window))
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to search for a event by ID
    def search_event(self, event_id, edit_window):
        found = False
        try:
            with open("event_pkl_file.pkl", "rb") as file:
                self.event_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Event data file not found")
            return
        
        # Search for event in the event list
        for event in self.event_list:
            if event['event_id'] == event_id:
                found = True
                self.show_edit_event_window(event, edit_window)
                break

        # Display appropriate message if event not found
        if not found:
            messagebox.showerror("Error", "Event ID not found")

    # Method to display window for editing event details
    def show_edit_event_window(self, event, edit_window):
        edit_window.destroy()  # Close the previous edit window
        # Open new window for event details
        details_window = tk.Toplevel()
        details_window.title("Edit Event")
        details_window.geometry("280x400")
        details_window.configure(bg="light green")

        # Labels
        tk.Label(details_window, text="Event ID:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Event Type:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Theme:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Date:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Time:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Duration:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Venue Address:").grid(row=6, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Client ID:").grid(row=7, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Guest List:").grid(row=8, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Company:").grid(row=9, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Invoice:").grid(row=10, column=0, padx=10, pady=10, sticky="e")

        # Entry fields with existing event data
        event_id_entry = tk.Entry(details_window)
        event_id_entry.insert(tk.END, event['event_id'])
        event_id_entry.config(state=tk.DISABLED)  # Disable editing of Event ID
        event_id_entry.grid(row=0, column=1, padx=10, pady=10)
        event_type_entry = tk.Entry(details_window)
        event_type_entry.insert(tk.END, event['event_type'])
        event_type_entry.grid(row=1, column=1, padx=10, pady=10)
        theme_entry = tk.Entry(details_window)
        theme_entry.insert(tk.END, event['theme'])
        theme_entry.grid(row=2, column=1, padx=10, pady=10)
        date_entry = tk.Entry(details_window)
        date_entry.insert(tk.END, event['date'])
        date_entry.grid(row=3, column=1, padx=10, pady=10)
        time_entry = tk.Entry(details_window)
        time_entry.insert(tk.END, event['time'])
        time_entry.grid(row=4, column=1, padx=10, pady=10)
        duration_entry = tk.Entry(details_window)
        duration_entry.insert(tk.END, event['duration'])
        duration_entry.grid(row=5, column=1, padx=10, pady=10)
        venue_address_entry = tk.Entry(details_window)
        venue_address_entry.insert(tk.END, event['venue_address'])
        venue_address_entry.grid(row=6, column=1, padx=10, pady=10)
        client_id_entry = tk.Entry(details_window)
        client_id_entry.insert(tk.END, event['client_id'])
        client_id_entry.grid(row=7, column=1, padx=10, pady=10)
        guest_list_entry = tk.Entry(details_window)
        guest_list_entry.insert(tk.END, event['guest_list'])
        guest_list_entry.grid(row=8, column=1, padx=10, pady=10)
        company_entry = tk.Entry(details_window)
        company_entry.insert(tk.END, event['company'])
        company_entry.grid(row=9, column=1, padx=10, pady=10)
        invoice_entry = tk.Entry(details_window)
        invoice_entry.insert(tk.END, event['invoice'])
        invoice_entry.grid(row=10, column=1, padx=10, pady=10)

        # Update Button
        update_button = tk.Button(details_window, text="Update Event", bg="blue", fg="black", font=("Arial", 12, "bold"),
                                  command=lambda: self.update_event(event, event_type_entry.get(), theme_entry.get(),
                                                                    date_entry.get(), time_entry.get(), duration_entry.get(),
                                                                    venue_address_entry.get(), client_id_entry.get(),
                                                                    guest_list_entry.get(), company_entry.get(),
                                                                    invoice_entry.get(), details_window))
        update_button.grid(row=11, column=0, columnspan=2, pady=10)

    # Method to update event details
    def update_event(self, old_event, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                     company, invoice, details_window):
        # Remove old event
        self.event_list.remove(old_event)
        # Create new updated event
        updated_event = Event(old_event['event_id'], event_type, theme, date, time, duration, venue_address, client_id,
                              guest_list, company, invoice)
        # Add updated event to list
        self.event_list.append(updated_event.to_dict())
        # Save to pickle file
        try:
            with open("event_pkl_file.pkl", "wb") as file:
                pickle.dump(self.event_list, file)
            messagebox.showinfo("Success", "Event updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update event: {e}")
        # Close edit window
        details_window.destroy()

    # Method to open window for deleting a event
    def delete_event_window(self):
        delete_window = tk.Toplevel()
        delete_window.title("Delete Event")
        delete_window.geometry("280x400")
        delete_window.configure(bg="light green")

        # Label
        tk.Label(delete_window, text="Enter Event ID:", bg="light green").grid(row=0, column=0, padx=10, pady=10)

        # Entry field for Event ID
        event_id_entry = tk.Entry(delete_window)
        event_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Delete Button
        delete_button = tk.Button(delete_window, text="Delete", bg="red", fg="black", font=("Arial", 12, "bold"),
                                  command=lambda: self.delete_event(event_id_entry.get(), delete_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to delete a event
    def delete_event(self, event_id, delete_window):
        found = False
        try:
            with open("event_pkl_file.pkl", "rb") as file:
                self.event_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Event data file not found")
            return
        # Search for event in the list
        for event in self.event_list:
            if event['event_id'] == event_id:
                found = True
                # Remove event from list
                self.event_list.remove(event)
                try:
                    # Save updated list to pickle file
                    with open("event_pkl_file.pkl", "wb") as file:
                        pickle.dump(self.event_list, file)
                    messagebox.showinfo("Success", "Event deleted successfully!")
                    # Close delete window after successful deletion
                    delete_window.destroy()
                    return
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete event: {e}")
         # Display message if event not found
        if not found:
            messagebox.showerror("Error", "Event ID not found")

    # Method to open window for displaying all event
    def display_event_window(self):
        display_window = tk.Toplevel()
        display_window.title("Display Events")
        display_window.geometry("500x300")
        display_window.configure(bg="light blue")

        # Create a text widget to display event information
        text_widget = tk.Text(display_window, bg="light yellow", fg="black", font=("Arial", 12), wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Load event data from pickle file
        try:
            with open("event_pkl_file.pkl", "rb") as file:
                self.event_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Event data file not found")

        # Display each event's information
        for event in self.event_list:
            text_widget.insert(tk.END, f"Event ID: {event['event_id']}\n")
            text_widget.insert(tk.END, f"Event Type: {event['event_type']}\n")
            text_widget.insert(tk.END, f"Theme: {event['theme']}\n")
            text_widget.insert(tk.END, f"Date: {event['date']}\n")
            text_widget.insert(tk.END, f"Time: {event['time']}\n")
            text_widget.insert(tk.END, f"Duration: {event['duration']}\n")
            text_widget.insert(tk.END, f"Venue Address: {event['venue_address']}\n")
            text_widget.insert(tk.END, f"Client ID: {event['client_id']}\n")
            text_widget.insert(tk.END, f"Guest List: {event['guest_list']}\n")
            text_widget.insert(tk.END, f"Company: {event['company']}\n")
            text_widget.insert(tk.END, f"Invoice: {event['invoice']}\n\n")

        # Disable text widget to make it read-only
        text_widget.config(state=tk.DISABLED)


