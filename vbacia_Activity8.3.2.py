import time

def count_odd_num(start, end):
    odd_count = 0
    
    for number in range(start, end + 1):
        if number % 2 == 0:
            continue
        
        odd_count += 1
        
    return odd_count

start = int(input("Enter a starting number: "))
end = int(input("Enter a an ending number: "))

result = count_odd_num(start, end)
time.sleep(.45)
print(f"Count the number in range: {result}")


