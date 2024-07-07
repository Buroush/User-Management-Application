# User Management Application

This project is a user management application developed using Python and the Tkinter library for the GUI. The application allows users to sign up, log in, edit their information, change their password, transfer funds, and log out. The user information is stored in a CSV file, and various functionalities ensure data integrity and security, such as account locking after multiple failed login attempts.

## Project Overview

### Features

- **Sign Up**: Users can register by providing their name, address, date of birth, initial account balance, and password.
  
- **Sign In**: Users can log in with their user ID and password. After three incorrect attempts, the account is locked.
  ![Sign In](https://github.com/Buroush/User-Management-Application/blob/main/Image/Sign-min.png)
  
- **User Menu**: After logging in, users can view their account balance, edit their information, change their password, and transfer funds.
  ![User Menu](https://github.com/Buroush/User-Management-Application/blob/main/Image/User-Menu-min.png)
  
- **Fund Transfer**: Users can transfer funds to other registered users.
  ![Fund Transfer](https://github.com/Buroush/User-Management-Application/blob/main/Image/Fund-Transfer.png)
  
- **Account Locking**: Accounts are locked after three incorrect login attempts.
  ![Account Locking](https://github.com/Buroush/User-Management-Application/blob/main/Image/Account-Locking.png)
  
- **Single Window Interface**: The application runs in a single window with different screens for each function.
  
- **Dark Mode**: The application uses a dark color scheme for better visibility.

## Object-Oriented Programming (OOP) Concepts

The project heavily relies on OOP principles such as encapsulation, abstraction, and polymorphism.

### Encapsulation
The application encapsulates related data and methods within a single class `UserManagementApp`. Each method operates on the object's state, keeping related functionality together and protecting the internal data from outside interference.

### Abstraction
The application abstracts away the complexities of interacting with user data stored in a CSV file. Users interact with simplified interfaces (GUI buttons, entry fields) without needing to understand the underlying implementation details (file handling, data manipulation).

### Polymorphism
Polymorphism allows methods to be overridden in derived classes. Though not directly demonstrated in this project, it could be applied in scenarios where different types of user interactions (e.g., admin vs. regular user) require different implementations of the same methods.

## Learning and Inspiration

This project was inspired by concepts and knowledge gained from two prominent courses:

### 1. The Joy of Computing using Python
By Prof. [Sudarshan Iyengar](https://www.linkedin.com/in/sudarshan-iyengar-3560b8145) | Indian Institute of Technology Ropar
- [The Joy of Computing using Python - Indian Institute of Technology Madras (NPTEL)](https://archive.nptel.ac.in/noc/Ecertificate/?q=NPTEL22CS31S2370231802145639)

### 2. Google IT Automation with Python Professional Certificate
By [Christine Rafla](https://www.linkedin.com/in/christinerafla), [Roger Martinez](https://www.linkedin.com/in/rogermartinez), [Kenny Sulaimon](https://www.linkedin.com/in/ken123103), Amanda Ballas, [Phelan V](https://www.linkedin.com/in/phelan-v-0a88237) | Google
- [IT Automation with Python - Google (Coursera)](https://www.coursera.org/account/accomplishments/verify/83G9Y48TUGKA)

## Detailed Explanation and Commentary

### Code Breakdown

#### Importing Libraries
```python
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import csv
import os
from datetime import datetime
```
* The necessary libraries are imported. Tkinter is used for creating the GUI, tkcalendar for date selection, and csv and os for handling file operations.

#### Constants for Dark Theme
```python
# Constants for the dark theme
BG_COLOR = "#2e2e2e"
FG_COLOR = "#ffffff"
ENTRY_BG = "#3e3e3e"
BUTTON_BG = "#4e4e4e"
```
* These constants define the colors used for the dark theme of the application.

#### User Management Class
```python
class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management Application")
        self.root.geometry("400x500")
        self.root.configure(bg=BG_COLOR)
        self.show_home()
```
* The `UserManagementApp` class is initialized with the root window. The window title, size, and background color are set.

#### Home Screen
```python
    def show_home(self):
        """Display the home screen with Sign Up and Sign In options."""
        self.clear_window()
        self.root.title("Home")
        
        tk.Label(self.root, text="Welcome to User Management", bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
        
        signup_button = tk.Button(self.root, text="Sign Up", command=self.show_signup, bg=BUTTON_BG, fg=FG_COLOR)
        signup_button.pack(pady=10)
        
        signin_button = tk.Button(self.root, text="Sign In", command=self.show_signin, bg=BUTTON_BG, fg=FG_COLOR)
        signin_button.pack(pady=10)
```
* The `show_home` method displays the home screen with buttons for Sign Up and Sign In.

#### Sign Up Screen
```python
    def show_signup(self):
        """Display the Sign Up screen."""
        self.clear_window()
        self.root.title("Sign Up")
        
        tk.Label(self.root, text="Sign Up", bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
        
        tk.Label(self.root, text="Name", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_name = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_name.pack(pady=5)
        
        tk.Label(self.root, text="Address", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_address = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_address.pack(pady=5)
        
        tk.Label(self.root, text="Date of Birth", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_dob = DateEntry(self.root, date_pattern='y-mm-dd', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_dob.pack(pady=5)
        
        tk.Label(self.root, text="Initial Balance", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_balance = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_balance.pack(pady=5)
        
        tk.Label(self.root, text="Password", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_password.pack(pady=5)
        
        tk.Label(self.root, text="Confirm Password", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_confirm_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_confirm_password.pack(pady=5)
        
        submit_button = tk.Button(self.root, text="Submit", command=self.submit_form, bg=BUTTON_BG, fg=FG_COLOR)
        submit_button.pack(pady=10)
        
        back_button = tk.Button(self.root, text="Back", command=self.show_home, bg=BUTTON_BG, fg=FG_COLOR)
        back_button.pack(pady=10)
```
* The `show_signup` method displays the Sign Up screen with entry fields for user details and password confirmation. It also includes buttons to submit the form or go back to the home screen.

#### Form Submission
```python
    def submit_form(self):
        """Handle the form submission for Sign Up."""
        name = self.entry_name.get()
        address = self.entry_address.get()
        dob = self.entry_dob.get()
        balance = self.entry_balance.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        
        if not (name and address and dob and balance and password and confirm_password):
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        try:
            balance = float(balance)
            if balance < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Balance must be a non-negative number.")


            return
        
        user_id = self.get_next_user_id()
        
        with open('user.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_id, name, address, dob, balance, password, 1])  # 1 for active account
        
        messagebox.showinfo("Success", f"User registered successfully. Your User ID is {user_id}.")
        self.show_home()
```
* The `submit_form` method handles form submission for Sign Up. It validates the input fields, checks for password confirmation, and ensures the balance is non-negative. The user information is then written to the CSV file, and a success message is displayed with the user ID.

#### Utility Functions
```python
    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def get_next_user_id(self):
        """Generate the next user ID based on the last entry in the CSV file."""
        if not os.path.exists('user.csv'):
            return 1
        
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            lines = list(reader)
            if not lines:
                return 1
            
            last_id = int(lines[-1][0])
            return last_id + 1
```
* `clear_window` clears all widgets from the window, and `get_next_user_id` generates the next user ID based on the last entry in the CSV file.

### Sign In Screen
```python
    def show_signin(self):
        """Display the Sign In screen."""
        self.clear_window()
        self.root.title("Sign In")
        
        tk.Label(self.root, text="Sign In", bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
        
        tk.Label(self.root, text="User ID", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_user_id = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_user_id.pack(pady=5)
        
        tk.Label(self.root, text="Password", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_user_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_user_password.pack(pady=5)
        
        login_button = tk.Button(self.root, text="Login", command=self.login_user, bg=BUTTON_BG, fg=FG_COLOR)
        login_button.pack(pady=10)
        
        back_button = tk.Button(self.root, text="Back", command=self.show_home, bg=BUTTON_BG, fg=FG_COLOR)
        back_button.pack(pady=10)
```
* The `show_signin` method displays the Sign In screen with entry fields for user ID and password. It also includes buttons to log in or go back to the home screen.

### Login Functionality
```python
    def login_user(self):
        """Handle the user login."""
        user_id = self.entry_user_id.get()
        password = self.entry_user_password.get()
        
        if not (user_id and password):
            messagebox.showerror("Error", "Please enter both User ID and Password.")
            return
        
        user_id = int(user_id)
        
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            users = list(reader)
            
        for user in users:
            if int(user[0]) == user_id:
                if int(user[6]) == 0:
                    messagebox.showerror("Error", "This account is locked.")
                    return
                if user[5] == password:
                    self.current_user = user
                    self.show_user_menu()
                    return
                else:
                    self.failed_attempts[user_id] = self.failed_attempts.get(user_id, 0) + 1
                    if self.failed_attempts[user_id] >= 3:
                        user[6] = 0  # Lock the account
                        with open('user.csv', mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(users)
                        messagebox.showerror("Error", "Account locked due to multiple failed attempts.")
                    else:
                        messagebox.showerror("Error", "Incorrect password.")
                    return
        
        messagebox.showerror("Error", "User ID not found.")
```
* The `login_user` method handles user login. It checks if the entered user ID and password are correct and updates the login attempts. If the password is entered incorrectly three times, the account is locked.

### User Menu
```python
    def show_user_menu(self):
        """Display the user menu after successful login."""
        self.clear_window()
        self.root.title("User Menu")
        
        tk.Label(self.root, text=f"Welcome, {self.current_user[1]}", bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
        
        balance_label = tk.Label(self.root, text=f"Account Balance: ${self.current_user[4]}", bg=BG_COLOR, fg=FG_COLOR)
        balance_label.pack(pady=5)
        
        edit_button = tk.Button(self.root, text="Edit Information", command=self.edit_info, bg=BUTTON_BG, fg=FG_COLOR)
        edit_button.pack(pady=5)
        
        change_password_button = tk.Button(self.root, text="Change Password", command=self.show_change_password, bg=BUTTON_BG, fg=FG_COLOR)
        change_password_button.pack(pady=5)
        
        transfer_button = tk.Button(self.root, text="Fund Transfer", command=self.show_fund_transfer, bg=BUTTON_BG, fg=FG_COLOR)
        transfer_button.pack(pady=5)
        
        logout_button = tk.Button(self.root, text="Logout", command=self.logout_user, bg=BUTTON_BG, fg=FG_COLOR)
        logout_button.pack(pady=10)
```
* The `show_user_menu` method displays the user menu after successful login, showing the user's name and account balance. It includes buttons for editing information, changing password, transferring funds, and logging out.

### Edit Information
```python
    def edit_info(self):
        """Display the user information (non-editable)."""
        self.clear_window()
        self.root.title("Edit Information")
        
        tk.Label(self.root, text="Edit Information", bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
        
        tk.Label(self.root, text=f"Name: {self.current_user[1]}", bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        tk.Label(self.root, text=f"Address: {self.current_user[2]}", bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        tk.Label(self.root, text=f"Date of Birth: {self.current_user[3]}", bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        tk.Label(self.root, text=f"Account Balance: ${self.current_user[4]}", bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        
        back_button = tk.Button(self.root, text="Back", command=self.show_user_menu, bg=BUTTON_BG, fg=FG_COLOR)
        back_button.pack(pady=10)
```
* The `edit_info` method displays the user's information in a non-editable format. It includes a button to go back to the user menu.

### Change Password
```python
    def show_change_password(self):
        """Display the Change Password screen."""
        self.clear_window()
        self.root.title("Change Password")
        
        tk.Label(self.root, text="Change Password", bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
        
        tk.Label(self.root, text="Current Password", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_current_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_current_password.pack(pady=5)
        
        tk.Label(self.root, text="New Password", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_new_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_new_password.pack(pady=5)
        
        tk.Label(self.root, text="Confirm New Password", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_confirm_new_password = tk.Entry(self.root, show='*', bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_confirm_new_password.pack(pady=5)
        
        submit_button = tk.Button(self.root, text="Submit", command=self.change_password, bg=BUTTON_BG, fg=FG_COLOR)
        submit_button.pack(pady=10)
        
        back_button = tk.Button(self.root, text="Back", command=self.show_user_menu, bg=BUTTON_BG, fg=FG_COLOR)
        back_button.pack(pady=10)
    
    def change_password(self):
        """Handle the password change request."""
        current_password = self.entry_current_password.get()
        new_password = self.entry_new_password.get()
        confirm_new_password = self.entry_confirm_new_password.get()
        
        if current_password != self.current_user[5]:
            messagebox.showerror("Error", "Current password is incorrect.")
            return
        
        if new_password != confirm_new_password:
            messagebox.showerror("Error", "New passwords do not match.")
            return
        
        self.current_user[5] = new_password
        
        users = []
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            for user in reader:
                if int(user[0]) == int(self.current_user

[0]):
                    user[5] = new_password
                users.append(user)
        
        with open('user.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)
        
        messagebox.showinfo("Success", "Password changed successfully.")
        self.show_user_menu()
```
* The `show_change_password` method displays the Change Password screen with fields for the current password, new password, and confirmation of the new password. The `change_password` method handles the password change request, ensuring the current password is correct and the new passwords match.

### Fund Transfer
```python
    def show_fund_transfer(self):
        """Display the Fund Transfer screen."""
        self.clear_window()
        self.root.title("Fund Transfer")
        
        tk.Label(self.root, text="Fund Transfer", bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
        
        tk.Label(self.root, text="Recipient User ID", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_recipient_id = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_recipient_id.pack(pady=5)
        
        tk.Label(self.root, text="Amount", bg=BG_COLOR, fg=FG_COLOR).pack()
        self.entry_amount = tk.Entry(self.root, bg=ENTRY_BG, fg=FG_COLOR)
        self.entry_amount.pack(pady=5)
        
        transfer_button = tk.Button(self.root, text="Transfer", command=self.transfer_funds, bg=BUTTON_BG, fg=FG_COLOR)
        transfer_button.pack(pady=10)
        
        back_button = tk.Button(self.root, text="Back", command=self.show_user_menu, bg=BUTTON_BG, fg=FG_COLOR)
        back_button.pack(pady=10)
    
    def transfer_funds(self):
        """Handle the fund transfer request."""
        recipient_id = self.entry_recipient_id.get()
        amount = self.entry_amount.get()
        
        if not (recipient_id and amount):
            messagebox.showerror("Error", "Please enter both Recipient User ID and Amount.")
            return
        
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Amount must be a positive number.")
            return
        
        recipient_id = int(recipient_id)
        sender_id = int(self.current_user[0])
        
        users = []
        recipient_found = False
        with open('user.csv', mode='r') as file:
            reader = csv.reader(file)
            for user in reader:
                if int(user[0]) == recipient_id:
                    recipient_found = True
                    recipient_balance = float(user[4])
                    user[4] = str(recipient_balance + amount)
                if int(user[0]) == sender_id:
                    sender_balance = float(user[4])
                    if sender_balance < amount:
                        messagebox.showerror("Error", "Insufficient funds.")
                        return
                    user[4] = str(sender_balance - amount)
                    self.current_user = user
                users.append(user)
        
        if not recipient_found:
            messagebox.showerror("Error", "Recipient User ID not found.")
            return
        
        with open('user.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)
        
        messagebox.showinfo("Success", "Funds transferred successfully.")
        self.show_user_menu()
```
* The `show_fund_transfer` method displays the Fund Transfer screen with fields for the recipient's user ID and the transfer amount. The `transfer_funds` method handles the fund transfer request, ensuring sufficient funds are available and updating the balances accordingly.

### Logout
```python
    def logout_user(self):
        """Handle user logout."""
        self.current_user = None
        self.show_home()
```
* The `logout_user` method handles user logout and returns to the home screen.

### Running the Application
```python
if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()
```
* This block runs the application by creating a Tkinter root window and an instance of the `UserManagementApp` class.

## Conclusion

This user management application demonstrates the application of various programming concepts and techniques learned from the courses "The Joy of Computing using Python" and "Google IT Automation with Python Professional Certificate". The project covers user interface design, file handling, data validation, and the implementation of security measures such as account locking.

The knowledge gained from these courses was crucial in understanding the fundamental concepts of Python programming and applying them to create a functional and secure application. The project showcases the importance of OOP principles, file manipulation, and user interaction in real-world applications.
#### Credits
- **Project Creator:** [Pankaj Mondal](https://github.com/Buroush)
- **LinkedIn:** [buroush](https://www.linkedin.com/in/buroush)
- **LeetCode:** [Buroush](https://leetcode.com/u/Buroush)
- **HackerRank:** [pankajmondalpro1](https://www.hackerrank.com/profile/pankajmondalpro1)
## References
1. [The Joy of Computing using Python - Indian Institute of Technology Madras (NPTEL)](https://archive.nptel.ac.in/noc/Ecertificate/?q=NPTEL22CS31S2370231802145639)
2. [IT Automation with Python - Google (Coursera)](https://www.coursera.org/account/accomplishments/verify/83G9Y48TUGKA)

---

