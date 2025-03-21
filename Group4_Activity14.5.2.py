from termcolor import colored
import time

employees = dict()

departments = ("tech support", "finance", "sales", "marketing")

def menu():
    print(f"""╠{'═' * 66}╣
║ {"[1] Add Employee".ljust(65)}║
║ {"[2] View Employees".ljust(65)}║
║ {"[3] Update Employee".ljust(65)}║
║ {"[4] Exit".ljust(65)}║""")
    print(f"""╩{'═' * 66}╩""")
    option = input("›› ")
    try:
        option = int(option)
        if not 1 <= option <= 4:
            raise Exception("Enter 1, 2, 3, or 4 only")
    except Exception as error:
        print('-' * 68)
        print(f"Invalid Input: {error}")
    else:
        if option == 1:
            add()
        elif option == 2:
            view()
        elif option == 3:
            update()
        elif option == 4:
            print("Exiting...Please Wait")
            time.sleep(1)
            print("Thankyou For Using The Program!")
            exit()

def add():
    print('═' * 68)
    print("Departments: ")
    [print(f"\t\t{x.title()}") for x in departments]
    print('═' * 68)
    name = input("Enter Employee Name:›› ").lower().strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter Employee Name:›› ").lower().strip()
    
    department = input("Enter department:›› ").lower().strip()
    while not department or department not in departments:
        print("Invalid department. Select a department above.")
        department = input("Enter department:›› ").lower().strip()
    
    hourly_rate = float(66)
    hours = input("Enter Hours Worked:›› ")
    while not hours or not hours.isdigit() or int(hours) < 1:
        print("Hours must be a positive number.")
        hours = input("Enter Hours Worked:›› ")
    hours = int(hours)
    salary = hourly_rate * hours
    print(colored(f"Your Total Salary is: {salary}","blue"))
    
    if name in employees:
        print("Employee already exists.")
    else:
        employees[name] = [department, hours, salary]

def view():
    if not employees:
        print('═' * 68)
        print(f"║{'No Employee Records Found.'.center(66)}║")
        return
    
    print('═' * 68)
    print(f"║{'Employee'.center(20)}|{'Department'.center(20)}|{'Hours Worked'.center(12)}|{'Salary'.center(11)}║")
    print('═' * 68)
    for key, value in employees.items():
        print(f"║{key.title().center(20)}|{value[0].title().center(20)}|{str(value[1]).center(12)}|{str(value[2]).center(11)}║")

def update():
    view()
    print('═' * 68)
    name = input("Enter Employee Name to Update:›› ").lower().strip()  # Ensure case insensitivity

    # Fix: Use `.keys()` to check exact match
    if name not in employees.keys():
        print(colored("Cannot Find Employee Data!","red"))
        return

    print("Select what you want to update:")
    print("1. Department\n2. Hours Worked")
    choice = input("> ")

    if choice == '1':
        new_department = input("Enter new department:›› ").lower().strip()
        while new_department not in departments:
            print("Invalid department. Select from the listed departments.")
            new_department = input("Enter new department: ").lower().strip()
        employees[name][0] = new_department

    elif choice == '2':
        new_hours = input("Enter new hours worked:›› ")
        while not new_hours.replace('.', '', 1).isdigit() or int(new_hours) < 1:
            print("Hours must be a positive number.")
            new_hours = input("Enter new hours worked:›› ")
        new_hours = int(new_hours)
        employees[name][1] = new_hours
        employees[name][2] = new_hours * float(66)

    else:
        print("Invalid choice.")

    print(colored("Employee data updated successfully!","green"))
    

app_name = colored("Employee Payroll System".center(66),"yellow")


print(f"""╦{'═' * 66}╦""")
print('║', end='')

for char in app_name:
    print(char, end="")
    # time.sleep(0.05)

print('║')
# time.sleep(0.5)

while True:
    menu()
