expenses = []
def add_expense ():
    while True:
        try:
           amount = int(input("Enter amount: "))
           break
        except ValueError:
           print("Please enter a valid number.")
    cate = input("Enter category: ")
    desc = input("Enter description: ")
    expense = {
        "amount" : amount,
        "category" : cate,
        "description" : desc
    }
    return expense

def view_expense(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    
    for i, exp in enumerate (expenses,start = 1):
       print(i, ".", exp["amount"], " - ", exp["category"], " - ", exp["description"])

def total_spend(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    print ("Total: ", total)

while True:
    print("\n----Expense Tracker----")
    print ("1. Add expense")
    print ("2. view expense")
    print ("3. show total")
    print ("4. Exit")
    while True:
        try:
            Menu = int(input("Choose from the options: "))
            break  # valid input → exit loop
        except ValueError:
            print("Invalid input. Please enter a number.")

    if Menu == 1:
       expenses.append(add_expense())
    elif Menu == 2:
        view_expense(expenses)
    elif Menu == 3:
        total_spend(expenses)
    elif Menu == 4:
        print("Goodbye")
        break
    else:
        print ("Invalid number please try again: ")

    