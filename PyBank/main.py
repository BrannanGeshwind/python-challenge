import os
import csv

# Importing CSV
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Opening CSV path for reference, declaring needed variables, lists, dictionaries
with open(csvpath, 'r') as csvfile:
    budgetdata = csv.DictReader(csvfile)
    budgetdata = list(budgetdata)

    TotalMonths = len(budgetdata)
    sumTotal = sum(int(row["Profit/Losses"]) for row in budgetdata)

    changes = []
    greatestincrease = {"amount": 0, "date": ""}
    greatestdecrease = {"amount": float('inf'), "date": ""}
    lastValue = float(budgetdata[0]["Profit/Losses"])
    # Starting Loops for lookups
    for row in budgetdata[1:]:
        curValue = int(row["Profit/Losses"])  
        change = curValue - lastValue
        changes.append(change)
        lastValue = curValue

        if change > greatestincrease["amount"]:
            greatestincrease["amount"] = change
            greatestincrease["date"] = row["Date"]
        
        if change < greatestdecrease["amount"]:
            greatestdecrease["amount"] = change
            greatestdecrease["date"] = row["Date"]



    avg = sum(changes) / len(changes)

# Outputting to GitBash
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {TotalMonths}')
print(f'Total: {sumTotal}')
print(f"Average Change: {int(avg)}")
print("Greatest Increase in Profits: " + greatestincrease["date"] + " ($" + str(greatestincrease["amount"]) + ")")
print("Greatest Decrease in Profits: " + greatestdecrease["date"] + " ($" + str(greatestdecrease["amount"]) + ")")

# Outputting as .txt file
outputpath = os.path.join('..', 'PyBank', 'Analysis', 'PyBankAnalysis.txt')
with open(outputpath, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {TotalMonths}\n")
    txtfile.write(f"Total: {sumTotal}\n")
    txtfile.write(f"Average Change: {int(avg)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatestincrease['date']} (${greatestincrease['amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatestdecrease['date']} (${greatestdecrease['amount']})\n")