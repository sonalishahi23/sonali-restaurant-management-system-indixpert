import json
from validation.auth_validation import EmailValidation, PasswordValidation
from admin_management.admin_dashboard import Admin_dashboard
from staff_management.staff_dashboard import StaffDashboard

class Login:

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
        
        found_email=False
        for user in data:
            if user["email"] == email and user["password"] == password:
                found_email=True
                print("\n" + "-" * 60)
                print(f"Login Successful! Welcome, {user['name']} ")
                print("-" * 60)
                
                if user["role"] == "admin":
                    print("Redirecting to Admin Dashboard...\n")
                    admin = Admin_dashboard()
                    admin.show_dashboard()

                elif user["role"] == "staff":
                    print("Redirecting to Staff Dashboard...\n")
                    staff = StaffDashboard()
                    staff.show_menu()
                return
            else:
                print("Invalid Email or Password")
                print("-" * 60)
        
        if not found_email:
            print("Email not registered. Please sign up first.")