import json
import uuid
from validation.auth_validation import Name_validation
from validation.common_validation import CommonValidation

class StaffOperations:
    
    def read_staff(self):
        try:
            with open("App/database/staff.json", "r") as file:
                return json.load(file)
        except:
            return []

    def write_staff(self, data):
        with open("App/database/staff.json", "w") as file:
            json.dump(data, file, indent=4)

    def generate_staff_id(self):
        return "ST" + str(uuid.uuid4().int)[:5]

    
    def add_staff(self):
        data = self.read_staff()
        validator1=Name_validation()
        while True:
            name = input("Enter Staff Name: ")
            if  validator1.validation_name(name):
                break
            else:
                print("Please Enter a Valid Name.")
    
        while True:
            role = input("Enter Role (Chef/Waiter/Manager): ").strip().lower()

            if role in ["chef", "waiter", "manager"]:
                role = role.capitalize()   
                break
            else:
                print("Invalid role! Please enter Chef, Waiter or Manager")

        while True:
            validator=CommonValidation()
            salary = input("Enter Salary: ")
            salary = validator.validate_salary(salary)

            if salary is not None:
                break

        staff_id = self.generate_staff_id()

        staff = {
            "staff_id": staff_id,
            "name": name,
            "role": role,
            "salary": salary,
        }

        data.append(staff)
        self.write_staff(data)

        print("\nStaff Added Successfully")
        print(f"ID   : {staff_id}")
        print(f"Name : {name}")
        print(f"Role : {role}")
        print(f"Salary : {salary}")

    
    def view_staff(self):
        data = self.read_staff()

        if not data:
            print("\n No staff found")
            return

        print("\n" + "=" * 60)
        print("STAFF LIST".center(60))
        print("=" * 60)

        for s in data:
            print(f"ID: {s['staff_id']} | Name: {s['name']} | Role: {s['role']}")

        print("=" * 60)

    def update_staff(self):
        data = self.read_staff()
        validator=CommonValidation()
        validator1=Name_validation()
        
        while True:
            staff_id = input("Enter Staff ID to update: ")
            staff_id = validator.validate_staff_id(staff_id)

            if staff_id is not None:
               break

        found=False
        for s in data:
            if s["staff_id"] == staff_id:
                found=True
                print("\nWhat do you want to update?")
                print("1. Update Name")
                print("2. Update Role")
                print("3. Update Salary")
                print("4. Update All")
                
                while True:
                    choice = input("Enter choice: ")
                    choice = validator.validate_choice(choice, 1, 4)

                    if choice is not None:
                       break

                if choice == 1:
                    while True:
                        name = input("Enter new name: ")
                        if validator1.validation_name(name):
                            s["name"] = name
                            break

                elif choice == 2:
                    while True:
                        role = input("Enter new role: ").strip().lower()

                        if role in ["chef", "waiter", "manager"]:
                            s["role"]= role.capitalize()   
                            break
                        else:
                            print("Invalid role! Please enter Chef, Waiter or Manager")
                
                elif choice == 3:
                        while True:
                            salary = input("Enter new Salary: ")
                            salary = validator.validate_salary(salary)

                            if salary is not None:
                                s["salary"]=salary
                                break
                elif choice == 4:
                        
                        while True:
                            name = input("Enter new name: ")
                            if validator1.validation_name(name):
                               break

    
                        while True:
                            role = input("Enter new role: ").strip().lower()
                            if role in ["chef", "waiter", "manager"]:
                                role = role.capitalize()   
                                break
                            else:
                                print("Invalid role! Please enter Chef, Waiter or Manager")

    
                        while True:
                            salary = input("Enter new Salary: ")

                            salary = validator.validate_salary(salary)

                            if salary is not None:
                                break

                        s["name"] = name
                        s["role"] = role
                        s["salary"] = salary
                else:
                    print("Invalid choice")
                    return

                self.write_staff(data)

                print("\nStaff Updated Successfully")
                print(f"ID    : {s['staff_id']}")
                print(f"Name  : {s['name']}")
                print(f"Role  : {s['role']}")
                print(f"Salary: {s['salary']}")
                return
        if not found:
            print("Staff not found")

    
    def delete_staff(self):
        data = self.read_staff()
        validator = CommonValidation()

    
        while True:
            staff_id = input("Enter Staff ID to delete: ")
            staff_id = validator.validate_staff_id(staff_id)

            if staff_id is not None:
                break

        found = False

        for s in data:
            if s["staff_id"] == staff_id:
                found = True

                print("\nStaff Found:")
                print(f"ID   : {s['staff_id']}")
                print(f"Name : {s['name']}")
                print(f"Role : {s['role']}")

            
            while True:
                confirm = input("Are you sure you want to delete? (yes/no): ").lower()

                if confirm == "yes":
                    data.remove(s)
                    self.write_staff(data)
                    print("Staff Deleted Successfully")
                    return

                elif confirm == "no":
                    print("Deletion Cancelled")
                    return

                else:
                    print("Please enter 'yes' or 'no'")

        if not found:
            print("Staff not found")