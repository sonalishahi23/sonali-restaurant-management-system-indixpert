from .staff_operation import StaffOperations
from validation.common_validation import CommonValidation

class StaffManagement:

    def show_menu(self):

        staff = StaffOperations()
        validator = CommonValidation()


        while True:
            print("\n" + "=" * 60)
            print("STAFF MANAGEMENT DASHBOARD".center(60))
            print("=" * 60)

            print("1. Add Staff")
            print("2. View Staff")
            print("3. Update Staff")
            print("4. Delete Staff")
            print("5. Back")

            print("-" * 60)
            choice = input("Enter choice (1-5): ")
            choice = validator.validate_choice(choice, 1, 5)

            if choice is None:
                continue

            if choice == 1:
                print("\n--- Add Staff ---")
                staff.add_staff()

            elif choice == 2:
                print("\n--- View Staff ---")
                staff.view_staff()

            elif choice == 3:
                print("\n--- Update Staff ---")
                staff.update_staff()

            elif choice == 4:
                print("\n--- Delete Staff ---")
                staff.delete_staff()

            elif choice == 5:
                print("\n--- BACK ---")
                break

            else:
                print("Invalid choice")