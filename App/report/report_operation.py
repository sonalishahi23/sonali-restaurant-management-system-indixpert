import json

class ReportOperations:

    def read_orders(self):
        try:
            with open("App/database/order.json", "r") as file:
                return json.load(file)
        except:
            return []

    def read_staff(self):
        try:
            with open("App/database/staff.json", "r") as file:
                return json.load(file)
        except:
            return []

    
    def total_orders(self):
        orders = self.read_orders()
        print("\n" + "=" * 60)
        print("📦 TOTAL ORDERS".center(60))
        print("=" * 60)
        print(f"Total Orders : {len(orders)}")
        print("=" * 60)

    
    def total_revenue(self):
        orders = self.read_orders()
        total = 0

        for o in orders:
            total += o["total_bill"]

        print("\n" + "=" * 60)
        print("TOTAL REVENUE".center(60))
        print("=" * 60)
        print(f"Total Revenue : ₹{total}")
        print("=" * 60)

    
    def pending_orders(self):
        orders = self.read_orders()
        count = 0

        for o in orders:
            if o["status"] == "Pending":
                count += 1

        print("\n" + "=" * 60)
        print("PENDING ORDERS".center(60))
        print("=" * 60)
        print(f"Pending Orders : {count}")
        print("=" * 60)

    
    def completed_orders(self):
        orders = self.read_orders()
        count = 0

        for o in orders:
            if o["status"] == "Completed":
                count += 1

        print("\n" + "=" * 60)
        print("COMPLETED ORDERS".center(60))
        print("=" * 60)
        print(f"Completed Orders : {count}")
        print("=" * 60)

    
    def total_staff(self):
        staff = self.read_staff()
        print("\n" + "=" * 60)
        print("TOTAL STAFF".center(60))
        print("=" * 60)
        print(f"Total Staff : {len(staff)}")
        print("=" * 60)