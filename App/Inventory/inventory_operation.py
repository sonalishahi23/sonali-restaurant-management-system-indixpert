from validation.common_validation import CommonValidation
import json

class InventoryOperations:

    def read_inventory(self):
        try:
            with open("App/database/inventory.json", "r") as file:
                return json.load(file)
        except:
            return []

    def write_inventory(self, data):
        with open("App/database/inventory.json", "w") as file:
            json.dump(data, file, indent=4)

    def add_item(self):
        data = self.read_inventory()
        validator=CommonValidation()

        print("\n" + "=" * 50)
        print("ADD NEW INVENTORY ITEM".center(50))
        print("=" * 50)

    
        while True:
            name_input = input("Enter item name: ")
            name = validator.validate_item_name(name_input)

            if name is None:
                continue

        
            if any(item["item_name"].lower() == name.lower() for item in data):
                print("Item already exists")
                continue

            break

        while True:
            qty_input = input("Enter quantity: ")

            if not qty_input.isdigit():
                print("Quantity must be numeric")
                continue

            quantity = int(qty_input)

            if quantity <= 0:
                print("Quantity must be greater than 0")
                continue

            break

        item = {
            "item_id": len(data) + 1,
            "item_name": name,
            "quantity": quantity
        }

        data.append(item)
        self.write_inventory(data)

        print("\n" + "-" * 50)
        print("Item added successfully!")
        print("-" * 50)

    
        print(f"{'ID':<5} {'ITEM NAME':<25} {'QUANTITY':<10}")
        print("-" * 50)
        print(f"{item['item_id']:<5} {item['item_name']:<25} {item['quantity']:<10}")
        print("-" * 50)

    def view_inventory(self):
        data = self.read_inventory()

        if not data:
            print("No items found")
            return

        print("\n" + "=" * 70)
        print("INVENTORY LIST".center(70))
        print("=" * 70)

        print(f"{'ID':<5} {'ITEM NAME':<25} {'QUANTITY':<10}")
        print("-" * 70)

        for item in data:
            print(f"{item['item_id']:<5} {item['item_name']:<25} {item['quantity']:<10}")

            if item["quantity"] < 5:
                print(" " * 10 + " Low Stock!")

        print("=" * 70)

    def update_stock(self):
        data = self.read_inventory()
        validator = CommonValidation()

        print("\n" + "=" * 50)
        print("UPDATE INVENTORY STOCK".center(50))
        print("=" * 50)

        while True:
            item_id_input = input("Enter item ID: ")
            item_id = validator.validate_id(item_id_input, "Item ID")

            if item_id is None:
                continue
            break

        for item in data:
            if item["item_id"] == item_id:

                print(f"\nCurrent Stock of {item['item_name']}: {item['quantity']}")

                
                while True:
                    print("\n1. Add Stock")
                    print("2. Remove Stock")

                    choice = input("Enter choice: ")
                    op = validator.validate_choice(choice, 1, 2)

                    if op is None:
                        continue
                    break


                while True:
                    qty_input = input("Enter quantity: ")

                    if not qty_input.isdigit():
                        print("Quantity must be numeric")
                        continue

                    qty = int(qty_input)

                    if qty <= 0:
                        print("Quantity must be greater than 0")
                        continue

                    if op == 2 and item["quantity"] < qty:
                        print("Not enough stock to remove")
                        continue

                    break

                if op == 1:
                    item["quantity"] += qty
                elif op == 2:
                    item["quantity"] -= qty
                self.write_inventory(data)

                print("\n" + "-" * 50)
                print("Stock updated successfully!")
                print("-" * 50)

                print(f"{'ID':<5} {'ITEM NAME':<25} {'QUANTITY':<10}")
                print("-" * 50)
                print(f"{item['item_id']:<5} {item['item_name']:<25} {item['quantity']:<10}")
                print("-" * 50)

                return

        print("Item not found")

    def delete_item(self):
        data = self.read_inventory()
        validator = CommonValidation()

        print("\n" + "=" * 50)
        print("DELETE INVENTORY ITEM".center(50))
        print("=" * 50)

    
        while True:
            item_id_input = input("Enter item ID: ")
            item_id = validator.validate_id(item_id_input, "Item ID")

            if item_id is None:
                continue
            break

        item_to_delete = None
        for item in data:
            if item["item_id"] == item_id:
                item_to_delete = item
                break

        if not item_to_delete:
            print("Item not found")
            return

    
        print("\nItem Found:")
        print(f"{'ID':<5} {'ITEM NAME':<25} {'QUANTITY':<10}")
        print("-" * 50)
        print(f"{item_to_delete['item_id']:<5} {item_to_delete['item_name']:<25} {item_to_delete['quantity']:<10}")
        print("-" * 50)

    
        confirm = input("Are you sure you want to delete? (yes/no): ").lower()

        if confirm != 'yes':
            print("Deletion cancelled")
            return

        data.remove(item_to_delete)
        self.write_inventory(data)

        print("\n" + "-" * 50)
        print("Item deleted successfully!")
        print("-" * 50)

    def load_default_inventory(self):
        data = self.read_inventory()

        if not data:
            default_items = [
                {"item_id": 1, "item_name": "Milk", "quantity": 50},
                {"item_id": 2, "item_name": "Butter", "quantity": 30},
                {"item_id": 3, "item_name": "Cheese", "quantity": 25},
                {"item_id": 4, "item_name": "Paneer", "quantity": 40},
                {"item_id": 5, "item_name": "Cream", "quantity": 20},
                {"item_id": 6, "item_name": "Curd", "quantity": 35},

    
                {"item_id": 7, "item_name": "Wheat Flour", "quantity": 60},
                {"item_id": 8, "item_name": "Maida", "quantity": 50},
                {"item_id": 9, "item_name": "Rice", "quantity": 80},
                {"item_id": 10, "item_name": "Basmati Rice", "quantity": 40},
                {"item_id": 11, "item_name": "Suji", "quantity": 30},
                {"item_id": 12, "item_name": "Besan", "quantity": 25},

    
                {"item_id": 13, "item_name": "Potato", "quantity": 100},
                {"item_id": 14, "item_name": "Onion", "quantity": 90},
                {"item_id": 15, "item_name": "Tomato", "quantity": 80},
                {"item_id": 16, "item_name": "Capsicum", "quantity": 40},
                {"item_id": 17, "item_name": "Cabbage", "quantity": 30},
                {"item_id": 18, "item_name": "Carrot", "quantity": 35},
                {"item_id": 19, "item_name": "Peas", "quantity": 40},
                {"item_id": 20, "item_name": "Corn", "quantity": 30},

    
                {"item_id": 21, "item_name": "Garlic", "quantity": 25},
                {"item_id": 22, "item_name": "Ginger", "quantity": 20},
                {"item_id": 23, "item_name": "Green Chilli", "quantity": 20},
                {"item_id": 24, "item_name": "Oil", "quantity": 40},
                {"item_id": 25, "item_name": "Salt", "quantity": 20},
                {"item_id": 26, "item_name": "Sugar", "quantity": 30},

    
                {"item_id": 27, "item_name": "Turmeric", "quantity": 15},
                {"item_id": 28, "item_name": "Red Chilli Powder", "quantity": 15},
                {"item_id": 29, "item_name": "Coriander Powder", "quantity": 20},
                {"item_id": 30, "item_name": "Garam Masala", "quantity": 15},
                {"item_id": 31, "item_name": "Jeera", "quantity": 15},

    
                {"item_id": 32, "item_name": "Pizza Base", "quantity": 30},
                {"item_id": 33, "item_name": "Pasta", "quantity": 40},
                {"item_id": 34, "item_name": "Noodles", "quantity": 40},
                {"item_id": 35, "item_name": "Burger Bun", "quantity": 30},
                {"item_id": 36, "item_name": "Sandwich Bread", "quantity": 30},
                {"item_id": 37, "item_name": "Mayonnaise", "quantity": 20},
                {"item_id": 38, "item_name": "Ketchup", "quantity": 25},

    
                {"item_id": 39, "item_name": "Chicken", "quantity": 40},
                {"item_id": 40, "item_name": "Eggs", "quantity": 60},

    
                {"item_id": 41, "item_name": "Tea Leaves", "quantity": 20},
                {"item_id": 42, "item_name": "Coffee", "quantity": 20},
                {"item_id": 43, "item_name": "Chocolate Syrup", "quantity": 15},
                {"item_id": 44, "item_name": "Mango Pulp", "quantity": 20},

    
                {"item_id": 45, "item_name": "Cocoa Powder", "quantity": 15},
                {"item_id": 46, "item_name": "Baking Powder", "quantity": 10},
                {"item_id": 47, "item_name": "Vanilla Essence", "quantity": 10},
                {"item_id": 48, "item_name": "Ice Cream Base", "quantity": 20},
                {"item_id": 49, "item_name": "Dry Fruits", "quantity": 15},

    
                {"item_id": 50, "item_name": "Lemon", "quantity": 30}
            ]

            self.write_inventory(default_items)
            