# Projekta plāns — Izdevumu izsekotājs

## A. Programmas apraksts

Šī programma ir komandrindas (CLI) lietojums, kas ļauj lietotājam
reģistrēt savus ikdienas izdevumus. Lietotājs var pievienot jaunus
izdevumus, apskatīt visus izdevumus, filtrēt tos pēc mēneša,
skatīt kopsummas pa kategorijām un eksportēt datus CSV failā.

Programma saglabā datus JSON failā, lai tie nepazustu pēc programmas aizvēršanas.

---

## B. Datu struktūra

Katrs izdevums tiek saglabāts kā vārdnīca ar šādiem laukiem:
{
"date": "2025-02-15",
"amount": 12.50,
"category": "Ēdiens",
"description": "Pusdienas kafejnīcā"
}

Visi izdevumi tiek glabāti sarakstā:
[
{...},
{...},
{...}
]

Šāda struktūra ir vienkārša, viegli saglabājama JSON failā
un ērti apstrādājama Python programmā.

---

## C. Moduļu plāns

Projektā būs šādi faili:

### app.py
Galvenā programma ar CLI izvēlni.
Šis fails apstrādā lietotāja ievadi un izsauc funkcijas no citiem moduļiem.

Galvenās funkcijas:
- show_menu() — parāda izvēlni
- add_expense() — pievieno jaunu izdevumu
- show_expenses() — parāda izdevumu sarakstu
- delete_expense() — dzēš izdevumu
- main() — galvenā programmas cilpa

### storage.py
Atbild par datu saglabāšanu JSON failā.

Funkcijas:
- load_expenses() — nolasa izdevumus no JSON faila
- save_expenses(expenses) — saglabā izdevumus JSON failā

### logic.py
Programmas loģika un aprēķini.

Funkcijas:
- sum_total(expenses) — aprēķina kopējo summu
- filter_by_month(expenses, year, month) — filtrē izdevumus pēc mēneša
- sum_by_category(expenses) — aprēķina summas pa kategorijām
- get_available_months(expenses) — atgriež mēnešus, kuros ir izdevumi

### export.py
Eksportē datus CSV failā.

Funkcijas:
- export_to_csv(expenses, filepath)

---

## D. Lietotāja scenāriji

### Scenārijs 1
Lietotājs izvēlas "Pievienot izdevumu".

Programma prasa:
- datumu
- kategoriju
- summu
- aprakstu

Ja dati ir pareizi, izdevums tiek pievienots sarakstam
un saglabāts JSON failā.

---

### Scenārijs 2
Lietotājs izvēlas "Parādīt izdevumus".

Programma parāda visus izdevumus tabulas formātā
un kopējo iztērēto summu.

---

### Scenārijs 3
Lietotājs izvēlas "Dzēst izdevumu".

Programma parāda numurētu izdevumu sarakstu.
Lietotājs izvēlas numuru, kuru dzēst.

---

## E. Robežgadījumi

Ja expenses.json neeksistē:
- programma izveido tukšu sarakstu.

Ja lietotājs ievada nepareizu summu:
- programma parāda kļūdu un prasa ievadi vēlreiz.

Ja lietotājs ievada nepareizu datuma formātu:
- programma parāda kļūdas paziņojumu.

Ja izdevumu saraksts ir tukšs:
- programma parāda ziņojumu "Nav izdevumu".