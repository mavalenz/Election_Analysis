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
# Open the election results and read the file
# election_data = open(file_to_load,'r')
    #or
with open(file_to_load) as election_data:
# To do: Print the file object and perform analysis.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# Or to be more clean an concise use the "with statement" to open the file as a text file.
with open(file_to_load) as election_data:

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

    # Print each row in the CSV file.
    # for row in file_reader:
        # print(row)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
