# **Election Analysis**

## *Overview of Election Audit:*
    -Tom, an employee of the Colorado board of elections, asked for support in running an election audit of the results from a U.S. congressional precinct in Colorado. In order to complete the audit, we used Python to compare the outcomes of the different candidates and different counties.

### Purpose:
    -The purpose of the analysis was to use Python to calculate the total number of votes, the number of votes per candidae, and the number of votes per county. Additionally, we determine which county had the largest turnout and which candidate was the winner.

## *Election-Audit Results:*
    -The total amount of votes that were cast in this congressional election was 369,711.
    
    -Jefferson county had 38,855 votes, which made up 10.5% of the total votes. Denver county had 306,055 votes, which made up 82.8% of the total votes. Arapahoe county had 24,801 votes, which made up 24,801 of the total votes.
    
    -Denver county had the largest overall turnout. This was determined by the following script:
        
        if (c_votes > winning_county_count):
            winning_county_count = c_votes
            winning_county = county_name
            
    -Charles Casper Stock had 85,213 votes, which made up 23.0% of the total votes. Diana DeGette had 272,892 votes, which made up 73.8% of the total votes. Raymon Anthony Doane had 11,606 votes, which made up 3.1% of the total votes.
    
    -Diana Degette won the election with 272,892 votes, which made up 73.8% of the total votes. This was determined by the following script:
    
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

![Election Results Summary](/Resources/election_results_summary.png)

## *Election-Audit Summary:*
    -Moving forward, the election commission will be able to continue to use this Python script to aid them in furture elections. The script can be easily reused with no modifications if the election commission uses datasets with the same structure and inputs as the current dataset. The script can also be modified to support the analysis for additional data points if the future datasets differ in structure or inputs from this current one.
    
        -One modification to the script could be made if the election commission wanted to include the party of the candidates. In this case, the script would be modified to include similar repitition statements, conditional statements, and print statements as the script that was written to complete the analysis of the candidates and counties. If the script was written in the same manner as the exist one and then included in it, the election commitee would be able to complete the same analysis on the different parties of the candidates. This would allow this to determine the winning party, how many overall votes that party had, and what percentage of the total votes that party obtained.
        
        -Another modification to the script could be made if the election comission wanted to include the party of the candidates. In this case, after the script was modififed to determine the winning party, a conditional statement could be used to determine if each of the candidates were a party of the overall winning party.
