# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# # Assign a variable for the file to load and the path. Direct Path
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file
# with open(file_to_load) as election_data:
#      # To do: perform analysis.
#      print(election_data)
#  # Close the file.
# election_data.close()

# Indirect Path Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row. next() method will skip the first row and return the next item in the list.
    headers = next(file_reader)
    print(headers)




# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
     # Write three counties to the file. \n mean new line
     txt_file.write("Arapahoe\nDenver\nJefferson")
# Close the file
txt_file.close()

# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
