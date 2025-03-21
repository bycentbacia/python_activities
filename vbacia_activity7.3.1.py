
print("=====================================================")
def calculate_membership(age, bmi, fitness_level):
    if age < 18:
        return "Not Eligible for Membership."
    discount = 0
    health_warning = ""
    membership_type = ""
    
    if bmi < 18.5:
        membership_type = "Basic Membership"
        discount += 10
    elif 18.5 <= bmi < 25:
        membership_type = "Standard Membership"
    else:
        membership_type= "Premuim Membership"
        health_warning = "Health risk Consider Maintaining healthy BMI"
    
    if age >= 45 and bmi >= 30:
            health_warning = "High health risk warning. Consult to your doctor"
    if fitness_level == "advance":
        discount += 5
        
    return membership_type, discount, health_warning

def main():
    try:
        age= int(input("Enter your age: "))
        bmi= float(input("Enter your BMI: "))
        fitness_level= input("Enter your Fitness level(Beginner, Intermediate, Advance): ").lower()
        
        result= calculate_membership(age, bmi, fitness_level)
        
        if isinstance(result, str):
            print(result)
            
        else:
            membership, discount, warning = result
            print(f"Member Type:  {membership}")
            print(f"Total Discount: {discount}%")
            if warning:
                print(warning)
    
    except ValueError:
        print("Invalid input. Please enter numeric number")

    return  
        
if __name__ == "__main__":
    main()
        
