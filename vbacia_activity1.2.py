name = "Vincent Villasis Bacia" # string
Birth_year = 2004  #integer
Current_year = 2025  #integer
age = Current_year - Birth_year  
Average_Daily_Water_Intake = 3.7 #float
Drink_Coffee_Daily = True 

user_info = {
    "Name": name,
    "Birth Year": Birth_year,
    "Current Year": Current_year,
    "Age": f"{age} years old",
    "Average Daily Water Intake": f"{Average_Daily_Water_Intake} liters",
    "Drink Coffee": Drink_Coffee_Daily
}

print("\n")
print("User Information:")
print("----------------------")
for key, value in user_info.items():
    print(f"{key}: {value}")


