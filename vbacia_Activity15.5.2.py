from termcolor import colored
import time
books = {
    "Beirut Hellfire Society": True,
    "Call Me By Your Name": True,
    "Jonathan Strange & Mr. Norrell": True,
    "Alita: Battle Angel": True,
    "The Hobbit": True,
    
}

def view_books():
    print(colored("\nAvailable Books:", "green"))
    if any(books.values()):
        for title, available in books.items():
            if available:
                print(f"- {title}")
        print()
    
def borrow_books(title):
    if title in books:
        if books[title]:
            books[title] = False
            print(f"\nYou have successfully borrowed '{title}'.\n")
        else:
            print(f"'{title}' is currently unavailable.\n")
    else:
        print(f"Book '{title}' not found.\n")
        
def return_books(title):
    if title in books:
        if not books[title]:
            books[title] = True
            print(f"\nYou have successfully returned '{title}'.\n")
        else:
            print(f"{title}' is not borrowed.\n")
    else:
        print(f"book '{title}' not found.\n")
        
def main():
    while True:
        print("Library System")
        print("1. ----> View Books")
        print("2. ----> Borrow Books")
        print("3. ----> Return Books")
        print("4. ----> Exit")
         
        try:
            choice = input("Enter choice (1-4): ")
            choice = int(choice)
            if choice == 1:
                view_books()
            elif choice == 2:
                title = input("Enter book title to borrow: ")
                borrow_books(title)
            elif choice == 3:
                title = input("Enter book title to return: ")
                return_books(title)
            elif choice == 4:
                print("Exiting...Please Wait")
                time.sleep(2)
                break
            else:
                print("Invalid choice. Enter 1, 2, 3, or 4 only.\n")
        except ValueError:
            print("Invalid choice Enter 1-4 only.\n")          
main()
        
            
        
    