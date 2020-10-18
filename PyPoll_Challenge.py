# Goals
# 1. The voter turnout for each county
# 2. The percentage of votes from each county out of the total count
# 3.The county with the highest turnout

# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
county_options = []
county_votes = {}

# 1: Create a county list and county votes dictionary.



# Track the number of voters for each county
county_name = ""
county_count = 0
county_percentage = 0

# 2: Track the largest county and county voter turnout.



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        county_name = row[1]

        # 3: Extract the county name from each row.


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if county_name not in county_options:

            # Add the candidate name to the candidate list.
            county_options.append(county_name)

            # And begin tracking that candidate's voter count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count
        county_votes[county_name] += 1

        # 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.


            # 4b: Add the existing county to the list of counties.


            # 4c: Begin tracking the county's vote count.


        # 5: Add a vote to that county's vote count.



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a repetition statement to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percent of total votes for the county.


         # 6d: Print the county results to the terminal.

         # 6e: Save the county votes to a text file.

         # 6f: Write a decision statement to determine the winning county and get its vote count.


    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
    for county_name in county_votes:

        # Retrieve vote count and percentage
        votes = county_votes.get(county_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > county_count) and (vote_percentage > county_percentage):
            county_count = votes
            winning_county = county_name
            county_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_county_summary = (
        f"-------------------------\n"
        f"County with the Highest Voter Turn Out: {winning_county}\n"
        f"Highest Vote Count for {winning_county}: {county_count:,}\n"
        f"Percentage of Total Votes: {county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_county_summary)
