from order.order_operation import OrderOperations
from validation.common_validation import CommonValidation
from menu.view_menu import ViewMenu

class OrderDashboard:

    def __init__(self):
        self.order = OrderOperations()
        self.validator = CommonValidation()

    def menu(self):
        while True:
            print("\n" + "=" * 70)
            print("ORDER DASHBOARD ".center(70))
            print("=" * 70)

            print("\n" + "-" * 25 + " OPTIONS " + "-" * 25)
            print("1. Start a New Order")
            print("2. View All Orders")
            print("3. Update Existing Order (Add/Delete Items)")
            print("4. Update Order Status")
            print("5. Delete an Order")
            print("6. View Menu ")
            print("7. Back")

            choice = input("Enter your choice (1-7): ")
            choice = self.validator.validate_choice(choice, 1, 7)

            if choice is None:
                continue

            if choice == 1:
                print("\n--- Starting a New Order ---")
                order_id = self.order.start_order()
                print(f"Your Order ID is: {order_id}")
                
                added_any = False

                while True:
                    print("\nAdd Items to Order")
                    result = self.order.add_item_to_order(order_id)

                    if result:
                        added_any = True
                    else:
                        print("Item not added due to stock issue")

                    while True:
                        more = input("Would the customer like to add another item? (yes/no): ").lower()

                        if more == "yes":
                            break
                        elif more == "no":
                            if added_any:
                                print("\nOrder Completed \n")
                            else:
                                print("\nOrder Failed \n")
                            break
                        else:
                            print("Please enter 'yes' or 'no'")
                    if more=="no":
                        break

            elif choice == 2:
                print("\n--- Viewing All Orders ---")
                self.order.view_all_orders()

            elif choice == 3:
                while True:
                    print("\n--- Updating an Existing Order ---")
                    order_id = input("Enter the Order ID you want to update: ")
                    order_id = self.validator.validate_order_id(order_id)

                    if order_id is not None:
                       order_id = int(order_id)
                       break
                while True:
                    print("\n" + "-" * 20 + " UPDATE OPTIONS " + "-" * 20)
                    print("1. Add Item")
                    print("2. Remove Item")
                    print("3. Back")
                    print("-" * 70)
                    opt = input("Choose an option (1-3): ")
                    opt = self.validator.validate_choice(opt, 1, 3)

                    if opt is None:
                        continue
                    if opt == 1:
                        self.order.add_item_to_order(order_id)
                    elif opt == 2:
                        self.order.delete_item_from_order(order_id)
                    elif opt == 3:
                        break
                    else:
                        print("Invalid choice, please try again.")

            elif choice == 4:
                while True:
                    print("\n--- Updating Order Status ---")
                
                    order_id = input("Enter the Order ID to update status: ")
                    order_id = self.validator.validate_order_id(order_id)

                    if order_id is not None:
                        order_id=int(order_id)
                        break
                self.order.update_order_status(order_id)   
                    

            elif choice == 5:
                while True:
                    print("\n--- Deleting an Order ---")
                    order_id = input("Enter the Order ID you want to delete: ")
                    order_id = self.validator.validate_order_id(order_id)

                    if order_id is not None:
                        order_id=int(order_id)
                        break
                while True:
                    confirm = input("Are you sure? (yes/no): ").lower()
                    if confirm == "yes":
                        self.order.delete_order(order_id)
                        break
                    elif confirm == "no":
                       print("Deletion cancelled")
                       break

                    else:
                        print("Invalid input! Please enter 'yes' or 'no'")

            elif choice==6:
                view = ViewMenu()
                view.view_menu()

            elif choice == 7:
                print("Exiting Order Dashboard.")
                break

            else:
                print("Invalid choice, please enter a number from 1 to 6.")