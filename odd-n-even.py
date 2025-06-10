while True:
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Please enter a positive number. ")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.\n ")



if number % 2 == 0:
    print(f"{number} is an even number. ")
else:
    print(f"{number} is an odd number.")