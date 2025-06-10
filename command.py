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
    


rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()