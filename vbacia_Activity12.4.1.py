from termcolor import colored

def calculate_total_cost(store_A=0.0, store_B=0.0, mistaken_item=0.0):
    try:
        if store_A == 0.0:
            store_A = float(input(colored("Enter the total cost of store A: ", "yellow")))
        if store_B == 0.0:
            store_B = float(input(colored("Enter the total cost of store B: ", "yellow")))
        if mistaken_item == 0.0:
            mistaken_item = float(input(colored("Enter the cost of the mistaken item: ", "yellow")))

        total_cost = store_A + store_B - mistaken_item
        sales_tax = total_cost * 0.08
        final_amount = total_cost + sales_tax

        print(colored(f"\nTotal Amount (before tax): ₱{total_cost:.2f}", "cyan"))
        print(colored(f"Sales Tax (8%): ₱{sales_tax:.2f}", "cyan"))
        print(colored(f"Final Amount (with tax): ₱{final_amount:.2f}\n", "cyan"))
    except ValueError:
        print(colored("\nInvalid input! Please enter numeric values.\n", "red"))

def voting_eligibility(name=" ", age=0):
    try:
        if age == 0:
            age = int(input(colored("Enter your age: ", "yellow")))
        if age >= 18:
            print(colored(f"{name}, you are eligible to vote!\n", "green"))
        else:
            print(colored(f"{name}, you are not eligible to vote!\n", "red"))
    except ValueError:
        print(colored("\nInvalid input! Please enter an integer.\n", "red"))

def positive_or_even(treasure=0):
    try:
        if treasure == 0:
            treasure = int(input(colored("Enter a number: ", "yellow")))
        if treasure > 0 and treasure % 2 == 0:
            print(colored("The treasure is unlocked!", "green"))
        elif treasure < 0:
            print(colored("The treasure is hidden underground!", "blue"))
        else:
            print(colored("The treasure is locked away forever!", "red"))
        print()
    except ValueError:
        print(colored("\nInvalid input! Please enter an integer.\n", "red"))

def combine_names(first_name="", last_name=""):
    if not first_name:
        first_name = input(colored("Enter your first name: ", "yellow"))
    if not last_name:
        last_name = input(colored("Enter your last name: ", "yellow"))
    full_name = f"{first_name} {last_name}"
    print(colored(f"Your full name is: {full_name}\n", "cyan"))

def menu():
    try: 
        while True:
            print(colored("""
    ========= ALL IN ONE FUNCTION =========
    1. Basic Calculator
    2. Check Voting Eligibility
    3. Check Number (Positive and Even)
    4. Combine First and Last Name
    5. Exit
    =======================================
    """, "magenta", attrs=["bold"]))
            choice = input(colored("Enter your choice (1-5): ", "yellow"))

            if choice == '1':
                calculate_total_cost()
            elif choice == '2':
                name = input(colored("Enter your name: ", "yellow"))
                age = int(input(colored("Enter your age: ", "yellow")))
                voting_eligibility(name, age)
            elif choice == '3':
                treasure = int(input(colored("Enter a number: ", "yellow")))
                positive_or_even(treasure)
            elif choice == '4':
                first_name = input(colored("Enter your first name: ", "yellow"))
                last_name = input(colored("Enter your last name: ", "yellow"))
                combine_names(first_name, last_name)
            elif choice == '5':
                print(colored("\nGoodbye!\n", "green", attrs=["bold"]))
                break
            else:
                print(colored("\nInvalid choice! Please enter a number between 1 and 5.\n", "red"))
    except ValueError:
        print("Invalid Input")
menu()
