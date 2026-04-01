from Inventory.inventory_operation import InventoryOperations
from validation.common_validation import CommonValidation

class InventoryDashboard:

    def show_menu(self):
        inv = InventoryOperations()
        inv.load_default_inventory()
        validator = CommonValidation()

        while True:
            print("\n" + "-" * 25 + " INVENTORY MENU " + "-" * 25)
            print("1. Add Item")
            print("2. View Inventory")
            print("3. Update Stock")
            print("4. Delete Item")
            print("5. Back")

            choice = input("Enter choice: ")
            validated_choice = validator.validate_choice(choice, 1, 5)

            if validated_choice is None:
               continue

            if validated_choice == 1:
                inv.add_item()
            elif validated_choice == 2:
                inv.view_inventory()
            elif validated_choice == 3:
                inv.update_stock()
            elif validated_choice == 4:
                inv.delete_item()
            elif validated_choice == 5:
                break
            else:
                print("Invalid choice")