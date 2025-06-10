while True:
    try:
        age = int(input("What is your age? "))
        if age < 0:
            print("So what are you, an infant? Age cannot be negative. please enter a valid number.\n")
            continue
        elif age > 120:
            print("No way you are that old! Please enter a valid age.\n")
            continue
        break
    except ValueError:
        print("Please enter a valid number for age.\n")


if age < 13:
    print("You are a child. ")
elif age >= 13 and age < 17:
    print("You are a teenager. ")
elif 18 >= age < 64:
    print("You are an adult. ")
else:
    print("You are a senior citizen. ")