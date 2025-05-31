command = input("Enter your command :  ").lower()

match command:
    case "start":
        print("Machine is Starting....")
    case "stop":
        print("Machine is stopping....")
    case "suspend":
        print("Suspending the machine....")
    case "":
        print("Invalid command..")



count = 1
while count <= 5:
    print(count)
    count += 1
    