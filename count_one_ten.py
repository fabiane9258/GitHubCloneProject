for number in range(1, 11):
    print(number)
print("Counting complete!")
# This code counts from 1 to 10 and prints each number.
# It uses a for loop to iterate through the range of numbers from 1 to 10.


for number in range(10, 0, -1):
    print(number)
print("Counting down complete!")
# This code counts down from 10 to 1 and prints each number.
# It uses a for loop with a negative step to iterate through the range of numbers from 10 to 1.


for number in range(1, 11, 2):
    print(number)
print("Counting by twos complete!, they are all odd numbers.")
# This code counts from 1 to 10 in steps of 2 and prints each number.

for number in range(2, 11, 2):
    print(number)
print("Counting by twos complete!, they are all even numbers.")
# This code counts from 2 to 10 in steps of 2 and prints each number.

for number in range(1, 11):
    print(f"Number: {number}, Square: {number**2}, Cube: {number**3}")
# This code counts from 1 to 10 and prints each number along with its square and cube.
print("Counting with squares and cubes complete!")


for i in range (5):
    for j in range(5):
        print("+", end = "")
    print()
# This code prints a 5x5 grid of plus signs.


for i in range(5):
    for j in range(i + 1):
        print("+", end="")
    print()
# This code prints a right-angled triangle pattern of plus signs.


for i in range(5, 0, -1):
    for j in range(i):
        print("+", end="")
    print()
# This code prints an inverted right-angled triangle pattern of plus signs.



rows = 5
for i in range(rows):
    spaces = ' ' * (rows - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
# This code prints a pyramid pattern of stars.
def draw_square(size, char="*", fill=True):
    for i in range(size):
        for j in range(size):
            if fill or i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(char, end=" ")
            else:
                print(" ", end=" ")
        print()


def draw_right_triangle(size, char="*"):
    for i in range(1, size + 1):
        print(char * i)


def draw_inverted_triangle(size, char="*"):
    for i in range(size, 0, -1):
        print(char * i)


def draw_pyramid(size, char="*"):
    for i in range(size):
        spaces = ' ' * (size - i - 1)
        stars = char * (2 * i + 1)
        print(spaces + stars)


def draw_diamond(size, char="*"):
    for i in range(size):
        print(" " * (size - i - 1) + char * (2 * i + 1))
    for i in range(size - 2, -1, -1):
        print(" " * (size - i - 1) + char * (2 * i + 1))


def main():
    while True:
        print("\nText-Based Shape Drawing App")
        print("1. Solid Square")
        print("2. Hollow Square")
        print("3. Right-Angled Triangle")
        print("4. Inverted Triangle")
        print("5. Centered Pyramid")
        print("6. Diamond")
        print("7. Exit")

        choice = input("Choose a shape (1–7): ")

        if choice == "7":
            print("Goodbye!")
            break

        try:
            size = int(input("Enter size (e.g., 5): "))
            if size < 1:
                print("Size must be positive.")
                continue
        except ValueError:
            print("Invalid size input. Please enter an integer.")
            continue

        char = input("Enter character to use (default '*'): ").strip()
        if not char:
            char = "*"

        print("\nYour Shape:\n")

        if choice == "1":
            draw_square(size, char, fill=True)
        elif choice == "2":
            draw_square(size, char, fill=False)
        elif choice == "3":
            draw_right_triangle(size, char)
        elif choice == "4":
            draw_inverted_triangle(size, char)
        elif choice == "5":
            draw_pyramid(size, char)
        elif choice == "6":
            draw_diamond(size, char)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This code defines a text-based shape drawing application that allows users to draw various shapes using a specified character.
# It includes options for solid squares, hollow squares, right-angled triangles, inverted triangles, centered pyramids, and diamonds.
# The user can specify the size of the shape and the character to use for drawing.
# The application runs in a loop until the user chooses to exit.


