


#Relational Expressions (Checking Age for Voting Eligibility)
# Get the age of the user
age = int(input("Enter your age: "))
# Check if the user is eligible to vote
if (age >= 18) :
    print("You are old enough to vote!")
else:   
    print("You are not old enough to vote!")
    
def check_voting_eligibility(age):
    age = int(input("Enter your age: "))
    if age >= 18:
        return "You are old enough to vote!"
    else:
        return "You are not old enough to vote!"
message = check_voting_eligibility(age)
print(message)
    
    


    
    