#ToDo list tutorial from Coursera
#Made by Mac Reske
#9.1.22

#initializing variables
user_input = "random"
data = []

#Creating menu
def show_menu():
    print("Menu")
    print("1. Add an item")
    print("2. Mark as done")
    print("3. View items")
    print("4. Exit")

#Main
while user_input != "4":
    show_menu()
    user_input = input('Enter your choice: ')
    
    if user_input == '1':
        item = input("What needs to be done?")
        data.append(item)
        print("Added item",item)
    elif user_input == '2':
        item = input("What is to be marked as complete?")
        if item in data:
            data.remove(item)
            print("Removed task",item)
        else:
            print("Item is not on the list")
    elif user_input == '3':
        print("List of to-do items:")
        for item in data:
            print(item)
    elif user_input == '4':
        print("Goodbye!")
    else:
        print("Please enter one of 1, 2, 3, 4.")

