from connect import *
import sys


def insert(name,phone):
	c.execute("""
		INSERT INTO phonedict VALUES(:name,:phone)
		""",{'name':name,'phone':phone})
	conn.commit()

def get():
	c.execute("SELECT * FROM phonedict")
	print(c.fetchall())

def delete_by_name(name):
	#print("yoyoyo")
	c.execute("DELETE FROM phonedict WHERE name =:name",{'name':name})
	conn.commit()
	#print(conn.total_changes)
	if conn.total_changes >= 1:
		return 1
	else:
		return 0
	

def delete_by_phone(phone):
	c.execute("DELETE FROM phonedict WHERE phone =:phone",{'phone':phone})
	conn.commit()
	if conn.total_changes >= 1:
		return 1
	else:
		return 0


conn.commit()


