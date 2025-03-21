def employee_management_system():
    employees = {}
    
    departments = ('HR', 'IT', 'Finance', 'Marketing', 'Operations')
    
    while True:
        print("""\nPlease choose an option: 
        1. Add an Employee
        2. View Employees
        3. Remove an Employee
        4. Exit""")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            name = input("\nEnter employee name: ").capitalize()
            
            if name in employees:
                print("\nError: Employee already exists!")
                continue
            
            print("\nAvailable departments:", departments)
            department = input("Enter employee department: ")
            
            if department not in departments:
                print("\nError: Invalid department!")
                continue
            
            try:
                salary = float(input("\nEnter employee salary: "))
                if salary <= 0:
                    print("\nError: Salary must be greater than 0!")
                    continue
            except ValueError:
                print("\nError: Invalid salary amount!")
                continue
            
            employees[name] = (department, salary)
            print("\nEmployee", name, "added successfully!")
            
        elif choice == '2':
            if not employees:
                print("\nNo employees found in the system.")
            else:
                print("\nEmployee Details:")
                print("-" * 21)
                for name in employees:
                    dept, salary = employees[name]
                    print("Name:", name)
                    print("Department:", dept)
                    print(f"Salary: {salary:.2f}")
                    print("-" * 21)
                
        elif choice == '3':
            print("\nCurrent Employees:")
            for name in employees:
                print(f"- {name}")
            name = input("\nEnter employee name to remove: ")
            if name in employees:
                del employees[name]
                print("\nEmployee", name, "removed successfully!")
            else:
                print("\nError: Employee not found!")
                
        elif choice == '4':
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid choice! Please enter 1, 2, 3, or 4")

employee_management_system()
