#Activity 3: User Login System (While Loop with Limited Attempts

correct_user = "Kamaisan"
correct_password = "Vincent123"

attempts = 3

while attempts > 0:
    
    username = input("Enter a user name: ")
    password = input("Enter a password: ")
    
    if username == correct_user and password == correct_password:
        print("Login Successfully!")
        break
    
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect username or password")

        else:
            print("  3 times fail , You are locked out. ")
            
        
    
    
