import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Create fresh table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (
    org TEXT UNIQUE,
    count INTEGER
)
''')

# Ask for file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

# Open file
fh = open(fname, 'r')

# Process each line
for line in fh:
    if not line.startswith('From '):
        continue

    parts = line.split()
    email = parts[1]

    if '@' not in email:
        continue

    domain = email.split('@')[1]

    # Insert or update count
    cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# Save changes
conn.commit()

# Display results
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(row[0], row[1])

# Close connections
cur.close()
conn.close()
