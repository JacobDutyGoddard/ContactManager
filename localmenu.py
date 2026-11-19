import azaleacore as ac
import main as code

options = ["Add Contact", "Search Contact", "Edit Contact", "Delete Contact", "Display All Contacts"]

def menu():
    print_menu()
    option = ac.gatherNumberInput("(6 or higher exits)\n> ")
    guide_program(option)
    
def print_menu():
    index = 1
    option = 7
    for option in options:
        print(f"{index}: {option}")
        index += 1    

def guide_program(choice):
    if choice == 1:
        main.addContact()
    elif choice == 2:
        main.searchContact()
    elif choice == 3:
        main.editContact()
    elif choice == 4:
        main.deleteContact()
    elif choice == 5:
        main.displayAllContacts()