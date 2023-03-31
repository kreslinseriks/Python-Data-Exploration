fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
emails = []

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        emails.append(email)
        count += 1

emails.sort()

for email in emails:
    print(email)

print("There were", count, "lines in the file with From as the first word.")

# Using regular expressions

import re

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
emails = []

for line in fhand:
    if re.search('^From ', line):
        email = re.findall('\S+@\S+', line)
        emails.append(email[0])
        count += 1

emails.sort()

for email in emails:
    print(email)

print("There were", count, "lines in the file with From as the first word.")

