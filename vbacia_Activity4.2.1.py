#  Arithmetic Expressions (Basic Calculator)
# Get the numbers from the user

store_A = float(input("Enter the first number: "))
store_B = float(input("Enter the second number: "))
mistaken_item = float(input("Enter the Mistaken Item: "))
# Add the numbers
total_cost = store_A + store_B
total_cost = total_cost - mistaken_item
sales_tax = (total_cost * (8/100) / 1)
final_amount = total_cost + sales_tax
# Display the result
print(f"The total amount is: {total_cost:.2f}")
print(f"The sales tax is: {sales_tax:.2f}")
# Final amount

print(f"The final amount is: {final_amount:.2f} ")






