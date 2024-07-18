import os
import csv

csv_file = ("Resources", "budget_data.csv")
csv_file = "budget_data.csv"

 #variables
total_months = 0
net_total= 0
previous_profit_loss = 0
monthly_changes = []
months = []

with open(csv_file, mode= 'r') as  file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

print("Financial Analysis")
print("------------------")

for row in csv_reader:
    month_year = row[0]
    profit_loss = int(row[1])
    total_months += 1
    net_total += int(row[1])
    if total_months > 1:
         if total_months > 1:
            change = profit_loss - previous_profit_loss
            monthly_changes.append(change)
            months.append(month_year)
    previous_profit_loss = previous_profit_loss
average_change = sum(monthly_changes) / len(monthly_changes)
greatest_increase = max(monthly_changes)
greatest_increase_index = monthly_changes.index(greatest_increase)
greatest_increase_month = months[greatest_increase_index]

greatest_decrease = min(monthly_changes)
greatest_decrease_index = monthly_changes.index(greatest_decrease)
greatest_decrease_month = months[greatest_decrease_index]

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")