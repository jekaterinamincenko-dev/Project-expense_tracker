from datetime import date
from storage import load_expenses, save_expenses
from logic import sum_total

CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]


def show_menu():
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("7) Iziet")

    return input("\nIzvēlies darbību: ")


def add_expense(expenses):
    today = date.today().strftime("%Y-%m-%d")

    date_input = input(f"Datums (YYYY-MM-DD) [{today}]: ")
    if date_input == "":
        date_input = today

    print("\nKategorija:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    cat_choice = int(input("Izvēlies kategoriju: "))
    category = CATEGORIES[cat_choice - 1]

    try:
        amount = float(input("Summa (EUR): "))
    except ValueError:
        print("Nepareiza summa.")
        return

    description = input("Apraksts: ")

    expense = {
        "date": date_input,
        "amount": amount,
        "category": category,
        "description": description,
    }

    expenses.append(expense)
    save_expenses(expenses)

    print(f"\n✓ Pievienots: {date_input} | {category} | {amount:.2f} EUR | {description}")


def show_expenses(expenses):
    if len(expenses) == 0:
        print("Nav izdevumu.")
        return

    print(f"\n{'Datums':<12} {'Summa':>10} {'Kategorija':<15} Apraksts")
    print("-" * 55)

    for exp in expenses:
        print(
            f"{exp['date']:<12} {exp['amount']:>8.2f} EUR "
            f"{exp['category']:<15} {exp['description']}"
        )

    print("-" * 55)

    total = sum_total(expenses)
    print(f"Kopā: {total:.2f} EUR ({len(expenses)} ieraksti)")


def main():
    expenses = load_expenses()

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "7":
            print("Uz redzēšanos!")
            break

        else:
            print("Nepareiza izvēle.")


if __name__ == "__main__":
    main()