import matplotlib.pyplot as plt
from collections import defaultdict
import datetime

def plot_spending_by_category(transactions):
    category_totals = defaultdict(float)
    for t in transactions:
        if t['type'] == 'expense':
            category_totals[t['category']] += t['amount']

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color='tomato')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_expense_over_time(transactions):
    daily_expense = defaultdict(float)
    for t in transactions:
        if t['type'] == 'expense':
            date = t['date']
            daily_expense[date] += t['amount']

    dates = sorted(daily_expense.keys(), key=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))
    values = [daily_expense[date] for date in dates]

    plt.figure(figsize=(8, 5))
    plt.plot(dates, values, marker='o', color='purple')
    plt.title("Expenses Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_goal_progress(goals):
    names = [g.name for g in goals]
    progress = [g.saved_amount for g in goals]
    targets = [g.target_amount for g in goals]

    plt.figure(figsize=(8, 5))
    bar_width = 0.4
    x = range(len(names))

    plt.bar(x, targets, width=bar_width, label='Target', color='lightgray')
    plt.bar([i + bar_width for i in x], progress, width=bar_width, label='Saved', color='green')
    
    plt.xlabel("Goals")
    plt.ylabel("Amount")
    plt.title("Financial Goals Progress")
    plt.xticks([i + bar_width / 2 for i in x], names)
    plt.legend()
    plt.tight_layout()
    plt.show()
