import os
import csv

# Importing CSV
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Opening CSV path for reference
with open(csvpath, 'r') as csvfile:
    budgetdata = csv.DictReader(csvfile)
    budgetdata = list(budgetdata)

    TotalMonths = len(budgetdata)
    sumTotal = sum(int(row["Profit/Losses"]) for row in budgetdata)

    changes = []
    lastValue = float(budgetdata[0]["Profit/Losses"])
    for row in budgetdata[1:]:
        curValue = int(row["Profit/Losses"])  
        change = curValue - lastValue
        changes.append(change)
        lastValue = curValue

    avg = sum(changes) / len(changes)

    

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {TotalMonths}')
print(f'Total: {sumTotal}')
print(f"Average Change: {int(avg)}")