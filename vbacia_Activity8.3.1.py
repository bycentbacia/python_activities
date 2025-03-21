
def sum_positive_number():
    total = 0
    
    while True:
        num = int(input("Enter Positive negative number to stop: "))
        
        if num < 0:
            break
        
        total += num
        
    print(f"The sum of all numbers entered is: {total}")
    
sum_positive_number()
        
