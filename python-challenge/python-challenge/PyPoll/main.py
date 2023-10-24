import os
import csv
csvpath_csv = os.path.join("Resources/election_data.csv")

counter = 0
candidates={"Charles Casper Stockham" : 0,
            "Diana DeGette" : 0,
            "Raymon Anthony Doane" : 0}

with open(csvpath_csv) as csvfile:
    election_data = csv.reader(csvfile,delimiter =",")
    next(election_data, None)
     
    for row in election_data:
        votes = row[2]
        counter = counter + 1
        if votes == "Charles Casper Stockham":
            candidates["Charles Casper Stockham"] = candidates["Charles Casper Stockham"] + 1
        if votes == "Diana DeGette":
            candidates["Diana DeGette"] = candidates["Diana DeGette"] + 1
        if votes == "Raymon Anthony Doane":
            candidates["Raymon Anthony Doane"] = candidates["Raymon Anthony Doane"] + 1

ccs_percent = (candidates["Charles Casper Stockham"]/counter)*100
dd_percent = (candidates["Diana DeGette"]/counter)*100
rad_percent = (candidates["Raymon Anthony Doane"]/counter)*100   

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