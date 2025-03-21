import time

def convert_km_to_miles(km):
    return km * 0.621371


def main():
    while True:
        try:
            km = float(input("Enter distance in kilometers: "))
            
            miles = convert_km_to_miles(km)
            print(f"{km:.2f} kilometers is equal to {miles:.4f} miles.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        again = input("Do you want to convert another distance? (yes/no): ").lower()
        if again != "yes":
            print("Exiting...Please Wait")
            time.sleep(2)
            print("Thank you for using the program!")
            break
     
main()