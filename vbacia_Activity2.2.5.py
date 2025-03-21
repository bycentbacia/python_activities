


employee_name = input("Enter the employee's name: ")
monthly_salary = float(input("Enter the employee's monthly salary: "))


tax_deduction = monthly_salary * 0.10
final_salary = monthly_salary - tax_deduction


print(f"{employee_name}'s final salary after tax is: Php {final_salary:.2f}")