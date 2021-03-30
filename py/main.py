import sqlite3
from ScheduledDate import *
from User import *

def main():
	con = sqlite3.connect('overseer.db')
	cur = con.cursor()
	
	date = ScheduledDate(cur)

	cur.execute("SELECT * FROM users")

	userData = cur.fetchone()
	while userData != None:
		if userData[2] == 0:
			user = User(userData, cur)
		userData = cur.fetchone()



	con.close()


if __name__ == "__main__":
	main()