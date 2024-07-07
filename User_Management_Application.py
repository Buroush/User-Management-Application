import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import csv
import os

# Dark Theme Colors
BG_COLOR = "#2e2e2e"
FG_COLOR = "#ffffff"
ENTRY_BG = "#3b3b3b"
BUTTON_BG = "#5a5a5a"

class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management System")
        self.root.configure(bg=BG_COLOR)
        self.show_home()

    # Function to clear the main window
    def clear_window(self):
        """Clear all widgets from the main window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    # Function to show the home screen
    def show_home(self):
        """Display the home screen with Sign Up and Sign In buttons."""
        self.clear_window()
        self.root.title("Home")

        signup_button = tk.Button(self.root, text="Sign Up", command=self.show_signup, bg=BUTTON_BG, fg=FG_COLOR)
        signup_button.grid(row=0, column=0, padx=20, pady=20)

        signin_button = tk.Button(self.root, text="Sign In", command=self.show_signin, bg=BUTTON_BG, fg=FG_COLOR)
        signin_button.grid(row=0, column=1, padx=20, pady=20)

    # Function to show the sign-up screen
    def show_signup(self):
        """Display the sign-up screen."""
        self.clear_window()
        self.root.title("Sign Up")

        tk.Label(self.root, text="Name", bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Address", bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_address.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Date of Birth", bg=BG_COLOR, fg=FG_COLOR).grid(row=2, column=0, padx=10, pady=5)
        self.entry_dob = DateEntry(self.root, date_pattern='yyyy-mm-dd', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_dob.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Password", bg=BG_COLOR, fg=FG_COLOR).grid(row=3, column=0, padx=10, pady=5)
        self.entry_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_password.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Confirm Password", bg=BG_COLOR, fg=FG_COLOR).grid(row=4, column=0, padx=10, pady=5)
        self.entry_password_confirm = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_password_confirm.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Account Balance", bg=BG_COLOR, fg=FG_COLOR).grid(row=5, column=0, padx=10, pady=5)
        self.entry_balance = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_balance.grid(row=5, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=self.submit_form, bg=BUTTON_BG, fg=FG_COLOR)
        submit_button.grid(row=6, column=0, columnspan=2, pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.show_home, bg=BUTTON_BG, fg=FG_COLOR)
        back_button.grid(row=7, column=0, columnspan=2, pady=10)

    # Function to submit the sign-up form
    def submit_form(self):
        """Validate and process the sign-up form."""
        name = self.entry_name.get()
        address = self.entry_address.get()
        dob = self.entry_dob.get()
        password = self.entry_password.get()
        password_confirm = self.entry_password_confirm.get()
        balance = self.entry_balance.get()

        if not (name and address and dob and password and password_confirm and balance):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != password_confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        try:
            balance = float(balance)
            if balance < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Account balance must be a non-negative number.")
            return

        user_id = self.get_next_user_id()
        new_user = [user_id, name, address, dob, password, str(balance)]

        with open('user.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_user)

        messagebox.showinfo("Success", f"User registered successfully. User ID: {user_id}")
        self.show_home()

    # Function to generate the next user ID
    def get_next_user_id(self):
        """Generate the next user ID by reading the last user ID from user.csv."""
        if not os.path.exists('user.csv'):
            return '1'

        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            next_user_id = max(int(row[0]) for row in reader) + 1
            return str(next_user_id)

    # Function to show the sign-in screen
    def show_signin(self):
        """Display the sign-in screen."""
        self.clear_window()
        self.root.title("Sign In")

        tk.Label(self.root, text="User ID", bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=10, pady=5)
        self.entry_user_id = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_user_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Password", bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, padx=10, pady=5)
        self.entry_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Confirm Password", bg=BG_COLOR, fg=FG_COLOR).grid(row=2, column=0, padx=10, pady=5)
        self.entry_password_confirm = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_password_confirm.grid(row=2, column=1, padx=10, pady=5)

        signin_button = tk.Button(self.root, text="Sign In", command=self.sign_in, bg=BUTTON_BG, fg=FG_COLOR)
        signin_button.grid(row=3, column=0, columnspan=2, pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.show_home, bg=BUTTON_BG, fg=FG_COLOR)
        back_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Function to handle sign-in
    def sign_in(self):
        """Validate user ID and password during sign-in."""
        user_id = self.entry_user_id.get()
        password = self.entry_password.get()
        password_confirm = self.entry_password_confirm.get()

        if not (user_id and password and password_confirm):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != password_confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        user_found = False
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user_id and row[4] == password:
                    user_found = True
                    break

        if user_found:
            messagebox.showinfo("Success", f"Logged in successfully as User ID: {user_id}.")
            self.show_dashboard(user_id)
        else:
            messagebox.showerror("Error", "User ID or password incorrect.")

    # Function to show the user dashboard
    def show_dashboard(self, user_id):
        """Display the user dashboard."""
        self.clear_window()
        self.root.title("Dashboard")
    
        # Retrieve user information from CSV
        user_info = None
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user_id:
                    user_info = row
                    break
    
        if user_info:
            # Extract relevant user information    
            user_name = user_info[1]
            account_balance = float(user_info[5])  # assuming balance is stored as string in CSV
    
            # Display user welcome and account balance
            tk.Label(self.root, text=f"Welcome {user_name}, Your Balance: ${account_balance:.2f}", bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, columnspan=2, padx=10, pady=5)

            # Buttons for other functionalities
            edit_button = tk.Button(self.root, text="Edit Info", command=lambda: self.show_edit_info(user_id), bg=BUTTON_BG, fg=FG_COLOR)
            edit_button.grid(row=1, column=0, padx=20, pady=20)

            change_password_button = tk.Button(self.root, text="Change Password", command=lambda: self.show_change_password(user_id), bg=BUTTON_BG, fg=FG_COLOR)
            change_password_button.grid(row=1, column=1, padx=20, pady=20)

            fund_transfer_button = tk.Button(self.root, text="Fund Transfer", command=lambda: self.show_fund_transfer(user_id), bg=BUTTON_BG, fg=FG_COLOR)
            fund_transfer_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

            logout_button = tk.Button(self.root, text="Logout", command=self.show_home, bg=BUTTON_BG, fg=FG_COLOR)
            logout_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)
        else:
            messagebox.showwarning("Warning", "User ID not found in database.")    
            self.show_home()
    
    # Function to show Edit Info screen
    def show_edit_info(self, user_id):
        """Display the Edit Info screen."""
        self.clear_window()
        self.root.title("Edit Info")

        tk.Label(self.root, text="New Name", bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="New Address", bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_address.grid(row=1, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=lambda: self.update_user_info(user_id), bg=BUTTON_BG, fg=FG_COLOR)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        back_button = tk.Button(self.root, text="Back", command=lambda: self.show_dashboard(user_id), bg=BUTTON_BG, fg=FG_COLOR)
        back_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Function to update user info
    def update_user_info(self, user_id):
        """Update user information."""
        new_name = self.entry_name.get()
        new_address = self.entry_address.get()

        rows = []
        updated = False
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user_id:
                    if new_name:
                        row[1] = new_name
                    if new_address:
                        row[2] = new_address
                    updated = True
                rows.append(row)

        if updated:
            with open('user.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            messagebox.showinfo("Success", "User information updated.")
            self.show_dashboard(user_id)
        else:
            messagebox.showwarning("Warning", "User ID not found.")

    # Function to show Change Password screen
    def show_change_password(self, user_id):
        """Display the Change Password screen."""
        self.clear_window()
        self.root.title("Change Password")

        tk.Label(self.root, text="Current Password", bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=10, pady=5)
        self.entry_current_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_current_password.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="New Password", bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, padx=10, pady=5)
        self.entry_new_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_new_password.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Confirm New Password", bg=BG_COLOR, fg=FG_COLOR).grid(row=2, column=0, padx=10, pady=5)
        self.entry_confirm_new_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_confirm_new_password.grid(row=2, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=lambda: self.change_password(user_id), bg=BUTTON_BG, fg=FG_COLOR)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        back_button = tk.Button(self.root, text="Back", command=lambda: self.show_dashboard(user_id), bg=BUTTON_BG, fg=FG_COLOR)
        back_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Function to change user password
    def change_password(self, user_id):
        """Change user password."""
        current_password = self.entry_current_password.get()
        new_password = self.entry_new_password.get()
        confirm_new_password = self.entry_confirm_new_password.get()

        if not (current_password and new_password and confirm_new_password):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if new_password != confirm_new_password:
            messagebox.showerror("Error", "New passwords do not match.")
            return

        rows = []
        password_changed = False
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user_id and row[4] == current_password:
                    row[4] = new_password
                    password_changed = True
                rows.append(row)

        if password_changed:
            with open('user.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            messagebox.showinfo("Success", "Password changed successfully.")
            self.show_dashboard(user_id)
        else:
            messagebox.showwarning("Warning", "User ID or current password incorrect.")

    # Function to show Fund Transfer screen
    def show_fund_transfer(self, user_id):
        """Display the Fund Transfer screen."""
        self.clear_window()
        self.root.title("Fund Transfer")

        tk.Label(self.root, text="Recipient User ID", bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=10, pady=5)
        self.entry_recipient_user_id = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_recipient_user_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Amount", bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, padx=10, pady=5)
        self.entry_amount = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_amount.grid(row=1, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=lambda: self.transfer_funds(user_id), bg=BUTTON_BG, fg=FG_COLOR)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        back_button = tk.Button(self.root, text="Back", command=lambda: self.show_dashboard(user_id), bg=BUTTON_BG, fg=FG_COLOR)
        back_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Function to transfer funds
    def transfer_funds(self, user_id):
        """Transfer funds from one user to another."""
        recipient_user_id = self.entry_recipient_user_id.get()
        amount = self.entry_amount.get()

        if not (recipient_user_id and amount):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Amount must be a positive number.")
            return

        rows = []
        funds_transferred = False
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user_id:
                    if float(row[5]) >= amount:
                        row[5] = str(float(row[5]) - amount)
                        funds_transferred = True
                    else:
                        messagebox.showerror("Error", "Insufficient balance.")
                        return
                if row[0] == recipient_user_id:
                    row[5] = str(float(row[5]) + amount)
                rows.append(row)

        if funds_transferred:
            with open('user.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            messagebox.showinfo("Success", f"Funds transferred successfully to User ID: {recipient_user_id}.")
            self.show_dashboard(user_id)
        else:
            messagebox.showwarning("Warning", "User ID not found.")

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()
