#import modules
import os
import csv

# Importing CSV
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Starting code, declaring needed variables, lists, dictionaries
with open(csvpath, 'r') as csvfile:
    electiondata = csv.DictReader(csvfile)
    electiondata = list(electiondata)

    totalVotes = len(electiondata)

    #Starting Loops for lookups
    candidateVotes = {}
    for row in electiondata:
        candidate = row["Candidate"]
        if candidate in candidateVotes:
            candidateVotes[candidate] += 1
        else:
            candidateVotes[candidate] = 1

    candidatePercentages = {}
    for candidate, votes in candidateVotes.items():
        percentage = (votes / totalVotes) * 100
        candidatePercentages[candidate] = percentage

# Outputting to GitBash
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for candidate, votes in candidateVotes.items():
    percentage = candidatePercentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
winner = max(candidateVotes, key=candidateVotes.get)
print(f"Winner: {winner}")
print("-------------------------")

# Outputting as .txt file
outputpath = os.path.join('..', 'PyPoll', 'Analysis', 'ElectionResults.txt')
with open(outputpath, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalVotes}\n")
    for candidate, votes in candidateVotes.items():
        percentage = candidatePercentages[candidate]
        txtfile.write("-------------------------\n")
        txtfile.write(f"Candidate: {candidate}\n")
        txtfile.write(f"Percentage of Votes: {percentage:.3f}%\n")
        txtfile.write(f"Total Votes: {votes}\n")
    txtfile.write("-------------------------\n")
    winner = max(candidateVotes, key=candidateVotes.get)
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")