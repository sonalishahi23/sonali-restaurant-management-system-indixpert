import json
import uuid
from validation.auth_validation import Name_validation, EmailValidation, PasswordValidation

class SignUp:

    def register_user(self):

        user_id = str(uuid.uuid4().int)[:6]

        validating_name = Name_validation()
        print("\n" + "=" * 60)
        print("           *****SIGN UP DASHBOARD*****  ")
        print("=" * 60)
        while True:
            name = input("Enter Name: ")
            if  validating_name.validation_name(name):
                break
            else:
                print("Please Enter a Valid Name.")

        email_validator = EmailValidation()

        while True:
            email = input("Enter Email: ")

            if not email_validator.validate_email(email):
                print("Please Enter a Valid E-mail")
                continue

            try:
                with open("App/database/users.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []

            email_exists = False

            for user in data:
                if user["email"] == email:
                    email_exists = True
                    print("Email already registered. Try another email.")
                    break

            if not email_exists:
                break

        password_validator = PasswordValidation()
        while True:
            password = input("Enter Password: ")
            if not password_validator.validate_password(password):
                print("Please Enter A Valid Password")
            else:
                break
        
        while True:
            print("\n" + "-" * 25 + " SELECT ROLE " + "-" * 25)
            print("1. Admin")
            print("2. Staff")
            print("-" * 60)

            choice = input("Choose Role: ")

            if choice == "1":
                role = "admin"
                break
            elif choice == "2":
               role = "staff"
               break
            else:
               print("Invalid role selected")
    
        user = {
            "id": user_id,
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }

        try:
            with open("App/database/users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(user)

        with open("App/database/users.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\n" + "=" * 60)
        print("SIGNUP SUCCESSFUL".center(60))
        print("=" * 60)
        print(f"Name: {name}")
        print(f"User ID: {user_id}")
        print(f"Role: {role.upper()}")
        print("-" * 60)