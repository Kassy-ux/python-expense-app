import json

# Load or initialize expenses
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    expense = {"name": name, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added: {name} - {amount}")

# View all expenses and total
def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    total = 0
    print("\nYour Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['amount']}")
        total += expense["amount"]
    print(f"Total spent: {total}\n")

# Main app loop
def main():
    expenses = load_expenses()
    while True:
        print("Expense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()