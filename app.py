from datetime import date
from models import Expense
from db import initialize_db, execute, fetch_all
from analytics import category_summary, monthly_total


def add_expense(expense: Expense) -> None:
    execute("""
        INSERT INTO expenses (expense_date, category, amount, description)
        VALUES (?, ?, ?, ?)
    """, (
        expense.expense_date.isoformat(),
        expense.category,
        expense.amount,
        expense.description
    ))


def list_expenses() -> None:
    rows = fetch_all("SELECT * FROM expenses ORDER BY expense_date DESC")
    print("\nID | Date | Category | Amount | Description")
    print("-" * 60)
    for r in rows:
        print(f"{r['id']} | {r['expense_date']} | {r['category']} | ₹{r['amount']} | {r['description']}")


def main() -> None:
    initialize_db()

    while True:
        print("""
1. Add Expense
2. View Expenses
3. Monthly Total
4. Category Analytics
5. Exit
""")

        choice = input("Choice: ").strip()

        if choice == "1":
            expense = Expense(
                expense_date=date.today(),
                category=input("Category: ").strip(),
                amount=float(input("Amount: ")),
                description=input("Description: ").strip()
            )
            add_expense(expense)
            print("✅ Expense recorded")

        elif choice == "2":
            list_expenses()

        elif choice == "3":
            month = input("Month (MM): ")
            print(f"📊 Total: ₹{monthly_total(month)}")

        elif choice == "4":
            print("\n📊 Category Summary")
            for cat, total in category_summary().items():
                print(f"{cat}: ₹{total}")

        elif choice == "5":
            print("👋 Goodbye")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
