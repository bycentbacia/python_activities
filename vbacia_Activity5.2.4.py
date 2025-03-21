#grocery bill calculator
#variables
Apple_Price = 10
Banana_Price = 5
Mango_Price = 15

#quantity
Apple_Quantity = int(input("Enter the quantity of Apples: "))
Banana_Quantity = int(input("Enter the quantity of Bananas: "))
Mango_Quantity = int(input("Enter the quantity of Mangoes: "))

#calculate total bill
#Add total each fruit price
Apple_Price = 10 * Apple_Quantity
Banana_Price = 5 * Banana_Quantity
Mango_Price = 15 * Mango_Quantity

#Add total bill
Total_Bill = Apple_Price + Banana_Price + Mango_Price


#print(f'Apple Price: {Apple_Price} PHP')
#print(f'Banana Price: {Banana_Price} PHP')
#print(f'Mango Price: {Mango_Price} PHP')
print("___________________________________")
print("Grocery Bill")
print("list of items and prices")
print("__________________________________")
print(f"Apple Price: {Apple_Price} PHP")
print(f"Banana Price: {Banana_Price} PHP")
print(f"Mango Price: {Mango_Price} PHP")
print("__________________________________")
print(f"Total Bill: {Total_Bill} PHP")