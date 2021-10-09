# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# ## Total number of votes cast
# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     # Read the header row.
#     headers = next(file_reader)
#     # Count each row in the CSV file using a loop +=1.
#     for row in file_reader:
#         # 2. Add to the total vote count.
#         total_votes += 1
# # 3. Print the total votes.
# print(total_votes)



## A complete list of candidates who received votes
# Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     # Read the header row.
#     headers = next(file_reader)
#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1
#         # Print the candidate name from each row.
#         candidate_name = row[2]
#         # If the candidate does not match any existing candidate...
#         if candidate_name not in candidate_options:
#             # Add it to the list of candidates.
#             candidate_options.append(candidate_name)
# # Print the candidate list.
# print(candidate_options)

# ## Total number of votes each candidate received
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     # Read the header row.
#     headers = next(file_reader)
#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1
#         # Print the candidate name from each row.
#         candidate_name = row[2]
#         if candidate_name not in candidate_options:
#             # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)
#            # Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0
#         # Add a vote to that candidate's count
#         candidate_votes[candidate_name] += 1
# # Print the candidate vote dictionary.
# print(candidate_votes)

# ## Percentage of votes each candidate won
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     # Read the header row.
#     headers = next(file_reader)
#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1
#         # Print the candidate name from each row.
#         candidate_name = row[2]
#         if candidate_name not in candidate_options:
#             # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)
#            # Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0
#         # Add a vote to that candidate's count
#         candidate_votes[candidate_name] += 1
# for candidate_name in candidate_votes:
#     # 2. Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # 3. Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100
#     # 4. Print the candidate name and percentage of votes.
#     print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

## The winner of the election based on popular vote
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)





# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# # Assign a variable for the file to load and the path. Direct Path
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file
# with open(file_to_load) as election_data:
#      # To do: perform analysis.
#      print(election_data)
#  # Close the file.
# election_data.close()

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#      # Write three counties to the file. \n mean new line
#      txt_file.write("Arapahoe\nDenver\nJefferson")
# # Close the file
# txt_file.close()
