

# This is a class for User object with properties and all properties are private and they are accessed using setters and getters.


class User:
    userCount = 0;
    def __init__(self):
        User.userCount += 1
        self.__userId = User.userCount
        self.__userName = ""
        self.__emailId = ""
        self.__zipCode = 0
        self.__password = ""
        self.__projectName = ""
   
    def getUserId(self):
        return self.__userId

    def setUserName(self, userName):
        self.__userName = userName

    def getUserName(self):
        return self.__userName

    def setEmailId(self, emailId):
        self.__emailId = emailId

    def getEmailId(self):
        return self.__emailId

    def setZipCode(self, zipCode):
        self.__zipCode = zipCode

    def getZipCode(self):
        return self.__zipCode

    def setPassword(self, password):
        self.__password = password

    def getPassword(self):
        return self.__password

    def setProject(self, projectName):
        self.__projectName = projectName

    def getProject(self):
        return self.__projectName