def check_number(number):
    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print(f"The number is zero.")

num = float(input("\nEnter a number to check: "))
check_number(num)