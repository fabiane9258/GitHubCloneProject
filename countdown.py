while True:
    try:
        start = int(input("Enter the number to start countdown from:"))
        if start < 0:
            print("Countdown cannot start from a negative number. Please enter a valid number.\n")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

while start >= 0:
    print(start)
    start -= 1
print("Blast Off!")
# This code implements a countdown from a user-defined starting number down to zero.
# It prompts the user for a starting number, checks if it's valid, and then counts down.
# If the input is invalid, it asks for a valid number again.
# The countdown continues until it reaches zero, at which point it prints "Blast Off!".