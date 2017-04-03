import mysql.connector
from user import User


class DatabaseQueries():
	def getUserData(self):
		cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='sys')
		cur = cnx.cursor()
		list1 = []
		try :
			cur.execute("SELECT * FROM user")
			if cur != None :
				for row in cur.fetchall():
					user = User()
					user.setUserName(row[1])
					user.setEmailId(row[2])
					user.setZipCode(row[3])
					user.setPassword(row[4])
					user.setProject(row[5])
					list1.append(user)
				cnx.close()
				return list1
			else :
				return None
		except:
			return None

	def setUserData(self,user):
		cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='sys')
		cur = cnx.cursor()
		add_user = ("INSERT INTO user "
			"(ID, userName, emailId, zipCode, password) "
			"VALUES (%s, %s, %s, %s, %s)")
		data_user = (user.getUserId(),user.getUserName(), user.getEmailId(), user.getZipCode(), user.getPassword())
		cur.execute(add_user, data_user)
		cnx.commit()
		cur.close()
		cnx.close()

	def updateUserProject(self,userName,project):
		cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='sys')
		cur = cnx.cursor()
		add_user = ("UPDATE user SET project = %s where userName = %s")
		data_user = (project,userName)
		cur.execute(add_user, data_user)
		cnx.commit()
		cur.close()
		cnx.close()