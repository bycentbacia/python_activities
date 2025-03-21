
#Activity 1: Dictionary Challenge - Student Grades Tracker 🎓

def student_grades():
    grades = {}
    for i in range (3):
        name = input(f"Enter the name of student {i+1}: ").strip()
        grade = float(input(f"Enter the grade for {name}: "))
        grades[name]= grade  
        
    while True:
        print("\n___________Menu__________")
        print("1. Update student grade")
        print("2. Remove student grade")
        print("3. View all grade")
        print("4. Exit")
        choice = input("Pick option: ")
        
        if choice == '1':
            name = input("Enter a student name to update grade: ").strip()
            if name in grades:
                grade = float(input(f"Enter the new grade for{name}: "))
                grades[name] = grade
                print(f"Updated grade for {name}.")
            else:
                print("Not on  a list!")
                
        elif choice == '2':
            name = input("Enter a student name to remove grade: ").strip()
            if name in grades:
                del grades[name]
                print(f"Remove {name} on a list.")
            else:
                print("Not on  a list!")
                
        elif choice == '3':
            print("\nFinal Student Grade: ")
            for name, grade in grades.items():
                print(f"{name}: {grade}")
                
        elif choice == '4':
            print("Exit!")
            break
    
        else:
            print("Invalid Choice!")

student_grades()
                
        

