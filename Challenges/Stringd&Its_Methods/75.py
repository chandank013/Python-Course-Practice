# Cheaking possword is matched or not

def confirm_password(password, confirm_password):
    if password == confirm_password:
        return True
    else:
        return False

# Example usage
password = input("Enter your password: ")
confirm_password_input = input("Confirm your password: ")

if confirm_password(password, confirm_password_input):
    print("Password confirmed.")
else:
    print("Passwords do not match.")