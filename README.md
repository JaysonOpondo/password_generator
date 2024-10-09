# password_generator
![Screenshot (29)](https://github.com/user-attachments/assets/6afb0579-3e23-4b9a-a0d2-94ea3e94aa54)
This simple Python script generates random passwords based on user input. The script generates passwords with letters, numbers, and symbols.

## Features
- Generates secure passwords of any length.
- Supports a variety of characters (letters, numbers, and symbols).

## How the Code Works:
1. Modules Used:
string: Provides groups of characters like letters, digits, and punctuation.
random: Helps pick random characters to make the password.

2. Function:
The code has a function named generate_password that creates a password.
The password length is set to 12 characters by default, but you can choose a different length if you want.

3. Character Pool:
The code combines:
Letters (A-Z, a-z)
Numbers (0-9)
Symbols (like @, #, $).
These characters are used to generate the password.

4. Password Creation:
The line password = ''.join(random.choice(characters) for i in range(length)):
random.choice(characters): Picks a random character from the pool.
for i in range(length): Does this as many times as the length of the password.
''.join(...): Combines all the chosen characters into a single password.

5. How It Works:
The code asks you how long you want your password to be.
It then uses the generate_password function to create a random password of that length and shows it to you.
