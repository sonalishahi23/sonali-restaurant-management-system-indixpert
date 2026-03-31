from datetime import datetime, timedelta
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
            print("Item ID cannot be empty")
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
    
    def validate_staff_id(self, staff_id):
        if not staff_id.strip():
            print("Staff ID cannot be empty")
            return None

        staff_id = staff_id.strip().upper()

        if not staff_id.startswith("ST") or not staff_id[2:].isdigit():
            print("Invalid Staff ID format (Example: ST30818)")
            return None
  
        return staff_id
    
    def validate_salary(self, salary):
        if not salary.strip():
            print("Salary cannot be empty")
            return None

        try:
            salary = float(salary)

            if salary <= 0:
                print("Salary must be greater than 0")
                return None

            return salary

        except:
            print("Invalid salary! Enter numbers only.")
            return None
        
    def validate_date(self, date_str):
        try:
            valid_date = datetime.strptime(date_str, "%d-%m-%Y").date()
            today = datetime.today().date()
            max_booking = today + timedelta(days=7)
            
            if valid_date < today or valid_date > max_booking:
                print(f"Invalid date! You can book only within 7 days from today.")
                return None
            
            return valid_date  
        except ValueError:
            print("Invalid date format! Please enter in dd-mm-yyyy format.")
            return None
        
    def validate_seats(self, seats_str, tables):
        """Validate required seats."""
        if not seats_str.isdigit():
           print("Seats must be a numeric value.")
           return None

        seats = int(seats_str)
        if seats < 1:
            print("You must book at least 1 seat.")
            return None

    
        if not any(table["seats"] >= seats for table in tables):
            print("No table available for this many seats.")
            return None

        return seats
    
    def validate_booking_id(self, booking_id):
        """Validate booking ID: numeric and 8 digits."""
        booking_id = str(booking_id)  # ensure it's string for isdigit()
        
        if not booking_id.isdigit():
            print("Booking ID must be numeric.")
            return None

        if len(booking_id) != 8:
            print("Booking ID must be 8 digits.")
            return None

        return int(booking_id)