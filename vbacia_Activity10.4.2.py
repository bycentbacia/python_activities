

words = set(input("Enter a Sentence: ").split())

print("\nUnique words: ", words)

while True:
    print("\nMenu")
    print("1. Add a words")
    print("2. Remove a word")
    print("3. Display Unique word")
    print("4. Exit")
    choice = input("Pick an option: ")
    
    if choice == '1':
        word = input("Enter a word to add: ").strip()
        words.add(word)
        print(f"Added '{word}' to the set.")
        
    elif choice == '2':
        word = input("Enter a word to remove: ").strip()
        if word in words:
            words.remove(word)
            print(f"Removed '{word}' to the set.")
        else: 
            print("Word not found in a sentence")   
    elif choice == '3':
        print("\nUnique Words: ", words)
    elif choice == '4':
        print("Exit")
        break
    else:
        print("Invalid Choice!")
          
    
        
    
            
        
    