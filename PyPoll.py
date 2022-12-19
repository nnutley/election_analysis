import os
# The data we need to retrieve/
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path.

file_to_load=os.path.join("election_results.csv")

#Open the election results and read the file
print(file_to_load)
with open(file_to_load) as election_data:

    #To do: perform analysis.

    print(election_data)
