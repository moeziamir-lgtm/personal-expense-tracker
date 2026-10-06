import json
from pathlib import Path
from expense_manager import (view_expenses, 
                             add_expense, 
                             search_expense,
                             delet_expense,
                             calculate_total,
                             category_total,
                             save_expense,
                             load_expense)


print("==========================")
print(" personal expense tracker")
print("==========================")


dirctory_path = Path("/mnt/d/practice/personal-expense-tracker/save_expense")

file_path = dirctory_path/"expenses.json"

dirctory_path.mkdir(parents=True, exist_ok=True)


expenses = load_expense(file_path)


while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. search")
    print("4. Deletion")
    print("5. calculate total")
    print("6. calculate total by category")
    print("7. Exit")
    choice = None
    while choice == None:
        try:
            choice = float(input("choose your option:  "))
        except ValueError:
            print("invalid number")    

    if choice == 1:
        add_expense(expenses,file_path)
        print("----------------------")

    elif choice == 2:
        view_expenses(expenses)
        print("----------------------")

    elif choice == 3:
        search_expense(expenses)
        print("------------------------")    

    elif choice == 4:
        delet_expense(expenses)
        save_expense(expenses, file_path)
        print("------------------------")    

    elif choice == 5:
        calculate_total(expenses)
        print("-------------------------")

        
    elif choice == 6:
        category_total(expenses)
        print("-------------------------")


    elif choice == 7:
            print("Goodbye")
            break
    
    else:
        print(" Please enter the valid number")

