import os
import csv

election_data = os.path.join( "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    count = 0
    total_votes = 0
    candidates = []
    percent_vote = []
    count_vote = []
    unique_candid = []
    index = 0
    candidate = 0



    for row in csvreader:
        total_votes = total_votes + 1
        candidates = row[2]
    if candidate in candidates:
        candidate_index = candidates.index(candidate)
        count_vote[candidate_index] = count_vote[candidate_index] + 1
    else:
        unique_candid.append(candidates)
        count_vote.append(1)

    for x in range(len(candidates)):
        unique_candid.append(x)
        y = candidates.count(x)
        count_vote.append(y)
        z = (y/count)*100
        percent_vote.append(z)

overall_winner = max(count_vote)
winner = unique_candid[count_vote.index(overall_winner)]

print()

file_output = os.path.join("Analysis", "Election_Results.txt")
with open('Election_Results.txt', 'w') as text:
    print("Election Results\n")
    print("Total Vote: " + str(total_votes))
    print(f"{candidates[candidate]}: {str(percent_vote[candidate])} ({str(count_vote[candidate])})")
    print(f"Winner: {winner}")

