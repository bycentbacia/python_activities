

task_we = []

for i in range (3):
    task = input(f"Enter task {i+1}: ")
    task_we.append(task)
    
print("\nCurrent Task: ", task)
update = int(input("Enter a task number (1-3): "))
if 0 <= update < len(task_we):
    task_we[update] = input("Enter new task update: ")
else: 
    print("Invalid Input")
    
print("\nUpdate Task: ", task_we)

remove_index = int(input("Enter a task number to remove (1-3): "))
if 0 <= remove_index <len(task_we):
    remove_index = task_we.pop(remove_index)
    print(f"Remove task: , {remove_index}")
else:
    print("Invalid Task Number")

print(f"Final to-do-list: ")
for i, task_we in enumerate(task_we, 1):
    print(f"{i}.  {task_we}")

    