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
    date = input ("Enter the date of the expense:  ")

    new_expense = {
                    "id_expense" : id_expense,
                    "description" : description,
                    "amount" : amount,
                    "category" : category,
                    "date" : date

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
            f"{expense["id_expense"]}. "        
            f"{expense["description"]}  |"
            f"{expense["category"]}  |"
            f"{expense["amount"]:.2f}"
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
    

while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. search")
    print("4. Deletion")
    print("5. calculate total")
    print("6. Exit")
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
        print("Goodbye")
        break
    else:
        print(" Please enter the valid number")

