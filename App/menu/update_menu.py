from .menu_operation import MenuOperations
from validation.common_validation import CommonValidation

class UpdateItem(MenuOperations):

    def update_item(self):

        data = self.read_menu()
        validator=CommonValidation()
        print("\n" + "=" * 65)
        print("UPDATE MENU ITEM ".center(65))
        print("=" * 65)

        while True:
            item_id = input("Enter Item ID to update: ")
            item_id = validator.validate_item_id(item_id)

            if item_id is not None:
               break

        found=False
        for item in data:
            if item["id"] == item_id:
                found=True
                print("\nCurrent Item Details:")
                print("-" * 65)
                print(f"ID       : {item['id']}")
                print(f"Name     : {item['name']}")
                print(f"Category : {item['category']}")
                print(f"Price    : ₹{item['price']}")
                print("-" * 65)

                print("\n" + "-" * 20 + " UPDATE OPTIONS " + "-" * 20)
                print("1. Update Name")
                print("2. Update Price")
                print("3. Update Both")
                print("-" * 65)

                while True:
                    choice = input("Enter choice: ")
                    choice = validator.validate_choice(choice, 1, 3)

                    if choice is not None:
                        break

                if choice == 1:
                    while True:
                        new_name = input("Enter new name: ")
                        new_name = validator.validate_item_name(new_name)

                        if new_name is not None:
                            break

                    item["name"] = new_name

                elif choice == 2:
                    while True:
                        price = input("Enter new price: ")

                        try:
                            price = float(price)
                            if price <= 0:
                                print("Price must be greater than 0")
                                continue
                            break
                        except:
                            print("Invalid price! Enter numbers only.")

                    item["price"] = price
                    
                
                elif choice == 3:
                    while True:
                        new_name = input("Enter new name: ")
                        new_name = validator.validate_item_name(new_name)

                        if new_name is not None:
                            break

                    while True:
                        price = input("Enter new price: ")

                        try:
                            price = float(price)
                            if price <= 0:
                                print("Price must be greater than 0")
                                continue
                            break
                        except:
                            print("Invalid price! Enter numbers only.")

                    item["name"] = new_name
                    item["price"] = price

                else:
                    print("Invalid choice")
                    return

                while True:
                    confirm = input("Are you sure you want to update? (yes/no): ").lower()

                    if confirm == "yes":
                        self.write_menu(data)
                        print("Item Updated Successfully")
                        break
                    elif confirm == "no":
                        print("Update Cancelled")
                        return
                    else:
                        print("Invalid input! Enter 'yes' or 'no'")

        
        if not found:
            print("Item not found")