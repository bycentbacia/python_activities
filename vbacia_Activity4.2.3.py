

#

treasure = int(input("Enter a number: "))
# Check if the number is positive if even, negative if odd
if (treasure > 0) and (treasure % 2 == 0):
    print("The treasure is unlocked!")

elif treasure < 0:
    print("The treasure is hidden underground!")
    
else:
    print("The treasure is locked away forever!")
    