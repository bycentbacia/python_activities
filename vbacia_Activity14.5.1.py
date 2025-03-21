def input_scores():
    math = float(input("Enter Math Score: "))
    science = float(input("Enter Science Score: "))
    english = float(input("Enter English Score: "))
    return math, science, english

def calculate_average(math, science, english):
    return (math + science + english) / 3

def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def display_results(math, science, english, average, grade):
    print("\n======== Student Grade Report =========")
    print(f"Math Score    : {math:.2f}")
    print(f"Science Score : {science:.2f}")
    print(f"English Score : {english:.2f}")
    print(f"Average Score : {average:.2f}")
    print(f"Letter Grade  : {grade}")
    print("=======================================")

def main():
    math, science, english = input_scores()
    average = calculate_average(math, science, english)
    grade = determine_grade(average)
    display_results(math, science, english, average, grade)

main()
