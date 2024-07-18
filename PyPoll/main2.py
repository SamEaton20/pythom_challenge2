import os
import csv

csv_file = os.path.join("Resources", "election_data.csv")
    
#variables
total_votes = 0
candidates = []
votes_per_candidate = {}

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate_name = row [2]

        if candidate_name in votes_per_candidate:
            votes_per_candidate[candidate_name] =+1
        else:
            votes_per_candidate[candidate_name] = 1
        if candidate_name not in candidates:
            candidates.append(candidate_name)
percenatage_per_candidate = {}
winner = ""
max_votes = 0

for candidate in candidates:
    votes = votes_per_candidate[candidate]
    percentage = (votes / total_votes) * 100
    percenatage_per_candidate[candidate] = percentage

    if votes > max_votes:
        max_votes = votes
        winner = candidate
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    votes = votes_per_candidate[candidate]
    percentage = percentage_per_candidate[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

