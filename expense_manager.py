
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

