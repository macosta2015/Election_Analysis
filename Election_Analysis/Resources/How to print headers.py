# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path. Folder and file name
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path. Folder and file name
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results through the variable and set the as variable, 
# then set the reader variable to read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Create header variable and use the reader variable to tell it what to read.  
    # Print the header row.
    headers = next(file_reader)
    print(headers)