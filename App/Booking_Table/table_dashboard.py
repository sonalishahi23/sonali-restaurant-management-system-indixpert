from Booking_Table.table_operation import TableOperations
from validation.common_validation import CommonValidation

class TableDashboard:

    def show_menu(self):

        table = TableOperations()
        validator = CommonValidation()


        while True:
            print("\n" + "=" * 65)
            print("====== TABLE BOOKING ======".center(65))
            print("=" * 65)
           
            print("1. Book Table")
            print("2. View Bookings")
            print("3. Cancel Booking")
            print("4. Check Availability")
            print("5. Back")
            print("=" * 65)

            choice = input("Enter choice (1-5): ")
            choice = validator.validate_choice(choice, 1, 5)

            if choice is None:
                continue

            
            if choice == 1:
                print("\n" + "-" * 65)
                print("BOOK TABLE".center(65))
                print("-" * 65)
                table.book_table()

            
            elif choice == 2:
                print("\n" + "-" * 65)
                print("ALL BOOKINGS".center(65))
                print("-" * 65)
                table.view_bookings()

            
            elif choice == 3:
                print("\n" + "-" * 65)
                print("CANCEL BOOKING".center(65))
                print("-" * 65)
                table.cancel_booking()

            
            elif choice == 4:
                print("\n" + "-" * 65)
                print("CHECK TABLE AVAILABILITY".center(65))
                print("-" * 65)
                table.check_availability()

            
            elif choice == 5:
                print("\n" + "=" * 65)
                print("Returning to BACK".center(65))
                print("=" * 65)
                break

            else:
                print("Invalid choice")