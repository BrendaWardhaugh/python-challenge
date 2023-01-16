import os
import csv

PROFIT_INDEX = 1
DATE = 0

py_bank_path = os.path.join("..", "Resources", "budget_data.csv")
py_bank_results = os.path.join("..", "Analysis", "py_bank_results.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
#identtify variables
month_count = 0
total_profit = 0
previous_profit = 0
profit_change = []
max_increase = 0
max_decrease = 0
max_increase_date = " "
max_decrease_date = " "
current_change = 0

with open(py_bank_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"csvHeader:{csv_header}")
    for row in csvreader:
      # Count the total number of months
        month_count += 1
       # calculate changes in "Profit/Losses" over the entire period
        current_profit = int(row[PROFIT_INDEX])
        total_profit += current_profit 
        # calculate the average change in profit/loss
        if previous_profit == 0:
            previous_profit = int(row[1])
        else:
            current_profit = int(row[1])
            current_change = current_profit - previous_profit
            profit_change.append(current_change)
            previous_profit = int(row[1])  
         # Calculate the greatest increase and greatest decrease in profits
        if current_change > max_increase:
            max_increase = current_change
            max_increase_date = row[0]
        if current_change < max_decrease:
            max_decrease = current_change
            max_decrease_date = row[0]

average = sum(profit_change) / len(profit_change)   



        
print("Financial Analysis")
print("---------------------------")
print(f"Total Month: {month_count}")
print(f"Total Profit: $ {total_profit}")
print(f"Average Change: {round(average, 2)}")
print(f"Greatest Increase in Profits: {max_increase_date}  (${max_increase}) ")
print(f"Greatest Drecrease in Profits: {max_decrease_date} (${max_decrease})")

#input results content for text file
text_to_write = ("Financial Analysis\n"
                 "---------------------------\n"
                 f"Total Month: {month_count}\n"
                 f"Total Profit: $ {total_profit}\n"
                 f"Average Change: {round(average, 2)}\n"
                 f"Greatest Increase in Profits: {max_increase_date}  (${max_increase})\n"
                 f"Greatest Drecrease in Profits: {max_decrease_date} (${max_decrease})\n")

#write results in text file
with open(py_bank_results, "w") as text_file:
    text_file.write(text_to_write)



