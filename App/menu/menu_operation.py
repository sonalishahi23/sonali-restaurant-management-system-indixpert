import json

class MenuOperations:

    def read_menu(self):
        try:
            with open("App/database/menu.json", "r") as file:
                data = json.load(file)

                if not data:
                    data = self.default_menu()
                    self.write_menu(data)

                return data

        except FileNotFoundError:
            data = self.default_menu()
            self.write_menu(data)
            return data

    def write_menu(self, data):
        with open("App/database/menu.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def default_menu(self):
        return [
    {"id":"BF101","name":"Aloo Paratha","price":100.0,"category":"Breakfast"},
    {"id":"BF102","name":"Poha","price":70.0,"category":"Breakfast"},
    {"id":"BF103","name":"Upma","price":80.0,"category":"Breakfast"},
    {"id":"BF104","name":"Idli Sambhar","price":90.0,"category":"Breakfast"},
    {"id":"BF105","name":"Masala Dosa","price":150.0,"category":"Breakfast"},

    {"id":"LN201","name":"Dal Tadka","price":150.0,"category":"Lunch"},
    {"id":"LN202","name":"Rajma Chawal","price":170.0,"category":"Lunch"},
    {"id":"LN203","name":"Chole Chawal","price":160.0,"category":"Lunch"},
    {"id":"LN204","name":"Kadhi Chawal","price":160.0,"category":"Lunch"},
    {"id":"LN205","name":"Jeera Rice","price":120.0,"category":"Lunch"},

    {"id":"DN301","name":"Paneer Butter Masala","price":230.0,"category":"Dinner"},
    {"id":"DN302","name":"Kadai Paneer","price":210.0,"category":"Dinner"},
    {"id":"DN303","name":"Dal Makhani","price":200.0,"category":"Dinner"},
    {"id":"DN304","name":"Butter Naan","price":50.0,"category":"Dinner"},
    {"id":"DN305","name":"Tandoori Roti","price":40.0,"category":"Dinner"},

    {"id":"SI401","name":"Plain Dosa","price":120.0,"category":"South Indian"},
    {"id":"SI402","name":"Rava Dosa","price":140.0,"category":"South Indian"},
    {"id":"SI403","name":"Medu Vada","price":100.0,"category":"South Indian"},
    {"id":"SI404","name":"Uttapam","price":130.0,"category":"South Indian"},
    {"id":"SI405","name":"Appam","price":120.0,"category":"South Indian"},

    {"id":"CH501","name":"Hakka Noodles","price":150.0,"category":"Chinese"},
    {"id":"CH502","name":"Fried Rice","price":140.0,"category":"Chinese"},
    {"id":"CH503","name":"Manchurian","price":160.0,"category":"Chinese"},
    {"id":"CH504","name":"Spring Roll","price":110.0,"category":"Chinese"},
    {"id":"CH505","name":"Schezwan Noodles","price":170.0,"category":"Chinese"},

    {"id":"IT601","name":"Margherita Pizza","price":200.0,"category":"Italian"},
    {"id":"IT602","name":"Farmhouse Pizza","price":250.0,"category":"Italian"},
    {"id":"IT603","name":"White Sauce Pasta","price":220.0,"category":"Italian"},
    {"id":"IT604","name":"Red Sauce Pasta","price":200.0,"category":"Italian"},
    {"id":"IT605","name":"Garlic Bread","price":120.0,"category":"Italian"},

    {"id":"SN701","name":"Veg Burger","price":120.0,"category":"Snacks"},
    {"id":"SN702","name":"French Fries","price":80.0,"category":"Snacks"},
    {"id":"SN703","name":"Cheese Balls","price":150.0,"category":"Snacks"},
    {"id":"SN704","name":"Paneer Tikka","price":180.0,"category":"Snacks"},
    {"id":"SN705","name":"Nachos","price":140.0,"category":"Snacks"},

    {"id":"BV801","name":"Cold Coffee","price":150.0,"category":"Beverages"},
    {"id":"BV802","name":"Hot Coffee","price":100.0,"category":"Beverages"},
    {"id":"BV803","name":"Masala Tea","price":50.0,"category":"Beverages"},
    {"id":"BV804","name":"Lassi","price":100.0,"category":"Beverages"},
    {"id":"BV805","name":"Mango Shake","price":150.0,"category":"Beverages"},

    {"id":"DS901","name":"Chocolate Cake","price":200.0,"category":"Desserts"},
    {"id":"DS902","name":"Brownie","price":120.0,"category":"Desserts"},
    {"id":"DS903","name":"Ice Cream","price":80.0,"category":"Desserts"},
    {"id":"DS904","name":"Gulab Jamun","price":100.0,"category":"Desserts"},
    {"id":"DS905","name":"Black Forest Cake","price":220.0,"category":"Desserts"},

    {"id":"SW1001","name":"Veg Sandwich","price":90.0,"category":"Sandwich"},
    {"id":"SW1002","name":"Grilled Sandwich","price":130.0,"category":"Sandwich"},
    {"id":"SW1003","name":"Cheese Sandwich","price":140.0,"category":"Sandwich"},
    {"id":"SW1004","name":"Paneer Sandwich","price":150.0,"category":"Sandwich"},
    {"id":"SW1005","name":"Club Sandwich","price":180.0,"category":"Sandwich"}
]

    def display_menu(self):
        menu = self.read_menu()

        print("\n" + "=" * 75)
        print("  ROYAL - MENU ".center(75))
        print("=" * 75)

        current_category = ""

        for item in menu:

            if item["category"] != current_category:
                current_category = item["category"]

                print("\n" + "-" * 75)
                print(f"{current_category.upper()}".center(75))
                print("-" * 75)
                print(f"{'ID':<10} {'Item Name':<40} {'Price (₹)':>10}")
                print("-" * 75)

        
            print(f"{item['id']:<10} {item['name']:<40} ₹{item['price']:>8}")

        print("\n" + "=" * 75)

    def get_item_by_id(self, item_id):
        data = self.read_menu()

        for item in data:
            if item["id"].lower() == item_id.lower():
                return item

        return None