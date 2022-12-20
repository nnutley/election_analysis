import csv
import os
# The data we need to retrieve/
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path.

file_to_load=os.path.join("Resources", "election_results.csv")

#Open the election results and read the file

with open(file_to_load) as election_data:

    #To do: perform analysis.

    print(election_data)

# Create a filename variable to a direct or indirect path to the file

file_to_save=os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file

open(file_to_save, "w")

#Use the open statement to open the file as a text file.

outfile=open(file_to_save, "w")

# Write some data to the file

outfile.write("Hello World")

# Close the file

outfile.close()