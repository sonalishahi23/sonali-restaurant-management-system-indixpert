import json
from validation.auth_validation import EmailValidation, PasswordValidation
from admin_management.admin_dashboard import Admin_dashboard
from staff_management.staff_dashboard import StaffDashboard
from datetime import datetime
import os


os.makedirs("App/logs", exist_ok=True)
class Login:
             
    def write_login_log(self, email, role, success=True):
        """Append login attempt info to a log file"""
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y %H:%M:%S")
        log_file = "App/logs/login_logs.txt"

        status = "Successful" if success else "Failed"

        with open(log_file, "a") as file:  # no UTF needed
            file.write(f"{date_time} | Email: {email} | Role: {role} | Login {status}\n")
          
    def login_user(self):

        email_validator = EmailValidation()
        password_validator = PasswordValidation()

        print("\n" + "=" * 60)
        print("           *****LOGIN DASHBOARD*****  ")
        print("=" * 60)

        while True:
            email = input("Enter Email: ")
            if email_validator.validate_email(email):
                break
            else:
                print("Invalid Email")

        while True:
            password = input("Enter Password: ")
            if password_validator.validate_password(password):
                break
            else:
                print("Invalid Password")

        try:
            with open("App/database/users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("No users registered")
            return
        
        found_email = False
        password_correct = False

        for user in data:
            if user["email"] == email:
                found_email = True
                if user["password"] == password:
                    password_correct = True
                    print("\n" + "-" * 60)
                    print(f"Login Successful! Welcome, {user['name']} ")
                    print("-" * 60)

                    self.write_login_log(email, user["role"], success=True)
            
                    if user["role"] == "admin":
                        print("Redirecting to Admin Dashboard...\n")
                        admin = Admin_dashboard()
                        admin.show_dashboard()

                    elif user["role"] == "staff":
                        print("Redirecting to Staff Dashboard...\n")
                        staff = StaffDashboard()
                        staff.show_menu()
                        return  
                    break  


        if not found_email:
            print("Email not registered. Please sign up first.")
            self.write_login_log(email, "Unknown", success=False)
        elif not password_correct:
            print("Invalid Email or Password")
            self.write_login_log(email, "Unknown", success=False)