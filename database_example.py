import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS teams
            (name text, team text, position text)''')

cur.execute('''INSERT INTO teams VALUES
            ('saquon barkley', 'eagles', 'RB')''')

con.commit()

for row in cur.execute('''SELECT * FROM teams'''):
    print(row)
