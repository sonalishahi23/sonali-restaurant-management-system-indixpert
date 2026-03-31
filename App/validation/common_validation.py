class CommonValidation:

    def validate_choice(self, choice, min_val, max_val):
        
        if not choice.isdigit():
            print("Invalid input! Please enter numbers only.")
            return None

        choice = int(choice)

        
        if choice < min_val or choice > max_val:
            print(f"Invalid choice! Please select between {min_val}-{max_val}.")
            return None

        return choice
    
    def validate_id(self, value, name="ID"):
        if not value.isdigit():
            print(f"Invalid {name}! Numbers only.")
            return None
        return int(value)
    
    def validate_item_name(self, name):
        if not name.strip():
            print("Item name cannot be empty")
            return None

        for ch in name:
            if not (ch.isalpha() or ch.isspace()):
                print("Item name should contain only alphabets")
                return None

        return name.strip()
    
    def validate_item_id(self, item_id):
        if not item_id.strip():
            print("❌ Item ID cannot be empty")
            return None

        item_id = item_id.strip().upper()

        if not item_id[:2].isalpha() or not item_id[2:].isdigit():
            print("Invalid Item ID format (Example: BF101 , LN201)")
            return None

        return item_id
    
    def validate_order_id(self, order_id):
    
        if not order_id.isdigit():
            print("Order ID must be numeric")
            return None

        if len(order_id) != 10:
            print("Order ID must be 10 digits")
            return None

        return int(order_id)