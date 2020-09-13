# THE DATA WE NEED TO RETRIEVE:
# 1. The total number of votes cast.
# 2. The list of candidates who received votes.
# 3. The total number of votes each candidate received.
# 4. The percentage of votes each candidate won.
# 5. The winner of the election based on popular vote.
# 6. *NEW* The number of votes that were casted from each county.
# 7. *NEW* The percentage of votes each county contributed to the election.
# 8. *NEW* The county with the highest voter turnout.


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
total_countyvotes = 0
# Initialize a candidate and counties list.
candidate_options = []
county = []
# Declare empty dictionaries.
candidate_votes = {}
county_votes = {}

# Declare winning candidate and Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Declare highest vote county and vote count tracker
highest_county = ""
highest_countycount = 0
highest_countypercentage = 0

# Open the election results, read the file and create variable.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    # For loop to go through each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count for the candidate and county.
        total_votes += 1
        total_countyvotes += 1
        # Print the candidate and county name from each row.
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0 

        # If the county does not match any existing county...
        if county_name not in county:
            # Add it to the list of counties.
            county.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Add a vote to that county's vote count.
        county_votes[county_name] += 1

#Save the results to our text file.
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

    # Print and write the "County Votes" header.
    print('County Votes:')
    txt_file.write('County Votes:')

   # Iterate through the counties list.
    for county in county_votes:
        # Retrieve vote count of a county.
        countyvotes = county_votes[county]
        # Calculate the percentage of votes of a county.
        county_percentage = float(countyvotes) / float(total_countyvotes) * 100
   
        # Print out each county's name, their vote count, and percentage of votes to the text.
        county_results = (f"\n{county}: {county_percentage: .1f}% ({countyvotes:,})")
        # Print each county, their vote, and percentage.
        print (county_results)
        # Save the county results to the text file.
        txt_file.write(county_results)

        # Find the county with the highest voter turnout
        if (countyvotes > highest_countycount) and (county_percentage):
            # If true then set highest_countycount to countyvotes, 
            # highest_countypercentage to county_percentage and
            # sent highest_county to county's name.
            highest_countycount = countyvotes
            highest_countypercentage = county_percentage
            highest_county = county

    # Print the county with the highest voter turnout to the text.
    highest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {highest_county}\n"
        f"-------------------------\n")
    print (highest_county_summary)
    # Save county with the highest voter turnout to the text.
    txt_file.write(highest_county_summary)

   # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print out each candidate's name, vote count, and percentage of votes to the terminal.
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, candidate and if votes 
        # are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

#Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)