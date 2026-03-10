import csv


def export_to_csv(expenses, filepath):
    """Eksportē izdevumus CSV failā."""
    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])

        for expense in expenses:
            writer.writerow([
                expense["date"],
                f"{expense['amount']:.2f}",
                expense["category"],
                expense["description"],
            ])