import tkinter as tk
from tkinter import simpledialog, messagebox, Listbox, Scrollbar
import re
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login App")

        self.stored_username = ""
        self.stored_password = ""
        self.stored_email = ""
        self.stored_phone = ""

        self.create_widgets()

    def create_widgets(self):
        self.setup_button = tk.Button(self.root, text="Set Up User", command=self.setup_user, bg="lightblue")
        self.setup_button.pack(padx=10, pady=5, ipadx=10)

        self.login_button = tk.Button(self.root, text="Log In", command=self.login_user, bg="lightgreen")
        self.login_button.pack(padx=10, pady=5, ipadx=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app, bg="lightgray")
        self.exit_button.pack(padx=10, pady=5, ipadx=10)

    def setup_user(self):
        self.stored_username = simpledialog.askstring("Set Up User", "Set your username:")

        while True:
            self.stored_password = simpledialog.askstring("Set Up User", "Set your password:", show='*')
            if self.stored_password is None:
                self.exit_app()
                return

            if self.validate_password(self.stored_password):
                break
            else:
                messagebox.showerror("Invalid Password",
                                     "Password must be at least 7 characters long, include at least one uppercase letter, one special character, and a combination of letters and numbers.")

        self.stored_email = simpledialog.askstring("Set Up User", "Set your email:")
        if self.stored_email is None:
            self.exit_app()
            return

        self.stored_phone = simpledialog.askstring("Set Up User", "Set your phone number:")
        if self.stored_phone is None:
            self.exit_app()
            return

        if self.stored_username and self.stored_password and self.stored_email and self.stored_phone:
            messagebox.showinfo("Set Up User", "User details saved successfully!")
        else:
            messagebox.showerror("Set Up User", "All fields are required.")

    def validate_password(self, password):
        if (len(password) >= 7 and
                re.search(r"[A-Z]", password) and
                re.search(r"[a-z]", password) and
                re.search(r"[0-9]", password) and
                re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
            return True
        return False

    def login_user(self):
        input_username = simpledialog.askstring("Log In", "Enter username:")
        if input_username is None:
            self.exit_app()
            return

        while input_username != self.stored_username:
            messagebox.showerror("Log In", "Username is incorrect. Please enter the correct username.")
            input_username = simpledialog.askstring("Log In", "Enter username:")
            if input_username is None:
                self.exit_app()
                return

        input_password = simpledialog.askstring("Log In", "Enter password:", show='*')
        if input_password is None:
            self.exit_app()
            return

        while input_password != self.stored_password:
            if not self.validate_password(input_password):
                messagebox.showerror("Log In", "Password must be at least 7 characters long, include at least one uppercase letter, one special character, and a combination of letters and numbers.")
            else:
                messagebox.showerror("Log In", "Password is incorrect. Please enter the correct password.")

            input_password = simpledialog.askstring("Log In", "Enter password:", show='*')
            if input_password is None:
                self.exit_app()
                return

        input_email = simpledialog.askstring("Log In", "Enter email:")
        if input_email is None:
            self.exit_app()
            return

        while input_email != self.stored_email:
            if '@' not in input_email:
                messagebox.showerror("Log In", "Enter a correct email ID format.")
            else:
                messagebox.showerror("Log In", "Email is incorrect. Please enter the correct email.")

            input_email = simpledialog.askstring("Log In", "Enter email:")
            if input_email is None:
                self.exit_app()
                return

        input_phone = simpledialog.askstring("Log In", "Enter phone number:")
        if input_phone is None:
            self.exit_app()
            return

        while input_phone != self.stored_phone:
            messagebox.showerror("Log In", "Phone number is incorrect. Please enter the correct phone number.")
            input_phone = simpledialog.askstring("Log In", "Enter phone number:")
            if input_phone is None:
                self.exit_app()
                return

        messagebox.showinfo("Log In", "Logged in successfully!")
        self.fetch_file()

    def fetch_file(self):
        directory = "E:\\python pro\\resumes"
        files = os.listdir(directory)
        if not files:
            messagebox.showerror("Fetch File", "No files found in the directory.")
            return

        self.file_window = tk.Toplevel(self.root)
        self.file_window.title("Select File")

        scrollbar = Scrollbar(self.file_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_listbox = Listbox(self.file_window, yscrollcommand=scrollbar.set)
        for file in files:
            self.file_listbox.insert(tk.END, file)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)

        select_button = tk.Button(self.file_window, text="Select", command=self.select_file)
        select_button.pack(pady=10)

        exit_button = tk.Button(self.file_window, text="Exit", command=self.file_window.destroy, bg="lightgray")
        exit_button.pack(pady=10)

    def select_file(self):
        file_name = self.file_listbox.get(tk.ACTIVE)
        self.read_file(file_name)

    def read_file(self, file_name):
        directory = "E:\\python pro\\resumes"
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                file_content = file.read()
            messagebox.showinfo("File Content", file_content)
        else:
            messagebox.showerror("Fetch File", "File not found.")

    def exit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
