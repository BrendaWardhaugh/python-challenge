import os
import csv

CANDIDATE_NAME = 2

py_poll_path = os.path.join("..", "Resources", "election_data.csv")
py_poll_results = os.path.join("..", "Analysis", "py_poll_results.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
#identtify variables
total_votes = 0
candidates = []
names = " "
ccs_votes = 0
dd_votes = 0
rad_votes = 0
ccs_percentage = 0
dd_percentage = 0
rad_percentage = 0
winner = " "


with open(py_poll_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"csvHeader:{csv_header}")
    for row in csvreader:
        #Count total number of votes cast
        total_votes += 1
        #Create a list of candidates who received votes
        names = str(row[CANDIDATE_NAME])
        if (names not in candidates):
            candidates.append(names)
        # Total number of votes each candidate won
        if candidates[0] == str(row[CANDIDATE_NAME]):    
            ccs_votes += 1
        elif candidates[1] == str(row[CANDIDATE_NAME]):    
            dd_votes += 1
        elif candidates[2] == str(row[CANDIDATE_NAME]):    
            rad_votes += 1
        # Percentage of votes each candidate won
        ccs_percentage = ccs_votes/total_votes *100
        dd_percentage = dd_votes/total_votes *100
        rad_percentage = rad_votes/total_votes *100
        # Winner of election
        if ccs_votes > dd_votes and rad_votes:
            winner = candidates[0]
        elif dd_votes > ccs_votes and rad_votes:
            winner = candidates[1]
        elif rad_votes > ccs_votes and dd_votes:
            winner = candidates[2]



print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
print(f"{candidates[0]}: {round(ccs_percentage, 3)}%  ({ccs_votes})")
print(f"{candidates[1]}: {round(dd_percentage, 3)}%  ({dd_votes})")
print(f"{candidates[2]}: {round(rad_percentage, 3)}%  ({rad_votes})")
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")

#input results content for text file
text_to_write = ("Election Results\n"
                 "---------------------------\n"
                 f"Total Votes: {total_votes}\n"
                 "---------------------------\n"
                 f"{candidates[0]}: {round(ccs_percentage, 3)}%  ({ccs_votes})\n"
                 f"{candidates[1]}: {round(dd_percentage, 3)}%  ({dd_votes})\n"
                 f"{candidates[2]}: {round(rad_percentage, 3)}%  ({rad_votes})\n"
                 "---------------------------\n"
                 f"Winner: {winner}\n"
                 "---------------------------\n")
                
#write results in text file
with open(py_poll_results, "w") as text_file:
    text_file.write(text_to_write)


