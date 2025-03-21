
#checking odd or even
def check_odd_even():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("Invalid input")


check_odd_even()