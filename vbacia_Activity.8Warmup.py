import time

user = int(input("Enter a number: "))

time.sleep(.1)
print("Number counter using for loop: ")

for num in range(1, user + 1):
    print (num)
    time.sleep(.1)

time.sleep(.1) 
print("\nNumber counter using While loop: ")

num = 1
while num < user + 1:
    print(num, end = ' ')
    num += 1
    time.sleep(.1)