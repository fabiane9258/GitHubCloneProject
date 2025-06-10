while True:
    try:
        Age = int(input("What is your age? "))
        if Age < 0:
            print("Age can not be negative. Enter a valid number.\n")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for age.\n")



if Age < 18:
    print("You are a minor.")
elif Age > 18 and Age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen, go claim your retirement benefits.")
    