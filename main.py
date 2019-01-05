__author__ = 'user'
import functions
import database
import cx_Oracle
from connection import con, cur
from flask import Flask, render_template, redirect, url_for, request

def main():
    database.make_all_tables()
    database.reset_withdrawals()
    choice = 1

    while choice != 0:

        print("--- Main Menu --- ")
        print("1. Sign Up (New Customer) ")
        print("2. Sign In (Existing Customer) ")
        print("3. Admin Sign In ")
        print("0. Quit ")

        try:
            choice = int(input())

        except:
            print("Invalid Choice")
            choice = 1
            continue

        if choice == 1:
            functions.sign_up();

        elif choice == 2:
            functions.sign_in();

        elif choice == 3:
            functions.admin_sign_in();

        elif choice == 0:
            print("Application Closed")

        else:
            print("Invalid Choice")



temp_usr = ''
temp_pwd = ''

app = Flask(__name__)

# use decorators to link the function to a url

@app.route('/')
def home():
    return '''
	<!DOCTYPE.html>
<html>
	<style>
	.header img {
  float: left;
  width: 100px;
  height: 100px;
  background: #555;
}

.header h1 {
  position: relative;
  top: 18px;
  left: 10px;
}
</style>
	<head>
		<title>People Bank</title>
		<link rel="stylesheet" type="text/css" href="static/webstyle.css">
	</head>
	<body>
		<div id="container">
			<div id="header"> <h1>PeOPlE Bank</h1></div>
			<div id="navigation">
				<ul>
					<a href="account"><li>Account</li></a>
					<a href="#"><li>Loans</li></a>
					<a href="#"><li>Policies</li></a>
					<a href="#"><li>Cards</li></a>
					<a href="contact.html"><li> Contact</li></a>
				</ul>
				<div style="clear: both;"></div>

			</div>
	<picture>
  <source media="(min-width: 1024px)" srcset="static/people.jpg">
  <source media="(min-width: 465px)" srcset="static/people.jpg">
  <img src="static/people.jpg" alt="Flowers" style="width:1200px;height:720px;border:0;">
</picture>


	   '''  # return a string

# Route for handling the login page logic
@app.route('/login', methods=['GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] or request.form['password']:
            temp_usr = string(request.form['username'])
            temp_pwd = string(request.form['password'])
            main()
            return ("Thanks for the input")
    return render_template('login.html', error=error)

# Route for handling the account page logic
@app.route('/account', methods=['GET', 'POST'])
def account():
    error = None
    if request.method == 'POST':
        if request.form['username'] or request.form['password']:
            temp_usr = request.form['username']
            temp_pwd = request.form['password']
            main()
    return render_template('account.html', error=error)



if __name__ == '__main__':
    app.run(debug=True)
    print(temp_usr)


