
def number():
    
    num1 = float(input("Enter a first number: "))
    num2 = float(input("Enter a second number: "))

    #perform arithmetic operations
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    
    if num2 != 0:
        print(f"Division: {num1} / {num2} = {num1 / num2}")
        print(f"Modulus: {num1} % {num2} = {num1 % num2}")
        print(f"Exponent: {num1} ** {num2} = {num1 ** num2}")
        print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
    else:
        print("Division: Cannot divide by zero")
        print("Modulus: Cannot divide by zero")
        print("Exponent: Cannot divide by zero")
        print("Floor Division: Cannot divide by zero")


number()