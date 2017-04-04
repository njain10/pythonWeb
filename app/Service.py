from user import User
from databaseQueries import DatabaseQueries

# This is the Service class which is responsible for the processing of data

class ServiceClass():

	# This is used to check if the username and email id is unique for the new registering user
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

    # This is used when user tries to login to check if he/she is a registered user
    def validateUser(self, userName, password):
    	databaseQueryObj = DatabaseQueries()
    	list1 = databaseQueryObj.getUserData()
    	if list1 != None :
    		for userFromdb in list1 :
    			if userFromdb.getUserName() == userName and userFromdb.getPassword() == password:
    				return True
        return False

    # This is used to return the user object based on the username recieved as input 
    def getUserData(self, userName):
    	databaseQueryObj = DatabaseQueries()
    	list1 = databaseQueryObj.getUserData()
    	if list1 != None :
    		for userFromdb in list1 :
    			if userFromdb.getUserName() == userName:
    				return userFromdb
        return None

    # This is used to check if the user is present in the database and if yes we would assign the project to the user
    def isUserPresent(self, userName, project):
    	databaseQueryObj = DatabaseQueries()
    	list1 = databaseQueryObj.getUserData()
    	if list1 != None :
    		for userFromdb in list1 :
    			if userFromdb.getUserName() == userName:
    				databaseQueryObj.updateUserProject(userName,project)
    				return True
    	return False

    # This will forward the user object to be stored in the database
    def setUserData(self, user):
    	databaseQueryObj = DatabaseQueries()
    	databaseQueryObj.setUserData(user)