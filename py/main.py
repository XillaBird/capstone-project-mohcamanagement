import sqlite3
from User import *

def main():
	con = sqlite3.connect('overseer.db')
	cur = con.cursor()
	
	date = ScheduledDate(cur)

	cur.execute("SELECT * FROM users")


	userList = list()

	userData = cur.fetchone()
	while userData != None:
		if userData[2] == 0:
			userList.append(User(userData, cur, date.getStartTimeDictionary(), date.getEndTimeDictionary()))
		userData = cur.fetchone()



	userList[0].calculateTotalHoursRequested()



	con.close()


if __name__ == "__main__":
	main()