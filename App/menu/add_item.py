from .menu_operation import MenuOperations
from validation.common_validation import CommonValidation

class AddItem(MenuOperations):
    
    def add_item(self):
        validator = CommonValidation()
        data = self.read_menu()
        print("\n" + "=" * 65)
        print("🍽️  ADD NEW ITEM 🍽️".center(65))
        print("=" * 65)

        
        while True:

            print("\n" + "-" * 25 + " SELECT CATEGORY " + "-" * 25)
            print("1. Breakfast")
            print("2. Lunch")
            print("3. Dinner")
            print("4. South Indian")
            print("5. Chinese")
            print("6. Italian")
            print("7. Snacks")
            print("8. Beverages")
            print("9. Desserts")
            print("10. Sandwich")
            print("-" * 65)

            choice = input("Enter choice: ")
            choice = validator.validate_choice(choice, 1, 10)

            if choice is not None:
                break

        if choice == 1:
            category = "Breakfast"
            prefix = "BF"
        elif choice == 2:
            category = "Lunch"
            prefix = "LN"
        elif choice == 3:
            category = "Dinner"
            prefix = "DN"
        elif choice == 4:
            category = "South Indian"
            prefix = "SI"
        elif choice == 5:
            category = "Chinese"
            prefix = "CH"
        elif choice == 6:
            category = "Italian"
            prefix = "IT"
        elif choice == 7:
            category = "Snacks"
            prefix = "SN"
        elif choice == 8:
            category = "Beverages"
            prefix = "BV"
        elif choice == 9:
            category = "Desserts"
            prefix = "DS"
        elif choice == 10:
            category = "Sandwich"
            prefix = "SW"
        else:
            print("Invalid choice")
            return
        
        print(f"\nSelected Category: {category}")

        while True:
            name = input("Enter item name: ")
            name = validator.validate_item_name(name)

            if name is not None:
                break
        while True:
            price = input("Enter price: ")

            try:
                price = float(price)
                if price <= 0:
                    print("Price must be greater than 0")
                    continue
                break
            except:
                print("Invalid price! Enter numbers only.")
        
        count = 1
        while True:
            item_id = prefix + str(100 + count)
            exists = False
            for item in data:
                if item["id"] == item_id:
                    exists = True
                    break
            if not exists:
                break
            count += 1

        new_item = {
            "id": item_id,
            "name": name,
            "price": price,
            "category": category
        }

        
        last_index = -1
        for i in range(len(data)):
            if data[i]["category"].lower() == category.lower():
                last_index = i

        
        if last_index == -1:
            data.append(new_item)
        else:
            
            data.insert(last_index + 1, new_item)

        self.write_menu(data)
        print("\n" + "=" * 65)
        print("ITEM ADDED SUCCESSFULLY".center(65))
        print("=" * 65)
        print(f"Item Name : {name}")
        print(f"Item ID   : {item_id}")
        print(f"Category  : {category}")
        print(f"Price     : ₹{price}")
        print("-" * 65)