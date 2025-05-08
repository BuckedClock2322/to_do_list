todo_list = []

def add_item():
    user_item = input("Please add your item > ")
    todo_list.append(user_item)
    menu()

def delete_item():
    amount = len(todo_list)
    print("There is ",amount,"entries in the list. Which one would you like to delete?")
    amount_input = int(input())
    todo_list.pop(amount_input+-1)
    print("The item has been deleted.")
    menu()

def write_to_file():
    f = open("To-Do_list.txt", "a")
    for n in todo_list:
        f.write(n)
        f.write(',')
        
    menu()

def read_list():
    amount = len(todo_list)
    print("There is ",amount,"entries in the list. Which one would you like to read?")
    amount_input = int(input())
    print(todo_list[amount_input+-1])
    menu()
    

def menu():
    print("This is a to-do list")
    print("These are your options: ")
    print("########################")
    print("1. Add Item ")
    print("2. Delete Item")
    print("3. Write Item to txt File")
    print("4. Read list")
    print("5. Exit")
    menu_choice = int(input("Enter your choice > "))
    if menu_choice == 1:
        add_item()
    elif menu_choice == 2:
        delete_item()
    elif menu_choice == 3:
        write_to_file()
    elif menu_choice == 4:
        read_list()
    elif menu_choice == 5:
        print("Goodbye.")
    else:
        print("You didn't choose a correct option.")
        menu()

menu()

