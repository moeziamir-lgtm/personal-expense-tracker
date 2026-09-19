print("==========================")
print(" personal expense tracker")
print("==========================")

expenses = [
    {
        "description" : "Coffee",
        "amount" : 10,
        "category" : "Food",
        "date" : "2026-09-07"
    },
    {
        "description" : "Bus",
        "amount" : 7.5,
        "category" : "Transport",
        "date" : "2026-09-08"
    }
]

expenses.append({
    "description" : "lunch",
    "amount" : 23.43,
    "category" : "Food",
    "date" : "2026-09-10"
})

def add_expense():
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
            print(f"{expense["description"]}  |"
            f"{expense["category"]}  |"
            f"{expense["amount"]:.2f}"
            )


def search_expense():
    cat = input("Please enter your desired category: ")
    for expense in expenses:
        Found = False
        if expense["category"] == cat:
            print(f"{expense["description"]}  |",
            f"{expense["category"]} |",
            f"{expense["amount"]:.2f}")
            Found = True

    if Found == False:
        print(f"No expense found for the category: {cat} ")   

while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. search")
    print("4. Exit")
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
        print("Goodbye")
        break

    else:
        print(" Please enter the valid number")




