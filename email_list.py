# Exploring e-mail - handling words using list
import re

# Open file, declare variables
fname = input('Enter a file name: ')
fhand = open(fname)
emails = []
from_count = 0

# Loop through text
for line in fhand :
    # Search for lines starting with From, split them, extract email addresses into new list, update From count
    if re.search('^From\s',line) :
        words = line.split()
        emails.append(words[1])
        from_count += 1

# Sort the newly created list of email addresses in alphabetic order
emails.sort()

# Print individual elements from the list as strings
for email in emails :
    print(email)

# Print the number of lines with From as the first word
print('There were ',from_count,'lines in the file with From as the first word')

        