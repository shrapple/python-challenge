import os
import csv
csvpath_csv = os.path.join("Resources/budget_data.csv")

#assigning names and starting values to variables
total = 0
total_change = 0
counter = 0    
greatest_increase = 0 
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""
lastprofit_loss = 1088983
#opening and reading the csv
with open(csvpath_csv) as csvfile:
    pybank_data = csv.reader(csvfile,delimiter =",")
    next(pybank_data, None)
#looking in each row of the data and creating new variables
# and their values based on information found in each row 
# hint: this is where you want to start and then create
# and set your initial variables 
    for row in pybank_data:
        profit_loss = int(row[1])
        total = total + profit_loss
        change = profit_loss - lastprofit_loss
        lastprofit_loss = profit_loss
        dates = row[0]
        total_change = total_change + change
        counter = counter + 1
#when it's checking each row, the change between the current and
#next row is being checked against itself, and then moves on to
# the next row to check for the demands created, here 
# using greater or less than with the change between months
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = dates
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = dates
#an average equation for an average
average = total_change/(counter-1)
#print out our information concisely, but also nicely
print("Financial Analysis")
print("-------------------")
print("Total Months:    " + str(counter))
print("Total:           $" + str(total)) 
print("Average Change:  $" + "(%.2f)"%average)
print("Greatest Increase in Profits:    " + str(greatest_increase_date) + "    ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits:    " + str(greatest_decrease_date) + "    ($" + str(greatest_decrease) + ")")
#writes a text file for what is included after f.write.
#the "a" means that if this python page is ran multiple times, it'll
#just keep adding to the same txt file. "w" can be used when wanting to replacde
f = open("myfile.txt","a") 
f.write("Financial Analysis-    Total Months: 86,   Total: $22564198,   Average Change: $(-8311.11),    Greatest Increase in Profits: Aug-16 ($1862002),    Greatest Decrease in Profits: Feb-14 ($-1825558)")
f.close()



