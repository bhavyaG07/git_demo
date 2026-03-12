import random
import string

def generate_password():
    length = int(input("Enter password length: "))

    if length < 12:
        print("Password length should be at least 12")
        return
    
    print("Include lowercase letters? (y/n): ")
    use_lower = input().lower() == 'y'

    print("Include uppercase letters? (y/n): ")
    use_upper = input().lower() == 'y'

    print("Include numbers? (y/n): ")
    use_numbers = input().lower() == 'y'

    print("Include special characters? (y/n): ")
    use_symbols = input().lower() == 'y'

    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation


    password = ""
    for _ in range(length):
        password += random.choice(characters)

    print("Generated password:", password)


generate_password()