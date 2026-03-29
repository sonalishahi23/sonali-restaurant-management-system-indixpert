from .menu_operation import MenuOperations
from validation.common_validation import CommonValidation

class DeleteItem(MenuOperations):

    def delete_item(self):

        data = self.read_menu()
        validator=CommonValidation()
        print("\n" + "=" * 65)
        print("DELETE MENU ITEM ".center(65))
        print("=" * 65)

        while True:
            item_id = input("Enter Item ID to delete: ")
            item_id = validator.validate_item_id(item_id)

            if item_id is not None:
                break

        found = False

        for item in data:
            if item["id"] == item_id:
                found = True
                print("\nItem Found:")
                print("-" * 65)
                print(f"ID       : {item['id']}")
                print(f"Name     : {item['name']}")
                print(f"Category : {item['category']}")
                print(f"Price    : ₹{item['price']}")
                print("-" * 65)

                while True:
                    confirm = input("Are you sure you want to delete? (yes/no): ").lower()

                    if confirm == "yes":
                        data.remove(item)
                        self.write_menu(data)
                        print("Item Deleted Successfully")
                        break

                    elif confirm == "no":
                        print("Deletion Cancelled")
                        return

                    else:
                        print("Invalid input! Enter 'yes' or 'no'")

                break   
        if not found:
            print("Item not found")