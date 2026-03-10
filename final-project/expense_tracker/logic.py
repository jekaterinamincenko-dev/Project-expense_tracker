def sum_total(expenses):
    """Aprēķina kopējo izdevumu summu."""
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return round(total, 2)
from datetime import datetime


def filter_by_month(expenses, year, month):
    """Atgriež izdevumus noteiktajā mēnesī."""
    result = []

    for expense in expenses:
        d = datetime.strptime(expense["date"], "%Y-%m-%d")

        if d.year == year and d.month == month:
            result.append(expense)

    return result


def sum_by_category(expenses):
    """Aprēķina summu pa kategorijām."""
    totals = {}

    for expense in expenses:
        cat = expense["category"]
        totals[cat] = totals.get(cat, 0) + expense["amount"]

    return {cat: round(total, 2) for cat, total in totals.items()}


def get_available_months(expenses):
    """Atgriež pieejamos mēnešus."""
    months = set()

    for expense in expenses:
        d = datetime.strptime(expense["date"], "%Y-%m-%d")
        months.add(f"{d.year}-{d.month:02d}")

    return sorted(months)