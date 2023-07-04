# Import OS and CSV
import os
import csv

# Set File Path for CSV file and output text file
csvpath = os.path.join(r"C:\Users\Gabrellea\Desktop\python-challenge\PyPoll\Resources\election_data.csv")
file_to_output = "election_results.txt"

# Set Variables 
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""



# Open the File
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #loop through to find the total votes
    for row in csvreader:

        # Find the total vote count
        total_votes += 1

        candidate = row["Candidate"]
        # if statement to run on first occurence of candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1



#Create Header and list candidates results in Output Text File 
with open(file_to_output, 'w') as txt_file:
    #create header
    election_header = (
        f"Election Results\n"
        f"---------------\n")
    txt_file.write(election_header)

    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
        
    winning_summary = (
        f"Winner: {winner}"
    )
    print(winning_summary)
    txt_file.write(winning_summary)
