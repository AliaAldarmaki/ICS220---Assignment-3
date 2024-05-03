# Import important libraries tkinter
import tkinter as tk
from tkinter import messagebox
# Import other classes instances
from employee import Employee, EmployeeManager
from client import Client, ClientManager
from event import Event, Event_Manager
from guest import Guest, GuestManager
from supplier import Supplier, SupplierManager
from venue import Venue, VenueManager
  
class EventManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Event Management System")
        self.root.geometry("800x450")  # Larger window size
        self.root.configure(bg="#FFA500")
        self.employee_manager = EmployeeManager()
        self.client_manager = ClientManager()
        self.event_manager = Event_Manager()
        self.guest_manager = GuestManager()
        self.supplier_manager = SupplierManager()
        self.venue_manager = VenueManager()

        # Create Company Organizer label
        label = tk.Label(self.root, text="Company Organizer", bg="#FFA500", fg="black", font=("Arial", 30, "bold"))
        label.pack(pady=50)

        # Create Button Menu
        button_menu = tk.Button(self.root, text="Button Menu", bg="#FFD700", fg="black", font=("Arial", 18, "bold"), command=self.open_menu, width=20)
        button_menu.pack(pady=20)

    def open_menu(self):
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Menu")
        menu_window.geometry("600x400")  # Larger menu window size
        menu_window.configure(bg="#FFDAB9")
        
        # Create buttons for Employee, Event, Guest, Venue, Supplier, Client
        buttons = ["Employee", "Event", "Guest", "Venue", "Supplier", "Client"]
        for button_text in buttons:
            button = tk.Button(menu_window, text=button_text, bg="#FFD700", fg="black", font=("Arial", 14, "bold"), command=lambda text=button_text: self.show_message(text), width=15)
            button.pack(pady=10)
            if button_text == "Employee":
                button.configure(command=self.open_employee_submenu)
            elif button_text == "Event":
                button.configure(command=self.open_event_submenu)
            elif button_text == "Guest":
                button.configure(command=self.open_guest_submenu)
            elif button_text == "Venue":
                button.configure(command=self.open_venue_submenu)
            elif button_text == "Supplier":
                button.configure(command=self.open_supplier_submenu)
            elif button_text == "Client":
                button.configure(command=self.open_client_submenu)

    def open_employee_submenu(self):
        submenu_window = tk.Toplevel(self.root)
        submenu_window.title("Employee Submenu")
        submenu_window.geometry("300x250")
        submenu_window.configure(bg="light pink")

        actions = ["ADD", "EDIT", "DELETE", "DISPLAY"]
        for action in actions:
            button = tk.Button(submenu_window, text=action, bg="red", fg="black", font=("Arial", 12, "bold"), width=15)
            button.pack(pady=10)

            if action == "ADD":
                button.configure(command=self.employee_manager.add_employee_window)
            elif action == "EDIT":
                button.configure(command=self.employee_manager.edit_employee_window)
            elif action == "DELETE":
                button.configure(command=self.employee_manager.delete_employee_window)
            elif action == "DISPLAY":
                button.configure(command=self.employee_manager.display_employee_window)


    def open_event_submenu(self):
        submenu_window = tk.Toplevel(self.root)
        submenu_window.title("Event Submenu")
        submenu_window.geometry("300x250")  # Submenu window size
        submenu_window.configure(bg="light blue")  # Set background color to light blue

        # Create buttons for Add, Edit, Delete, Display
        actions = ["ADD", "EDIT", "DELETE", "DISPLAY"]
        for action in actions:
            button = tk.Button(submenu_window, text=action, bg="dark blue", fg="black", font=("Arial", 12, "bold"), width=15)
            button.pack(pady=10)
            if action == "ADD":
                button.configure(command=self.event_manager.add_event_window)
            elif action == "EDIT":
                button.configure(command=self.event_manager.edit_event_window)
            elif action == "DELETE":
                button.configure(command=self.event_manager.delete_event_window)
            elif action == "DISPLAY":
                button.configure(command=self.event_manager.display_event_window)
            

    def open_guest_submenu(self):
        submenu_window = tk.Toplevel(self.root)
        submenu_window.title("Guest Submenu")
        submenu_window.geometry("300x250")  # Submenu window size
        submenu_window.configure(bg="light green")  # Set background color to light green

        # Create buttons for Add, Edit, Delete, Display
        actions = ["ADD", "EDIT", "DELETE", "DISPLAY"]
        for action in actions:
            button = tk.Button(submenu_window, text=action, bg="dark green", fg="black", font=("Arial", 12, "bold"), width=15)
            button.pack(pady=10)

            if action == "ADD":
                button.configure(command=self.guest_manager.add_guest_window)
            elif action == "EDIT":
                button.configure(command=self.guest_manager.edit_guest_window)
            elif action == "DELETE":
                button.configure(command=self.guest_manager.delete_guest_window)
            elif action == "DISPLAY":
                button.configure(command=self.guest_manager.display_guest_window)

    def open_venue_submenu(self):
        submenu_window = tk.Toplevel(self.root)
        submenu_window.title("Venue Submenu")
        submenu_window.geometry("300x250")  # Submenu window size
        submenu_window.configure(bg="light yellow")  # Set background color to light yellow

        # Create buttons for Add, Edit, Delete, Display
        actions = ["ADD", "EDIT", "DELETE", "DISPLAY"]
        for action in actions:
            button = tk.Button(submenu_window, text=action, bg="dark goldenrod", fg="black", font=("Arial", 12, "bold"), width=15)
            button.pack(pady=10)

            if action == "ADD":
                button.configure(command=self.venue_manager.add_venue_window)
            elif action == "EDIT":
                button.configure(command=self.venue_manager.edit_venue_window)
            elif action == "DELETE":
                button.configure(command=self.venue_manager.delete_venue_window)
            elif action == "DISPLAY":
                button.configure(command=self.venue_manager.display_venue_window)

    def open_supplier_submenu(self):
        submenu_window = tk.Toplevel(self.root)
        submenu_window.title("Supplier Submenu")
        submenu_window.geometry("300x250")  # Submenu window size
        submenu_window.configure(bg="light coral")  # Set background color to light coral

        # Create buttons for Add, Edit, Delete, Display
        actions = ["ADD", "EDIT", "DELETE", "DISPLAY"]
        for action in actions:
            button = tk.Button(submenu_window, text=action, bg="dark red", fg="black", font=("Arial", 12, "bold"), width=15)
            button.pack(pady=10)

            if action == "ADD":
                button.configure(command=self.supplier_manager.add_supplier_window)
            elif action == "EDIT":
                button.configure(command=self.supplier_manager.edit_supplier_window)
            elif action == "DELETE":
                button.configure(command=self.supplier_manager.delete_supplier_window)
            elif action == "DISPLAY":
                button.configure(command=self.supplier_manager.display_supplier_window)

    def open_client_submenu(self):
        submenu_window = tk.Toplevel(self.root)
        submenu_window.title("Client Submenu")
        submenu_window.geometry("300x250")  # Submenu window size
        submenu_window.configure(bg="purple")  # Set background color to light violet

        # Create buttons for Add, Edit, Delete, Display
        actions = ["ADD", "EDIT", "DELETE", "DISPLAY"]
        for action in actions:
            button = tk.Button(submenu_window, text=action, bg="dark violet", fg="black", font=("Arial", 12, "bold"), width=15)
            button.pack(pady=10)

            if action == "ADD":
                button.configure(command=self.client_manager.add_client_window)
            elif action == "EDIT":
                button.configure(command=self.client_manager.edit_client_window)
            elif action == "DELETE":
                button.configure(command=self.client_manager.delete_client_window)
            elif action == "DISPLAY":
                button.configure(command=self.client_manager.display_client_window)

    def show_message(self, button_text):
        messagebox.showinfo("Menu Item Clicked", f"You clicked {button_text}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = EventManager()
    app.run()
