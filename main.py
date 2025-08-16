import csv

income = 0.0
expense = 0.0

with open('transactions.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        amount = float(row['Amount'])
        
        if amount > 0:
            income += amount
        else:
            expense -= amount
        
print("--- Financial Summary ---")
print(f"Total income = ${income:.2f}")
print(f"Total expense = ${abs(expense):.2f}")

print(f"Net Balance = ${(income + expense):.2f}")
