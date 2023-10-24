import os
import csv
csvpath_csv = os.path.join("Resources/election_data.csv")
#defining and setting initial values for my variables
counter = 0
candidates={"Charles Casper Stockham" : 0,
            "Diana DeGette" : 0,
            "Raymon Anthony Doane" : 0}
#opening and reading the csv
with open(csvpath_csv) as csvfile:
    election_data = csv.reader(csvfile,delimiter =",")
    next(election_data, None)
#checking row by row (for loop)
    for row in election_data:
        votes = row[2]
        counter = counter + 1
#checking each entry in the 3 column for candidates entered names
        if votes == "Charles Casper Stockham":
            candidates["Charles Casper Stockham"] = candidates["Charles Casper Stockham"] + 1
        if votes == "Diana DeGette":
            candidates["Diana DeGette"] = candidates["Diana DeGette"] + 1
        if votes == "Raymon Anthony Doane":
            candidates["Raymon Anthony Doane"] = candidates["Raymon Anthony Doane"] + 1
#finding and labeling some percent variables
ccs_percent = (candidates["Charles Casper Stockham"]/counter)*100
dd_percent = (candidates["Diana DeGette"]/counter)*100
rad_percent = (candidates["Raymon Anthony Doane"]/counter)*100   
#displaying it nicely for the consumer
print("Election Results")
print("-------------------")
print("Total Votes:    " + str(counter))
print("-------------------")
print("Charles Casper Stockham: " + "%.3f"%ccs_percent + "% (" + str(candidates["Charles Casper Stockham"]) + ")")
print("Diana DeGette: " + "%.3f"%dd_percent + "% (" + str(candidates["Diana DeGette"]) + ")")
print("Raymon Anthony Doane: " + "%.3f"%rad_percent + "% (" + str(candidates["Raymon Anthony Doane"]) + ")")
print("-------------------")
print("Winner:  Diana DeGette")
print("-------------------")
#writing a text file containting the string ("Election Results, Total Votes:....")
f = open("myfile.txt","a") 
f.write("Election Results-  Total Votes: 369711,    Charles Casper Stockham: 23.049% (85213),   Diana DeGette: 73.812% (272892),    Raymon Anthony Doane: 3.139% (11606),   Winner: Diana DeGette")
f.close()