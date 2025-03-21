


#This program converts the speed in to m/s
speed_meters_per_second = float(input("Enter the speed in meters per second: "))


# Convert the speed from km/h to m/s
kilometers_per_hour = speed_meters_per_second * 3.6
miles_per_hour = speed_meters_per_second * 2.23694
feet_per_second = speed_meters_per_second * 3.28084
knots = speed_meters_per_second * 1.94384
mach_number = speed_meters_per_second / 343

print(f"The speed in kilometers per hour is: {kilometers_per_hour:.2f}")
print(f"The speed in miles per hour is: {miles_per_hour:.2f}")
print(f"The speed in feet per second is: {feet_per_second:.2f}")
print(f"The speed in knots is: {knots:.2f}")
print(f"The speed in mach number is: {mach_number:.2f}")




