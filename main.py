import json
from pathlib import Path
from expense_manager import test_module, view_expenses, add_expense

print("==========================")
print(" personal expense tracker")
print("==========================")

test_module()


dirctory_path = Path("/mnt/d/practice/personal-expense-tracker/save_expense")

file_path = dirctory_path/"expenses.json"

dirctory_path.mkdir(parents=True, exist_ok=True)

def load_expense(file_path : Path)-> dict:
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(f"expenses file was not found in {file_path}")

    except json.JSONDecodeError as error:
        raise ValueError(
            f"file contain invalid json: {error}"
        )    


expenses = load_expense(file_path)



def search_expense():
    cat = input("Please enter your desired category: ")
    Found = False
    for expense in expenses:
        if expense["category"] == cat:
            print(f"{expense["description"]}  |",
            f"{expense["category"]} |",
            f"{expense["amount"]:.2f}")
            Found = True

    if Found == False:
        print(f"No expense found for the category: {cat} ")   

def delet_expense():

    choice = None
    while choice == None:
        try:
            choice = int(input("Please enter the expense id to remove: "))
        except ValueError:
            print("Invalid value")    

    Found = False

    for expense in expenses:
        if expense["id_expense"] == choice:
            expenses.remove(expense)
            print("Expense deleted successfuly")
            Found = True
            save_expense()

    if Found == False:
        print("Expense not found")

def calculate_total():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f" The total expense amount is:  {total:.3f}")

    if expenses == []:
        print("There is no expense to be added") 
    

def category_total():

    if expenses == []:
        print("No expense found")


    categories = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    categories_1 = list(categories.items()) 
    n = 0

    while n < len(categories):
        largest = max(categories_1, key=lambda x:x[1])
        print(largest)
        categories_1.remove(largest)
        n += 1

def save_expense():
    
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

    print(" your expenses have been saved successfully")    



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
        add_expense(expenses)
        save_expense()
        print("----------------------")

    elif choice == 2:
        view_expenses(expenses)
        print("----------------------")

    elif choice == 3:
        search_expense()
        print("------------------------")    

    elif choice == 4:
        delet_expense()
        print("------------------------")    

    elif choice == 5:
        calculate_total()
        print("-------------------------")

        
    elif choice == 6:
        category_total()
        print("-------------------------")


    elif choice == 7:
            print("Goodbye")
            break
    
    else:
        print(" Please enter the valid number")

