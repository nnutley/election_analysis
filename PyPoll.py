# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis", "election_analysis.txt")


# Initialize a total vote counter
total_votes=0

# Candidate Options
candidate_options=[]
#Declare the empty dictionary
candidate_votes={}

#winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader=csv.reader(election_data)


    # Read the header row
    headers=next(file_reader)


    #Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes +=1
    
        #Print the candidate name from each row
        candidate_name=row[2]


        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
        
        #Save the results to the text file
        with open(file_to_save, "w") as txt_file:
        
            election_results=(
                f"\nElection Results\n"
                f"---------------------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"---------------------------------------\n")
            print(election_results, end="")

            #save the final vote count to the text file
            txt_file.write(election_results)

            #Determine the percentage of votes for each candidate by looping through the counts

            #iterate through the candidate list
            for candidate_name in candidate_votes:
                #retrieve vote count of a candidate
                votes=candidate_votes[candidate_name]

                #calculate the percentage of votes
                vote_percentage=float(votes)/float(total_votes)*100

                #print out each candidate's name, vote count and percentage of votes @ termianl
                candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                #print each candidate, their voter count and the % @ terminal
                print(candidate_results)

                #save the candidate results to text file
                txt_file.write(candidate_results)

                #Determine wining vote count and candidate
                #Determine if the votes is greater than the winning count
                if (votes>winning_count) and (vote_percentage>winning_percentage):
                    #if true then set winning_count=votes and winnin_percentage=vote_percentage
                    winning_count=votes
                    winning_percentage=vote_percentage
                    #and set the winning_candidate equal to the candidate's name
                    winning_candidate=candidate_name

            winning_candidate_summary=(
                f"-----------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"------------------\n")

            #save the winning candidate's results to text file
            txt_file.write(winning_candidate_summary)