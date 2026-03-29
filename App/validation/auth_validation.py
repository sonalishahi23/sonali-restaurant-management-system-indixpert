class Name_validation:
    def validation_name(self,name):
        name = name.strip()

        if name == "":
            print("Name cannot be empty")
            return False

        fullname = name.replace(" ", "")

        if not fullname.isalpha():
            print("Name must contain alphabets only")
            return False
        
        if len(fullname) < 4:
            print("Name must be at least use 4 character")
            return False

        return True

class EmailValidation:

    def validate_email(self, email):

        email = email.strip()

        if not email.endswith("@gmail.com"):
            print("Email must end with @gmail.com")
            return False

        username = email.replace("@gmail.com", "")

        if username == "":
            print("Email must contain characters before @gmail.com")
            return False

        if not username.isalnum():
            print("Email must contain only alphabets and numbers")
            return False

        
        if not any(ch.isalpha() for ch in username):
            print("Email must contain at least one alphabet")
            return False

        return True
    
class PasswordValidation:

    def validate_password(self, password):

        if len(password) < 6:
            print("Password must be at least 6 characters long")
            return False

        has_alpha = False
        has_digit = False
        has_at = False

        for ch in password:
            if ch.isalpha():
                has_alpha = True
            elif ch.isdigit():
                has_digit = True
            elif ch == "@":
                has_at = True

        if not has_alpha:
            print("Password must contain at least one alphabet")
            return False

        if not has_digit:
            print("Password must contain at least one number")
            return False

        if not has_at:
            print("Password must contain @ symbol")
            return False

        return True