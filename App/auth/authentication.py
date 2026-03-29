from auth.sign_up import SignUp
from auth.login import Login

class Authentication:

    def menu(self):

        while True:
            print("\n" + "=" * 60)
            print("           *****ROYAL RESTAURANT*****  ")
            print("=" * 60)

            print("\n" + "-" * 25 + " WELCOME " + "-" * 25)
            print("\n1. Sign Up")
            print("2. Login")
            print("3. Exit")
            print("-" * 60)

            choice = input("Enter choice: ")

            if choice == "1":
                print("\nRedirecting to Sign Up...\n")
                SignUp().register_user()

            elif choice == "2":
                print("\nRedirecting to Login...\n")
                Login().login_user()

            elif choice == "3":
                print("\nThank you for visiting")
                break

            else:
                print("Invalid choice")