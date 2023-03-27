# Exploring email - handling words using dictionary
import re

# Definitions of variables
base = 0
longest_domain = 0
domains = []
counts = dict()

# Opening the file
fname = input('Enter a file name: ')
fhand = open(fname)

# Make a list of all domains
for line in fhand :
    if re.search('^From\s',line) :
        domain = re.findall('.@(.*?)\s',line)
        domains.append(domain)
    
# Count the number of domains that were used to send email using dictionary, print dictionary
for domain in domains :
    if str(domain) not in counts :
        counts[str(domain)] = 1
    else :
        counts[str(domain)] = counts[str(domain)] + 1
print(counts,'\n')

# Sort dictionary by value
sorted_domains = dict(sorted(counts.items(), key=lambda x:x[1]))

# Get longest domain for calculation of whitespaces
for key in sorted_domains :
    if len(key) > longest_domain :
        longest_domain = len(key)

# Print the sorted values
print('SORTED:')
for key in sorted_domains :
    print(' ' * (longest_domain - len(key)),key[2:len(key) - 2],':',sorted_domains[key], '*' * sorted_domains[key])