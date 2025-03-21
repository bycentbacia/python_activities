import time
from colorama import Fore, init
init(autoreset=True)

fruits = []

for i in range(3):
    fruit = input(f"Enter Unique favorite {i+1}: ")
    fruits.append(fruit)

print(Fore.MAGENTA +"\nList of Fruits: ", fruits)
time.sleep(1)
remove_fruit = input("\nEnter a fruit to remove: " )
if remove_fruit in fruits:
    fruits.remove(remove_fruit)
    print(Fore.BLUE +"Updated fruit list: ", fruits)
    time.sleep(2)
    
else:
    print("Not found in a list!")
    time.sleep(2)
    
fruits_tuple = tuple(fruits)
print("\nFruits as a tuple: ",fruits_tuple)
time.sleep(2)
try:
    index = int(input(Fore.YELLOW +"\nEnter an index (0 to {}): ".format(len(fruits_tuple)-1))) #Return the number of items in a container
    print(Fore.GREEN +"Selected fruit: ",fruits_tuple[index])
except (IndexError, ValueError): 
    print(Fore.RED +"Invalid Index!")
    time.sleep(2)
