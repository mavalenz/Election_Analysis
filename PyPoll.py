# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Open the data the file in Python
import csv
import os
# Assign a variable for the file to load and the path by joining the resources folder and csv file.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a variable to count up all the votes
total_votes = 0

# Declare a new list to print the candidate name from each row
candidate_options = []

# Declare an empty dictionary to set us up for counting votes per candidate
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
# election_data = open(file_to_load,'r') 
# OR
with open(file_to_load) as election_data:
# To do: Print the file object and perform analysis.
    # print(election_data)

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# Or to be more clean an concise use the "with statement" to open the file as a text file.
# with open(file_to_load) as election_data:

# Practice for below: with open(file_to_save, "w") as txt_file:
# Write some data to the file.
# outfile.write("Hello World")
    # txt_file.write("Hello World! ")
# Close the file
# outfile.close()

# Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
# OR and quick and cleaner way to add the above and using the "newline escape sequence" to separate to new lines.
    # txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader =csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # print(row)
        # Increment total votes by 1 to calculate the total votes number
        total_votes += 1
    
        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        # candidate_options.append(candidate_name)

    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add the vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

    # Print the candidate vote dictionary.
    # print(candidate_votes)

    # Print the candidate list.
    # print (candidate_options)

    # Print the total votes.
    # print(total_votes)
            
    # Determine the percentage of votes for each candidate by looping through the counts.
    #1. Iterate through the candidate list. 
        for candidate_name in candidate_votes:
            #2. Retreive vote count of a candidate. 
            votes = candidate_votes[candidate_name]
            #3. Calculate the percentage of votes.
            vote_percentage = float(votes)/float(total_votes) * 100
            #4. Print the candidate name and percentage of votes.
            # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

            # To do: print out each candidate's name, vote count and percentage of votes to terminal.
            # print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count and percentage of votes to the terminal.
            candidate_results = (f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            # Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determing the winning vote count and candidate
            #1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #2. If true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                #3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        # To do: print out the winning candidate, vote count and percentage of votes to terminal.
        winning_candidate_summary = (
            f"-----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------------\n")
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)
