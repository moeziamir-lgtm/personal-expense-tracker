from datetime import date
import json
from pathlib import Path


def test_module():
    print("I am testing the module")

def view_expenses(expenses):

    
    print("Current Expense")
    print("-----------------")
    
    if expenses == []:
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


def generate_id(expenses):
    if not expenses:
        return 1
    return max(expense["id_expense"] for expense in expenses) + 1




def add_expense(expenses):
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

   
def search_expense(expenses):
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

def delet_expense(expenses):

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

def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f" The total expense amount is:  {total:.3f}")

    if expenses == []:
        print("There is no expense to be added") 


def category_total(expenses):

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

def save_expense(expenses, file_path):
    
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

    print(" your expenses have been saved successfully")    

