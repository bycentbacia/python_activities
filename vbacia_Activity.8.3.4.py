from colorama import Fore, init


init(autoreset=True)

while True: 
    try:
        number = int(input(Fore.YELLOW + "Enter a number between 1 and 10: "))
        
        if 1 <= number <= 10:
            break
        else:
            print(Fore.RED + "Error: Enter a number between 1 and 10")  
    except ValueError:
        print(Fore.RED + "Invalid Input")
        
print(Fore.GREEN + f"\nMultiplication table for {number}: ")

for i in range(1, 11):
    print(Fore.CYAN + f"{number} x {i} = {number * i}")
