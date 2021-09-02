import sqlite3
conn = sqlite3.connect('phonebook.db')
c = conn.cursor()
c.execute("""
	CREATE TABLE IF NOT EXISTS phonedict(name text, phone text)
	""")
conn.commit()