import random

print("\n=========================================")
print("              CIPHERVAULT")
print(" Create Smart. Verify Strong. Stay Secure.")
print("=========================================\n")
print("Welcome to CIPHERVAULT!\n")

while True:
    print("1. Generate a Password")
    print("2. Validate a Password")
    print("3. Check Password Strength")
    print("4. Exit \n")

    x = int(input("Enter your choice: "))

    password = ''
    error = 0
    letters1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    if x == 1:
        number_of_letters1 = int(input("How many lowercase letters would you like in your password? "))
        number_of_letters2 = int(input("How many uppercase letters would you like in your password? "))
        number_of_symbols = int(input("How many symbols would you like in your password? "))
        input_number = int(input("How many numbers would you like in your password? "))

        if number_of_letters1 == 0:
            print("Invalid input! Password must contain at least one lowercase letter.\n")
            error = 1
        if number_of_letters2 == 0:
            print("Invalid input! Password must contain at least one uppercase letter.\n")
            error = 1
        if number_of_symbols == 0:
            print("Invalid input! Password must contain at least one symbol.\n")
            error = 1
        if input_number == 0:
            print("Invalid input! Password must contain at least one number.\n")
            error = 1

        if error == 0:
            for number1 in range(0, input_number):
                password = password + random.choice(numbers)
            for letter1 in range(0, number_of_letters1):
                password = password + random.choice(letters1)
            for letter1 in range(0, number_of_letters2):
                password = password + random.choice(letters2)
            for symbol1 in range(0, number_of_symbols):
                password = password + random.choice(symbols)

            final_password = list(password)
            random.shuffle(final_password)
            final_password = "".join(final_password)

            if len(final_password) < 10:
                print("Password must be at least 10 characters!\n")

            else:
                print("Your password is: ", final_password)

    if x == 2:
        password = input("Enter your password: ")

        if not len(password) >= 8:
            error = 1
            print("Password must be at least 8 characters!\n")
        if not any(char in letters1 for char in password):
            error = 1
            print("Password must contain at least one lower case letter!\n")
        if not any(char in letters2 for char in password):
            error = 1
            print("Password must contain at least one upper case letter!\n")
        if not any(char in numbers for char in password):
            error = 1
            print("Password must contain at least one number!\n")
        if not any(char in symbols for char in password):
            error = 1
            print("Password must contain at least one special character!\n")

        if error == 0:
            print("Password satisfies the necessary conditions!\n")
        else:
            print("Password does not satisfy the necessary conditions!\n")

    if x == 3:
        strong = 0
        moderate = 0
        easy = 0
        n = 0

        input1 = input("Enter your password: ")
        length = len(input1)

        while n < length - 2:
            if (input1[n] in letters1 and input1[n + 1] in letters1 and input1[n + 2] in letters1) or \
                    (input1[n] in numbers and input1[n + 1] in numbers and input1[n + 2] in numbers) or \
                    (input1[n] in symbols and input1[n + 1] in symbols and input1[n + 2] in symbols) or \
                    (input1[n] in letters2 and input1[n + 1] in letters2) and input1[n + 2] in letters2:
                easy = 1
            n += 1

        n = 0
        while n < length - 1:
            if (input1[n] in letters1 and input1[n + 1] in letters1) or \
                    (input1[n] in numbers and input1[n + 1] in numbers) or \
                    (input1[n] in symbols and input1[n + 1] in symbols) or \
                    (input1[n] in letters2 and input1[n + 1] in letters2):
                moderate = 1
            n += 1

        n = 0
        while n < length - 1:
            if ((input1[n] in letters1) != (input1[n + 1] in letters1)) or \
                    ((input1[n] in letters2) != (input1[n + 1] in letters2)) or \
                    ((input1[n] in numbers) != (input1[n + 1] in numbers)) or \
                    ((input1[n] in symbols) != (input1[n + 1] in symbols)):
                strong = 1
            n += 1

        if easy == 1:
            print("Your password is too easy!\n")
        elif moderate == 1:
            print("Your password is moderate!\n")
        elif strong == 1:
            print("Your password is strong!\n")

    if x == 4:
        print("Thank you for using CIPHERVAULT!")
        break