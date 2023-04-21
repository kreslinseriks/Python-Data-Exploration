import sqlite3
import re

# Create database 
conn = sqlite3.connect('mbox_data.sqlite')
cur = conn.cursor()

# Table that will be populated with emails
cur.execute('''
            CREATE TABLE IF NOT EXISTS Email
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            email_address TEXT NOT NULL UNIQUE)''')

# Table that will be populated with domains
cur.execute('''
            CREATE TABLE IF NOT EXISTS Domain
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            domain_name TEXT NOT NULL UNIQUE)''')

# Table that will be populated with weekdays
cur.execute('''
            CREATE TABLE IF NOT EXISTS Weekday
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            week_day TEXT NOT NULL UNIQUE)''')

# Table that will be populated with spam-confidence level
cur.execute('''
            CREATE TABLE IF NOT EXISTS Spam
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            spam_confidence REAL)''')

# Table that describes relations and links all the other tables together
cur.execute('''
            CREATE TABLE IF NOT EXISTS Relations
            (email_id INTEGER,
            domain_id INTEGER,
            weekday_id INTEGER,
            spam_id INTEGER,
            FOREIGN KEY(email_id) REFERENCES email(id),
            FOREIGN KEY(domain_id) REFERENCES domain(id),
            FOREIGN KEY(weekday_id) REFERENCES weekday(id),
            FOREIGN KEY(spam_id) REFERENCES spam(id))''')

# Open file
fhand = open('mbox-short.txt')

# Loop through each line of the file
for line in fhand :

    # Extracts email, domain, weekday 
    if re.search('^From\s',line) :
        email = line.split()[1].strip()
        domain = str(re.findall('.@(.*?)\s',line))
        domain = domain[2:len(domain)-2]
        weekday = line.split()[2].strip()
    
    # Extracts spam-confidence level
    if re.search('^X-DSPAM-Confidence:\s',line) :
        spam = line.split()[1].strip()

        # Insert email into the email table
        cur.execute('INSERT OR IGNORE INTO email (email_address) VALUES (?)', (email,))
        cur.execute('SELECT id FROM email WHERE email_address = ?', (email, ))

        # Makes sure that id for relations table corresponds to id in the email table (same done below for each table)
        try:
            emails_id = cur.fetchone()[0]
        except:
            emails_id = cur.lastrowid

        # Insert domain into the domain table
        cur.execute('INSERT OR IGNORE INTO domain (domain_name) VALUES (?)', (domain,))
        cur.execute('SELECT id FROM domain WHERE domain_name = ?', (domain, ))
        try:
            domains_id = cur.fetchone()[0]
        except:
            domains_id = cur.lastrowid

        # Insert weekday into the weekday table
        cur.execute('INSERT OR IGNORE INTO weekday (week_day) VALUES (?)', (weekday,))
        cur.execute('SELECT id FROM weekday WHERE week_day = ?', (weekday, ))
        try:
            weekdays_id = cur.fetchone()[0]
        except:
            weekdays_id = cur.lastrowid

        # Insert spam-confidence level into the spam table
        cur.execute('INSERT OR IGNORE INTO spam (spam_confidence) VALUES (?)', (spam,))
        cur.execute('SELECT id FROM spam WHERE spam_confidence = ?', (spam, ))
        try:
            spams_id = cur.fetchone()[0]
        except:
            spams_id = cur.lastrowid

        # Insert values in the relations table
        cur.execute('INSERT INTO relations VALUES(?, ?, ?, ?)', (emails_id, domains_id, weekdays_id, spams_id, ))

# Commit changes to the database
conn.commit()

# Get list of unique domains
cur.execute('SELECT DISTINCT domain_name FROM Domain')

# Print out the list of unique domains and save them in variable
all_domains = []
print('The following domains are unique:')
for row in cur.fetchall():
    shortened = str(row)
    print(shortened[2:len(shortened)-2])
    all_domains.append(str(row[0]))
print()

# Asks for user input - a domain from the list acquired before
while True :
    user_domain = input("Plese enter domain name from the aforementioned list: ")
    if user_domain in all_domains :
        break
    else :
        print("The input is incorrect. Try again.")

# SELECT query for emails from the selected domain
cur.execute('''
    SELECT email.email_address
    FROM email
    JOIN relations ON email.id = relations.email_id
    JOIN domain ON domain.id = relations.domain_id
    WHERE domain.domain_name = ?
''', (user_domain,))

# Gets and prints the results
email_list = cur.fetchall()
print("The folllowing emails were received from user chosen domain:")
for address in email_list :
    address = str(address)
    print(address[2:len(address)-2])
print()

# SELECT query for emails received only on Saturdays and Sundays
cur.execute('''
    SELECT email.email_address
    FROM email
    JOIN relations ON email.id = relations.email_id
    JOIN weekday ON weekday.id = relations.weekday_id
    WHERE weekday.week_day = 'Fri' OR weekday.week_day = 'Sat'
''')
            
# Gets and prints the results
weekday_email_list = cur.fetchall()
print("The folllowing emails were received on Friday or Saturday:")
for address in weekday_email_list :
    address = str(address)
    print(address[2:len(address)-2])
print()

# SELECT query for data from all tables: weekday, domain, email, spam-confidence level
cur.execute('''
    SELECT weekday.week_day, domain.domain_name, email.email_address, spam.spam_confidence 
    FROM email 
    JOIN relations ON email.id = relations.email_id
    JOIN weekday ON relations.weekday_id = weekday.id 
    JOIN domain ON relations.domain_id = domain.id 
    JOIN spam ON relations.spam_id = spam.id
    ORDER BY weekday.week_day, domain.domain_name, email.email_address, spam.spam_confidence
''')

# Print results, place them in colums indentented certain distance from each other
rows = cur.fetchall()
for row in rows:
    print('{:<10}{:<25}{:<35}{}'.format(row[0], row[1], row[2], row[3]))

# Close database
cur.close()
