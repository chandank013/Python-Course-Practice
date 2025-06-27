# Importing the regular expression module for pattern matching
import re

# Function to check the strength of a password
def check_password_strength(password):
    strength = 0  # Initialize strength counter
    # Define criteria for a strong password
    criteria = {
        "length": len(password) >= 8,  # Check if password length is at least 8
        "uppercase": bool(re.search(r'[A-Z]', password)),  # Check for uppercase letters
        "lowercase": bool(re.search(r'[a-z]', password)),  # Check for lowercase letters
        "digit": bool(re.search(r'\d', password)),  # Check for digits
        "special_char": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))  # Check for special characters
    }

    # Calculate strength based on criteria
    for key, met in criteria.items():  # Iterate through each criterion
        if met:  # If the criterion is met
            strength += 1  #234 Increment the strength counter

    # Display strength level based on the number of criteria met
    if strength == 5:
        return "Strong"  # All criteria met
    elif 3 <= strength < 5:
        return "Moderate"  # 3 or 4 criteria met
    else:
        return "Weak"  # Less than 3 criteria met

# Input password from user
password = input("Enter your password: ")  # Prompt user for password
strength = check_password_strength(password)  # Check the strength of the password
print(f"Password strength: {strength}")  # Display the password strength