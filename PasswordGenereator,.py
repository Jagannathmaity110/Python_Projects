import random
import string

def generate_password(length, use_uppercase = True, use_digits = True, use_symbol = True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbol :
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))    


length = int(input("Enter the length of the password"))
print(f"Gnereate Password :{generate_password(length)}")