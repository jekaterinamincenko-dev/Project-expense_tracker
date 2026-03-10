import json
import os

FILEPATH = "final-project/expense_tracker/expenses.json"


def load_expenses():
    """Nolasa izdevumus no JSON faila."""
    if not os.path.exists(FILEPATH):
        return []

    with open(FILEPATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    """Saglabā izdevumus JSON failā."""
    with open(FILEPATH, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)