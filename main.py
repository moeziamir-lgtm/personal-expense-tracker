from datetime import date
import json
from pathlib import Path

print("==========================")
print(" personal expense tracker")
print("==========================")

expenses = [ 
    {
        "id_expense" : 1,
        "description" : "Coffee",
        "amount" : 10,
        "category" : "Food",
        "date" : "2026-09-07"
    },
    {
        "id_expense" : 2,
        "description" : "Bus",
        "amount" : 7.5,
        "category" : "Transport",
        "date" : "2026-09-08"
    },
    {
            "id_expense" : 3,
            "description" : "Travel",
            "amount" : 23.43,
            "category" : "Entertainment",
            "date" : "2026-08-17"
        },
    {
            "id_expense" : 4,
            "description" : "stationary",
            "amount" : 18.10,
            "category" : "kids",
            "date" : "2026-07-27"
        },
    {
            "id_expense" : 5,
            "description" : "medicine",
            "amount" : 18.10,
            "category" : "Medical",
            "date" : "2026-07-27"
        }
]
 
expenses.append({
    "id_expense" : 6,
    "description" : "lunch",
    "amount" : 23.43,
    "category" : "Food",
    "date" : "2026-09-10"
})

def generate_id(expenses):
    if not expenses:
        return 1
    return max(expense["id_expense"] for expense in expenses) + 1


def add_expense():
    id_expense = generate_id(expenses)
    description = input (" Enter the description of the expense: ")
    amount = None
    while amount == None:
        try:
            amount = float(input (" Enter the amount of the expense:  "))
        except ValueError:
            print("Invalid number")

    category = input(" Enter the category of the expense:  ")
    date1 = date.today().isoformat()
    
    new_expense = {
                    "id_expense" : id_expense,
                    "description" : description,
                    "amount" : amount,
                    "category" : category,
                    "date" : date1

                    }
    expenses.append(new_expense)


def view_expense():
    print("Current Expense")
    print("-----------------")
    if not expenses:
        print("there is no expenses")
    else:
        for expense in expenses:
            print(
            f"{expense["id_expense"]:<3}"        
            f"{expense["description"]:<14} |"
            f"{expense["category"]:<15} |"
            f"{expense["amount"]:<10.2f} |"
            f"{expense["date"]:<15}"
            )       


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
    directory_path = Path("/mnt/d/practice/personal-expense-tracker/save_expense")
    file_path = directory_path /"expense.json"

    directory_path.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

    print(" you expenses have been saved successfully")    

    

while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. search")
    print("4. Deletion")
    print("5. calculate total")
    print("6. calculate total by category")
    print("7. Save Expenses")
    print("8. Exit")
    choice = None
    while choice == None:
        try:
            choice = float(input("choose your option:  "))
        except ValueError:
            print("invalid number")    

    if choice == 1:
        add_expense()
        print("----------------------")

    elif choice == 2:
        view_expense()
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
            save_expense()
            print("-------------------------")    

    elif choice == 8:
            print("Goodbye")
            break
    
    else:
        print(" Please enter the valid number")

