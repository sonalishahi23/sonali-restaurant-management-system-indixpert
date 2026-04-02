import json
import uuid
from menu.menu_operation import MenuOperations
from validation.common_validation import CommonValidation
from datetime import datetime
import os
from Inventory.dish_ingredients import dish_ingredients
from Inventory.inventory_operation import InventoryOperations

class OrderOperations:

    def write_order_log(self, order_id, action, total_bill=None):

        os.makedirs("App/logs", exist_ok=True)
        log_file = "App/logs/order_logs.txt"

        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y %H:%M:%S")

        total_info = f" | Total: Rs{total_bill}" if total_bill else ""

        with open(log_file, "a") as file:
            file.write(f"{date_time} | Order ID: {order_id} | Action: {action}{total_info}\n")

    def read_orders(self):
        try:
            with open("App/database/order.json", "r") as file:
                return json.load(file)
        except:
            return []

    def write_orders(self, data):
        with open("App/database/order.json", "w") as file:
            json.dump(data, file, indent=4)

    
    def generate_order_id(self):
        return int(str(uuid.uuid4().int)[:10])

    
    def start_order(self):
        return self.generate_order_id()

    
    def add_item_to_order(self, order_id):
        orders = self.read_orders()

        
        order = None
        for o in orders:
            if o["order_id"] == order_id:
                order = o
                break

        
        if order is None:
            order = {
                "order_id": order_id,
                "items": [],
                "total_bill": 0.0,
                "status": "Pending"
            }
            orders.append(order)

        menu= MenuOperations() 
        validator=CommonValidation()
        while True:
            item_id = input("Enter item ID: ")
            item_id = validator.validate_item_id(item_id)

            if item_id is None:
                continue
            item = menu.get_item_by_id(item_id)

            if item is None:
                print("Item not found in menu. Try again.")
                continue
            
            break

        item_name = item["name"]
        price = item["price"]

        print(f"Selected Item Name: {item_name} - Price of Item: ₹{price}")
        while True:
            quantity = input("Enter quantity: ")
            try:
                quantity = int(quantity)

                if quantity <= 0:
                    print("Quantity must be greater than 0")
                    continue

                break
            except:
                print("Invalid input. Enter numbers only")
        
        total = quantity * price

        

        if not self.reduce_inventory(item_name,quantity):
            print("Order failed due to insufficient stock!")
            return False

        order["items"].append({
            "item_id": item_id,
            "item_name": item_name,
            "quantity": quantity,
            "price": price,
            "total": total
        })
        
        order["total_bill"] = sum(i["total"] for i in order["items"])

        self.write_orders(orders)
        self.write_order_log(order_id, "Item Added", order["total_bill"])
        print(f"Item added to Order ID: {order_id}. Current Total: {order['total_bill']}")
        return True

    
    def view_order(self, order_id):
        orders = self.read_orders()
        for order in orders:
            if order["order_id"] == order_id:
                print("\n" + "=" * 70)
                print(f"ORDER DETAILS (ID: {order_id})".center(70))
                print("=" * 70)

                print(f"{'Item':25} {'Qty':5} {'Price':10} {'Total':10}")
                print("-" * 70)

                for item in order["items"]:
                    print(f"{item['item_name']:25} {item['quantity']:5} ₹{item['price']:8} ₹{item['total']:8}")

                print("-" * 70)
                print(f"{'TOTAL BILL':45} ₹{order['total_bill']}")
                print(f"Status: {order['status']}")
                print("=" * 70)
                return

        print("Order not found")

    
    def view_all_orders(self):
        orders = self.read_orders()

        if not orders:
            print("\nNo orders found")
            return

        for order in orders:
            self.view_order(order["order_id"])

    
    def update_order_status(self, order_id):
        orders = self.read_orders()
        validator=CommonValidation() 
        for order in orders:
            if order["order_id"] == order_id:
                print("1. Pending\n2. Completed\n3. Cancelled")
                
                while True:
                    choice = input("Enter choice: ")
                    choice = validator.validate_choice(choice, 1, 3)

                    if choice is not None:
                       break
                    
                if choice == 1:
                    order["status"] = "Pending"
                elif choice == 2:
                    order["status"] = "Completed"
                elif choice == 3:
                    order["status"] = "Cancelled"
                else:
                    print("Invalid choice")
                    return
                self.write_orders(orders)
                print("Status Updated Successfully")
                self.write_order_log(order_id, f"Status Updated to {order['status']}", order["total_bill"])
                return
        print("Order not found")

    
    def delete_order(self, order_id):
        orders = self.read_orders()
        new_orders = [o for o in orders if o["order_id"] != order_id]
        if len(new_orders) != len(orders):
            self.write_orders(new_orders)
            print(f"Order ID {order_id} deleted")
            self.write_order_log(order_id, "Order Deleted")
        else:
            print("Order not found")
    
    def delete_item_from_order(self, order_id):
        orders = self.read_orders()
        order = next((o for o in orders if o["order_id"] == order_id), None)

        if not order:
            print("Order not found")
            return

        if not order["items"]:
            print("No items to delete in this order")
            return

        print("Items in this order:")
        print("-" * 60)
        for idx, item in enumerate(order["items"], start=1):
            print(f"{idx}. {item['item_name']} (ID: {item['item_id']}) - Qty: {item['quantity']} - Total: {item['total']}")
        
        while True:
            try:
                choice =input("Enter the item number which you want to delete: ")
                choice=int(choice)
                if choice<=0:
                    print("Choice must be greater than 0")
                    continue
                if 1 <= choice <= len(order["items"]):
                    removed = order["items"].pop(choice - 1)
                    order["total_bill"] = sum(i["total"] for i in order["items"])
                    self.write_orders(orders)
                    self.write_order_log(order_id, f"Item Removed: {removed['item_name']}", order["total_bill"])
                    print(f"\nRemoved {removed['item_name']}")
                    print(f"New Total: ₹{order['total_bill']}")
                    break
                else:
                    print("Invalid choice")

            except:
                print("Invalid input! Enter numbers only.")

    def reduce_inventory(self, dish_name, quantity):
        inv = InventoryOperations()
        data = inv.read_inventory()

        ingredients = dish_ingredients.get(dish_name, [])

        for ing in ingredients:
            for item in data:
                if item["item_name"] == ing:
                    if item["quantity"] < quantity:
                        print(f"{ing} is out of stock!")
                        return False
        
        for ing in ingredients:
            for item in data:
                if item["item_name"] == ing:
                    item["quantity"] -= quantity

        inv.write_inventory(data)
        return True

        
    