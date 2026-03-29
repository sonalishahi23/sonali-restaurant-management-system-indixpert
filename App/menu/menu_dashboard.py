from .add_item import AddItem
from .update_menu import UpdateItem
from .delete_menu import DeleteItem
from .view_menu import ViewMenu
from validation.common_validation import CommonValidation

class MenuDashboard:

    def menu_dashboard(self):
        validator = CommonValidation()
        while True:
            print("\n" + "=" * 65)
            print("----- MENU MANAGEMENT -----".center(65))
            print("=" * 65)
            
            print("1 Add Item")
            print("2 View Menu")
            print("3 Update Item")
            print("4 Delete Item")
            print("5 Back")
            print("-" * 65)
            choice = input("Enter choice: ")
            validated_choice = validator.validate_choice(choice, 1, 5)

            if validated_choice is None:
                continue

            if validated_choice == 1:
                print("\nAdding New Item...\n")
                AddItem().add_item()

            elif validated_choice == 2:
                print("\nShowing Menu...\n")
                ViewMenu().view_menu()

            elif validated_choice == 3:
                print("\nUpdating Item...\n")
                UpdateItem().update_item()

            elif validated_choice == 4:
                print("\nDeleting Item...\n")
                DeleteItem().delete_item()

            elif validated_choice == 5:
                print("\nReturning to Admin Dashboard...")
                break

            else:
                print("Invalid choice")