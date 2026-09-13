print(" personal expense tracker")

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

for expense in expenses:
    print(
        f"{expense["description"]} | "
        f"{expense["category"]} | "
        f"{expense["amount"]:.2f} | "

    )    

def add_expense():
    description = input (" Enter the description of the expense: ")
    amount = float(input (" Enter the amount of the expense:  "))
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

while True:
    answer = input("do you want to continue? (y/n)").lower()

    if answer == "n":
        print (" Goodbye")
        break

    elif answer == "y":
        add_expense()

    else:
        print("Please pay attention and type 'y' or 'n' ")    



view_expense()

        
