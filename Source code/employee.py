# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import pickle
import datetime

# Define a class to represent a Employee
class Employee:
    # Initialize Employee attributes
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

    # Convert employee information to a dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'employee_id': self.employee_id,
            'department': self.department,
            'job_title': self.job_title,
            'basic_salary': self.basic_salary,
            'age': self.age,
            'date_of_birth': self.date_of_birth,
            'passport_details': self.passport_details
        }

# Define a class to manage employee
class EmployeeManager:
    # Initialize the employee list
    def __init__(self):
        self.employee_list = []

    # Open a window to add a new employee
    def add_employee_window(self):
        # Create a new window
        self.add_employee_window = tk.Toplevel()
        self.add_employee_window.title("Add Employee")
        self.add_employee_window.geometry("280x400")
        self.add_employee_window.configure(bg="light pink")

        # Labels for employee information
        tk.Label(self.add_employee_window, text="Name:", bg="light pink").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_employee_window, text="Employee ID:", bg="light pink").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_employee_window, text="Department:", bg="light pink").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_employee_window, text="Job Title:", bg="light pink").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_employee_window, text="Basic Salary:", bg="light pink").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_employee_window, text="Age:", bg="light pink").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_employee_window, text="Date of Birth:", bg="light pink").grid(row=6, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.add_employee_window, text="Passport Details:", bg="light pink").grid(row=7, column=0, padx=10, pady=10, sticky="e")

        # Entry fields for employee information
        self.name_entry = tk.Entry(self.add_employee_window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.employee_id_entry = tk.Entry(self.add_employee_window)
        self.employee_id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.department_entry = tk.Entry(self.add_employee_window)
        self.department_entry.grid(row=2, column=1, padx=10, pady=10)
        self.job_title_entry = tk.Entry(self.add_employee_window)
        self.job_title_entry.grid(row=3, column=1, padx=10, pady=10)
        self.basic_salary_entry = tk.Entry(self.add_employee_window)
        self.basic_salary_entry.grid(row=4, column=1, padx=10, pady=10)
        self.age_entry = tk.Entry(self.add_employee_window)
        self.age_entry.grid(row=5, column=1, padx=10, pady=10)
        self.date_of_birth_entry = tk.Entry(self.add_employee_window)
        self.date_of_birth_entry.grid(row=6, column=1, padx=10, pady=10)
        self.passport_details_entry = tk.Entry(self.add_employee_window)
        self.passport_details_entry.grid(row=7, column=1, padx=10, pady=10)

        # Button to add employee
        add_button = tk.Button(self.add_employee_window, text="Add Employee", bg="red", fg="black", font=("Arial", 12, "bold"), command=self.add_employee)
        add_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Method to add a new employee
    def add_employee(self):
        # Get employee information from entry fields
        name = self.name_entry.get()
        employee_id = self.employee_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        passport_details = self.passport_details_entry.get()

        # Validate employee ID , name and DOB
        def is_valid_employee_id(employee_id):
            return employee_id.isdigit()

        def is_valid_name(name):
            return name.replace(" ", "").isalpha()
        
        def validate_date_of_birth(date_of_birth):
            try:
                datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        
        # Validate input
        if not name or not is_valid_name(name) or not employee_id or not is_valid_employee_id(employee_id) \
                or not department or not job_title or not basic_salary:
            messagebox.showerror("Error", "Please fill in all required fields with valid input.")
            return
        
        # Additional validation for age
        if age:
            try:
                age = int(age)
                if not 18 <= age <= 100:
                    messagebox.showerror("Error", "Please enter a valid age (between 18 and 100).")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid age.")
                return

        # Additional validation for basic salary
        if basic_salary:
            try:
                basic_salary = float(basic_salary)
                if basic_salary <= 0:
                    messagebox.showerror("Error", "Please enter a valid basic salary (greater than zero).")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid basic salary.")
                return

        # Additional validation for date of birth
        if date_of_birth and not validate_date_of_birth(date_of_birth):
            messagebox.showerror("Error", "Please enter a valid date of birth (YYYY-MM-DD).")
            return

        # Create employee object
        employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.employee_list.append(employee.to_dict())  # Convert to dictionary and append

        # Save employee data to a pickle file
        try:
            with open("employee_pkl_file.pkl", "wb") as file:
                pickle.dump(self.employee_list, file)
            messagebox.showinfo("Success", "Employee added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add employee: {e}")

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.employee_id_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)
        self.basic_salary_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.date_of_birth_entry.delete(0, tk.END)
        self.passport_details_entry.delete(0, tk.END)

    # Method to open a window for editing a employee
    def edit_employee_window(self):
        # Create a new window for editing employee
        edit_window = tk.Toplevel()
        edit_window.title("Edit Employee")
        edit_window.geometry("280x400")
        edit_window.configure(bg="light pink")

        # Label
        tk.Label(edit_window, text="Enter Employee ID:", bg="pink").grid(row=0, column=0, padx=10, pady=10)

        # Entry field for Employee ID
        employee_id_entry = tk.Entry(edit_window)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Search Button
        search_button = tk.Button(edit_window, text="Search", bg="red", fg="black", font=("Arial", 12, "bold"),
                                command=lambda: self.search_employee(employee_id_entry.get(), edit_window))
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to search for a employee by ID
    def search_employee(self, employee_id, edit_window):
        found = False
        try:
            with open("employee_pkl_file.pkl", "rb") as file:
                self.employee_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Employee data file not found")
            return

        # Search for employee in the employee list
        for employee in self.employee_list:
            if employee['employee_id'] == employee_id:
                found = True
                self.show_edit_employee_window(employee, edit_window)
                break

        # Display appropriate message if employee not found
        if not found:
            messagebox.showerror("Error", "Employee ID not found")

    # Method to display window for editing employee details
    def show_edit_employee_window(self, employee, edit_window):
        edit_window.destroy()  # Close the previous edit window
        # Open new window for employee details
        details_window = tk.Toplevel()
        details_window.title("Edit Employee")
        details_window.geometry("280x400")
        details_window.configure(bg="light pink")

        # Labels
        tk.Label(details_window, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Employee ID:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Department:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Job Title:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Basic Salary:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Age:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Date of Birth:").grid(row=6, column=0, padx=10, pady=10, sticky="e")
        tk.Label(details_window, text="Passport Details:").grid(row=7, column=0, padx=10, pady=10, sticky="e")

        # Entry fields with existing employee data
        name_entry = tk.Entry(details_window)
        name_entry.insert(tk.END, employee['name'])
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        employee_id_entry = tk.Entry(details_window)
        employee_id_entry.insert(tk.END, employee['employee_id'])
        employee_id_entry.config(state=tk.DISABLED)  # Disable editing of Employee ID
        employee_id_entry.grid(row=1, column=1, padx=10, pady=10)
        department_entry = tk.Entry(details_window)
        department_entry.insert(tk.END, employee['department'])
        department_entry.grid(row=2, column=1, padx=10, pady=10)
        job_title_entry = tk.Entry(details_window)
        job_title_entry.insert(tk.END, employee['job_title'])
        job_title_entry.grid(row=3, column=1, padx=10, pady=10)
        basic_salary_entry = tk.Entry(details_window)
        basic_salary_entry.insert(tk.END, employee['basic_salary'])
        basic_salary_entry.grid(row=4, column=1, padx=10, pady=10)
        age_entry = tk.Entry(details_window)
        age_entry.insert(tk.END, employee['age'])
        age_entry.grid(row=5, column=1, padx=10, pady=10)
        date_of_birth_entry = tk.Entry(details_window)
        date_of_birth_entry.insert(tk.END, employee['date_of_birth'])
        date_of_birth_entry.grid(row=6, column=1, padx=10, pady=10)
        passport_details_entry = tk.Entry(details_window)
        passport_details_entry.insert(tk.END, employee['passport_details'])
        passport_details_entry.grid(row=7, column=1, padx=10, pady=10)

        # Update Button
        update_button = tk.Button(details_window, text="Update Employee", bg="blue", fg="black", font=("Arial", 12, "bold"),
                                command=lambda: self.update_employee(employee, name_entry.get(), department_entry.get(),
                                                                    job_title_entry.get(), basic_salary_entry.get(),
                                                                    age_entry.get(), date_of_birth_entry.get(),
                                                                    passport_details_entry.get(), details_window))
        update_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Method to update employee details
    def update_employee(self, old_employee, name, department, job_title, basic_salary, age, date_of_birth,
                        passport_details, edit_window):
        # Remove old employee
        self.employee_list.remove(old_employee)
        # Create new updated employee
        updated_employee = Employee(name, old_employee['employee_id'], department, job_title, basic_salary, age,
                                    date_of_birth, passport_details)
        # Add updated employee to list
        self.employee_list.append(updated_employee.to_dict())
        # Save to pickle file
        try:
            with open("employee_pkl_file.pkl", "wb") as file:
                pickle.dump(self.employee_list, file)
            messagebox.showinfo("Success", "Employee updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update employee: {e}")
        # Close edit window
        edit_window.destroy()

    # Method to open window for deleting a employee
    def delete_employee_window(self):
        delete_window = tk.Toplevel()
        delete_window.title("Delete Employee")
        delete_window.geometry("280x400")
        delete_window.configure(bg="light pink")

        # Label
        tk.Label(delete_window, text="Enter Employee ID:", bg="light pink").grid(row=0, column=0, padx=10, pady=10)

        # Entry field for Employee ID
        employee_id_entry = tk.Entry(delete_window)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Delete Button
        delete_button = tk.Button(delete_window, text="Delete", bg="red", fg="black", font=("Arial", 12, "bold"),
                                command=lambda: self.delete_employee(employee_id_entry.get(), delete_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Method to delete a employee
    def delete_employee(self, employee_id, delete_window):
        found = False
        try:
            with open("employee_pkl_file.pkl", "rb") as file:
                self.employee_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Employee data file not found")
            return

        # Search for employee in the list
        for employee in self.employee_list:
            if employee['employee_id'] == employee_id:
                found = True
                # Remove employee from list
                self.employee_list.remove(employee)
                try:
                    # Save updated list to pickle file
                    with open("employee_pkl_file.pkl", "wb") as file:
                        pickle.dump(self.employee_list, file)
                    messagebox.showinfo("Success", "Employee deleted successfully!")
                    # Close delete window after successful deletion
                    delete_window.destroy()
                    return
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete employee: {e}")

        # Display message if employee not found
        if not found:
            messagebox.showerror("Error", "Employee ID not found")

    # Method to open window for displaying all employee
    def display_employee_window(self):
        display_window = tk.Toplevel()
        display_window.title("Display Employees")
        display_window.geometry("500x300")
        display_window.configure(bg="light pink")

        # Create a text widget to display employee information
        text_widget = tk.Text(display_window, bg="light yellow", fg="black", font=("Arial", 12), wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Load employee data from pickle file
        try:
            with open("employee_pkl_file.pkl", "rb") as file:
                self.employee_list = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Employee data file not found")

        # Display each employee's information
        for employee in self.employee_list:
            text_widget.insert(tk.END, f"Name: {employee['name']}\n")
            text_widget.insert(tk.END, f"Employee ID: {employee['employee_id']}\n")
            text_widget.insert(tk.END, f"Department: {employee['department']}\n")
            text_widget.insert(tk.END, f"Job Title: {employee['job_title']}\n")
            text_widget.insert(tk.END, f"Basic Salary: {employee['basic_salary']}\n")
            text_widget.insert(tk.END, f"Age: {employee['age']}\n")
            text_widget.insert(tk.END, f"Date of Birth: {employee['date_of_birth']}\n")
            text_widget.insert(tk.END, f"Passport Details: {employee['passport_details']}\n\n")

        # Disable text widget to make it read-only
        text_widget.config(state=tk.DISABLED)
