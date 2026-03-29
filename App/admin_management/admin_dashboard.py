from report.report_dashboard import ReportDashboard 
from menu.menu_dashboard import MenuDashboard
from order.order_dashboard import OrderDashboard
from staff_management.staff_manage import StaffManagement 
from Booking_Table.table_dashboard import TableDashboard
from billing_payment.generate_bill import BillGenerator
from validation.common_validation import CommonValidation


class Admin_dashboard:

    def show_dashboard(self):
        validator = CommonValidation()
        while True:
            print("\n" + "=" * 65)
            print("*******ADMIN DASHBAORD*******".center(65))
            print("=" * 65)
            
            print("1. Manage Menu")
            print("2. Manage Order")
            print("3. Manage Staff")
            print("4. View Reports")
            print("5. Manage Table Booking")
            print("6. Generate Bill")
            print("7. Logout")
            print("-" * 65)

            

            choice = input("Enter your choice (1-7): ")
            validated_choice = validator.validate_choice(choice, 1, 7)

            if validated_choice is None:
                continue

            if validated_choice == 1:
                print("\nOpening Menu Management...\n")
                MenuDashboard().menu_dashboard()

            elif validated_choice == 2:
                print("\nOpening Menu Management...\n")
                OrderDashboard().menu()

            elif validated_choice == 3:
                print("\nOpening Staff Management...\n")
                StaffManagement().show_menu()

            elif validated_choice == 4:
                print("\nOpening Reports...\n")
                ReportDashboard().show_menu()

            elif validated_choice == 5:
                print("\nOpening Table Booking System...\n")
                TableDashboard().show_menu()

            elif validated_choice == 6:
                order_id = input("Enter Order ID: ")
                order_id = validator.validate_id(order_id, "Order ID")

                if order_id is None:
                    continue
                print("\nGenerating Bill...\n")
                BillGenerator().generate_bill(order_id)
            elif validated_choice == 7:
                print("Logout")
                break
            else:
                print("Invalid choice")
            