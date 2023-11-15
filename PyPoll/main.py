import csv
import os

#set the path

CSV_PATH = os.path.join("Resources", "election_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# open and read the file 

with open(CSV_PATH, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    header = next(csv_reader)
    rows = list(csv_reader)

    print("Election Results")
    print("-------------------------")

    #Find the total number of votes cast
    total_votes = len(rows)
    print(f"Total votes: {total_votes}")
    print("-------------------------")

    #Find a complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote

    candidate_votes = {}

    # Loop through rows and count votes for each candidate
    for row in rows:
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    winner = ""
    winner_votes = 0

    # Loop through candidate votes and print results
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.2f}% ({votes})")

        # Check for the winner
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

        #create the output and print the results

    with open("analysis/Output.txt", "w") as text_file:
        text_file.write("Election Results\n")
        text_file.write("----------------------------\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        text_file.write("----------------------------\n")
        for candidate, votes in candidate_votes.items():
            percentage = (votes / total_votes) * 100
            text_file.write(f"{candidate}: {percentage:.2f}% ({votes})\n")
        text_file.write("----------------------------\n")
        text_file.write(f"Winner: {winner}\n")
        text_file.write("-------------------------\n")
     

   