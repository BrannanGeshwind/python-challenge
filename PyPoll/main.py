import os
import csv

# Importing CSV
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    electiondata = csv.DictReader(csvfile)
    electiondata = list(electiondata)

    totalVotes = len(electiondata)










print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
