from datetime import date
from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months

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
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
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

def show_category_summary(expenses):
    totals = sum_by_category(expenses)

    if not totals:
        print("Nav izdevumu.")
        return

    print("\nKopsavilkums pa kategorijām:")
    print("-" * 30)

    total = 0

    for cat, amount in totals.items():
        print(f"{cat:<20} {amount:>8.2f} EUR")
        total += amount

    print("-" * 30)
    print(f"KOPĀ: {total:.2f} EUR")

def filter_expenses_by_month(expenses):
    months = get_available_months(expenses)

    if not months:
        print("Nav izdevumu.")
        return

    print("\nPieejamie mēneši:")
    for i, m in enumerate(months, 1):
        print(f"{i}) {m}")

    try:
        choice = int(input("Izvēlies mēnesi: "))
        selected = months[choice - 1]
    except:
        print("Nepareiza izvēle.")
        return

    year, month = map(int, selected.split("-"))
    filtered = filter_by_month(expenses, year, month)

    print(f"\n{selected} izdevumi:")
    show_expenses(filtered)

def delete_expense(expenses):
    if not expenses:
        print("Nav izdevumu.")
        return

    print("\nIzdevumi:")

    for i, exp in enumerate(expenses, 1):
        print(
            f"{i}) {exp['date']} | {exp['amount']:.2f} EUR | "
            f"{exp['category']} | {exp['description']}"
        )

    try:
        choice = int(input("\nKuru dzēst? (0 lai atceltu): "))

        if choice == 0:
            return

        removed = expenses.pop(choice - 1)
        save_expenses(expenses)

        print(
            f"✓ Dzēsts: {removed['date']} | {removed['amount']:.2f} EUR | "
            f"{removed['category']} | {removed['description']}"
        )

    except:
        print("Nepareiza izvēle.")

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

        elif choice == "3":
            filter_expenses_by_month(expenses)

        elif choice == "4":
            show_category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        else:
            print("Nepareiza izvēle.")


if __name__ == "__main__":
    main()