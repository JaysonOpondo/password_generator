# Importing necessary modules for handling characters and generating random values

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input
password_length = int(input("Enter the desired password length: "))
# Generate Password
generated_password = generate_password(password_length)
# Display the Password
print("Generated Password:", generated_password)
