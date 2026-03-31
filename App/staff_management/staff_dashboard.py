from menu.view_menu import ViewMenu
from order.order_operation import OrderOperations
from billing_payment.generate_bill import BillGenerator   
from Booking_Table.table_dashboard import TableDashboard
from validation.common_validation import CommonValidation

class StaffDashboard:

    def show_menu(self):

        order = OrderOperations()
        menu = ViewMenu()

        while True:
            print("\n" + "=" * 65)
            print("****** Staff Dashboard ******".center(65))
            print("=" * 65)
            print("1. View Menu")
            print("2. Take Order")
            print("3. View Orders")
            print("4. Update Order Status")
            print("5. Generate Bill")
            print("6. Table Booking")  
            print("7. Logout")
            print("-" * 65)

            choice = input("Enter your choice: ")

            
            if choice == "1":
                print("\nShowing Menu...\n")
                menu.view_menu()

            
            elif choice == "2":
                order_id = order.start_order()
                print("New Order Started. Order ID:", order_id)

                while True:
                    print("\nAdd Item to Order")
                    order.add_item_to_order(order_id)
                    while True:

                        more = input("Would the customer like to add another item? (yes/no): ").lower()

                        if more == "yes":
                            break
                        elif more == "no":
                            print("\nOrder Completed\n")
                            break
                        else:
                            print("Please enter 'yes' or 'no'")
                    if more=="no":
                        break

            
            elif choice == "3":
                print("\nAll Orders:\n")
                order.view_all_orders()

            
            elif choice == "4":
                validator=CommonValidation()
                while True:
                    print("\n--- Updating Order Status ---")
                    order_id = input("Enter Order ID: ")
                    order_id = validator.validate_order_id(order_id)

                    if order_id is not None:
                        order_id=int(order_id)
                        break
                order.update_order_status(order_id)

            
            elif choice == "5":
                print("\nGenerating Bill...\n")
                BillGenerator().generate_bill()

            elif choice == "6":
                print("\nOpening Table Booking...\n")
                TableDashboard().show_menu()


            elif choice == "7":
                print("Logout")
                break

            else:
                print("Invalid choice")