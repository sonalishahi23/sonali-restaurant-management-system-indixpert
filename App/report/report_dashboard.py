from .report_operation import ReportOperations
from validation.common_validation import CommonValidation

class ReportDashboard:

    def show_menu(self):

        report = ReportOperations()
        validator = CommonValidation()


        while True:
            print("\n" + "=" * 65)
            print("====== REPORT DASHBOARD ======".center(65))
            print("=" * 65)
            
            print("1. Total Orders")
            print("2. Total Revenue")
            print("3. Pending Orders")
            print("4. Completed Orders")
            print("5. Total Staff")
            print("6. Back")
            print("-" * 65)

            choice = input("Enter choice (1-6): ")
            choice = validator.validate_choice(choice, 1, 6)

            if choice is None:
                continue

            if choice == 1:
                print("\n" + "-" * 25 + " TOTAL ORDERS " + "-" * 25)
                report.total_orders()

            elif choice == 2:
                print("\n" + "-" * 25 + " TOTAL REVENUE " + "-" * 25)
                report.total_revenue()

            elif choice == 3:
                print("\n" + "-" * 25 + " PENDING ORDERS " + "-" * 25)
                report.pending_orders()

            elif choice == 4:
                print("\n" + "-" * 25 + " COMPLETED ORDERS " + "-" * 25)
                report.completed_orders()

            elif choice == 5:
                print("\n" + "-" * 25 + " TOTAL STAFF " + "-" * 25)
                report.total_staff()

            elif choice == 6:
                print("\nReturning to Admin Dashboard...\n")
                break

            else:
                print("Invalid choice")