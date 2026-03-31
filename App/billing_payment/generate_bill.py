from datetime import datetime
from order.order_operation import OrderOperations 
from validation.common_validation import CommonValidation 
import os

os.makedirs("App/logs", exist_ok=True)
class BillGenerator:

    def __init__(self):
        self.order_ops = OrderOperations()

    def write_log(self, order_id, subtotal, gst, total, status):
        """Append bill info to log file"""
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y %H:%M:%S")
        log_file = "App/logs/bill_logs.txt"

        with open(log_file, "a") as file:  
            file.write(f"{date_time} | Order ID: {order_id} | "
                       f"Subtotal: Rs{subtotal} | GST: Rs{gst:.2f} | "
                       f"Total: Rs{total:.2f} | Status: {status}\n")


    def generate_bill(self,order_id=None):
        
        validator=CommonValidation()
        while True:
            if order_id is None:
                order_id = input("Enter Order ID: ")

    
            order_id_str = str(order_id)
            order_id = validator.validate_order_id(order_id_str)
            if order_id is None:
                print("Invalid Order ID")
                order_id = None  
                continue  


            orders = self.order_ops.read_orders()

            order = None
            for o in orders:
                if o["order_id"] == order_id:
                    order = o
                    break

            if order is None:
                print("Order not found")
                order_id = None  
                continue

            break

        # Date & Time
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y %H:%M")

        subtotal = order["total_bill"]
        gst = subtotal * 0.05
        final_total = subtotal + gst

        print("\n" + "=" * 50)
        print("              ROYAL RESTAURANT  ")
        print("=" * 50)
        print(f"Order ID : {order_id}")
        print(f"Date     : {date_time}")
        print("-" * 50)

        
        for item in order["items"]:
            name = item["item_name"]
            qty = item["quantity"]
            total = item["total"]

            print(f"{name} x {qty}")
            print(f"{'':30}₹{total}")
            print("-" * 50)

        
        print(f"{'Subtotal':30} ₹{subtotal}")
        print(f"{'GST (5%)':30} ₹{gst:.2f}")
        print("=" * 50)
        print(f"{'TOTAL':30} ₹{final_total:.2f}")
        print("=" * 50)

        print(f"Status : {order['status']}")
        print("\nThank You! Visit Again ")
        print("=" * 50)

        self.write_log(order_id, subtotal, gst, final_total, order['status'])