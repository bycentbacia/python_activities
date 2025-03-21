


principal_amount = float(input("Enter the principal amount(dollars): $"))
annual_interest_rate = float(input("Enter the annual interest rate (percentage): "))
time_period = float(input("Enter the time period in years (months): "))

# Calculate the compound interest
convert_time_period = time_period / 12
# formula for compound interest
compound_interest = principal_amount * (1 + (annual_interest_rate / 100)) ** convert_time_period

print(f"The final amount is: ${compound_interest:.2f}")






