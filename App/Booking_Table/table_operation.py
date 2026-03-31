import json
import uuid
from datetime import datetime, timedelta
from validation.auth_validation import Name_validation
from validation.common_validation import CommonValidation
import os

class TableOperations:
    TABLES = [
        {"table_id": "T1", "seats": 2},
        {"table_id": "T2", "seats": 3},
        {"table_id": "T3", "seats": 4},
        {"table_id": "T4", "seats": 5},
        {"table_id": "T5", "seats": 6},
        {"table_id": "T6", "seats": 7},
        {"table_id": "T7", "seats": 8},
        {"table_id": "T8", "seats": 9},
        {"table_id": "T9", "seats": 10},
        {"table_id": "T10", "seats": 6}
    ]

    SLOTS = [
        "10:00 AM - 12:00 PM",
        "12:00 PM - 2:00 PM",
        "2:00 PM - 4:00 PM",
        "6:00 PM - 8:00 PM",
        "8:00 PM - 10:00 PM"
    ]

    def __init__(self):
        os.makedirs("App/logs", exist_ok=True)

    def write_booking_log(self,booking_id, customer_name, table_no, status):
        """Append booking info to log file"""
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y %H:%M:%S")
        log_file = "App/logs/booking_logs.txt"

        with open(log_file, "a") as file:
            file.write(f"{date_time} | Booking ID: {booking_id} | "
                   f"Name: {customer_name} | Table: {table_no} | Status: {status}\n")

    def read_data(self):
        try:
            with open("App/database/table_booking.json", "r") as file:
                return json.load(file)
        except:
            return []

    def write_data(self, data):
        with open("App/database/table_booking.json", "w") as file:
            json.dump(data, file, indent=4)

    def generate_booking_id(self):
        data = self.read_data()

        while True:
            booking_id = str(uuid.uuid4().int)[:8]

            exists = False
            for b in data:
                if str(b["booking_id"]) == booking_id:
                    exists = True
                    break

            if not exists:
                return booking_id


    def is_valid_date(self, date_str):
        try:
            booking_date = datetime.strptime(date_str, "%d-%m-%Y")
        except:
            return False

        today = datetime.now()

        if booking_date < today:
            return False

        if booking_date > today + timedelta(days=7):
            return False

        return True
    
    def get_available_tables(self, date, slot):
        data = self.read_data()

        booked_tables = []

        for b in data:
            if b["date"] == date and b["slot"] == slot and b["status"] == "Booked":
                booked_tables.extend(b["tables"])

        available = []
        for t in self.TABLES:
            if t["table_id"] not in booked_tables:
                available.append(t)

        return available
    
    def find_tables_for_seats(self, available_tables, required_seats):

        best_table = None

        for t in available_tables:
            if t["seats"] >= required_seats:
                if best_table is None or t["seats"] < best_table["seats"]:
                   best_table = t

        if best_table:
            return [best_table]

        return None
                
    def book_table(self):
        data = self.read_data()
        validator1=Name_validation()
        print("\n" + "=" * 65)
        print("TABLE BOOKING ".center(65))
        print("=" * 65)
        while True:
            name = input("Enter customer name: ")
            if  validator1.validation_name(name):
                break
            else:
                print("Please Enter a Valid Name.")

        while True:
            validator=CommonValidation()
            date_input = input("Enter the date you want to book a table (dd-mm-yyyy): ")
            booking_date = validator.validate_date(date_input)
            if booking_date:
                print("Date accepted:", booking_date.strftime("%d-%m-%Y"))
                break

        if not self.is_valid_date(date_input):
            print("Invalid date (max 7 days allowed)")
            return
        
        while True:
            print("\n" + "-" * 25 + " AVAILABLE SLOTS " + "-" * 25)
            for i, s in enumerate(self.SLOTS, start=1):
                print(i, s)
            print("-" * 65)

            slot_choice = input("Select slot: ")
            slot_choice = validator.validate_choice(slot_choice, 1, 6)

            if slot_choice is not None:
                break

        if slot_choice < 1 or slot_choice > len(self.SLOTS):
            print("Invalid slot")
            return

        slot = self.SLOTS[slot_choice - 1]

        available_tables = self.get_available_tables(date_input, slot)

        print("\n" + "-" * 25 + " AVAILABLE TABLES " + "-" * 25)
        for t in available_tables:
            print(t["table_id"], "- Seats:", t["seats"])

        while True:
            seats_input = input("Enter required seats: ")
            required_seats = validator.validate_seats(seats_input, available_tables)
            if required_seats:
                print(f"Seats accepted: {required_seats}")
                break

        selected_table = None

        for t in available_tables:
            if t["seats"] >= required_seats:
                if selected_table is None or t["seats"] < selected_table["seats"]:
                    selected_table = t

        if not selected_table:
            print("No table available for this requirement")
            return

        booking = {
        "booking_id": self.generate_booking_id(),
        "customer_name": name,
        "date": date_input,
        "slot": slot,
        "tables": [selected_table["table_id"]],
        "seats": required_seats,
        "status": "Booked"
        }

        data.append(booking)
        self.write_data(data)

        print("\n" + "=" * 65)
        print("BOOKING CONFIRMED".center(65))
        print("=" * 65)
        print(f"Booking ID : {booking['booking_id']}")
        print(f"Customer   : {name}")
        print(f"Date       : {date_input}")
        print(f"Slot       : {slot}")
        print(f"Table      : {selected_table['table_id']}")
        print("=" * 65)

        booking_id = booking["booking_id"]
        customer_name = booking["customer_name"]
        table_no = booking["tables"][0]
        status = booking["status"]


        self.write_booking_log(booking_id, customer_name, table_no, status)

    def view_bookings(self):
        data = self.read_data()

        if not data:
            print("No bookings found")
            return

        for b in data:
            print("\n" + "=" * 60)
            print(f"BOOKING ID: {b['booking_id']}".center(60))
            print("=" * 60)
            print(f"Name   : {b['customer_name']}")
            print(f"Date   : {b['date']}")
            print(f"Slot   : {b['slot']}")
            print(f"Tables : {', '.join(b['tables'])}")
            print(f"Seats  : {b['seats']}")
            print(f"Status : {b['status']}")
            print("=" * 60)

    def cancel_booking(self):
        data = self.read_data()
        validator=CommonValidation()
        while True:
            booking_id_input = input("Enter booking ID: ")
            booking_id = validator.validate_booking_id(booking_id_input)
            if booking_id:
                print(f"Booking ID accepted: {booking_id}")
                break
        for b in data:
            if str(b["booking_id"]) == str(booking_id):
                b["status"] = "Cancelled"
                self.write_data(data)
                print("Booking cancelled")

                booking_id = b["booking_id"]
                customer_name = b["customer_name"]
                table_no = b["tables"][0]  # assuming single table
                status = b["status"]

                self.write_booking_log(booking_id, customer_name, table_no, status)
            
                return

        print("Booking not found")

    def check_availability(self):
        while True:
            validator=CommonValidation()
            date_input = input("Enter the date you want to book a table (dd-mm-yyyy): ")
            booking_date = validator.validate_date(date_input)
            if booking_date:
                print("Date accepted:", booking_date.strftime("%d-%m-%Y"))
                break

        if not self.is_valid_date(date_input):
            print("Invalid date (max 7 days allowed)")
            return
        while True:
            print("\nSlots:")
            for i, s in enumerate(self.SLOTS, start=1):
                print(i, s)

            slot_choice = input("Select slot: ")
            slot_choice = validator.validate_choice(slot_choice, 1, 6)

            if slot_choice is not None:
                break

        slot = self.SLOTS[slot_choice - 1]

        available_tables = self.get_available_tables(date_input, slot)

        print("\n" + "-" * 25 + " AVAILABLE TABLES " + "-" * 25)
        for t in available_tables:
            print(t["table_id"], "- Seats:", t["seats"])
