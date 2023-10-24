import os
import csv
csvpath_csv = os.path.join("Resources/budget_data.csv")

#assigning variables values
total = 0
total_change = 0
counter = 0    
greatest_increase = 0 
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""
lastprofit_loss = 1088983
#
with open(csvpath_csv) as csvfile:
    pybank_data = csv.reader(csvfile,delimiter =",")
    next(pybank_data, None)
    

    for row in pybank_data:
        profit_loss = int(row[1])
        total = total + profit_loss
        change = profit_loss - lastprofit_loss
        lastprofit_loss = profit_loss
        dates = row[0]
        total_change = total_change + change
        counter = counter + 1

        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = dates
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = dates

average = total_change/(counter-1)

print("Financial Analysis")
print("-------------------")
print("Total Months:    " + str(counter))
print("Total:           $" + str(total)) 
print("Average Change:  $" + "(%.2f)"%average)
print("Greatest Increase in Profits:    " + str(greatest_increase_date) + "    ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits:    " + str(greatest_decrease_date) + "    ($" + str(greatest_decrease) + ")")





