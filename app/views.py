# This the controller where the request come in and it decides what to be given as view.

from flask import render_template, flash, redirect, request
from app import app
from app.user import User
from app.Service import ServiceClass


serviceObj = ServiceClass()

# Requirement 1 returns OK for this route
@app.route('/')
def returnOk():
	return "Ok"

# This will send a page to create new user
@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    return render_template('newUser.html')

# This will return login page for existing user
@app.route('/home', methods=['GET','POST'])
def home():
	return render_template('home.html')

# Requirement 2 : Takes the user detail and sends it to service class
@app.route('/new-Profile', methods=['POST'])
def newProfile():
	if request.method == 'POST':
		user = User()
		user.setUserName(request.form['userName'])
		user.setEmailId(request.form['emailId'])
		user.setZipCode(request.form['zipCode'])
		user.setPassword(request.form['password'])
		if serviceObj.checkIfUnique(user) :
			serviceObj.setUserData(user)
			return render_template('home.html')
		else :
			return "User already exist. Please login"

# This will be called to check if the user is a registered user
@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':	
		userName = request.form['username']
		password = request.form['password']
		if serviceObj.validateUser(userName,password):
			return render_template("addProject.html")
		else :
			return "User not registered. Please Register"

# Once user logs in this will be used to set the user's project
@app.route('/project', methods=['POST'])
def project():
	if request.method == 'POST':	
		userName = request.form['username']
		project = request.form['project']
		if serviceObj.isUserPresent(userName, project):
			return "Project assigned to User Successfully"
		else :
			return "User not registered. Please enter a valid username"

# Requirement 3 : Using profile/username gives the details of the user
@app.route('/profile/<userName>', methods=['GET'])
def getProfileUsingUsername(userName):
	if request.method == 'GET':	
		user = serviceObj.getUserData(userName)
		if user != None:
			return render_template("profileDisplay.html", result = user)
		else :
			return "User not registered. Please enter a valid username"