from flask import render_template, flash, redirect, request
from app import app
from user import User
from Service import ServiceClass

# index view function suppressed for brevity

serviceObj = ServiceClass()

@app.route('/')
def returnOk():
	return "Ok"

@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    return render_template('newUser.html')

@app.route('/home', methods=['GET','POST'])
def home():
	return render_template('home.html')


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

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':	
		userName = request.form['username']
		password = request.form['password']
		if serviceObj.validateUser(userName,password):
			return render_template("addProject.html")
		else :
			return "User not registered. Please Register"

@app.route('/project', methods=['POST'])
def project():
	if request.method == 'POST':	
		userName = request.form['username']
		project = request.form['project']
		if serviceObj.isUserPresent(userName, project):
			return "Project assigned to User Successfully"
		else :
			return "User not registered. Please enter a valid username"

@app.route('/profile/<userName>', methods=['GET'])
def getProfileUsingUsername(userName):
	if request.method == 'GET':	
		user = serviceObj.getUserData(userName)
		if user != None:
			return render_template("profileDisplay.html", result = user)
		else :
			return "User not registered. Please enter a valid username"