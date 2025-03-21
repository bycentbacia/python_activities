def greet_user(name):
    print(f"\nHello, {name}! Welcome!")

def add_numbers(num1, num2):
    return num1 + num2

def check_number(number):
    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print(f"The number is zero.")

def main_menu():
    while True:
        print("\n++++++++++++Main Menu++++++++++++"),
        print("1. Greet the User ")
        print("2. Add Two Numbers ")
        print("3. Check if a Number is Positive or Negative")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("\nEnter your name: ")
            greet_user(name)
        elif choice == "2":
            try:
                num1 = float(input("\nEnter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = add_numbers(num1, num2)
                print(f"The sum of {num1} and {num2} is {result}")
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        elif choice == "3":
            try:
                number = float(input("\nEnter a number to check: "))
                check_number(number)
            except ValueError:
                print("Invalid input! Please enter a numerical value.")
        elif choice == "4":
            print("Goodbye po see you next Activity!")
            break
        else:
            print("Invalid choice! Please choose a valid option (1-4).")

main_menu()
