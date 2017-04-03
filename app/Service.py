from user import User
from databaseQueries import DatabaseQueries

class ServiceClass():

    def checkIfUnique(self, user):
    	userName = user.getUserName()
    	password = user.getEmailId()
    	databaseQueryObj = DatabaseQueries()
    	list1 = databaseQueryObj.getUserData()
    	if list1 != None :
    		for userFromdb in list1 :
    			if userFromdb.getUserName() ==  userName:
    				return False
        		elif userFromdb.getEmailId() == password:
        			return False
        return True

    def validateUser(self, userName, password):
    	databaseQueryObj = DatabaseQueries()
    	list1 = databaseQueryObj.getUserData()
    	if list1 != None :
    		for userFromdb in list1 :
    			if userFromdb.getUserName() == userName and userFromdb.getPassword() == password:
    				return True
        return False

    def getUserData(self, userName):
    	databaseQueryObj = DatabaseQueries()
    	list1 = databaseQueryObj.getUserData()
    	if list1 != None :
    		for userFromdb in list1 :
    			if userFromdb.getUserName() == userName:
    				return userFromdb
        return None

    def isUserPresent(self, userName, project):
    	databaseQueryObj = DatabaseQueries()
    	list1 = databaseQueryObj.getUserData()
    	if list1 != None :
    		for userFromdb in list1 :
    			if userFromdb.getUserName() == userName:
    				databaseQueryObj.updateUserProject(userName,project)
    				return True
    	return False

    def setUserData(self, user):
    	databaseQueryObj = DatabaseQueries()
    	databaseQueryObj.setUserData(user)