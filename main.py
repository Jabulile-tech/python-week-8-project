from transactions import Transaction
from budget import Budget
from goals import Goal
from data_manager import save_data, load_data

transactions = []
budgets = {}
goals = []

def add_transaction():
    amount = float(input("Amount: "))
    category = input("Category: ")
    t_type = input("Type (income/expense): ")
    date = input("Date (YYYY-MM-DD): ")
    note = input("Note (optional): ")

    t = Transaction(amount, category, t_type, date, note)
    transactions.append(t.to_dict())

    if t_type == "expense" and category in budgets:
        budgets[category].add_expense(amount)

def set_budget():
    category = input("Category: ")
    limit = float(input("Limit: "))
    budgets[category] = Budget(category, limit)

def set_goal():
    name = input("Goal name: ")
    target = float(input("Target amount: "))
    goals.append(Goal(name, target))

def show_summary():
    print("\nTransactions:")
    for t in transactions:
        print(t)

    print("\nBudgets:")
    for category, b in budgets.items():
        print(f"{category}: Spent {b.spent}, Remaining {b.remaining()}")

    print("\nGoals:")
    for g in goals:
        print(f"{g.name}: Saved {g.saved_amount}/{g.target_amount}")

def save_all():
    save_data("transactions.json", transactions)
    save_data("budgets.json", {k: v.__dict__ for k, v in budgets.items()})
    save_data("goals.json", [g.__dict__ for g in goals])

def main():
    while True:
        print("\n1. Add Transaction\n2. Set Budget\n3. Set Goal\n4. Summary\n5. Save & Exit")
        choice = input("Choose: ")

        if choice == '1': add_transaction()
        elif choice == '2': set_budget()
        elif choice == '3': set_goal()
        elif choice == '4': show_summary()
        elif choice == '5': 
            save_all()
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
from visualizer import plot_spending_by_category, plot_expense_over_time, plot_goal_progress

def show_charts():
    plot_spending_by_category(transactions)
    plot_expense_over_time(transactions)
    plot_goal_progress(goals)

# In the main menu:
def main():
    while True:
        print("\n1. Add Transaction\n2. Set Budget\n3. Set Goal\n4. Summary\n5. Charts\n6. Save & Exit")
        choice = input("Choose: ")

        if choice == '1': add_transaction()
        elif choice == '2': set_budget()
        elif choice == '3': set_goal()
        elif choice == '4': show_summary()
        elif choice == '5': show_charts()
        elif choice == '6': 
            save_all()
            break
        else:
            print("Invalid input.")

from utils import input_float, input_date

def add_transaction():
    amount = input_float("Amount: ")
    category = input("Category: ")
    t_type = input("Type (income/expense): ").lower()
    date = input_date("Date (YYYY-MM-DD): ")
    note = input("Note (optional): ")
    
    t = Transaction(amount, category, t_type, date, note)
    transactions.append(t.to_dict())

    if t_type == "expense" and category in budgets:
        budgets[category].add_expense(amount)
