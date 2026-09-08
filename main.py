print(" personal expense tracker")

expense = {
    "Description" : "Food",
    "Amount" : 30.5,
    "Currency" : "USD",
    "Date" : "15-09-2026"
}

print(expense["Amount"])
print(expense["Currency"])

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

expenses[0]
expenses[1]

print ( expenses[0], expenses[1])

expenses.append({
    "description" : "lunch",
    "amount" : 23.43,
    "category" : "Food",
    "date" : "2026-09-10"
})

print(expenses[0])
print(expenses[2])

for expense in expenses:
    print(expense)

for expense in expenses:
    print(expense["description"])


for expense in expenses:
    print(expense["description"], expense["amount"])


for expense in expenses:
    print(
        f"{expense["description"]} | "
        f"{expense["category"]} | "
        f"{expense["amount"]:.2f} | "

    )    